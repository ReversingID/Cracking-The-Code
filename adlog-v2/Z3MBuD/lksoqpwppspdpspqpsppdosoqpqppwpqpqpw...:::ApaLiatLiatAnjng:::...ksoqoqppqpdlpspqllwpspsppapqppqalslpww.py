from urllib2 import Request, urlopen, URLError, HTTPError
from time import sleep
import os, sys

def Logo():
    sleep(0.5)
    os.system('clear')
    sleep(0.3)
    print '\x1b[31;1m   __  __      ____                    _       ___'
    sleep(0.2)
    print '  |  \\/  |_ __|  _ \\ _   _ _ __  _ __ / |_ __ / _ \\ '
    sleep(0.2)
    print "  | |\\/| | '__| |_) | | | | '_ \\| '_ \\| | '_ \\ (_) |"
    sleep(0.2)
    print '  \x1b[37;1m| |  | | | _|  _ <| |_| | | | | | | | | | | \\__, |'
    sleep(0.2)
    print '  |_|  |_|_|(_)_| \\__\\__,_|_| |_|_| |_|_|_| |_| /_/\n'
    sleep(0.5)
    print '        Tools Scanner AdLog V2 | \x1b[32;1mBy Mr.Runn1n9\n'
    sleep(0.5)
    print '                \x1b[36;1m----------------------'
    print "                '\x1b[33;1mIndonesian The Coder\x1b[36;1m'"
    print '                          \x1b[37;1mX'
    print "                      \x1b[36;1m'\x1b[33;1mAK.Triya\x1b[36;1m'"
    print '                ----------------------\n'


def Logo2():
    os.system('clear')
    print '\x1b[31;1m   __  __      ____                    _       ___'
    print '  |  \\/  |_ __|  _ \\ _   _ _ __  _ __ / |_ __ / _ \\ '
    print "  | |\\/| | '__| |_) | | | | '_ \\| '_ \\| | '_ \\ (_) |"
    print '  \x1b[37;1m| |  | | | _|  _ <| |_| | | | | | | | | | | \\__, |'
    print '  |_|  |_|_|(_)_| \\__\\__,_|_| |_|_| |_|_|_| |_| /_/\n'
    print '        Tools Scanner AdLog V2 | \x1b[32;1mBy Mr.Runn1n9\n'
    print '                \x1b[36;1m----------------------'
    print "                '\x1b[33;1mIndonesian The Coder\x1b[36;1m'"
    print '                          \x1b[37;1mX'
    print "                      \x1b[36;1m'\x1b[33;1mAK.Triya\x1b[36;1m'"
    print '                ----------------------\n'


def Scan():
    f = open('Z3MBuD/j3mb03d.txt', 'r')
    link = raw_input('  \x1b[34;1m--------------------\n  [\x1b[37;1mEx: http://xxx.xxx\x1b[34;1m]\n    \x1b[36;1m>> \x1b[32;1mTarget \x1b[37;1m:\x1b[33;1m ')
    while True:
        sub_link = f.readline()
        if not sub_link:
            break
        req_link = 'http://' + link + '/' + sub_link
        req = Request(req_link)
        try:
            response = urlopen(req)
        except HTTPError as e:
            continue
        except URLError as e:
            continue
        else:
            os.system('clear')
            Logo2()
            print '  \x1b[32;1mFound \x1b[37;1m:\x1b[33;1m', req_link


def Space(j):
    i = 0
    while i <= j:
        print ' ',
        i += 1


Logo()
Scan()
