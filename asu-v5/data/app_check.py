import os
import re
import sys
import bs4
import json
import requests
import interpreter
from data.color import *
from multiprocessing.pool import ThreadPool

def back():
    raw_input("\n[+] press enter to menu...")
    interpreter.ASU()

class onAppByQuery:
    def __init__(self):
        self.u="https://mbasic.facebook.com/{}"
        self.log=0
        self.fail=0
        self.found=0
        self.file()

    def file(self):
        try:
            self.a=open(raw_input("[?] account list: ")).read().splitlines()
        except Exception as e:
            print "%s"%(e)
            self.file()
        self.q()

    def q(self):
        self.query=raw_input("[?] app query: ").lower()
        if self.query =="":
            self.q()
        else:
            self.out()

    def out(self):
        try:
            self.o=raw_input("[?] result filename: ")
            if self.o =="":
                self.out()
            else:
                self.outs=open("out/"+self.o,"w").close()
        except Exception as e:
            print "%s"%(e)
            self.out()
        self.thr()

    def thr(self):
        try:
            self.pool=input("[?] Thread: ")
        except Exception as e:
            print "%s"%(e)
            self.thr()
        ThreadPool(self.pool).map(self.cek,self.a)
        if os.path.getsize("out/"+self.o) !=0:
            print "\n[+] all done, %s app written saved to: out/%s"%(
                len(open("out/"+self.o).read().splitlines()),self.o)
            back()
        else:
            print "\n[-] all done, no app written with query: %s"%(self.query)
            back()

    def cek(self,a):
        print "\r[+] Checking: %s/%s - Found: %s - Login Fail: %s"%(
            self.log,len(self.a),self.found,self.fail),;sys.stdout.flush()
        z=a.split("|")
        r=requests.Session()
        s=r.post(
        "https://mbasic.facebook.com/login",
            data={
                "email":z[-0],
                "pass":z[-1]
            }
        ).url
        if "save-device" in s or "m_sess" in s:
            self.log+=1
            self.open(z,r)
        else:
            self.fail+=1

    def open(self,a,req):
        data=[]
        bs=bs4.BeautifulSoup(
            req.get(self.u.format("settings/apps/tabbed/?tab=active")).text,
        "html.parser")
        #print bs
        for i in bs.find_all("div",class_="cx"):
            if self.query in i.text.lower():
                data.append(i.text)
                open("out/"+self.o,"a+").write("[%s|%s]: %s\n"%(
                    a[-0],a[-1],i.text))
        if len(data) !=0:
            self.found+=1

class check:
    def __init__(self):
        self.u="https://mbasic.facebook.com/{}"
        self.log=0
        self.fail=0
        self.found=0
        self.file()

    def file(self):
        try:
            self.a=open(raw_input("[?] account list: ")).read().splitlines()
        except Exception as e:
            print "%s"%(e)
            self.file()
        self.out()

    def out(self):
        try:
            self.o=raw_input("[?] result filename: ")
            if self.o =="":
                self.out()
            else:
                self.outs=open("out/"+self.o,"w").close()
        except Exception as e:
            print "%s"%(e)
            self.out()
        self.thr()

    def thr(self):
        try:
            self.pool=input("[?] Thread: ")
        except Exception as e:
            print "%s"%(e)
            self.thr()
        ThreadPool(self.pool).map(self.cek,self.a)
        if os.path.getsize("out/"+self.o) !=0:
            print "\n[+] all done, %s app written saved to: out/%s"%(
                len(open("out/"+self.o).read().splitlines()),self.o)
            back()
        else:
            print "\n[-] all done, no app written"
            back()

    def cek(self,a):
        print "\r[+] Checking: %s/%s - Found: %s - Login Fail: %s"%(
            self.log,len(self.a),self.found,self.fail),;sys.stdout.flush()
        z=a.split("|")
        r=requests.Session()
        s=r.post(
        "https://mbasic.facebook.com/login",
            data={
                "email":z[-0],
                "pass":z[-1]
            }
        ).url
        if "save-device" in s or "m_sess" in s:
            self.log+=1
            self.open(z,r)
        else:
            self.fail+=1

    def open(self,a,req):
        data=[]
        bs=bs4.BeautifulSoup(
            req.get(self.u.format("settings/apps/tabbed/?tab=active")).text,
        "html.parser")
        #print bs
        for i in bs.find_all("div",class_="cx"):
            if len(i.text) !=0:
                data.append(i.text)
                try:
                    open("out/"+self.o,"a+").write("[%s|%s]: %s\n"%(
                        a[-0],a[-1],i.text))
                except:pass
        if len(data) !=0:
            self.found+=1
            open("out/"+self.o,"a+").write("\n\n\n")

