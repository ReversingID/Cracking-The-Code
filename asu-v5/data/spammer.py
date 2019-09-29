import sys
import bs4
import json
import random
import requests
import interpreter
from data import login,token
from data.color import *
from data import language
from data import pagespam
from data.chatSpammer import *
from data import grupSpammer
from data import online_sender
from data import page_wallspam
from multiprocessing.pool import ThreadPool


#<-- auto tag -->

class autotag:
    def __init__(self):
        self.ok=[]
        self.al()

    def al(self):
        try:
            self.a=open(raw_input("[?] account list: ")).read().splitlines()
        except Exception as e:
            print "[!] %s"%(e)
            self.al()
        self.ck()

    def g(self,a):
        p=requests.Session()
        s=token.token(a)
        if s !=False:
            lo=login.log(p,a)
            if lo !=False:
                self.randc(s,p)

    def ck(self):
        print "+ <n> for other msg,ex: best product<n>good"
        self.cs=raw_input("[?] message: ").split("<n>")
        if self.cs =="":self.ck()
        else:self.uu()

    def uu(self):
        self.cp=raw_input("[?] post url: ").replace("www.facebook.com","mbasic.facebook.com")
        if self.cp =="":self.uu()
        else:
            ThreadPool(input("[?] Thread: ")).map(self.g,self.a)
            raw_input("\npress enter to menu...")
            interpreter.ASU()

    def randc(self,t,p):
        dt=[]
        dok=[]
        for i in requests.get(
            "https://graph.facebook.com/me/friends?access_token=%s"%(
                t)).json()["data"]:
            dt.append(i["id"])
        for i in range(5):
            dok.append("@[%s:1]\n"%(dt[random.randrange(0,len(dt))]))
        self.ok="%s %s"%("".join(dok),random.choice(self.cs))
        self.postcoment(p,self.cp,self.ok)

    def postcoment(self,cookies,url,comments):
        data=[]
        bs=bs4.BeautifulSoup(cookies.get(url).text,"html.parser")
        for i in bs("form"):
            try:
                if "/a/comment.php" in i["action"]:
                    data.append("https://mbasic.facebook.com"+i["action"])
                    break
            except:pass
        for i in bs("input"):
            try:
                if "fb_dtsg" in i["name"]:data.append(i["value"])
                if "jazoest" in i["name"]:data.append(i["value"]);break
            except:pass
        if len(data) !=3:
            return None
        else:
            self.post(
                cookies,data[0],fb_dtsg=data[1],
            jazoest=data[2],comment_text=comments)

    def post(self,*args,**kwds):
        if args[0].post(args[1],data=kwds).status_code ==200:
            print("%s[*]%s %s"%(G,N,"send success."))
        else:
            print("%s[*]%s %s"%(R,N,"send fail."))

#<-- comments spammers -->

class commentspam(object):
    def __init__(self):
        return None

    def postcoment(self,cookies,url,comments):
        data=[]
        bs=bs4.BeautifulSoup(cookies.get(url).text,"html.parser")
        for i in bs("form"):
            try:
                if "/a/comment.php" in i["action"]:
                    data.append("https://mbasic.facebook.com"+i["action"])
                    break
            except:pass
        for i in bs("input"):
            try:
                if "fb_dtsg" in i["name"]:data.append(i["value"])
                if "jazoest" in i["name"]:data.append(i["value"]);break
            except:pass
        if len(data) !=3:
            return None
        else:
            commentspam().post(
                cookies,data[0],fb_dtsg=data[1],
            jazoest=data[2],comment_text=comments)

    def post(self,*args,**kwds):
        if args[0].post(args[1],data=kwds).status_code ==200:
            print("%s[*]%s %s"%(G,N,"send success."))
        else:
            print("%s[*]%s %s"%(R,N,"send fail."))

