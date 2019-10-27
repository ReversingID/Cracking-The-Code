#mulut anda kotor
import os, sys, fileinput, time

black  = '\x1b[0;30m'
blue   = '\x1b[0;34m'
ijo    = '\x1b[0;32m'
bm     = '\x1b[0;35m'
red    = '\x1b[0;31m'
purple = '\x1b[0;35m'
brown  = '\x1b[0;33m'
abu    = '\x1b[0;37m'
gr     = '\x1b[1;32m'
Kuning = '\x1b[1;33m'
putih  = '\x1b[1;37m'

N = '\x1b[0m'
D = '\x1b[90m'
W = '\x1b[0;37m'
B = '\x1b[1;34m'
R = '\x1b[1;31m'
G = '\x1b[1;32m'
Y = '\x1b[1;33m'
C = '\x1b[1;36m'

ask    = D + '[' + B + '?' + C + '] '
sukses = G + '[' + W + '\xe2\x88\x9a' + G + '] '
eror   = R + '[' + C + '!' + B + ']'

print '\x1b[0;35m            ________                ___________'
print '\x1b[0;35m            \\______ \\   __DW__   ____ \\_   _____/ ____   ____'
print '\x1b[0;35m             |    |  \\_/ __ \\_/ ___\\ |    __)_ /    \\_/ ___\\ '
print '\x1b[0;32m' + bm + '[' + gr + '+' + bm + ']' + red + '______________________________________________________' + bm + '[' + gr + '+' + bm + ']'
print '\x1b[1;37m[' + Kuning + '01' + putih + ']' + abu + 'Encript File '
print '\x1b[1;37m[' + purple + '02' + putih + ']' + abu + 'Decrypt File'
print '\x1b[1;37m[' + red + '00' + putih + ']' + abu + 'Exit '

def dekrip():
    try:
        sc = raw_input(ask + W + 'Input Your File/sdcard ' + G + '|> ' + W)
        f = open(sc, 'r')
        filedata = f.read()
        f.close()
        newdata = filedata.replace('eval', 'echo')
        out = raw_input(ask + W + 'Output Your File /sdcard' + G + ' |> ' + W)
        f = open(out, 'w')
        f.write(newdata)
        f.close()
        os.system('touch tes.sh')
        os.system('bash ' + out + ' > tes.sh')
        os.remove(out)
        os.rename('tes.sh', out)
        print sukses + 'File Berhasil di Decrypt..'
    except KeyboardInterrupt:
        print eror + ' Berhenti!'
    except IOError:
        print eror + ' File Not Found!'


def enkrip():
    try:
        script = raw_input(ask + W + 'Input Alamat File ' + G + '> ' + W)
        output = raw_input(ask + W + 'Alamat Output File ' + G + '> ' + W)
        os.system('bash-obfuscate ' + script + ' -o ' + output)
        print sukses + 'File Berhasil Di Encript.'
    except KeyboardInterrupt:
        print eror + ' Berhenti!'
    except IOError:
        print eror + ' File Not Found!'


takok = raw_input(W + 'Input Number' + G + ' |> ')
if takok == '1' or takok == '01':
    enkrip()
elif takok == '2' or takok == '02':
    dekrip()
else:
    print eror + ' Wrong input'
