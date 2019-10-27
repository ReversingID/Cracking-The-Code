###########################################
# Coded by Mr.Runn1n9                     #
# Created : Jumat, 4 Oktober 2019 [12:16] #
###########################################

import sys, os
from time import sleep
sleep(0.5)
os.system('clear')
sleep(1)
msg = '\x1b[36;1m=======================================================================\n\n                          \x1b[32;1mTool by \x1b[31;1mMr.Runn1n9\n\n\x1b[36;1m======================================================================='
print msg
sleep(2)
title = raw_input('\n \x1b[33;1mTitle:\x1b[37;1m ')
sleep(0.5)
background = raw_input('\n \x1b[33;1mWarna Background (ex:\x1b[37;1mwhite\x1b[33;1m):\x1b[37;1m ')
sleep(0.5)
color1 = raw_input('\n \x1b[33;1mWarna Teks di atas (ex:\x1b[35;1mpurple\x1b[33;1m):\x1b[37;1m ')
sleep(0.5)
heading = raw_input('\n \x1b[33;1mTeks pertama (ex:\x1b[31;1mHacked by Mr.Runn1n9\x1b[33;1m):\x1b[37;1m ')
sleep(0.5)
imgurl = raw_input('\n \x1b[33;1mUrl Gambar:\x1b[37;1m ')
sleep(0.5)
music = raw_input('\n \x1b[33;1mUrl Musik (ex:\x1b[37;1mhttps://jembud.mp3\x1b[33;1m):\x1b[37;1m ')
sleep(0.5)
color2 = raw_input('\n \x1b[33;1mWarna Pesan (ex:\x1b[37;1mblack\x1b[33;1m):\x1b[37;1m ')
sleep(0.5)
message = raw_input('\n \x1b[33;1mPesan:\x1b[37;1m ')
sleep(0.5)
alert = raw_input('\n \x1b[33;1mAlert:\x1b[37;1m ')
sleep(3)
os.system('clear')
sleep(1)
print '\x1b[36;1m=======================================================================\n'
sleep(0.5)
print ' \x1b[32;1mSuccess membuat Script'
sleep(0.5)
print ' Script tersimpan di \x1b[33;1mInternal\n'
sleep(0.5)
print '\x1b[36;1m=======================================================================\n'
fo = open('/storage/emulated/0/script.html', 'w')
script1 = '<html><head><title>'
script2 = title
script3 = '</title></head>'
script4 = '<body><body bgcolor='
script5 = background
script6 = '>\n<script type="text/javascript" src="http://htmlfreecodes.com/codes/rain.js"></script><br><div class="error">'
script7 = '<link href="https://fonts.googleapis.com/css?family=Chicle|Underdog&display=swap " rel="stylesheet" type="text/css"><font color=" '
script8 = color1
script9 = ' ">'
script10 = '<br><center><div style="text-shadow: 0px 0px 10px";><font face="Chicle" size="20">'
script11 = heading
script12 = '</font></center></div><br><br>'
script13 = '<center><img style="width:60%" src=" '
script14 = imgurl
script15 = 'title="Dont Touch Me!></center><br>'
script16 = '<center><audio src=" '
script17 = music
script18 = ' " autoplay controls></audio></center><br>'
script19 = '<font color=" '
script20 = color2
script21 = ' ">'
script22 = '<center><font face="Underdog" size="10"><b>'
script23 = message
script24 = '</b></font></center>\n</body>'
script25 = '<script>\nalert(" '
script26 = alert
script27 = ' ")</script></html>'
fo.write(script1)
fo.write(script2)
fo.write(script3)
fo.write(script4)
fo.write(script5)
fo.write(script6)
fo.write(script7)
fo.write(script8)
fo.write(script9)
fo.write(script10)
fo.write(script11)
fo.write(script12)
fo.write(script13)
fo.write(script14)
fo.write(script15)
fo.write(script16)
fo.write(script17)
fo.write(script18)
fo.write(script19)
fo.write(script20)
fo.write(script21)
fo.write(script22)
fo.write(script23)
fo.write(script24)
fo.write(script25)
fo.write(script26)
fo.write(script27)
fo.close()
