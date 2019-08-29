import pandas as pd
import numpy as np

wejscie = pd.read_csv('raport.csv', delimiter=',', header=1, usecols=[0,2,3], converters=[])

print(wejscie)