import requests
from parsel import Selector
from colorama import Fore, Style
import os

from tools.router.atk_sky import main as ak_sky


def detect():
    print(Fore.GREEN)
    print("["+Fore.CYAN+"DETECT"+Fore.GREEN+"] detecting provider")
    num = 0
    ### Crawling to the website fetch links and images -> store images -> crawl more to the fetched links and scrap more images
    all_images  = {} # website links as "keys" and images link as "values"
    # GET request to recurship site
    test = ["192.168.0.1","192.168.1.1","192.168.2.1"]

    for ip in test:
        print("["+Fore.CYAN+"DETECT"+Fore.GREEN+"] trying "+ ip)
        nm = str(num)
        url = "http://"+ip+"/"
        num = num + 1
        router = 0
        try:
            response = requests.get(url, timeout=5)
            selector = Selector(response.text)
            href_links = selector.xpath('//a/@href').getall()
            detect = False
            if "sky_" in href_links:
                print("["+Fore.CYAN+"DETECT"+Fore.GREEN+"] found provider")
                print("[provider] provider = sky")
                router = "sky"
                break
            elif "#passwordInfo" in href_links:
                print("["+Fore.CYAN+"DETECT"+Fore.GREEN+"] found provider")
                print("["+Fore.CYAN+"provider"+Fore.GREEN+"] vodaphone")
                print(Fore.RED+"[!] vodeaphone can't be attacked")
                print(Fore.RED+"[!] enter the wifi password on the url")
                print(Fore.GREEN+"["+Fore.CYAN+"url"+Fore.GREEN+"] http://"+ip)
                input("["+Fore.GREEN+"ENTER"+Fore.GREEN+"] hit enter to continue "+Style.RESET_ALL)
                break

            else:
                pass
        except Exception:
            pass
          
    if router == "sky":
        ak_sky()
    else:
        os.system("clear")
        print(Fore.RED+"[!] unkown provider")
        print("[!] make sure it's not an 3rd part extention that you have connected to")
        print("[!] curently supports: \nsky \nvodaphone ["+Fore.CYAN+"NOT REALLY"+Fore.RED+"] \n"+Style.RESET_ALL)
        input(Fore.GREEN+"["+Fore.CYAN+"ENTER"+Fore.GREEN+"] hit enter to continue ")