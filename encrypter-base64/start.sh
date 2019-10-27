############################################
#           Coded by: Mr.Runn1n9           #
# Created : Sabtu, 19 Oktober 2019 [03:53] #
############################################

sleep 0.5
clear
sleep 0.7
read -p $'\n    \033[34;1m╔════════╗\n    ║\033[37;1mUsername\033[34;1m║ \033[37;1m:\033[33;1m ' user
printf "    \033[34;1m╚════════╝\n"
sleep 0.5
read -p $'            ╔════════╗\n            ║\033[37;1mPassword\033[34;1m║ \033[37;1m:\033[33;m ' pass
printf "            \033[34;1m╚════════╝\n"
sleep 1.5
if [[ $user == Gatau && $pass == Lah ]];
then
clear
sleep 0.3
printf "\n    \033[34;1m[\033[36;1m01\033[34;1m] \033[37;1mEncrypt"
sleep 0.2
printf "\n    \033[34;1m[\033[36;1m02\033[34;1m] \033[37;1mDecrypt"
sleep 1
read -p $'\n\n    \033[34;1m[\033[31;1m!\033[34;1m] \033[32;1mChoose an Option:\033[36;1m ' opsi
if [[ $opsi == 1 || $opsi == 01 ]]; then
python2 j3mb03d/ekdodoowoeooe99eowo9w9e99d9e9oeoeoe..::RecoderGOBLOK::..kskowowowppepspsppwpwowoleodpeppwwo.py
elif [[ $opsi == 2 || $opsi == 02 ]]; then
python2 j3mb03d/dsiwoowo22pepofoeo2o2o0202929eo9t9r..::ApaLiatLiatKontol::..kkororoeoo2900o3ooroflleleleppwlflfodl.py
else
clear
sleep 0.1
printf "\n    \033[34;1m╔══════════════╗\n    ║\033[31;1mOption Failed!\033[34;1m║\n    ╚══════════════╝\n\n\033[37;1m"
fi
else
clear
printf "\n    \033[34;1m╔═════════════╗\n    ║\033[31;1mLogin Failed!\033[34;1m║\n    ╚═════════════╝\n\n\033[37;1m"
exit 1
fi
