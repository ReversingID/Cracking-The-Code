# Apalu Liat2 Anjiing Mau Recode Ya Kontoll
# Buat Sendiri Goblok Jangan Recode Punya Orang
# Sumpah Gak Guna Lu Ngentot
# Yang Peling Ngeri Hasil Record Di Pake Pames
# Lu Sehat Njing Hargai Karya Orang Bangsatt
# Kalo Mau Recode Cantumkan Author Nya Goblok
# Piks Lu Script Kiddie Gak Guna Cem Sampahh
# coder: Rusmana-ID
# Team : Black Coder Crush

b="\033[34;1m"
m="\033[31;1m"
k="\033[33;1m"
h="\033[32;1m"
p="\033[39;1m"
pu="\033[36;1m"
c="\033[35;1m"
bl="\033[30;1m"

function __main__(){
    clear
    printf "${m}                   ─▄────▄▄▄▄▄▄▄────▄─\n"
    printf "${pu}     ─╔╗─╔╗───╔═╗${m}  ▀▀▄─▄█████████▄─▄▀▀\n"
    printf "${pu}     ╔╝║╔╝║╔═╗║═╣${m}  ────██─▀███▀─██────\n"
    printf "${pu}     ║╬║║╬║║╬║╠═║${m}  ──▄─▀████▀████▀─▄──\n"
    printf "${pu}     ╚═╝╚═╝╚═╝╚═╝${m}  ▀█────██▀█▀██────█▀\n"
    printf "${m}                   ─▄────▄▄▄▄▄▄▄────▄─\n"
    printf "${pu}          ───────╔╗─╔═╗╔╗╔╗────\n"
    printf "${pu}          ╔╦╦╗╔═╗║╚╗║═╣╠╣║╚╗╔═╗${m}*${h}NEW\n"
    printf "${pu}          ║║║║║╩╣║╬║╠═║║║║╔╣║╩╣\n"
    printf "${pu}          ╚══╝╚═╝╚═╝╚═╝╚╝╚═╝╚═╝\n"
    printf "${p}          ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
    printf "${p}          [${h}•${p}]${c}Update${m}: *${bl}Mr.Tr3v!0n\n"
    printf "${p}          [${h}•${p}]${c}Hammer${m}: *${bl}Can Yalçın\n"
    printf "            ${m}*${bl}Black Coder Crush${m}*\n"
    printf "${p}          ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
    printf "${m}\n         ╔══════════════════════╗ \n${p}"
    printf "${m}         ║ ${p} Masukan Web Tanpa${m}!! ${m}║\n"
    printf "${m}         ║ ${p}    https or http    ${m}║\n"
    printf "${m}         ╚══════════════════════╝${p}"

    function scan_ip(){
        printf "${b}         ╔══════════════════════╗ \n${p}"
        ping -c 1 "$XxXxXxXxXxXx" | grep "PING" | awk {'print "\033[34;1m         ║\033[39;1mIP WEB\033[31;1m: \033[32;1m" $3'} | tr -d '()'
        printf "${b}         ╚══════════════════════╝\n${p}"
    }

    printf "${b}\n         ╔══════════════════════╗ \n"
    printf "${b}         ║${p}WEB TARGET${m}: ${k}"
    read XxXxXxXxXxXx;
    printf "${b}         ╚══════════════════════╝\n${p}"
    scan_ip
}

function ddos(){
    printf "\n${p}         ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
    printf "${b}         ╔══════════════════════╗ \n"
    printf "${b}         ║${p}Mulai DDOS ${m}[${k}Y${m}/${k}T${m}]${h}: ${p}"
    read d;
    printf "${b}         ╚══════════════════════╝\n"

    if [ $d = Y ] || [ $d = y ]; then
        ip_web
    elif [ $d = T ] || [ $d = t ]; then
        printf "${p}  Bye *_*\n"
        exit
    else
        printf "Salah!!\n"
        exit
    fi
}

function ip_web(){
    printf "${b}         ╔══════════════════════╗ \n"
    printf "${b}         ║${p}Input IP WEB ${m}: ${p}"
    read ip;
    printf "${b}         ╚══════════════════════╝\n"
    progres_bar
    printf "\n"
    python __attacker__.py -s $ip
}

progres_bar(){
    function ProgressBar {
        let _progress=(${1}*100/${2}*100)/100
        let _done=(${_progress}*3)/10
        let _left=30-$_done
        _done=$(printf "%${_done}s")
        _left=$(printf "%${_left}s")
        printf "\r${c}Load${m}: ${k}[${p}${_done// /#}${_left// /${m}-}${k}] ${pu}${_progress}%%"
    }

    _start=1
    _end=100

    for number in $(seq ${_start} ${_end}); do
        sleep 0.1
        ProgressBar ${number} ${_end}
    done
}

__main__
ddos