class comments:
    def __init__(self):
        config=json.loads(open("config/config.json").read())
        self.s=requests.Session()
        s=login.log(self.s,config["email"]+"|"+config["pass"])
        if s is True:
            self.url()
        else:exit(R+"[!]"+N+" Login failed.")
    def url(self):
        self.urls=raw_input(G+"[*]"+N+" Post URL: ")
        if self.urls =="":
            self.url()
        else:
            if "mbasic" in self.urls:
                print(G+"[*]"+N+" <s> for new lines and (,) coma for other msg")
                self.msg()
            else:print(
                R+"[!]"+N+" get url on mbasic.facebook.com pls");self.url()

    def msg(self):
        self.r=raw_input(G+"[?]"+N+" message: ").replace("<s>","\n").split(",")
        self.count()

    def count(self):
        try:
            self.c=input(G+"[?]"+N+" Count: ")
        except Exception as e:
            print(R+"[!]"+N+" "+str(e));self.count()
        self.thr()

    def thr(self):
        try:
            self.t=input(G+"[?]"+N+" Thread: ")
        except Exception as e:
            print("%s[!]%s %s"%(R,N,e))
            self.thr()
        ThreadPool(self.t).map(self.kirim,range(self.c))

    def kirim(self,mes):
        commentspam().postcoment(
            self.s,self.urls,comments=random.choice(self.r))

# mass change nickname

class cn(object):
    def __init__(self):
        self.option=""
        self.namage={
            "1":"nickname",
            "2":"maiden_name",
            "3":"alternate_spelling",
            "4":"married_name",
            "5":"fathers_name",
            "6":"birth_name",
            "7":"former_name",
            "8":"name_with_title",
            "9":"other"}
        self.f=0
        self.o=0
        self.k=0
        self.success=[]
        self.x()

    def x(self):
        try:
            self.a=open(
                raw_input("%s[?]%s Account List: "%(G,N))).read().splitlines()
        except Exception as e:
            print("%s[*]%s %s"%(R,N,e))
            self.x()
        self.cx()

    def cx(self):
        print("\n\t [ Select Option ]\n")
        for x in enumerate(["Nama Panggilan","Nama Sebelum Menikah",
            "Ejaan Alternatif",
            "Nama setelah Menikah",
            "Nama Ayah",
            "Nama Kecil",
            "Nama Sebelumnya",
            "Nama dengan Gelar",
            "Lainnya"]):
            print "%s. %s"%(x[0]+1,x[1])
        print
        self.cc()

    def cc(self):
        try:
            opt=raw_input("%s[?]%s Option>> "%(G,N))
            self.option=self.namage[opt]
        except Exception as (e):
            print "%s[!]%s %s"%(R,N,e)
            self.cc()
        print "[+)> DropDown: %s"%(self.option)
        self.n()

    def n(self):
        self.c=raw_input("%s[?]%s NickName: "%(G,N))
        if self.c =="":
            self.n()
        self.thr()

    def thr(self):
        try:
            self.t=ThreadPool(input("%s[?]%s Thread: "%(G,N)))
        except Exception as (e):
            print "%s[!]%s %s"%(R,N,e)
            self.thr()
        self.t.map(self.login,self.a)
        if len(self.success) !=0:
            print "\n[+] Success: %s"%(len(self.success))
            for x in self.success:
                print "[+] %s"%(x)
        else:
            print("\n[-] no result.")
        print("\n[+] finished.")
        raw_input("press enter to menu...")
        interpreter.ASU()

    def login(self,account):
        s=requests.Session()
        z=s.post(
        "https://mbasic.facebook.com/login",
            data={
                "email":account.split("|")[-0],
                "pass":account.split("|")[-1]
            }
        ).url
        if "save-device" in z or "m_sess" in z or "home.php" in z:
            language.lang(s,"https://mbasic.facebook.com/language.php")
            self.cng(s,"https://mbasic.facebook.com/profile/edit/info/nicknames",
                account)
        else:
            self.f+=1
        print "\r[+] Running: %s/%s LoginFail:-%s Error-:%s"%(
            self.o,len(self.a),self.f,self.k),;sys.stdout.flush()

    def cng(self,s,url,account):
        data=[]
        data2=[]
        g=bs4.BeautifulSoup(s.get(url).text,"html.parser")
        for x in g("form"):
            if "fieldwithtextanddropdown" in x["action"]:
                data.append("https://mbasic.facebook.com/%s"%(x["action"]))
        for x in g("input"):
            try:
                if "fb_dtsg" in x["name"]:
                    data.append(x["value"])
                if "jazoest" in x["name"]:
                    data.append(x["value"])
                if "additional_types" in x["name"]:
                    data.append(x["name"])
            except:pass
        if len(data) ==4:
            s.post(data[0],
            data={
                "fb_dtsg":data[1],
                "jazoest":data[2],
                data[3]:"nicknames",
                "dropdown":self.option,
                "text":self.c,"checkbox":"on",
                "save":"Simpan"
            }).text
            self.success.append(account)
            self.o+=1
        else:self.k+=1

