##############################################
# Coded by Mr.Runn1n9 | Indonesian The Coder #
#      Created: 21 Oktober 2019 [20:48]      #
##############################################

sleep 0.2
clear
printf "\n    \033[34;1m╔══════════════════════════════════════╗\n  ╔═║\033[32;1mGithub \033[37;1m: https://github.com/mr-runn1n9\033[34;1m║═╗\n  ║ ╚══════════════════╔═══════════════════╝ ║\n"
printf "  ╚════════════════════╝   \033[33;1mMoon-Buggy        \033[34;1m║"
printf "\n    \033[34;1m╔════════════════════╗     \033[33;1mV1     \033[34;1m╔══════╝\n  ╔═║\033[32;1mInstall bahan? (\033[37;1mY\033[32;1m/\033[37;1mn\033[32;1m)\033[34;1m║════════════╝\n  ║ ╚════════════════════╝\n"
printf "  ╚"
sleep 0.5
printf "═"
sleep 0.3
printf "═"
sleep 0.2
printf "═"
sleep 0.1
printf "═"
sleep 0.4
printf "═"
sleep 0.2
printf "═"
sleep 0.3
printf "═"
sleep 0.2
printf "═"
sleep 0.1
printf "═"
sleep 0.7
read -p $'\033[32;1m>\033[37;1m ' j3mb03d
if [[ $j3mb03d == Y || $j3mb03d == y ]]; then
sleep 0.5
clear
pkg update && pkg upgrade
clear
pkg install moon-buggy
sleep 1.5
clear
moon-buggy
elif [[ $j3mb03d == N || $j3mb03d == n ]]; then
sleep 0.5
clear
moon-buggy
else
sleep 0.2
clear
printf "\n    \033[34;1m╔════════════════════════╗\n    ║\033[31;1mGagal menggunakan Tools!\033[34;1m║\n    ╚════════════════════════╝\n\033[37;1m"
fi
