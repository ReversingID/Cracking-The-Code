import base64, os, sys
from time import sleep

def Logo():
    sleep(0.5)
    print "\x1b[31;1m   __  __      ____                    _       ___\n  |  \\/  |_ __|  _ \\ _   _ _ __  _ __ / |_ __ / _ \\ \n  | |\\/| | '__| |_) | | | | '_ \\| '_ \\| | '_ \\ (_) |\n  \x1b[37;1m| |  | | | _|  _ <| |_| | | | | | | | | | | \\__, |\n  |_|  |_|_|(_)_| \\__\\__,_|_| |_|_| |_|_|_| |_| /_/\n\n         \x1b[34;1m------------------------------------\n         \x1b[37;1mTools Encrypt Base64 | By \x1b[32;1mMr.Runn1n9\n         \x1b[34;1m------------------------------------\n"


os.system('clear')
Logo()
sleep(1)
cok = raw_input('  \x1b[37;1mCode :\x1b[33;1m ')
dec = base64.b64decode(cok)
sleep(1)
os.system('clear')
Logo()
print '  \x1b[37;1mResults :\x1b[32;1m', dec, '\n\x1b[37;1m'
