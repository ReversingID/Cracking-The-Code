import os, sys
print '\x1b[1;32mMasukan Username&Password:)'
print ''
print '\x1b[1;31;1mKalo Gak Tau Buka Link Dibawah Ini'
print ''
print ''
print '\x1b[37;1m===> https://linkduit.net/paWRx <==='
print ''
print ''
print ''
username = 'INDONESIA'
password = '1945'

def restart():
    ngulang = sys.executable
    os.execl(ngulang, ngulang, *sys.argv)


def main():
    uname = raw_input('Username ==> ')
    if uname == username:
        pwd = raw_input('Password ==> ')
        if pwd == password:
            print '\n\x1b[1;34mSelamat Datang Di Script Nilkahis Cyber',
            sys.exit()
        else:
            print '\n\x1b[1;36mPassword Salah !!!\x1b[00m'
            print 'Coba Lagi\n'
            restart()
    else:
        print '\n\x1b[1;36mUsername Salah !!!\x1b[00m'
        print 'Coba Lagi\n'
        restart()


try:
    main()
except KeyboardInterrupt:
    os.system('clear')
    restart()
