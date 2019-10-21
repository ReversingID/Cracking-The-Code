sleep 0.5
clear
sleep 0.7
read -p $'\n    \033[34;1m╔════════╗\n    ║\033[37;1mUsername\033[34;1m║ \033[37;1m:\033[33;1m ' user
printf "    \033[34;1m╚════════╝\n"
sleep 0.5
read -p $'            ╔════════╗\n            ║\033[37;1mPassword\033[34;1m║ \033[37;1m:\033[33;m ' pass
printf "            \033[34;1m╚════════╝\n"
if [[ $user == Kepo && $pass == Cukk ]];
then
clear
sleep 0.5
python2 Z3MBuD/lksoqpwppspdpspqpsppdosoqpqppwpqpqpw...:::ApaLiatLiatAnjng:::...ksoqoqppqpdlpspqllwpspsppapqppqalslpww.py
else
clear
sleep 0.3
printf "\n    \033[34;1m╔═════════════╗\n    ║\033[31;1mLogin Failed!\033[34;1m║\n    ╚═════════════╝\n\n\033[37;1m"
exit 1
fi
