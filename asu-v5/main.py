import re, os, bs4, sys, time, json, random, requests, interpreter, subprocess
from data.color import *

def cktime(url):
    s    = bs4.BeautifulSoup(requests.get(url).text,"html.parser")
    data = {"day":s.find("div",{"id":"el_d1"}).text,
            "hour":s.find("div",{"id":"el_h1"}).text,
            "minute":s.find("div",{"id":"el_m1"}).text,
            "sec":s.find("div",{"id":"el_s1"}).text}
    return "[+] Masa Aktif  : %s - %s - %s - %s"%(data["day"],data["hour"],data["minute"],data["sec"])

def count(delay,m,day,mon,year,hor,min,sec):
    g   = requests.get("https://raw.githubusercontent.com/asu-labs/server/master/server1.txt").text.replace("\n","").format("/index.php")
    req = requests.post("https://www.timeanddate.com/scripts/gocountdown.php",
          data={
          "theme":"generic",
          "msg":m,
          "day":day,
          "month":mon,
          "year":year,
          "hour":hor,
          "min":min,
          "sec":sec,
          "p0":"108",
          "p0txt":"Jakarta",
          "ud":"1",
          "ud":"0",
          "ud":"0",
          "csz":"on",
          "submit":"Create Countdown"})
    open('/data/data/com.termux/files/usr/lib/.k','w').write(m)
    return requests.post(g, data={"id":m,"url":req.url+delay}).text

class reg(object):
    def __init__(self):
        os.system("clear")
        self.user=self.id()
        print "[*] new user: %s%s%s\n" % (G,self.user,N)
        self.menu()

    def menu(self):
        print "[1] 1 days activation id (free trial)"
        print "[2] 1 month activation (IDR: $2 / Rp.20.0000)"
        print "[3] Unlimited Feature (IDR: $10 / Rp.100.0000)\n"
        self.c()

    def c(self):
        r=raw_input("[?> ")
        if r =="1":
            self.hr()
        elif r =="2":
            self.mon()
        elif r =="3":
            self.year()
        elif r =="4":
            self.zp()
        elif r =="":
            self.c()
        else:
            print "[!] invalid option"
            self.c()

    def year(self):
        raw_input("[!] press enter to get unlimited feature (whatsapp)")
        subprocess.check_output(["am","start","https://api.whatsapp.com/send?phone=62895353484895&text=saya%20ingin%20membeli%20asu%20toolkit%20unlimited"])

    def hr(self):
        td = []
        p  = bs4.BeautifulSoup(requests.get("https://www.timeanddate.com/calendar/monthly.html?year=%s&month=%s&country=65"%(time.localtime()[0],time.localtime()[1])).text,"html.parser")
        for x in p.find_all("div",class_="ccd"):
            td.append(x.text)
        if time.localtime()[2] == int(td.pop()):
            exit(count(" [ 1 HARI ]",self.user,
            "1",time.localtime()[1],time.localtime()[0],
            time.localtime()[3],time.localtime()[4],
            time.localtime()[5]))
        else:
            exit(count(" [ 1 HARI ]",self.user,
            time.localtime()[2]+1,
            time.localtime()[1],time.localtime()[0],
            time.localtime()[3],time.localtime()[4],
            time.localtime()[5]))

    def mon(self):
        td = []
        p  = time.localtime()[1]
        if p ==12:
            exit(count(" [ 1 BULAN ]",self.user,
            time.localtime()[2],"1",time.localtime()[0],
            time.localtime()[3],time.localtime()[4],
            time.localtime()[5]))
        else:
            exit(count(" [ 1 BULAN ]",self.user,
            time.localtime()[2],time.localtime()[1]+1,
            time.localtime()[0],
            time.localtime()[3],time.localtime()[4],
            time.localtime()[5]))

    def zp(self):
        exit(count(" [ 1 BULAN ]",self.user,
        time.localtime()[2],time.localtime()[1],
        time.localtime()[0],
        time.localtime()[3],time.localtime()[4]+5,
        time.localtime()[5]))

    def id(self):
        self.ab = []
        ab      = list("abcdefghijklmnopqrstuvwxyz1234567890")
        for x in range(10):
            self.ab.append(random.choice(ab))
            self.ab.append(random.choice(ab).upper())
        return "".join(self.ab)

def login():
    req = requests.Session()
    e   = raw_input('[!] No Account Detected\n[*] Login Your Fb\n[?] Username: ')
    p   = raw_input('[?] Password: ')
    print '[*] Login ...'
    s = req.post('https://mbasic.facebook.com/login', data={'email': e, 'pass': p}).url
    if 'save-device' in s or 'm_sess' in s:
        i = json.dumps({'email': e, 'pass': p, 'name': bs4.BeautifulSoup(req.get('https://mbasic.facebook.com/me').text, features='html.parser').find('title').text})
        open('config/config.json', 'w').write(i)
        exit('[*] Login Success..\n[!] Run again: python2 ASU.py')
    if 'checkpoint' in s or 'challange' in s:
        exit('[!] checkpoint challange,your account was locked by facebook,pls open your facebook in browser before you login with asu toolkit')
    else:
        exit('[!] Login Failed.\n[!] Run again: python2 ASU.py')

class regis(object):
    def __init__(self):
        self.kent="%s{}"%(requests.get("https://raw.githubusercontent.com/asu-labs/server/master/server1.txt").text.replace("\n",""))
        self.checkSession()

    def akin(self):
        if os.path.exists('config'):
            if os.path.exists('config/config.json'):
                if os.path.exists('config/config.json') != 0:
                    interpreter.ASU()
                else:
                    login()
            else:
                login()
        else:
            os.mkdir('config')
            login()

    def checkSession(self):
        self.dt = '/data/data/com.termux/files/usr/lib/.k'
        if os.path.exists(self.dt):
            if os.path.getsize(self.dt) != 0:
                self.cek()
            else:
                reg()
        else:
            reg()

    def cek(self):
        data  = []
        cekid = open(self.dt).read().replace("\n","")
        s     = requests.get(self.kent.format("trialconfirm.txt")).text
        for x in s.split("\n"):
            if x == "":
                pass
            if len(re.findall(cekid,x)) != 0:
                data.append(x)
        if len(data) != 0:
            z = cktime(re.findall("-> (.*?) ",data[0])[0])
            print z
            if "0 - 0 - 0 - 0" in z:
                print "[:(] the trial time is up"
                r = raw_input("[?] buy active period? y/n): ").lower()
                if r == "y":
                    reg()
                else:
                    exit("[*] bye")
            else:
                self.akin()
        else:
            z = requests.get(self.kent.format("trial.txt")).text
            if len(re.findall(cekid,z)) != 0:
                print("[!] id %s%s%s unconfirmed" % (G,cekid,N))
                raw_input("[!] press enter to get confirmation admin (whatsapp) ..")
                subprocess.check_output(["am","start","https://api.whatsapp.com/send?phone=62895353484895&text=konfirmasi saya dengan id: %s" % (open("/data/data/com.termux/files/usr/lib/.k").read())]);
                exit()
            else:
                reg()
