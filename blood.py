#スクレイピングに必要なモジュール
import requests
from bs4 import BeautifulSoup
#モジュールインポート
import sitelist

import time #sleep用
import sys  #エラー検知用
import re   #正規表現


try:
    # スクレイピング対象の URL にリクエストを送り HTML を取得する
    res = requests.get("https://db.netkeiba.com/horse/ped/2017104771")

    res.raise_for_status()  #URLが正しくない場合，例外を発生させる

    # レスポンスの HTML から BeautifulSoup オブジェクトを作る
    soup = BeautifulSoup(res.content, 'html.parser')

    Stallion_Names_m = []
    Stallion_Names_mm = []
    Stallion_Names_mmm = []
    Stallion_Names_mfm = []
    Stallion_Names_fm = []
    Stallion_Names_fmm = []
    Stallion_Names_ffm = []



    #馬名取得
    Stallion_Names = soup.find_all('td', class_='b_ml')
    Stallion_Names_list = []
    for Stallion_Name in Stallion_Names:
        Stallion_Name = Stallion_Name.find('a')
        print(Stallion_Name)
        Stallion_Name = Stallion_Name.get_text('a')
        print(Stallion_Name)
        Stallion_Name = Stallion_Name.split('\n')[0]
        print(Stallion_Name)
        #リスト作成
        Stallion_Names_list.append(Stallion_Name)

    Stallion_Names_m.append(Stallion_Names_list[0])
    Stallion_Names_mm.append(Stallion_Names_list[1])
    Stallion_Names_mmm.append(Stallion_Names_list[2])
    Stallion_Names_mfm.append(Stallion_Names_list[9])
    Stallion_Names_fm.append(Stallion_Names_list[16])
    Stallion_Names_fmm.append(Stallion_Names_list[17])
    Stallion_Names_ffm.append(Stallion_Names_list[24])


    print(Stallion_Names_m)
    print(Stallion_Names_mm)
    print(Stallion_Names_mmm)
    print(Stallion_Names_mfm)
    print(Stallion_Names_fm)
    print(Stallion_Names_fmm)
    print(Stallion_Names_ffm)

except:
    print(sys.exc_info())
    print("サイト取得エラー")





