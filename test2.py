import time
wo=1
with open("test.txt", "r", encoding='utf-8') as f:
    line = f.read()
a = line[700]+line[701]+line[702]+line[703]



print('\033[93m'+a+'\033[0m')