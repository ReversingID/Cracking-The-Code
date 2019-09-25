print '\x1b[31;1m\n         `/ymMMMMMMMMMMMMMMmy/`\n       /hMMMMMMMMMMMMMMMMMMMMMMh/\n     /mMMmNMMMMMNNNNNNNNMMMMMNNMMm/\n   `hNmo:dMMNNNmNNmNNmNNmNNNMMd:omNh`\n  .mh:+/hMNNNNmNNmNdhmmNNmNNNNMy/o:hm.\n `d+://sNmMMMmMMMmdy+/mMMMmMMMmNs///+d`\n ys.o/oMmNNNmNNMNNMmdMNNMNNmNNNmMo/o.ys\n`my.-/NmMMMMmMMNmNNyyNNmNMMmMMMMmN/:`ym`\n-h/+s/MmMMMNmNNNdym++mymNNNmNMMNmM:so/h-\n-N.o.sMmMMMNh/:-`-Mo\x1b[37;1msM-`-:/hNMMMmMs.+.N-\n`ho/-ohmMMMM/    -M/+M.    /MMMMmho-/oh\n s+-s-odmNNN`     /-:/     .NNNmd+:s-+s\n `mo/-:+ymMm                mMms+:-/om`\n  .h/+/y`hhs                yyh`y/+/h.\n   `hd/::-+.                .+-::/dy`\n     /hs+/::.--          --.::/+sh:\n       :hds+/-`          `-/+sdh:\n         `/ymM+          oMmy/'
print '\x1b[1;33mSudah punya ID dan Password nya?'
print '\x1b[1;32mSilahkan Login '
import os, sys

def wa():
    os.system('xdg-open https://api.whatsapp.com/send?phone=6281249281196&text=Assalamualaikum')


def restart():
    ngulang = sys.executable
    os.execl(ngulang, ngulang, *sys.argv)


user = raw_input('ID: ')
import getpass
sandi = raw_input('Password: ')
if sandi == 'ganteng' and user == 'Mrlink':
    print 'Kamu Telah Login System Saya'
    sys.exit
else:
    print 'Login GAGAL, Silahkan hubungi Saya'
    wa()
    restart()