# Mass Change Bio
class cb(object):
    def __init__(self):
        self.f=0
        self.o=0
        self.ok=[]
        self.i="https://mbasic.facebook.com/{}"
        self.ak()

    def ak(self):
        try:
            self.a=open(raw_input(
                    "%s[?]%s Account list: "%(G,N))).read().splitlines()
        except Exception as e:
            print("%s[!]%s %s"%(R,N,e))
            self.ak()
        print("%s[*]%s %s account loaded."%(G,N,len(self.a)))
        self.bio()

    def bio(self):
        self.b=raw_input("%s[?]%s New Bio: "%(G,N))
        if self.b =="":
            self.bio()
        if len(self.b)<6:
            print ("%s[!]%s bio must contain 6characters."%(R,N))
            self.bio()
        self.thread()

    def thread(self):
        try:
            self.th=ThreadPool(input("%s[?]%s Thread: "%(G,N)))
        except Exception as e:
            print("%s[!]%s %s"%(R,N,e))
            self.thread()
        self.th.map(self.change,self.a)
        print "\n\n"
        for x in self.ok:
            print x
        raw_input("\n\n[*] finished.\npress enter to menu...")
        interpreter.ASU()

    def change(self,a):
        s=requests.Session()
        log=s.post(self.i.format("login"),
        data={
            "email":a.split("|")[-0],
            "pass":a.split("|")[-1]
        }).url
        if "save-device" in log or "m_sess" in log or "home.php" in log:
            language.lang(s,self.i.format("language.php"))
            self.nb(s,a)
        else:
            self.f+=1
        print "\r%s[*]%s Change bio: %s/%s Login Fail: %s"%(
            G,N,self.o,len(self.a),self.f),;sys.stdout.flush()

    def nb(self,s,a):
        data=[]
        k=bs4.BeautifulSoup(
            s.get(self.i.format("profile/basic/intro/bio")).text,
        features="html.parser")
        for x in k("input"):
            try:
                if "fb_dtsg" in x["name"]:
                    data.append(x["value"])
                if "jazoest" in x["name"]:
                    data.append(x["value"])
            except:pass
        if len(data) ==2:
            s.post(self.i.format("profile/intro/bio/save"),
            data={
                "fb_dtsg":data[0],
                "jazoest":data[1],
                "bio":self.b,
                "submit":"Simpan"
            }).text
            self.ok.append("[*] %s : %s ->%sOK%s"%(a,self.b,G,N))
            self.o+=1

