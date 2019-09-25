#!bin/bash

bi='\033[34;1m' #biru
i='\033[32;1m' #ijo
pur='\033[35;1m' #purple
cy='\033[36;1m' #cyan
me='\033[31;1m' #merah
pu='\033[37;1m' #putih
ku='\033[33;1m' #kuning

clear
python2 key.py
clear
python2 code.py
clear
sleep 3
echo $me"██████╗  █████╗ ██████╗ ██╗  ██╗    ███████╗██████╗ "
sleep 0.3
echo $me"██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝    ██╔════╝██╔══██╗"
sleep 0.3
echo $me"██║  ██║███████║██████╔╝█████╔╝     █████╗  ██████╔╝"
sleep 0.3
echo $me"██║  ██║██╔══██║██╔══██╗██╔═██╗     ██╔══╝  ██╔══██╗"
sleep 0.3
echo $me"██████╔╝██║  ██║██║  ██║██║  ██╗    ██║     ██████╔╝"
sleep 0.3
echo $me"╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝     ╚═════╝ "
echo $me"                                                    "
echo ""
echo ""
sleep 0.3
echo $bi"====================================="
sleep 0.3
echo $ku"[1]" $cy"DarkFb 1.6" "             " $i"<Active>"
sleep 0.3
echo $bi"====================================="
sleep 0.3
echo $ku"[2]" $cy"DarkFB 1.7" "             " $i"<Active>"
sleep 0.3
echo $bi"====================================="
sleep 0.3
echo $ku"[3]" $cy"DarkFB VIP" "             " $i"<Active>"
sleep 0.3
echo $bi"====================================="
sleep 0.3
echo $ku"[99]" $cy"Subscribe" "             " $i"<Active>"
sleep 0.3
echo $bi"====================================="
sleep 0.3
echo $ku"[00]" $cy"exit" "           " $i"<Always Active>"
sleep 0.3
echo $bi"====================================="
sleep 0.3
echo ""
sleep 0.3
read -p "Pilih No ==> " pil

if [ $pil = 1 ]; then
    clear
    figlet -f slant "T U N G G U" | lolcat
    sleep 1
    git clone https://github.com/pashayogi/SETAN
    cd SETAN
    python2 SETAN.py
fi

if [ $pil = 2 ]; then
    clear
    figlet -f slant "T U N G G U" | lolcat
    sleep 1
    git clone https://github.com/storiku/darkfb
    cd darkfb
    python2 Dark.py
fi

if [ $pil = 3 ]; then
    clear
    figlet -f slant "T U N G G U" | lolcat
    sleep 1
    python2 fbv3.py
fi

if [ $pil = 99 ]; then
    clear
    figlet -f slant "T U N G G U" | lolcat
    sleep 1
    xdg-open https://www.youtube.com/channel/UCl5K989iHzi4G6MMEJauwtg
fi

if [ $pil = 00 ]; then
    clear
    figlet -f slant "T U N G G U" | lolcat
    sleep 1
    exit
fi