class ina:
    def __init__(self):
        self.u="https://mbasic.facebook.com/{}"
        self.log=0
        self.fail=0
        self.found=0
        self.file()

    def file(self):
        try:
            self.a=open(raw_input("[?] account list: ")).read().splitlines()
        except Exception as e:
            print "%s"%(e)
            self.file()
        self.q()

    def q(self):
        self.query=raw_input("[?] app query: ").lower()
        if self.query =="":
            self.q()
        else:
            self.out()

    def out(self):
        try:
            self.o=raw_input("[?] result filename: ")
            if self.o =="":
                self.out()
            else:
                self.outs=open("out/"+self.o,"w").close()
        except Exception as e:
            print "%s"%(e)
            self.out()
        self.thr()

    def thr(self):
        try:
            self.pool=input("[?] Thread: ")
        except Exception as e:
            print "%s"%(e)
            self.thr()
        ThreadPool(self.pool).map(self.cek,self.a)
        if os.path.getsize("out/"+self.o) !=0:
            print "\n[+] all done, %s app written saved to: out/%s"%(
                len(open("out/"+self.o).read().splitlines()),self.o)
            back()
        else:
            print "\n[-] all done, no app written with query: %s"%(self.query)
            back()

    def cek(self,a):
        print "\r[+] Checking: %s/%s - Found: %s - Login Fail: %s"%(
            self.log,len(self.a),self.found,self.fail),;sys.stdout.flush()
        z=a.split("|")
        r=requests.Session()
        s=r.post(
        "https://mbasic.facebook.com/login",
            data={
                "email":z[-0],
                "pass":z[-1]
            }
        ).url
        if "save-device" in s or "m_sess" in s:
            self.log+=1
            self.open(z,r)
        else:
            self.fail+=1

    def open(self,a,req):
        data=[]
        bs=bs4.BeautifulSoup(
            req.get(self.u.format("settings/apps/tabbed/?tab=inactive")).text,
        "html.parser")
        #print bs
        for i in bs.find_all("div",class_="cx"):
            if self.query in i.text.lower():
                data.append(i.text)
                try:
                    open("out/"+self.o,"a+").write("[%s|%s]: %s\n"%(
                        a[-0],a[-1],i.text))
                except:pass
        if len(data) !=0:
            self.found+=1

class apps(object):
    def __init__(self):
        print "\n\t[ Select Actions ]\n"
        print "  {%s01%s} Check All App From Account List."%(G,N)
        print "  {%s02%s} Check All App By Query Account List"%(G,N)
        print "  {%s03%s} Check All Expired App By Query Account List"%(G,N)
        print "  {%s04%s} Back To Menu.\n"%(R,N)
        self.c()

    def c(self):
        r=raw_input("%s[%s*%s]%s Actions>> "%(G,R,G,N))
        if r =="":
            self.c()
        elif r =="1" or r =="01":
            check()
        elif r =="2" or r =="02":
            onAppByQuery()
        elif r =="3" or r =="03":
            ina()
        elif r =="4" or r =="04":
            raw_input("press enter to menu...")
            interpreter.ASU()
        else:
            print "%s[!]%s invalid options!"%(R,N)
            self.c()