# Mass Up Status
class profilepost(object):
    def __init__(self):
        self.fail=0
        self.okk=0
        self.i="https://mbasic.facebook.com/{}"
        print("%s[!]%s sparator: |"%(R,N))
        self.list()

    def list(self):
        try:
            self.a=open(
                raw_input("%s[?]%s Account List: "%(
            G,N))).read().splitlines()
        except Exception as __error__:
            print("%s[!]%s %s"%(R,N,__error__))
            self.list()
        print("%s[*]%s use coma (,) for random msg: p,hello"%(R,N))
        self.openfile()

    def openfile(self):
        try:
            self.poto=raw_input("%s[?]%s message: "%(G,N))
            if self.poto =="":
                self.openfile()
        except Exception as __error__:
            print("%s[!]%s %s"%(R,N,__error__))
            self.openfile()
        self.thread()

    def thread(self):
        try:
            self.t=ThreadPool(input("%s[?]%s Thread: "%(G,N)))
        except Exception as __error__:
            print("%s[!]%s %s"%(R,N,__error__))
            self.thread()
        self.t.map(self.ganti,self.a)
        print("\n[*] finished.")
        raw_input("press enter to menu...")
        interpreter.ASU()


    def ganti(self,a):
        s=requests.Session()
        p=s.post(self.i.format("login"),
            data=
                {
                    "email":a.split("|")[-0],
                    "pass":a.split("|")[-1]
                }
        ).url
        if "save-device" in p or "m_sess" in p or "home.php" in p:
            self.ok(s,a)
        else:
            self.fail+=1

    def ok(self,s,a):
        data=[]
        bs=bs4.BeautifulSoup(
            s.get(self.i.format("profile.php")).text,
        features="html.parser")
        for x in bs("form"):
            if "composer" in x["action"]:
                data.append(self.i.format( x["action"]))
        for x in bs("input"):
            try:
                if "fb_dtsg" in x["name"]:
                    data.append(x["value"])
                if "jazoest" in x["name"]:
                    data.append(x["value"])
                if "privacyx" in x["name"]:
                    data.append(x["value"])
                if "target" in x["name"]:
                    data.append(x["value"])
            except:pass
        if len(data) ==5:
            s.post(data[0],
            data=
                {
                    "fb_dtsg":data[1],
                    "jazoest":data[2],
                    "privacyx":data[3],
                    "r2a":"1",
                    "xhpc_timeline":"1",
                    "target":data[4],
                    "c_src":"timeline_self",
                    "cwevent":"composer_entry",
                    "referrer":"timeline",
                    "ctype":"inline",
                    "cver":"amber",
                    "xc_message":random.choice(self.poto.split(",")),
                    "view_post":"Kirim"})
            self.okk+=1
            print("\r%s[*]%s Sending-:%s/%s Login fail-:%s"%(
                G,N,self.okk,len(self.a),self.fail)),;sys.stdout.flush()

