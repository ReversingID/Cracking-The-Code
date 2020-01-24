import marshal, os, sys, time
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

def keluar():
    print Y + '[!] ' + C + 'Keluar'
    os.system('exit')


def ban():
    os.system('clear')
    print ' ___          ___                _ _'
    print '| _ \\  ___   / __|___ _ __  _ __(_) |___'
    print "|  _/ |___| | (__/ _ \\ '  \\| '_ \\ | / -_)"
    print '|_|          \\___\\___/_|_|_| .__/_|_\\___|'
    print


def py2():
    try:
        ban()
        print R + ' Ex = /sdcard/namafile.py'
        print
        a = raw_input(C + '[?] Masukan File' + G + ' > ')
        x = open(a).read()
        b = compile(x, '', 'exec')
        c = marshal.dumps(b)
        d = open(a, 'w')
        d.write('#Aouthour    : Mr.Gaming\n')
        d.write('#GITHUB      : https://github.com/clayhacker-max\n')
        d.write('#Sekolah     : Smk Al-Idhar\n')
        d.write('import marshal\n')
        d.write('exec(marshal.loads(' + repr(c) + '))')
        d.close()
        time.sleep(1)
        print
        print R + '[+]' + G + ' File Berhasil Di Compile'
        print R + '[!]' + G + ' Silahkan Cek Sendiri >> ' + a
        print
        raw_input(W + '[!]' + R + ' Kembali')
        awal()
    except KeyboardInterrupt:
        print
        print G + '[!]' + R + ' ERROR'
        print
        keluar()


def py3():
    try:
        os.system('clear')
        ban()
        print R + ' Ex = /sdcard/namafile.py'
        print
        a = raw_input(C + '[?] Masukan File ' + G + ' > ')
        x = open(a).read()
        b = compile(x, '', 'exec')
        c = marshal.dumps(b)
        d = open(a, 'w')
        d.write('#Compyled By : Mr.Gaming\n')
        d.write('#GITHUB      : https://github.com/clayhacker-max\n')
        d.write('#Sekolah     : Smk Al-Idhar\n')
        d.write('import marshal\n')
        d.write('exec(marshal.loads(' + repr(c) + '))')
        d.close()
        time.sleep(1)
        print
        print R + '[+]' + G + ' File Berhasil Di Compile '
        print R + '[!]' + G + ' Silahkan Cek Sendiri >> ' + a
        print
        raw_input(W + '[!]' + R + ' Kembali')
        awal()
    except KeyboardInterrupt:
        print
        print G + '[!]' + R + ' ERROR'
        print
        keluar()


def awal():
    os.system('clear')
    print R + ' ___          ___                _ _'
    print R + '| _ \\  ___   / __|___ _ __  _ __(_) |___'
    print W + "|  _/ |___| | (__/ _ \\ '  \\| '_ \\ | / -_)"
    print W + '|_|          \\___\\___/_|_|_| .__/_|_\\___| ' + G + 'https://github.com/clayhacker-max'
    print C + 50 * '-'
    print B + '[+] Author  : Mr.Gaming'
    print B + '[+] Nomor   : 08xxxxxxxx45'
    print B + '[+] Sekolah : Smk Al-Idhar'
    print C + 50 * '-'
    print
    print Y + '[1].' + G + 'PYTHON2'
    print Y + '[2].' + G + 'PYTHON3'
    print Y + '[0].' + G + 'EXIT'
    print
    pilih = raw_input(Y + '[?]' + W + ' Masukan Pilihan Anda ' + G + '> ')
    if pilih == '1':
        py2()
    elif pilih == '2':
        py3()
    elif pilih == '0':
        keluar()
    else:
        print R + '[!] Pilihan ' + pilih + ' tidak ada'
        keluar()


if __name__ == '__main__':
    awal()
