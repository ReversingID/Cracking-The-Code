import requests
import json
import requests,os,md5,hashlib,getpass,json

def basetoken(uri=None):
    s=json.loads(open("config/config.json").read())
    sc="62f8ce9f74b12f84c123cc23437a4a32"
    data = {"api_key":"882a8490361da98702bf97a021ddc14d",
    "credentials_type":"password","email":s["email"],"format":"JSON",
    "generate_machine_id":"1",
    "generate_session_cookies":"1",
    "locale":"en_US","method":"auth.login",
    "password":s["pass"],"return_ssl_resources":"0","v":"1.0"}
    sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+s["email"]+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+s["pass"]+'return_ssl_resources=0v=1.0'+sc
    x=hashlib.new("md5")
    x.update(sig)
    data.update({"sig":x.hexdigest()})
    try:
        return requests.get('https://api.facebook.com/restserver.php',
            params=data).json()["access_token"]
    except:return None

def token(akun):
    try:
        return requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email={}&locale=en_US&password={}&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6".format(akun.split("|")[-0],akun.split("|")[-1])).json()["access_token"]
    except:
        return False
