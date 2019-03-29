import numpy as np
import pandas as pd
import csv
from itertools import combinations

class Apriori(object):
    def __init__(self, csvfile):
        conteudo = csv.reader(csvfile, delimiter=',')
        todas_compras = []
        self.itens = set()
        for row in conteudo:
            if '' in row:
                row.remove('')
            todas_compras.append(row)
            self.itens |= set(row)
        self.len_data = len(todas_compras)
        self.hashMap = pd.Series(todas_compras)

    def varredura(self):
        self.c = []
        self.l = []
        self.l.append(list(self.itens))
        version = 0
        while True:
            print('----- VERSION '+ str(version+1) + ' -----')
            print(self.l[version])
            self.c.append(self.core(self.l[version]))
            print(self.c[-1])
            comb = list(combinations(list(self.c[version][self.c[version]['Contagem'] > 6].index), 2))
            self.l.append(comb)
            if version == 1:
                break
            version += 1

    def core(self, letter_L):
        result = pd.DataFrame(index=letter_L, columns='Contagem %'.split())
        for i in letter_L:
            counter = 0
            for j in self.hashMap:
                if isinstance(i, str):
                   i = [i]
                if set(j).issuperset(i):
                    counter += 1
            result.loc[i, 'Contagem'] = counter
            result.loc[i, '%'] = (counter/self.len_data)*100
        return result

teste = open('data.csv')
a = Apriori(teste)
a.varredura()