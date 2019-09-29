import requests,bs4,time,mechanize,sys

class report:
    def __init__(self):
        self.f=0
        self.ok=0
        self.gagal=0
        self.u="https://mbasic.facebook.com/{}"
        print "* sparator: |"
        self.ac()

    def ac(self):
        try:
            self.a=open(raw_input("[?] account list: ")).read().splitlines()
        except Exception as e:
            print "[!] %s"%e
            self.ac()
        self.id()

    def id(self):
        self.i=raw_input("[?] target id: ")
        if self.i =="":
            self.id()
        else:
            map(self.do,self.a)

    def do(self,a):
        print "\r[%s/%s]: Reporting... Login Failed-:%s, Errors-:%s"%(
            self.ok,len(self.a),self.f,self.gagal),;sys.stdout.flush()
        ak=a.split("|")
        m=mechanize.Browser()
        m.set_handle_robots(False)
        m.addheaders=[("User-Agent","Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36")]
        m.open(self.u.format("login"))
        m._factory.is_html=True
        m.select_form(nr=0)
        m["email"]=ak[-0]
        m["pass"]=ak[-1]
        log=m.submit().geturl()
        if "save-device" in log or "m_sess" in log:
            self.ok+=1
            try:
                self.open(m)
            except:
                self.gagal+=1
        else:self.f+=1

    def open(self,m):
        m.open(self.u.format(self.i))
        m._factory.is_html=True
        m.open(m.find_link(url_regex="owner").url)
        m._factory.is_html=True
        m.open(m.find_link(url_regex="nfx/basic").url)
        m._factory.is_html=True
        m.select_form(nr=0)
        m.form["tag"]=["profile_fake_account"]
        m.submit()
        m._factory.is_html=True
        m.select_form(nr=0)
        m.form["action_key"]=["FRX_PROFILE_REPORT_CONFIRMATION"]
        m.submit()
        m._factory.is_html=True
        m.select_form(nr=0)
        m.form["checked"]=["yes"]
        m.submit()
