from matplotlib import pyplot as plt
import sys

#plt.xkcd()

plik_raportu = 'n1w1.csv'
fin = open(plik_raportu, 'r')
dane = fin.readlines()

wykres_x = []
tnaw = []
twyw = []
wnaw = []
wwyw = []
sp = []
tzew = []
wzew = []
chster = []
wilgster = []
wymobr = []
labels=[]

for i in range(2,len(dane)):
    wiersz = dane[i].strip().split(",")
    wykres_x.append(i)
    labels.append(wiersz[0])
    tnaw.append(wiersz[1])
    twyw.append(wiersz[2])
    wnaw.append(wiersz[3])
    wwyw.append(wiersz[4])
    sp.append(wiersz[5])
    tzew.append(wiersz[6])
    wzew.append(wiersz[7])
    chster.append(wiersz[8])
    wilgster.append(wiersz[9])
    wymobr.append(wiersz[10])


plt.plot(wykres_x,tnaw, label='T Naw')
plt.plot(wykres_x,twyw, label='T Wyw')
plt.plot(wykres_x,wnaw, label='Wilg Naw')
plt.plot(wykres_x,wwyw, label='Wilg Wyw')
plt.plot(wykres_x,sp, label='SP')
plt.plot(wykres_x,tzew, label='T Zewn')
plt.plot(wykres_x,wzew, label='Wilg Zewn')
plt.plot(wykres_x,chster, label='Chiller Ster')
plt.plot(wykres_x,wilgster, label='Wilg Ster')
plt.plot(wykres_x,wymobr, label='Wym Obr Ster')

plt.xlabel('Data')
plt.legend()
plt.xticks(wykres_x,labels,rotation='vertical')

plt.grid(True)
plt.tight_layout()
plt.show()
fin.close()