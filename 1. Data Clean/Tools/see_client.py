import csv

ncodpers = '219093'

f = open('./Data/train_ver2_clean2.csv')
csv_f = csv.reader(f)
headers = csv_f.next()

for cliente in csv_f:
    if cliente[1].strip() == ncodpers:
        print cliente
"""
f = open('./Data/test_ver2.csv')
csv_f = csv.reader(f)
headers = csv_f.next()

for cliente in csv_f:
    if cliente[1] == ncodpers:
        print cliente
"""
