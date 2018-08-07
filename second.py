first = ['sai','tom','taylor']
last = ['ram','soumya''bublu']
names = zip(first,last)
for a,b in names:
    print(a,b)


answer = lambda x: x*7
print(answer(5))


import heapq
stocks = {
    'goog':520.45,
    'fb':457,
    'yahoo':4785
}
print(sorted(zip(stocks.values(),stocks.keys())))
print(heapq.nsmallest(2,stocks))












'''
from PIL import Image   ///pillow 
a = Image.open('tiger.jpg')
a.split()
'''





