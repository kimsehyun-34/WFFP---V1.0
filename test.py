from cgi import print_form
import urllib.request
import time

data6='11'
data2='20221103'

#정시간
url1 = ('http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst?serviceKey=kFg3740w8oA0URfa6U0acwTHl6OBznrukbTSF5qHxgELxjG2jtx2Z7ozqItFCHb%2FLTqdMYBKqbgoJyxHQSDatA%3D%3D&numOfRows=4&pageNo=1&base_date='+data2+'&base_time='+data6+'00&nx=62&ny=125')

savename = "test.txt"

urllib.request.urlretrieve(url1, savename)