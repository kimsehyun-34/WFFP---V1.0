from tkinter import *
import urllib.request
import time

# 1. 루트화면 (root window) 생성
tk = Tk()
wo = 1
now = time
y = now.localtime().tm_year
m = now.localtime().tm_mon
d = now.localtime().tm_mday
h = now.localtime().tm_hour


def event():
    button['text'] = ('계산중..')
    if (d < 10):
        a = y, m, 0, d  # 년, 월, 일 data2
        data = str(a)
        data_split = data.split(',')
        data_join = ''.join(data_split)
        data1 = data_join.strip('() ')
        data2 = data1.replace(' ', '')
        print(data2)

    if (d > 10):
        a = y, m, d  # 년, 월, 일 data2
        data = str(a)
        data_split = data.split(',')
        data_join = ''.join(data_split)
        data1 = data_join.strip('() ')
        data2 = data1.replace(' ', '')
        print(data2)

    data3 = str(h)  # 시간 data6
    data6 = str(h)

    if (h > 9):
        h2 = h
        data3 = str(h2)
        data4 = data3.strip('() ')
        data5 = data4.replace(',', '')
        data6 = data5.replace(' ', '')
        print(data6)

    if (h < 10):
        h2 = 0, h
        data3 = str(h2)
        data4 = data3.strip('() ')
        data5 = data4.replace(',', '')
        data6 = data5.replace(' ', '')
        print(data6)

    # 정시간
    url1 = ('http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst?serviceKey=kFg3740w8oA0URfa6U0acwTHl6OBznrukbTSF5qHxgELxjG2jtx2Z7ozqItFCHb%2FLTqdMYBKqbgoJyxHQSDatA%3D%3D&numOfRows=4&pageNo=1&base_date='+data2+'&base_time='+data6+'00&nx=62&ny=125')
    data6_1 = '08'
    data6_2 = '09'
    data6_3 = '11'
    data6_4 = '12'
    data6_5 = '14'
    data6_6 = '16'
    data6_7 = '18'
    # 저녁시간 url
    url01 = ('http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst?serviceKey=kFg3740w8oA0URfa6U0acwTHl6OBznrukbTSF5qHxgELxjG2jtx2Z7ozqItFCHb%2FLTqdMYBKqbgoJyxHQSDatA%3D%3D&numOfRows=4&pageNo=1&base_date='+data2+'&base_time='+data6_1+'00&nx=62&ny=125')
    url02 = ('http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst?serviceKey=kFg3740w8oA0URfa6U0acwTHl6OBznrukbTSF5qHxgELxjG2jtx2Z7ozqItFCHb%2FLTqdMYBKqbgoJyxHQSDatA%3D%3D&numOfRows=4&pageNo=1&base_date='+data2+'&base_time='+data6_2+'00&nx=62&ny=125')
    url03 = ('http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst?serviceKey=kFg3740w8oA0URfa6U0acwTHl6OBznrukbTSF5qHxgELxjG2jtx2Z7ozqItFCHb%2FLTqdMYBKqbgoJyxHQSDatA%3D%3D&numOfRows=4&pageNo=1&base_date='+data2+'&base_time='+data6_3+'00&nx=62&ny=125')
    url04 = ('http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst?serviceKey=kFg3740w8oA0URfa6U0acwTHl6OBznrukbTSF5qHxgELxjG2jtx2Z7ozqItFCHb%2FLTqdMYBKqbgoJyxHQSDatA%3D%3D&numOfRows=4&pageNo=1&base_date='+data2+'&base_time='+data6_4+'00&nx=62&ny=125')
    url05 = ('http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst?serviceKey=kFg3740w8oA0URfa6U0acwTHl6OBznrukbTSF5qHxgELxjG2jtx2Z7ozqItFCHb%2FLTqdMYBKqbgoJyxHQSDatA%3D%3D&numOfRows=4&pageNo=1&base_date='+data2+'&base_time='+data6_5+'00&nx=62&ny=125')
    url05 = ('http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst?serviceKey=kFg3740w8oA0URfa6U0acwTHl6OBznrukbTSF5qHxgELxjG2jtx2Z7ozqItFCHb%2FLTqdMYBKqbgoJyxHQSDatA%3D%3D&numOfRows=4&pageNo=1&base_date='+data2+'&base_time='+data6_6+'00&nx=62&ny=125')
    url06 = ('http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst?serviceKey=kFg3740w8oA0URfa6U0acwTHl6OBznrukbTSF5qHxgELxjG2jtx2Z7ozqItFCHb%2FLTqdMYBKqbgoJyxHQSDatA%3D%3D&numOfRows=4&pageNo=1&base_date='+data2+'&base_time='+data6_7+'00&nx=62&ny=125')

    data2_0 = int(data2)-1  # 현재날짜 -1 (어제)
    data2_1 = str(data2_0)

    # 아침 url
    url8 = ('http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst?serviceKey=kFg3740w8oA0URfa6U0acwTHl6OBznrukbTSF5qHxgELxjG2jtx2Z7ozqItFCHb%2FLTqdMYBKqbgoJyxHQSDatA%3D%3D&numOfRows=4&pageNo=1&base_date='+data2_1+'&base_time='+data6_1+'00&nx=62&ny=125')
    url9 = ('http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst?serviceKey=kFg3740w8oA0URfa6U0acwTHl6OBznrukbTSF5qHxgELxjG2jtx2Z7ozqItFCHb%2FLTqdMYBKqbgoJyxHQSDatA%3D%3D&numOfRows=4&pageNo=1&base_date='+data2_1+'&base_time='+data6_2+'00&nx=62&ny=125')
    url11 = ('http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst?serviceKey=kFg3740w8oA0URfa6U0acwTHl6OBznrukbTSF5qHxgELxjG2jtx2Z7ozqItFCHb%2FLTqdMYBKqbgoJyxHQSDatA%3D%3D&numOfRows=4&pageNo=1&base_date='+data2_1+'&base_time='+data6_3+'00&nx=62&ny=125')
    url12 = ('http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst?serviceKey=kFg3740w8oA0URfa6U0acwTHl6OBznrukbTSF5qHxgELxjG2jtx2Z7ozqItFCHb%2FLTqdMYBKqbgoJyxHQSDatA%3D%3D&numOfRows=4&pageNo=1&base_date='+data2_1+'&base_time='+data6_4+'00&nx=62&ny=125')
    url14 = ('http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst?serviceKey=kFg3740w8oA0URfa6U0acwTHl6OBznrukbTSF5qHxgELxjG2jtx2Z7ozqItFCHb%2FLTqdMYBKqbgoJyxHQSDatA%3D%3D&numOfRows=4&pageNo=1&base_date='+data2_1+'&base_time='+data6_5+'00&nx=62&ny=125')
    url16 = ('http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst?serviceKey=kFg3740w8oA0URfa6U0acwTHl6OBznrukbTSF5qHxgELxjG2jtx2Z7ozqItFCHb%2FLTqdMYBKqbgoJyxHQSDatA%3D%3D&numOfRows=4&pageNo=1&base_date='+data2_1+'&base_time='+data6_6+'00&nx=62&ny=125')
    url18 = ('http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst?serviceKey=kFg3740w8oA0URfa6U0acwTHl6OBznrukbTSF5qHxgELxjG2jtx2Z7ozqItFCHb%2FLTqdMYBKqbgoJyxHQSDatA%3D%3D&numOfRows=4&pageNo=1&base_date='+data2_1+'&base_time='+data6_7+'00&nx=62&ny=125')

    savename = "test.txt"
    savename8 = "test7.txt"  # 저장파일 이름 지정
    savename9 = "test9.txt"
    savename11 = "test11.txt"
    savename12 = "test12.txt"
    savename14 = "test14.txt"
    savename16 = "test16.txt"
    savename18 = "test18.txt"

    data6 = int(data6)

    urllib.request.urlretrieve(url1, savename)

    if (data6 < 8):
        urllib.request.urlretrieve(url8, savename8)
        urllib.request.urlretrieve(url9, savename9)
        urllib.request.urlretrieve(url11, savename11)
        urllib.request.urlretrieve(url12, savename12)
        urllib.request.urlretrieve(url14, savename14)
        urllib.request.urlretrieve(url16, savename16)
        urllib.request.urlretrieve(url18, savename18)

    if (7 < data6 < 12):
        urllib.request.urlretrieve(url9, savename9)
        urllib.request.urlretrieve(url11, savename11)
        urllib.request.urlretrieve(url12, savename12)
        urllib.request.urlretrieve(url14, savename14)
        urllib.request.urlretrieve(url16, savename16)
        urllib.request.urlretrieve(url18, savename18)

    if (data6 > 22):
        urllib.request.urlretrieve(url01, savename9)
        urllib.request.urlretrieve(url02, savename11)
        urllib.request.urlretrieve(url03, savename12)
        urllib.request.urlretrieve(url04, savename14)
        urllib.request.urlretrieve(url05, savename16)
        urllib.request.urlretrieve(url06, savename18)

    print("조회완료")

    if (data6 < 9):
        with open("test9.txt", "r", encoding='utf-8') as f:
            line = f.read()
        b = line[700]+line[701]+line[702]+line[703]
        print("9시 포함")

        if (data6 < 8):
            with open("test7.txt", "r", encoding='utf-8') as f:
                line = f.read()
            c = line[700]+line[701]+line[702]+line[703]
            print("8시 포함")

    with open("test11.txt", "r", encoding='utf-8') as f:
        line = f.read()
    da = line[700]+line[701]+line[702]+line[703]

    with open("test12.txt", "r", encoding='utf-8') as f:
        line = f.read()
    e = line[700]+line[701]+line[702]+line[703]

    with open("test14.txt", "r", encoding='utf-8') as f:
        line = f.read()
    fa = line[700]+line[701]+line[702]+line[703]

    with open("test16.txt", "r", encoding='utf-8') as f:
        line = f.read()
    g = line[700]+line[701]+line[702]+line[703]

    with open("test18.txt", "r", encoding='utf-8') as f:
        line = f.read()
    ha = line[700]+line[701]+line[702]+line[703]

    if (data6 > 22):
        with open("test01.txt", "r", encoding='utf-8') as f:
            line = f.read()
        i = line[700]+line[701]+line[702]+line[703]

        with open("test02.txt", "r", encoding='utf-8') as f:
            line = f.read()
        j = line[700]+line[701]+line[702]+line[703]

        with open("test03.txt", "r", encoding='utf-8') as f:
            line = f.read()
        k = line[700]+line[701]+line[702]+line[703]

        with open("test04.txt", "r", encoding='utf-8') as f:
            line = f.read()
        l = line[700]+line[701]+line[702]+line[703]

        with open("test05.txt", "r", encoding='utf-8') as f:
            line = f.read()
        n = line[700]+line[701]+line[702]+line[703]

        with open("test06.txt", "r", encoding='utf-8') as f:
            line = f.read()
        ma = line[700]+line[701]+line[702]+line[703]

    if data6 < 9:
        print(c)
        b = float(c)

        if data6 < 8:
            print(b)
            c = float(b)

    print(da)
    print(e)
    print(fa)
    print(g)
    print(ha)

    da = float(da)
    e = float(e)
    fa = float(fa)
    g = float(g)
    ha = float(ha)

    if (data6):
        p = (da+e+fa+g+ha)/6

    if (data6 < 8):
        p = (b+c+da+e+fa+g+ha)/7
        if (data6 < 9):
            p = (c+da+e+fa+g+ha)/6

    if (data6 > 22):
        i = float(i)
        j = float(j)
        k = float(k)
        l = float(l)
        n = float(n)
        ma = float(ma)
        p = (i+j+k+l+ma+n)/6

    print("평균기온: ", round(p, 1), "°C")
    button['text'] = ('평균기온:', round(p, 1), '°C')


button = Button(tk, text='날씨조회', command=event)


# side로 배치설정, padx로 좌우 여백설정, pady로 상하 여백설정
button.pack(side=LEFT, padx=10, pady=10)

tk.mainloop()
