#スクレイピングに必要なモジュール
import requests
from bs4 import BeautifulSoup
#モジュールインポート
import sitelist

import time #sleep用
import sys  #エラー検知用
import re   #正規表現


for scraping_sitename in sitelist.SITE_URL:

    try:
        # スクレイピング対象の URL にリクエストを送り HTML を取得する
        res = requests.get(scraping_sitename)

        res.raise_for_status()  #URLが正しくない場合，例外を発生させる

        # レスポンスの HTML から BeautifulSoup オブジェクトを作る
        soup = BeautifulSoup(res.content, 'html.parser')



        #RaceData01sのリスト作成
        RaceData01s = soup.find('div', class_='RaceData01')
        RaceData01s = RaceData01s.get_text()
        
        RaceData01s_list = RaceData01s.split('\n')
	
        #print(RaceData01s_list)   #debug
	
        tmp = RaceData01s_list[1].split(' / ')
        Course = tmp[1][:1]
        Distance = tmp[1][1:5]
        Course2 = tmp[1][7:]

        racetrack = RaceData01s_list[3][-1]



        #RaceData02sのリスト作成
        RaceData02s = soup.find('div', class_='RaceData02')
        RaceData02s = RaceData02s.get_text()
        
        RaceData02s_list = RaceData02s.split('\n')
	
        #print(RaceData02s_list)   #debug

        Frequency = RaceData02s_list[1]
        Racecourse = RaceData02s_list[2]
        Days = RaceData02s_list[3]
        Conditions = RaceData02s_list[4]
        Class = RaceData02s_list[5]
        Sexuality = RaceData02s_list[7]
        Handicap = RaceData02s_list[8]
        Starters = RaceData02s_list[9][:-1]


        RaceNames = soup.find('div', class_='RaceName')
        RaceNames = RaceNames.get_text(strip=True)

        RaceNums = soup.find('span', class_='RaceNum')
        RaceNums = RaceNums.get_text(strip=True)



        tmp = RaceData01s_list[1].split(' / ')
        Field = tmp[1][:1]
        Distance = tmp[1][1:5]
        Field2 = tmp[1][7:]
        Weather = RaceData01s_list[2][-1]
        racetrack = RaceData01s_list[3][-1]

        #ペース取得　取れてない
        HaronTimestmp = soup.find('tr', class_='HaronTime')
        HaronTimes = HaronTimestmp.find_all('td')
        for HaronTime in HaronTimes:
            HaronTime = HaronTime.get_text(strip=True)
            try :
                HaronTimes_list
                HaronTimes_list = HaronTimes_list + "-" + HaronTime
            except :
                HaronTimes_list = HaronTime
        print(HaronTimes_list)



        print(RaceNames)   #debug
        print(RaceNums)   #debug
        print(Frequency)   #debug
        print(Racecourse)   #debug
        print(Days)   #debug
        print(Conditions)   #debug
        print(Class)   #debug
        print(Sexuality)   #debug
        print(Racecourse)   #debug
        print(Handicap)   #debug
        print(Starters)   #debug
        print(Field)   #debug
        print(Distance)   #debug
        print(Field2)   #debug
        print(Weather)   #debug
        print(racetrack)   #debug



        #順位のリスト作成
        Ranks = soup.find_all('div', class_='Rank')
        Ranks_list = []
        for Rank in Ranks:
            Rank = Rank.get_text(strip=True)
            #リスト作成
            Ranks_list.append(Rank)
        print(Ranks_list)   #debug


        #馬名取得
        Horse_Names = soup.find_all('span', class_='Horse_Name')
        Horse_Names_list = []
        Horse_links_list = []
        for Horse_Name in Horse_Names:

            Horse_link = Horse_Name.find('a')
            Horse_Name = Horse_link.get('title')
            Horse_link = Horse_link.get('href').split('/')
            Horse_links = Horse_link[0]+'//'+Horse_link[2]+'/'+Horse_link[3]+'/ped/'+Horse_link[4]
            #リスト作成
            Horse_Names_list.append(Horse_Name)
            Horse_links_list.append(Horse_links)
        print(Horse_Names_list) #debug
        print(Horse_links_list) #debug

        
        Stallion_Names_m = []
        Stallion_Names_mm = []
        Stallion_Names_mmm = []
        Stallion_Names_mfm = []
        Stallion_Names_fm = []
        Stallion_Names_fmm = []
        Stallion_Names_ffm = []

        
        ##クロスの後ろに「a」が入るバグ?直す　201207
        for Horse_links_name in Horse_links_list:

            #攻撃とみなされないように時間を置く
            time.sleep(1)
            try:
                req = requests.get(Horse_links_name)
                req.raise_for_status()  #URLが正しくない場合，例外を発生させる
                soup2 = BeautifulSoup(req.content, 'html.parser')


            #馬名取得
                Stallion_Names = soup2.find_all('td', class_='b_ml')
                Stallion_Names_list = []
                for Stallion_Name in Stallion_Names:
                    Stallion_Name = Stallion_Name.find('a')
                    Stallion_Name = Stallion_Name.get_text('a')
                    Stallion_Name = Stallion_Name.split('\n')[0]
                    #リスト作成
                    Stallion_Names_list.append(Stallion_Name)

                Stallion_Names_m.append(Stallion_Names_list[0])
                Stallion_Names_mm.append(Stallion_Names_list[1])
                Stallion_Names_mmm.append(Stallion_Names_list[2])
                Stallion_Names_mfm.append(Stallion_Names_list[9])
                Stallion_Names_fm.append(Stallion_Names_list[16])
                Stallion_Names_fmm.append(Stallion_Names_list[17])
                Stallion_Names_ffm.append(Stallion_Names_list[24])
            except:
                print(sys.exc_info())
                print("サイト取得エラー")

    
        print(Stallion_Names_m)
        print(Stallion_Names_mm)
        print(Stallion_Names_mmm)
        print(Stallion_Names_mfm)
        print(Stallion_Names_fm)
        print(Stallion_Names_fmm)
        print(Stallion_Names_ffm)
        
        



        #人気取得
        Ninkis = soup.find_all('span', class_='OddsPeople')
        Ninkis_list = []
        for Ninki in Ninkis:
            Ninki = Ninki.get_text(strip=True)
            #リスト作成
            Ninkis_list.append(Ninki)
        print(Ninkis_list)  #debug
        
        #Odds取得
        Odds = soup.find_all('td', class_='Odds Txt_R')
        Odds_list = []
        for Odd in Odds:
            Odd = Odd.get_text(strip=True)
            Odds_list.append(Odd)
        print(Odds_list)

        #馬番取得
        Txt_Cs = soup.find_all('td', class_=re.compile("Num Txt_C"))
        Txt_Cs_list = []
        for Txt_C in Txt_Cs:
            Txt_C = Txt_C.get_text(strip=True)
            #リスト作成
            Txt_Cs_list.append(Txt_C)
        print(Txt_Cs_list)

        #枠取得
        Wakus = soup.find_all('td', class_=re.compile("Num Waku"))
        Wakus_list = []
        for Waku in Wakus:
            Waku = Waku.get_text(strip=True)
            #リスト作成
            Wakus_list.append(Waku)
        print(Wakus_list)

        #Detail_Left取得
        Lgt_Txts = soup.find_all('span', class_='Lgt_Txt')
        Lgt_Txts_list = []
        Age_list = []
        Sex_list = []
        for Lgt_Txt in Lgt_Txts:
            Age = Lgt_Txt.get_text(strip=True)[0]
            Sex = Lgt_Txt.get_text(strip=True)[1]
            
            #リスト作成
            Age_list.append(Age)
            Sex_list.append(Sex)
        print(Age_list)
        print(Sex_list)

        #jocky取得
        #下のよくわからん直近重賞データまで拾ってくるから頭数でarray絞るが吉。
        Jockeys = soup.find_all('td', class_='Jockey')
        Jockeys_list = []
        for Jockey in Jockeys:
            Jockey = Jockey.get_text(strip=True)
            #リスト作成
            Jockeys_list.append(Jockey)
        print(Jockeys_list)

        #JockeyWeight取得
        JockeyWeights = soup.find_all('span', class_='JockeyWeight')
        JockeyWeights_list = []
        for JockeyWeight in JockeyWeights:
            JockeyWeight = JockeyWeight.get_text(strip=True)
            #リスト作成
            JockeyWeights_list.append(JockeyWeight)
        print(JockeyWeights_list)

        #Time取得
        #num%3==1はTime
        #num%3==3は上り3ハロン
        #num%3==2の着差はいらないのでない？
        Times = soup.find_all('td', class_='Time')
        Times_list = []
        Rase_list = []
        key = 0
        for Time in Times:
            key += 1
            Time = Time.get_text(strip=True)
            if key % 3 == 1 :
                Times_list.append(Time)
            if key % 3 == 0 :
                Rase_list.append(Time)
        print(Times_list)
        print(Rase_list)
        
        

        #PassageRate取得
        PassageRates = soup.find_all('td', class_='PassageRate')
        PassageRates_list = []
        for PassageRate in PassageRates:
            PassageRate = PassageRate.get_text(strip=True)
            PassageRates_list.append(PassageRate)
        print(PassageRates_list)

        #Odds取得
        Weights = soup.find_all('td', class_='Weight')
        Weights_list = []
        for Weight in Weights:
            Weight = Weight.get_text(strip=True)
            Weights_list.append(Weight)
        print(Weights_list)

    except:
        print(sys.exc_info())
        print("サイト取得エラー")

    #攻撃とみなされないように時間を置く
    time.sleep(1)
    

    
    

