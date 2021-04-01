#!/usr/bin/python3
# Import Modules
try:
    import os,sys,time,random,urllib.request,json,readline
    from platform import system
except Exception as F:
    exit("\x1b[1;31m   [!] \x1b[0;32m%s\x1b[0;39m"%(F)+"\x1b[0;39m")
# Color
A = "\x1b[1;32m"
B = "\x1b[1;31m"
C = "\x1b[1;33m"
D = "\x1b[1;36m"
E = "\x1b[0;39m"
rand = (A,B,C,D)
W = random.choice(rand)
# Adaptor
name = system()
if name == "Windows":
    clr = "cls"
else:
    clr = "clear"
if sys.version_info[0] != 3:
    exit(B+"   [!] "+A+"This tool work only on python3!"+E)
else:
    pass
# Banner
BR = W+"""
	 ___ ____            _____               _
	|_ _|  _ \          |_   _| __ __ _  ___| | __
	 | || |_) |  _____    | || '__/ _` |/ __| |/ /
	 | ||  __/  |_____|   | || | | (_| | (__|   <
	|___|_|               |_||_|  \__,_|\___|_|\_\ 
"""
# IP
def check():
    try:
        os.system(clr)
        print(BR)
        print(C+"\n   [+] "+D+"Checking your internet "+E+"...")
        urllib.request.urlopen("https://www.google.com")
    except Exception:
        exit(B+"   [!] "+A+"Please check your internet!"+E)
def track():
    ip = input(C+"   [+] "+D+"Target IP: "+E)
    print(B+"   [!] "+A+"Tracking IP "+E+"...")
    req = json.loads(urllib.request.urlopen("https://ipapi.co/"+ip+"/json/").read())
    try:
        print(B+"\n   [+] "+A+"IP                 : "+E+"%s"%req["ip"])
        print(B+"   [+] "+A+"IP Version         : "+E+"%s"%req["version"])
        print(B+"   [+] "+A+"City               : "+E+"%s"%req["city"])
        print(B+"   [+] "+A+"Region             : "+E+"%s"%req["region"])
        print(B+"   [+] "+A+"Region Code        : "+E+"%s"%req["region_code"])
        print(B+"   [+] "+A+"Country            : "+E+"%s"%req["country"])
        print(B+"   [+] "+A+"Country Name       : "+E+"%s"%req["country_name"])
        print(B+"   [+] "+A+"Country Code       : "+E+"%s"%req["country_code"])
        print(B+"   [+] "+A+"Country Code ISO   : "+E+"%s"%req["country_code_iso3"])
        print(B+"   [+] "+A+"Country Capital    : "+E+"%s"%req["country_capital"])
        print(B+"   [+] "+A+"Country TLD        : "+E+"%s"%req["country_tld"])
        print(B+"   [+] "+A+"Continent Code     : "+E+"%s"%req["continent_code"])
        print(B+"   [+] "+A+"European Union     : "+E+"%s"%req["in_eu"])
        print(B+"   [+] "+A+"Postal             : "+E+"%s"%req["postal"])
        print(B+"   [+] "+A+"Latitude           : "+E+"%s"%req["latitude"])
        print(B+"   [+] "+A+"Longitude          : "+E+"%s"%req["longitude"])
        print(B+"   [+] "+A+"Timezone           : "+E+"%s"%req["timezone"])
        print(B+"   [+] "+A+"UTC Offset         : "+E+"%s"%req["utc_offset"])
        print(B+"   [+] "+A+"Calling Code       : "+E+"%s"%req["country_calling_code"])
        print(B+"   [+] "+A+"Currency           : "+E+"%s"%req["currency"])
        print(B+"   [+] "+A+"Currency Name      : "+E+"%s"%req["currency_name"])
        print(B+"   [+] "+A+"Languages          : "+E+"%s"%req["languages"])
        print(B+"   [+] "+A+"Country Area       : "+E+"%s"%req["country_area"])
        print(B+"   [+] "+A+"Country Population : "+E+"%s"%req["country_population"])
        print(B+"   [+] "+A+"ASN                : "+E+"%s"%req["asn"])
        print(B+"   [+] "+A+"ORG                : "+E+"%s"%req["org"])
        input(C+"\n   [!] "+D+"Press enter to menu"+E)
        menu()
    except KeyboardInterrupt:
       exit()
    except Exception:
        print(B+"\n   [!] "+A+"Unknown"+E)
        input(C+"   [!] "+D+"Press enter to menu"+E)
        menu()
def menu():
    try:
        os.system(clr)
        print(BR)
        print(B+"\n\t\t   [01] "+A+"CHECK YOUR IP")
        print(B+"\t\t   [02] "+A+"TRACK IP")
        print(B+"\t\t   [00] "+A+"EXIT\n"+E)
        x = int(input(C+"   [+] "+D+"Your choose: "+E))
        if x == "01" or x == 1:
            print(B+"   [!] "+A+"Checking your IP "+E+"...")
            query = json.loads(urllib.request.urlopen("http://ip-api.com/json/").read())
            print(B+"\n   [+] "+A+"Your Public IP : "+E+query["query"])
            print(B+"   [+] "+A+"Country        : "+E+query["country"])
            print(B+"   [+] "+A+"Country Code   : "+E+query["countryCode"])
            print(B+"   [+] "+A+"Region         : "+E+query["region"])
            print(B+"   [+] "+A+"Region Name    : "+E+query["regionName"])
            print(B+"   [+] "+A+"City           : "+E+query["city"])
            print(B+"   [+] "+A+"Zip Code       : "+E+query["zip"])
            print(B+"   [+] "+A+"Latitude       : "+E+str(query["lat"]))
            print(B+"   [+] "+A+"Longitude      : "+E+str(query["lon"]))
            print(B+"   [+] "+A+"Timezone       : "+E+query["timezone"])
            print(B+"   [+] "+A+"ISP            : "+E+query["isp"])
            print(B+"   [+] "+A+"ORG            : "+E+query["org"])
            print(B+"   [+] "+A+"AS             : "+E+query["as"])
            input(C+"\n   [!] "+D+"Press enter to menu"+E)
            menu()
        elif x == "02" or x == 2:
            track()
        elif x == 0:
            sys.exit()
        else:
            print(B+"   [!] "+A+"Wrong choice !!!"+E)
            time.sleep(1)
            menu()
    except KeyboardInterrupt or EOFError:
        print(B+"\n   [!] "+A+"Exiting "+E+"...")
        time.sleep(0.1)
        sys.exit()
    except Exception as F:
        exit(B+"   [!] "+A+"%s"%(F)+E)
if __name__ == "__main__":
    check()
    menu()
