import os,sys,re,random
from random import choice as rc

os.system("xdg-open https://www.facebook.com/mdmahfujhasan.joy")

#########COLOR########
GREEN ='\x1b[38;5;46m'
RED = '\x1b[38;5;196m'
WHITE = '\033[1;97m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
EXTRA ='\x1b[38;5;208m'
############LOGO###########
logo = f"""
{WHITE}
███    ███  █████  ██   ██ ███████ ██    ██ ███████ 
████  ████ ██   ██ ██   ██ ██      ██    ██    ███  
██ ████ ██ ███████ ███████ █████   ██    ██   ███   
██  ██  ██ ██   ██ ██   ██ ██      ██    ██  ███    
██      ██ ██   ██ ██   ██ ██       ██████  ███████ 
                   

\t[>>] Author  :  MD Mahfuz Hasan 
\t{GREEN}[ TEST YOUR LUCK GUYZ ]{WHITE}"""

def main():
    print(logo)
    print(40*"-")
    print("[1] Boys Test Your Luck")
    print("[2] Girls Test Your Luck")
    print(40*'-')
    luck = input("[>>] choose : ")
    if luck in ["1","01"]:
        jawn()
    elif luck in ["2","02"]:
        chuna()

def clear():
	os.system('clear')
	print(logo)


def jawn():
    clear()
    girlfriends =["you are in relation soon as soon possible","No chance to find girlfriend","Error In your life","first go and wash your face","No Gril Found in Your life "," Dear friend You have Lots of girls in your life don't try on Next Girl","Dear Friend Better Luck Next Time","Dear Friend You have A loyal Girlfriend Stay loyal with her"]
    gfs = rc(girlfriends)
    print(40*'-')
    print("\t[ NOTE ]")
    print(40*'-')
    print(gfs)
    print(40*'-')


def chuna():
    clear()
    boyfriends = ["Dear Girl You have no more space your boyfriends limit is full","Dear Girl yiu are so Lucky you will get soon Loyal Boyfriend"," Dear girl you have ugli face you can't be create relationship","Dear Girl You have lots for boyfriends plz stop it","Dear Girls face your face and Try again later","Better Luck next time","A good person comming soon in your life","you have Caring loving boyfriend don't dump him"]
    bfs = rc(boyfriends)
    print(40*'-')
    print("\t[ NOTE ]")
    print(40*'-')
    print(bfs)
    print(40*'-')

main()
