import os, sys, time, requests
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
logo = R + '\n   ___________             _\n  / ___/_  __/________    (_)___ _____  _____\n  \\__ \\ / / / ___/ __ \\  / / __ `/ __ \\/ ___/\n ___/ // / / /  / /_/ / / / /_/ / / / (__  )\n/____//_/ /_/   \\____/_/ /\\__,_/_/ /_/____/\n     ' + G + 'Mr.Gaming 215' + R + '   /___/'

def run(x):
    for n in x + '\n':
        sys.stdout.write(n)
        sys.stdout.flush()
        time.sleep(0.1)


def main():
    os.system('clear')
    print logo
    print
    no = raw_input(Y + '[' + W + '?' + Y + '][' + W + 'TARGET' + Y + ']>> ' + G)
    run(Y + '[!] Checking Target ...')
    time.sleep(4)
    if no < 5:
        print R + '[!] Target Not Found'
        sys.exit()
    elif '62' in no or '+62' in no or '08' in no:
        print Y + '[' + W + 'LOCATION' + Y + ']: ' + W + 'Indonesian'
        time.sleep(4)
        serang(no)
    else:
        print R + '[!] Tool Not Support ' + no
        print G + '[!] Tool Support Indonesian Number'
        sys.exit()


def serang(no):
    os.system('clear')
    print logo
    print
    run(Y + '[!] Attack ...')
    time.sleep(2)
    while True:
        try:
            print G + 'Success Send Trojans Mr.Gaming: ' + Y + no
        except:
            pass


if __name__ == '__main__':
    try:
        main()
    except requests.exceptions.ConnectionError:
        print R + '[x] No Connection'
        sys.exit()