class main:
    def __init__(self):
        print '\n\t[ Select Actions ]\n'
        print '  {%s01%s} Chat Spammers'%(G,N)
        print '  {%s02%s} Group Chat Spammers'%(G,N)
        print '  {%s03%s} Page Spammers'%(G,N)
        print '  {%s04%s} Group Spammers'%(G,N)
        print '  {%s05%s} Status Mass Spammers'%(G,N)
        print '  {%s06%s} Bio Mass Spammers'%(G,N)
        print '  {%s07%s} Nickname Mass Change Spammers'%(G,N)
        print '  {%s08%s} Comments Spammers'%(G,N)
        print '  {%s09%s} Comments Spammers + auto tag with account list'%(G,N)
        print '  {%s10%s} Back To Menu Option\n'%(R,N)
        self.pilih()

    def backk(self):
        import interpreter
        raw_input("press enter to menu...")
        interpreter.ASU()

    def pilih(self):
        self.asu=raw_input("%s[%s+%s]%s Actions>> " %(G, R, G, N))
        if self.asu =="":
            self.pilih()
        elif self.asu =="1" or self.asu =="01":
            self.chat()
        elif self.asu == '2' or self.asu == '02':
            self.grup()
        elif self.asu =="3" or self.asu =="03":
            self.page()
        elif self.asu =="4" or self.asu =="04":
            self.other()
        elif self.asu =="5" or self.asu =="05":
            profilepost()
        elif self.asu =="6" or self.asu =="06":
            cb()
        elif self.asu =="7" or self.asu =="07":
            cn()
        elif self.asu =="8" or self.asu =="08":
            comments()
            print("\n[+] finished.")
            self.backk()
        elif self.asu =="9" or self.asu =="09":
            autotag()
        elif self.asu =="10":
            self.backk()
        else:
            print("%s[!]%s invalid options!"%(R,N))
            self.pilih()

    def page(self):
        print '\n\t[ Select Actions ]\n'
        print '{%s01%s} Page Chat Spammers'%(G,N)
        print '{%s02%s} Page Wall Spammers'%(G,N)
        print '{%s03%s} Page Comments Spammers'%(G,N)
        print '{%s04%s} Back To Menu Option\n'%(R,N)
        self.pilpage()

    def pilpage(self):
        r=raw_input("%s[%s+%s]%s Actions>> " %(G, R, G, N))
        if r =="1" or r =="01":
            pagespam.pejSpam()
            self.backk()
        elif r =="02" or r =="2":
            page_wallspam.pejSpam()
            self.backk()
        elif r =="":
            self.pilpage()
        elif r =="3" or r =="03":
            pagespam.wallpage()
            self.backk()
        elif r =="4" or r =="04":
            self.backk()
        else:
            print("%s[!]%s invalid options!"%(R,N))
            self.pilpage()

    def chat(self):
        print '\n\t[ Select Actions ]\n'
        print '  {%s01%s} Single Chat Spammer' % (G, N)
        print '  {%s02%s} Mass Chat Spammer With List Of ID Targets' % (G, N)
        print '  {%s03%s} Online Friends Sender' % (G, N)
        print '  {%s04%s} Spam ALL inbox list'%(G,N)
        print '  {%s05%s} Back To Menu Option\n'%(R,N)
        self.chatpilih()

    def chatpilih(self):
        r=raw_input("%s[%s+%s]%s Actions>> " %(G, R, G, N))
        if r == '1' or r == '01':
            try:
                SPAMMER()
                self.backk()
            except Exception as __errors__:
                print("%s[!]%s %s"%(R,N,__errors__))
        elif r == '2' or r == '02':
            massal()
            self.backk()
        elif r == '3' or r == '03':
            online_sender.buddy()
            self.backk()
        elif r == '4' or r == '04':
            spamChatlist()
            self.backk()
        elif r =="5" or r =="05":
            self.backk()
        elif r =="":
            return self.chatpilih()
        else:
            print('[!] Invalid Options!')
            self.chatpilih()

    def grup(self):
        print '\n\t[ Select Actions ]\n'
        print '  {%s01%s} Single Group Chat Spam' % (G, N)
        print '  {%s02%s} Mass Spam With List Of Group ID\n' % (G, N)
        print '  {%s03%s} Back To Menu Option\n'%(R,N)
        self.grupil()

    def grupil(self):
        r=raw_input("%s[%s+%s]%s Actions>> " %(G, R, G, N))
        if r == '1' or r == '01':
            grupSpammer._grupSpammer()
            self.backk()
        elif r =="2" or r =="02":
            grupSpammer._spamMassal()
            self.backk()
        elif r =="3" or r =="03":
            self.backk()
        elif r =="":
            self.grupil()
        else:
            print("%s[!]%s invalid options!"%(R,N))
            self.grupil()

    def other(self):
        print '\n\t[ Select Actions ]\n'
        print '  {%s01%s} Mass Your Group Spam'%(G,N)
        print '  {%s02%s} Single Your Group Spam v2'%(G,N)
        print '  {%s03%s} Back To Menu Option\n'%(R,N)
        self.otherpil()

    def otherpil(self):
        r=raw_input("%s[%s+%s]%s Actions>> " %(G, R, G, N))
        if r =='1' or r =='01':
            grupSpammer.spammas()
        elif r =='2' or r =='02':
            grupSpammer.spamGroups()
        elif r =='3' or r =='03':
            self.backk()
        elif r =="":
            self.otherpil()
        else:
            print("%s[!]%s invalid options!"%(R,N))
            self.otherpil()

