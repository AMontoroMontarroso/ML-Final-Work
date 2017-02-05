# -*- coding: utf-8 -*-

import csv
import random

f = open('./Data/train_ver2.csv')
csv_f = csv.reader(f)
headers = csv_f.next()
clients = dict()


features = {
2:'ind_empleado',
3:'pais_residencia',
9:'indrel',
10:'ult_fec_cli_1t',
11:'indrel_1mes',
12:'tiprel_1mes',
13:'indresi',
14:'indext',
15:'conyuemp',
16:'canal_entrada',
17:'indfall',
18:'tipodom'
19:'cod_prov',
20:'nomprov',
21:'ind_actividad_cliente',
22:'renta',
23:'segment'
}

for cliente in csv_f:
    if cliente[1] not in clients:
        clients[cliente[1]] = [[cliente[x] for x in sorted(features.keys())]]
    else:
        clients[cliente[1]].append([cliente[x] for x in sorted(features.keys())])

distintos = [0] * len(features)
for k in clients:
    cliente = zip(*clients[k])
    for i, feature in enumerate(cliente):
        distinto = False
        for e1 in feature:
            for e2 in feature:
                if e1 != e2 and e1.strip() != '' and e2.strip() != '' and e1.strip() != 'NA' and e2.strip() != 'NA':
                    distintos[i] += 1
                    distinto = True
                    break
            if distinto:
                break

from tabulate import tabulate

table = zip([features[k] for k in sorted(features)], distintos)
print tabulate(table, headers = ['Feature', 'Diferents'])
