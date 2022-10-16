from cgi import print_form
import urllib.request
import time

now = time
y= now.localtime().tm_year
m=now.localtime().tm_mon
d=now.localtime().tm_mday
h=now.localtime().tm_hour

a=y,m,d #년, 월, 일 data2 화
data=str(a)
data_split = data.split(',')
data_join = ''.join(data_split)
data1=data_join.strip('() ')
data2=data1.replace(' ', '')
print(data2)


data3=str(h) #시간 data6 화
data6=str(h)
if (h<10):
    h2=0,h
    data3=str(h2)
    data4=data3.strip('() ')
    data5=data4.replace(',', '')
    data6=data5.replace(' ', '')
print(data6)

url = ('http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst?serviceKey=kFg3740w8oA0URfa6U0acwTHl6OBznrukbTSF5qHxgELxjG2jtx2Z7ozqItFCHb%2FLTqdMYBKqbgoJyxHQSDatA%3D%3D&numOfRows=4&pageNo=1&base_date='+data2+'&base_time='+data6+'00&nx=64&ny=127')
savename = "test.txt"

urllib.request.urlretrieve(url, savename)