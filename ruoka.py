#! /usr/bin/python

import urllib.request
import urllib.parse
import re
from sys import argv
from colorama import Fore, Style


def getVegan():
    print(Fore.RED)
    for arg in argv[1:]:
        if arg.startswith("--vegan"):
            vsplit = arg.split('=')
            if len(vsplit) == 1:
                print("vegan set to default value because of no argument given with --vegan. please give either true or false as an argument")
                print(Style.RESET_ALL)			
                quit(1)
            else:
                if vsplit[1].lower() == "true":
                    return True
                elif vsplit[1].lower() == "false":
                    return False
                else:
                    print(f"illegal argument {vsplit[1]} given to --vegan. please only use true or false as arguments")
                    print(Style.RESET_ALL)			
                    quit(1)
        elif arg in ["--help", "-h"]:
            print("""#	usage: ruoka [command]
#
#	--vegan=VEGAN		Use true if you only want to see the vegan menu. Use false if you only want to see normal menu. Don't use if you want to see both
#	-h --help			Get help on the commands and flags""")
            print(Style.RESET_ALL)			
            quit()
		
print(Style.RESET_ALL)			

VEGAN = getVegan();

print(Style.BRIGHT)

url = 'https://www.mayk.fi/tietoa-meista/ruokailu'
days = ["Maanantai:     ",
        "MaVeg: ",
        "Tiistai:       ",
        "TiVeg: ",
        "Keskiviikko:   ",
        "KeVeg: ",
        "Torstai:       ",
        "ToVeg: ",
        "Perjantai:     ",
        "PeVeg: "]
ft = ""

print("Getting food menu...")
r = urllib.request.Request(url)
rp = urllib.request.urlopen(r)
rpd = rp.read()

menu = re.findall(r'<p class=\"ruoka-header-(ruoka|kasvisruoka)\">([^<]*)<',str(rpd))

for i, foods in enumerate(menu):
    f = ",".join(foods[1:]).replace("\\xc3\\xb6", 'ö').replace("\\xc3\\xa4", 'ä')
    if i % 2 == 0:
        print(Fore.CYAN + days[i])
        if not VEGAN:
            ft = Fore.WHITE + "Norm: "
            print(ft, f)
	
    else:
        if VEGAN is True or VEGAN is None:
            ft = Fore.GREEN + "Vege: "
            print(ft, f)
            print()
   
print(Style.RESET_ALL)