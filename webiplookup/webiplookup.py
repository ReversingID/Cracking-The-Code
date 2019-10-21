from bs4 import BeautifulSoup
import requests, sys, os, pyfiglet
h = '\x1b[92m'
p = '\x1b[0m'
os.system('clear')
ascii_banner = pyfiglet.figlet_format('webiplookup')
print ascii_banner
print '[' + h + '1' + p + ']' + h + ' SUBDOMAIN SCANNER \n' + p + '[' + h + '2' + p + '] ' + h + 'IP TO HOST \n' + p + '[' + h + '3' + p + '] ' + h + 'INFO TOOLS \n' + p + '[' + h + '4' + p + '] ' + h + 'YOUTUBE \n' + p + '[' + h + '5' + p + '] ' + h + 'EXIT'
pilih = raw_input(p + 'Junior:~# ')
if pilih == '1':
    junior = raw_input('DOMAIN : ')
    api = requests.get('https://webiplookup.com/' + junior + '/domain.htm')
    data = api.text
    soup = BeautifulSoup(data, 'html.parser')
    save = open('hasil1.txt', 'w')
    for link in soup.findAll('a'):
        gun = link.get('href')
        save.write(gun + '\n')
        print gun

    print p + ('result save : ' + h + 'hasil1.txt') + p
if pilih == '2':
    junior = raw_input('IP/DOMAIN : ')
    api = requests.get('https://webiplookup.com/' + junior)
    data = api.text
    soup = BeautifulSoup(data, 'html.parser')
    save = open('hasil2.txt', 'w')
    for link in soup.findAll('a'):
        gun = link.get('href')
        save.write(gun + '\n')
        print gun

    print p + ('result save : ' + h + 'hasil2.txt') + p
if pilih == '3':
    print 'WEBIPLOOKUP VERSI TOOLS \nTOOLS   :' + h + ' WEBIPLOOKUP \n' + p + 'VERSION : ' + h + '1.0 \n' + p + 'AUTHOR  : ' + h + 'JUNIOR404 \n' + p + 'TEAM    : ' + h + 'CRABS' + p
if pilih == '4':
    os.system('xdg-open https://youtube.com/GUNAWANID')
if pilih == '5':
    print 'thank you for using this tool'
    os.system('exit')
