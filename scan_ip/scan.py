import os, sys, json, hashlib, socket
from time import sleep, strftime
from random import choice as pilih
if sys.version_info.major != 2:
    print '\x1b[91mPlease Use Python v2 up'
    exit()
import urllib2

class color:
    HEADER = '\x1b[95m'
    OKBLUE = '\x1b[94m'
    OKCYAN = '\x1b[96m'
    OKGREEN = '\x1b[92m'
    WARNING = '\x1b[93m'
    FAIL = '\x1b[91m'
    ENDC = '\x1b[0m'
    BOLD = '\x1b[1m'
    DARK = '\x1b[2m'
    UNDERLINE = '\x1b[4m'
    REVERSE = '\x1b[7m'
    w = (FAIL, HEADER, OKGREEN, OKBLUE, WARNING)
    W = pilih(w)


def Banner():
    os.system('clear')
    sleep(0.2)
    print color.ENDC + color.FAIL + '|--------\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\xa6 \xe2\x95\xa6\xe2\x95\x94\xe2\x95\xa6\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\xa6  \xe2\x95\x94\xe2\x95\xa6\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\xa6----------|'
    sleep(0.2)
    print color.HEADER + '|--------\xe2\x95\x91  \xe2\x95\x91 \xe2\x95\x91 \xe2\x95\x91 \xe2\x95\x91\xe2\x95\xa3 \xe2\x95\xa0\xe2\x95\x90\xe2\x95\xa3 \xe2\x95\x91   \xe2\x95\x91 \xe2\x95\x91 \xe2\x95\x91\xe2\x95\x91 \xe2\x95\x91\xe2\x95\x91----------|'
    sleep(0.2)
    print color.OKGREEN + '|--------\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d \xe2\x95\xa9 \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x9d  \xe2\x95\xa9 \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\xa9\xe2\x95\x90\xe2\x95\x9d--------|'
    sleep(0.2)
    print color.ENDC + color.DARK + '[' + color.OKCYAN + color.DARK + strftime('%a %d.%m.%Y %H:%M %Z') + color.ENDC + color.DARK + ']\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80[' + color.WARNING + 'Cute81 TOOL v1.1t' + color.ENDC + color.DARK + ']' + color.ENDC
    print ''


def Input(text, type='vart'):
    while 1:
        try:
            if type == 'int':
                i = int(raw_input(color.BOLD + color.ENDC + '[' + color.OKGREEN + '?' + color.ENDC + ']' + color.ENDC + color.OKGREEN + text + color.ENDC))
            elif type == 'vart':
                i = raw_input(color.BOLD + color.ENDC + '[' + color.OKGREEN + '?' + color.ENDC + ']' + color.ENDC + color.OKGREEN + text + color.ENDC)
                if len(i) == 0:
                    print showstatus('Input wrong . . .', 'warn')
                    continue
                else:
                    break
        except KeyboardInterrupt:
            print showstatus('KeyboardInterrupt thrown! Exiting thread. . .', 'warn')
            exit()
        except EOFError:
            print ''
            print showstatus('Input wrong. . .', 'warn')
            continue
        except:
            print showstatus('Input wrong. . .', 'warn')
            continue
        else:
            break

    return str(i)


def showstatus(message, type='new', escape_x=None):
    icon = '*'
    if type == 'warn':
        icon = '!'
        escape = color.FAIL + color.REVERSE
        escape0 = color.FAIL
    elif type == 'new':
        icon == '*'
        escape = color.OKGREEN
        escape0 = color.OKGREEN
    if escape_x != None:
        escape = escape_x
        escape0 = escape_x
    message = color.ENDC + color.BOLD + escape + '[' + icon + ']' + color.ENDC + escape0 + message + color.ENDC
    return message


def main():
    global response
    sleep(0.2)
    server = Input('Input Domain/Ip \x1b[31m: ')
    url = 'http://ip-api.com/json/'
    try:
        ip1 = socket.gethostbyname(server)
        response = urllib2.urlopen(url + ip1)
        print color.ENDC
    except:
        print '\x1b[0m\x1b[1m\x1b[91m\x1b[7m[!]\x1b[0m\x1b[31mCheck again, Domain or Ip target wrong. . .' + color.ENDC
        sys.exit()


def Tampil():
    data = response.read()
    values = json.loads(data)
    sleep(0.3)
    print '\x1b[30;1;2m|\x1b[32mIP       \x1b[31m: \x1b[33m' + values['query']
    sleep(0.3)
    print '\x1b[30;1;2m|\x1b[32mStatus   \x1b[31m: \x1b[33m' + values['status']
    sleep(0.3)
    print '\x1b[30;1;2m|\x1b[32mProvinsi \x1b[31m: \x1b[33m' + values['regionName']
    sleep(0.3)
    print '\x1b[30;1;2m|\x1b[32mNegara   \x1b[31m: \x1b[33m' + values['country']
    sleep(0.3)
    print '\x1b[30;1;2m|\x1b[32mKota     \x1b[31m: \x1b[33m' + values['city']
    sleep(0.3)
    print '\x1b[30;1;2m|\x1b[32mISP      \x1b[31m: \x1b[33m' + values['isp']
    sleep(0.3)
    print '\x1b[30;1;2m|\x1b[32mLat,Lon  \x1b[31m: \x1b[33m' + str(values['lat']) + ',' + str(values['lon'])
    sleep(0.3)
    print '\x1b[30;1;2m|\x1b[32mZIPCODE  \x1b[31m: \x1b[33m' + values['zip']
    sleep(0.3)
    print '\x1b[30;1;2m|\x1b[32mTimeZone \x1b[31m: \x1b[33m' + values['timezone']
    sleep(0.3)
    print '\x1b[30;1;2m|\x1b[32mAS       \x1b[31m: \x1b[33m' + values['as']
    sleep(0.5)
    print '\x1b[41;97m\n[+]TERIMA KASIH TELAH MENGGUNAKAN TOOLS INI[+]\x1b[0m'


if __name__ == '__main__':
    Banner()
    main()
    Tampil()
