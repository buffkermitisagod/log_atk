print("booting...")
import colorama
import os
os.system("clear")

# external
from colorama import Fore, Style

# tools import
print("loging else tools...")
from tools.dic_gen import dic as dic

print("loding router attacks...")
from tools.router.detect import detect as route
from tools.router.sniff import pack_cap as pack
from tools.router.wifi_password import main as wifi_atk

print("loading socail attacks...")
from tools.social_tools.maininsta import main as insta
from tools.social_tools.face_main import main as face

print("loading service attacks...")
from tools.service.ssh import _brute_ as ssh

print("loading phishing attacks....")
from tools.login.gmail_main import main as gmail_pish
from tools.login.facebook_main import main as face_pish
from tools.login.insta_main import main as insta_phish

while True:
    os.system("clear")
    print(Fore.GREEN)
    banner = """
 _______________________________________________
|"""+Fore.BLUE+"""  __   _    ___         _       ___     ___    """+Fore.GREEN+"""|
|"""+Fore.BLUE+""" |  \ | |  /   \   __  | |     /   \   / __|   """+Fore.GREEN+"""|
|"""+Fore.BLUE+""" |   \| | |  |  | |__| | |    |  |  | | / ___  """+Fore.GREEN+"""|
|"""+Fore.BLUE+""" | |\   | |  |  |      | |__  |  |  | | \|_ _| """+Fore.GREEN+"""|
|"""+Fore.BLUE+""" |_| \__|  \___/       |____|  \___/   \___/   """+Fore.GREEN+"""|
|_______________________________________________|
|                                               |
|              ["""+Fore.CYAN+"""passwords attack"""+Fore.GREEN+"""]               |
|_______________________________________________|

    """
    print(banner)
    print("------------["+Fore.CYAN+"LOGIN ATTACKS"+Fore.GREEN+"]------------")
    print("1) router admin attack      ")
    print("2) sniff http admin login's ["+Fore.RED+"NEEDS HTTP & DOESN'T WORK WITH SOME ROUTERS"+Fore.GREEN+"]")
    print("3) face-brute               ["+Fore.RED+"USES TOR"+Fore.GREEN+"]")
    print("4) insta-brute              ["+Fore.RED+"USES TOR"+Fore.GREEN+"]")
    print("5) ssh-brute                ") 
    print("6) wifi password attack's   ["+Fore.RED+"AIRCRAC-NG NEEDED"+Fore.GREEN+"]")
    print("------------["+Fore.CYAN+"SOCIAL ATTACKS"+Fore.GREEN+"]-----------")
    print("7. gmail login page         ["+Fore.RED+"NGROK NEEDED"+Fore.GREEN+"]")
    print("8. facebook login page      ["+Fore.RED+"NGROK NEEDED"+Fore.GREEN+"]")
    print("9. instagram login page     ["+Fore.RED+"NGROK NEEDED"+Fore.GREEN+"]")
    print("----------------["+Fore.CYAN+"ELSE"+Fore.GREEN+"]-----------------")
    print("99) dict-gen                ["+Fore.RED+"USES ALOT OF SPACE"+Fore.GREEN+"]")
    print("100) info")
    
    #print(Style.RESET_ALL)

    cho = int(input("\n\n\n["+Fore.CYAN+"ENTER"+Fore.GREEN+"] enter option: "+Style.RESET_ALL))
    os.system("clear")
    try:
           #log attack#
        if cho == 1:
            route()
        elif cho == 2:
            pack()
        elif cho == 3:
            face
        elif cho == 4:
            insta()
        elif cho == 5:
            ssh()
        elif cho == 6:
            wifi_atk()
        
           #phising#
        elif cho == 7:
            gmail_pish()
        elif cho == 8:
            face_pish()
        elif cho == 9:
            insta_phish()
        
           #else#
        elif cho == 99:
            dic()
        elif cho == 100:
            print(Fore.GREEN+"["+Fore.CYAN+"LOG ATTCK INFO"+Fore.GREEN+"]")
            print("router attacks only support a limited")
            print("number of routers when i have accses to more")
            print("i will add more or you can develop a attack for them")
            print("and send it to me, u will be mentioned for you help\n\n")
            print("["+Fore.CYAN+"SOCIAL ATTACKS INFO"+Fore.GREEN+"]")
            print("all socail attack will store")
            print("all passwords in a user and pass")
            print(".txt file to use\n\n")
            print("["+Fore.CYAN+"ELSE"+Fore.GREEN+"]")
            print("if u develop any tools that u think would suit this program")
            print("please let me know and i will add them in an give u credit for it")
            input("\n\n\n[ENTER] hit enter to continue: "+Style.RESET_ALL)
        else:
            print("["+Fore.RED+"!"+Fore.GREEN+"] ERROR unkown tool / option ("+str(cho)+") is not an option"+Style.RESET_ALL)
    except KeyboardInterrupt:
        print("\n\n["+Fore.RED+"!"+Fore.GREEN+"] user quit from opt("+str(cho)+")"+Style.RESET_ALL)