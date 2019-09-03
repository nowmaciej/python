"""
Program pobiera plik input.csv wygenerowany z BMS - raport wejsc w danym miesiacu do pomieszczen TVN.
Nastepnie formatuje dane wyjsciowe zamieniajac pracownikow Onet na Obsluga techniczna, a pozostawiajac Imie, Nazwisko
pracownikow TVN. Wyjscie zapisuje w pliku output.csv
"""

import csv
from datetime import datetime

raport_input = open('input.csv','r') #plik wejsciowy
raport_output = open('output.csv','w', newline='') #plik wyjsciowy, newline='' dla usuniecia \r\n z konca linii

ile_wizyt = dict() #podliczenie ilosci wizyt dla kazdej osoby

row = csv.reader(raport_input) #wczytanie wszystkich wierszy pliku
next(row) #przeskoczenie pierwszego wiersza (smieci z BMS)
next(row) #przeskoczenie drugiego wiersza (naglowki po angielsku)

header = list(['Data','Osoba','Nr karty','Pomieszczenie']) #stworzenie wlasnych naglowkow (nazw kolumn)

writer = csv.writer(raport_output) #stworzenie wskaznika do zapisu do pliku
writer.writerow(header) #zapisanie naglowka

for data_row in row: #wykonaj dla kazdego wiersza
  data = datetime.strptime(data_row[0],'%Y-%m-%d %H:%M:%S') #formatowanie daty
  osoba = data_row[1] #wczytanie kolumny osoba
  karta = int(data_row[2]) #wczytanie kolumny nr karty
  pomieszczenie = str(data_row[3].split('\\')[-1]) #formatowanie nazwy pomieszczenia

  if osoba != '': #sprawdzenie czy nie jest pusty wpis
    osoba = osoba.strip().split('\\')[6].split('_') #pobranie tylko imienia, nazwiska, firmy
    if str(osoba[2]) != 'Tvn': #sprawdzenie czy TVN
      osoba = 'Obsluga techniczna'
    else:
      osoba = ' '.join(osoba[0:2]) #wybranie tylko imienia i nazwiska jezeli TVN

    if osoba not in ile_wizyt: #sprawdzenie czy osoba jest juz policzona
        ile_wizyt[osoba] = 1
    else:
      ile_wizyt[osoba] += 1 #zwiekszenie licznika wizyt osoby

    writer.writerow([data,osoba,karta,pomieszczenie]) #zapisanie wiersza do pliku
  else:
    continue  #jak jest pusta osoba to pomija

raport_input.close() #zamkniecie plikow
raport_output.close()

print('Ilosc wizyt na osobe:')
print(ile_wizyt)
  
