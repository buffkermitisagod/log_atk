import os
import itertools

def dic():
    os.system("clear")
    print("""
     _    _    __   ______    ___      __   __  _
    | \  (_)  / _| |__  __|  / __|__  | _| |  \| | 
    |  | | | | |_    | |    | |_|_ _| | _| | |\  |
    |_/  |_|  \__|   |_|     \____/   |__| |_| \_|
    ---------------------------------------------- 
    1) genarate from a ist of letters
    2) fill in the blanks (eg: q?e?t?)

    """)
    choice = int(input("[ENTER] enter option: "))
    if choice == 2:
        words = input("[ENTER] enter the word (eg: n?m?? or ????): ")
        alph = input("[ENTER] enter the letters (eg: wofj): ")
        word = input("[ENTER] enter the path to the worlist file: ")
        mx = len(alph)
        #alp = words.split("")
        count  = 0

        for x in words:
            if x == "?":
                count += 1
            else:
                pass
            chk = x

        print("[GEN] (?) in word: ",count)

        print("[GEN] making word list now")
        PASSWORD_LIST = itertools.product(alph, repeat=count)

        for pas in PASSWORD_LIST:
            pas = str(pas)
            pas = pas.replace("')","")
            pas = pas.replace("('","")
            pas = pas.replace("'","")
            pas = pas.replace(" ","")
            #print(pas)
            u = str(pas)
            u = u.split(",")
            
            
            b = []
            c = 0
            for v in words:
                run = False
                if v == "?":
                    try:
                        v = u[c]
                        run = True
                        c += 1
                    except Exception as e:
                        print("[!] unkown error:",e)
                        run = False
                else:
                    run = True
                if run == True:
                    b.append(v)
                else:
                    pass

            u = str(b)
            u = u.replace("['","")
            u = u.replace("']","")
            u = u.replace("'","")
            u = u.replace(",","")
            u = u.replace(" ","")
            u = u.replace("|","")
            print(u)
    if choice == 1:
        chars = input("[ENTER] enter the charecters (eg: qyr12): ")
        i = int(input("[ENTER] enter the lenght of the passwords: "))
        word = input("[ENTER] enter the path to the worlist file: ")
        print("[GEN] genarating list...")
        PASSWORD_LIST = itertools.product(chars, repeat=i)
        x = 0
        done = []
        for pas in PASSWORD_LIST:
            pas = str(pas)
            pas = pas.replace("')","")
            pas = pas.replace("('","")
            pas = pas.replace("'","")
            pas = pas.replace(",","")
            pas = pas.replace(" ","")
            u = str(pas)
            done.append(u)
            x = x + 1
        print("[GEN] genarated")
        print("[GEN] lenght of genarated wordlist is (",x,")")
    print("[GEN] saving file...")
    try:
        f = open(word,"r+")
        for r in done:
            t = r+"\n"
            f.write(t)
        f.close()
    except FileNotFoundError:
        f = open(word,"x+")
        for r in done:
            t = r+"\n"
            f.write(t)
        f.close()