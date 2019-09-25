import os, sys
os.system('clear')
os.system('sleep 0.5')
print '\x1b[1;34;1mSetelah ini kamu akan otomatis pergi ke browser'
os.system('sleep 0.5')
print ''
os.system('sleep 2')
print '\x1b[1;34;1mUntuk Mengambil License...'
os.system('xdg-open https://linkduit.net/VrjIl')
print ''
print ''
password = 'INDONESIA-JAYA-MERDEKA-1945-NKRI-HARGA-MATI-15/11/03'

def restart():
    ngulang = sys.executable
    os.execl(ngulang, ngulang, *sys.argv)


def main():
    pwd = raw_input('License ==> ')
    if pwd == password:
        print '\n\x1b[1;34mSelamat Datang Di Script Nilkahis Cyber',
        sys.exit()
    else:
        print '\n\x1b[1;36mPassword Salah !!!\x1b[00m'
        print 'Coba Lagi\n'
        restart()


try:
    main()
except KeyboardInterrupt:
    os.system('clear')
    restart()
