import urllib.request
import time

now = time
y = now.localtime().tm_year
m = now.localtime().tm_mon
d = now.localtime().tm_mday
h = now.localtime().tm_hour

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
    urllib.request.urlretrieve(url11, savename11)  # 저장
    urllib.request.urlretrieve(url12, savename12)
    urllib.request.urlretrieve(url14, savename14)
    urllib.request.urlretrieve(url16, savename16)
    urllib.request.urlretrieve(url18, savename18)

if (7 < data6 < 12):
    urllib.request.urlretrieve(url9, savename9)
    urllib.request.urlretrieve(url11, savename11)  # 저장
    urllib.request.urlretrieve(url12, savename12)
    urllib.request.urlretrieve(url14, savename14)
    urllib.request.urlretrieve(url16, savename16)
    urllib.request.urlretrieve(url18, savename18)

if (data6 > 22):
    urllib.request.urlretrieve(url01, savename9)  # 저장
    urllib.request.urlretrieve(url02, savename11)
    urllib.request.urlretrieve(url03, savename12)
    urllib.request.urlretrieve(url04, savename14)
    urllib.request.urlretrieve(url05, savename16)
    urllib.request.urlretrieve(url06, savename18)

print("조회완료")
