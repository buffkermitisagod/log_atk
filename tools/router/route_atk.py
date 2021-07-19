import random

def proxy():
    print("[PROXY] generating proxy browser")
    agents = ["Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
                "Mozilla/5.0 (Linux; Android 9.0; MI 8 SE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.119 Mobile Safari/537.36",
                "Mozilla/5.0 (Windows Phone 8.1; ARM; Trident/7.0; Touch; WebView/2.0; rv:11.0; IEMobile/11.0; NOKIA; Lumia 525) like Gecko"]
    r = random.randint(0,(len(agents) - 1))
    print("[PROXY] using proxy num: ", r)
    age = agents[r]
    return age