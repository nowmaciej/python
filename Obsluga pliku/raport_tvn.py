import sys

plik_wyjsciowy = 'raport_out.csv'

if len(sys.argv) == 1:
    print('\nMusisz podac conajmniej jeden argument!!!\n')
    print('Format wykonania programu wyglada nastepujaco:\n')
    print('raport.exe [plik_wejsciowy] [opcjonalnie: plik_wyjsciowy]\n')
    print('Jezeli nie podasz pliku wyjsciowego, przyjmie on nazwe raport_out.csv (jezeli istnieje ZOSTANIE NADPISANY bez pytania)\n')
    print('Autor: Maciej Nowak - 2019\n')
    sys.exit()

if len(sys.argv) > 1:
    plik_wejsciowy = sys.argv[1]
if len(sys.argv) > 2:
    plik_wyjsciowy = sys.argv[2]


fin = open(plik_wejsciowy,'r')
fout = open(plik_wyjsciowy,'w')

plik_in = fin.readlines()

naglowek = 'Data,Osoba,Nr karty,Pomieszczenie\n'
fout.write(naglowek)

i=0

for i in range(2,len(plik_in)):
    wiersz = plik_in[i].strip().split(",")

    wiersz[3]='011'
    
     
    if wiersz[2]!='0' and wiersz[1]!='':
        firma = wiersz[1].split("\\")
        if firma[4]=='Kolokacja':
            if firma[5] == 'TVN':
                osoba=firma[6].split("_")
                wiersz[1]=''+osoba[1]+' '+osoba[0]
            else:
                wiersz[1]='Inny kolokant'
        else:
            wiersz[1]='Obsluga techniczna'
        
        wiersz = map(str, wiersz)
        wiersz = ",".join(wiersz)
        fout.write("%s\n" % wiersz)
        print(wiersz)
        
            
print('\n\n')
print('Zakonczono konwersje pliku '+plik_wejsciowy+'. Koncowy raport znajduje sie w pliku: '+plik_wyjsciowy+'\n')
print('Autor: Maciej Nowak - 2019\n')

fin.close()
fout.close()