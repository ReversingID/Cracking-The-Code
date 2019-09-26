import os, sys, socket
wd = '\x1b[90;1m'
GL = '\x1b[96;1m'
BB = '\x1b[34;1m'
YY = '\x1b[33;1m'
GG = '\x1b[32;1m'
WW = '\x1b[0;1m'
RR = '\x1b[31;1m'
CC = '\x1b[36;1m'
B = '\x1b[34m'
Y = '\x1b[33;1m'
G = '\x1b[32m'
W = '\x1b[0;1m'
R = '\x1b[31m'
C = '\x1b[36;1m'
print RR + '\t\t     SCANNER IP WEBSITE'
print ' '
print WW + '\t   #######################################'
print '\t   #          Author : iExEi HD          #'
print '\t   #       Team :Lead Cyber Team         #'
print '\t   #     Team :Fours Army Hacktivits     #'
print '\t   # Team :Indonesian Termux Association #'
print '\t   #       Team :2Lul Story Team         #'
print '\t   #######################################'
print '\n'
server = raw_input(BB + '\tMasukan Url Website : ' + GG)
print ' '
ip = socket.gethostbyname(server)
print BB + 'Alamat IP Url : ' + GG, ip
print ' '
print YY + '\tTERIMA KASIH TELAH MENGGUNAKAN TOLS INI :)' + W
sys.exit(1)
os.system('exit')
