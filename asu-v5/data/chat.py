import requests,os,json,time
from data.color import *
import random

print
class chat:
    def __init__(self):
        self.bulan={
            "1":"januari","2":"februari",
            "3":"maret","4":"april","5":"mei",
            "6":"juni","7":"juli","8":"agustus",
            "9":"september","10":"oktober",
            "11":"november","12":"desember"}
        self.path=".asu-chat-config.txt"
        self.server="https://jasa-huruftimbul.cloudaccess.host/{}"
        if os.path.exists(self.path):
            if os.path.getsize(self.path) !=0:
                self.config=json.loads(open(self.path).read())
                self.openchat()
            else:
                self.regis()
        else:self.regis()

    def openchat(self):
        print "\t\t[ CHATROOM]\n"
        for i in requests.get(self.server.format("chat.txt")).text.splitlines():
            try:
                s=json.loads(i)
                lis=['\033[1;37m\033[31m', '\033[1;37m\033[34m',
                    '\033[1;32m','\033[33m','\033[36m']
                print "[(%s)> %s%s%s]: %s"%(s["time"],
                    random.choice(lis),s["name"],N,s["message"])
            except:pass
        print "\n\t[CTRL+C] for refresh chat\n"
        while True:
            try:
                self.reply()
            except:
                os.system("clear")
                self.openchat()
                self.reply()


    def reply(self):

        self.cht=raw_input("[%s]> "%(self.config["name"]))
        if self.cht =="":
            self.reply()
        else:
            s=time.localtime()
            print("[*] "+requests.post(
            self.server.format("chat.php"),
                data={"chat":self.cht,"name":self.config["name"],
            "time":"%s %s %s|%s:%s"%(
                s[2],self.bulan[str(s[1])][0:3],s[0],s[3],s[4])}).json()["message"])
        self.reply()

    def regis(self):
        print "\t[ Create Chatroom account ]\n"
        self.name=raw_input("[?] name: ")
        if self.name =="":self.regis()
        else:
            open(self.path,"w").write(json.dumps({"name":self.name}))
            print("[+] success")
            self.config=json.loads(open(self.path).read())
            os.system("clear")
            print ("[+] opening chatroom...")
            self.openchat()
