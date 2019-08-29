import math

punkty = [(1,2),(2,4),(8,6),(2,8),(9,0),(3,1)]

def odleglosc(a,b):
    return int(math.sqrt((a[1]-a[0])**2+(b[1]-b[0])**2))

promienie_okregow = []

i = 0

for i in range(0,len(punkty)-1):
    for j in range(i+1, len(punkty)):
        print(odleglosc(punkty[i], punkty[j]))
        if odleglosc(punkty[i], punkty[j]) not in promienie_okregow:
            promienie_okregow.append(odleglosc(punkty[i], punkty[j]))
            

            
print('Ilosc okregow wynosi: {}:::{}'.format(len(promienie_okregow),promienie_okregow))