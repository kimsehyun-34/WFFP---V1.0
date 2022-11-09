import time
from 조회저장 import data6
wo = 1

# with open("test.txt", "r", encoding='utf-8') as f:
#    line = f.read()
#a = line[700]+line[701]+line[702]+line[703]

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
d = line[700]+line[701]+line[702]+line[703]

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
h = line[700]+line[701]+line[702]+line[703]


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
    m = line[700]+line[701]+line[702]+line[703]

if data6 < 9:
    print(c)
    b = float(c)
    if data6 < 8:
        print(b)
        c = float(b)

print(d)
print(e)
print(fa)
print(g)
print(h)

d = float(d)
e = float(e)
fa = float(fa)
g = float(g)
h = float(h)

if (data6):
    p = (d+e+fa+g+h)/6

if (data6 < 8):
    p = (b+c+d+e+fa+g+h)/7
    if (data6 < 9):
        p = (c+d+e+fa+g+h)/6

if (data6 > 22):
    i = float(i)
    j = float(j)
    k = float(k)
    l = float(l)
    n = float(n)
    m = float(m)
    p = (i+j+k+l+m+n)/6

print("평균기온: ", round(p, 1), "°C")
