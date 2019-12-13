import sys
import datetime
import os

directory = os.fsencode('./')
x = datetime.datetime.now()
miesiac_dzisiaj = x.strftime("%m")
plik_wejsciowy = ''

fpout = open('podsumowanie.csv','w')
fpout.write('Podsumowanie ilosci bledow sterownikow w aktualnym ({})\n\n'.format(miesiac_dzisiaj))


for filename in os.listdir(directory):
    plik_wejsciowy = filename.decode("utf-8")
    
    sterownik = plik_wejsciowy[0:-4]
  
    if plik_wejsciowy[-3:]==('txt'):
        plik_wyjsciowy = 'out_' + plik_wejsciowy
        fin = open(plik_wejsciowy,'r')
        fout = open(plik_wyjsciowy,'w')

        plik_in = fin.readlines()

        naglowek = ''

        for i in range(1,7):
            naglowek += plik_in[i]
            
        naglowek += 'Line\tLevel\tTime\tStamp\tError Code\n'

        fout.write(naglowek)

        wiersz_out = []
        ilosc_bledow = {}

        for i in range(9,len(plik_in)):
            wiersz = plik_in[i].strip().split("\t")
            data = wiersz[2].strip().split("/")
                 
            if wiersz[1] == "E" and data[0] == miesiac_dzisiaj:
                if wiersz[3] not in ilosc_bledow:
                    ilosc_bledow[wiersz[3]]=0
                else:
                    ilosc_bledow[wiersz[3]]+=1
                        
                wiersz_out = wiersz[2:4]
                wiersz_out = map(str, wiersz_out)
                wiersz_out = "\t".join(wiersz_out)
                fout.write("%s\n" % wiersz_out)

        if ilosc_bledow == {}:
            fout.write("\nBrak bledow typu ERROR w obecnym miesiacu [%s]\n" % miesiac_dzisiaj)
            fpout.write('{}\tBrak bledow\n'.format(sterownik))
        else:
            fout.write("\nIlosc wystapien bledow: %s\n" % ilosc_bledow)
            fpout.write('{}\t{}\n'.format(sterownik,ilosc_bledow))
        
        fin.close()
        fout.close()
fpout.close()
