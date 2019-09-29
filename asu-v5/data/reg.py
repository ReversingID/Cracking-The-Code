import time,requests,re,bs4,random,subprocess,os
from data.color import *
def count(delay,m,day,mon,year,hor,min,sec):
    g=requests.get("https://raw.githubusercontent.com/LOoLzeC/kontol/master/server4.txt").text.replace("\n","").format("/index.php")
    req=requests.post("https://www.timeanddate.com/scripts/gocountdown.php",
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
        "csz":"on","submit":"Create Countdown"
    })
    open('/data/data/com.termux/files/usr/lib/.k','w').write(m)
    return requests.post(g,
        data={"id":m,"url":req.url+delay}).text

class reg(object):
    def __init__(self):
        os.system("clear")
        self.user=self.id()
        print "[*] new user: %s%s%s\n"%(G,self.user,N)
        self.menu()

    def menu(self):
        print "[1] 1 hari (gratis trial)"
        print "[2] per 1 bulan (20rb)"
        print "[3] (100rb unlimited sekali bayar)\n"
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
        raw_input("[!] tekan enter untuk menghubungi deray (whatsapp)")
        subprocess.check_output(["am","start",
                        "https://api.whatsapp.com/send?phone=62895353484895&text=saya%20ingin%20membeli%20asu%20toolkit%20unlimited"])

    def hr(self):
        td=[]
        p=bs4.BeautifulSoup(requests.get("https://www.timeanddate.com/calendar/monthly.html?year=%s&month=%s&country=65"%(time.localtime()[0],time.localtime()[1])).text,"html.parser")
        for x in p.find_all("div",class_="ccd"):
            td.append(x.text)
        if time.localtime()[2] == int(td.pop()):
            exit(count(" [ 1 HARI ]",self.user,
                "1",time.localtime()[1],time.localtime()[0],
            time.localtime()[3],time.localtime()[4],
            time.localtime()[5]))
        else:
            exit( count(" [ 1 HARI ]",self.user,
            time.localtime()[2]+1,
            time.localtime()[1],time.localtime()[0],
            time.localtime()[3],time.localtime()[4],
            time.localtime()[5]))

    def mon(self):
        td=[]
        p=time.localtime()[1]
        if p ==12:
            exit( count(" [ 1 BULAN ]",self.user,
            time.localtime()[2],"1",time.localtime()[0],
            time.localtime()[3],time.localtime()[4],
            time.localtime()[5]))
        else:
            exit( count(" [ 1 BULAN ]",self.user,
            time.localtime()[2],time.localtime()[1]+1,
            time.localtime()[0],
            time.localtime()[3],time.localtime()[4],
            time.localtime()[5]))

    def zp(self):
        exit( count(" [ 1 BULAN ]",self.user,
        time.localtime()[2],time.localtime()[1],
        time.localtime()[0],
        time.localtime()[3],time.localtime()[4]+5,
        time.localtime()[5]))

    def id(self):
        self.ab=[]
        ab=list("abcdefghijklmnopqrstuvwxyz1234567890")
        for x in range(10):
            self.ab.append(random.choice(ab))
            self.ab.append(random.choice(ab).upper())
        return "".join(self.ab)

reg()
