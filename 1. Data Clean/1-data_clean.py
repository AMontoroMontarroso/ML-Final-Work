import csv
import datetime
from string import strip
from calendar import monthrange


def monthdelta(d1, d2):
    delta = 0
    while True:
        mdays = monthrange(d1.year, d1.month)[1]
        d1 += datetime.timedelta(days=mdays)
        if d1 <= d2:
            delta += 1
        else:
            break
    return delta


f = open('./Data/train_ver2.csv')
csv_f = csv.reader(f)
headers = csv_f.next()
clientes_ind_empleado = dict()
clientes_pais_residencia = dict()
clientes_sexo = dict()
clientes_age = dict()
clientes_fecha_alta = dict()
clientes_indrel_1mes = dict()
clientes_indresi = dict()
clientes_indext = dict()
clientes_conyuemp = dict()
clientes_canal_entrada = dict()
clientes_indfall = dict()
clientes_tipodom = dict()
clientes_nomprov = dict()
clientes_renta = dict()
clientes_segment = dict()

for c in csv_f:
    c = map(strip, c)
    if c[1] not in clientes_ind_empleado and c[2] != '' and c[2] != 'NA':
        clientes_ind_empleado[c[1]] = c[2]
    if c[1] not in clientes_pais_residencia and c[3] != '' and c[3] != 'NA':
        clientes_pais_residencia[c[1]] = c[3]
    if c[1] not in clientes_sexo and c[4] != '' and c[4] != 'NA':
        clientes_sexo[c[1]] = c[4]
    if c[1] not in clientes_age and c[5] != '' and c[5] != 'NA':
        clientes_age[c[1]] = c[5]
    if c[1] not in clientes_fecha_alta and c[6] != '' and c[6] != 'NA':
        clientes_fecha_alta[c[1]] = c[6]
    if c[1] not in clientes_indrel_1mes and c[11] != '' and c[11] != 'NA':
        clientes_indrel_1mes[c[1]] = c[11]
    if c[1] not in clientes_indresi and c[13] != '' and c[13] != 'NA':
        clientes_indresi[c[1]] = c[13]
    if c[1] not in clientes_indext and c[14] != '' and c[14] != 'NA':
        clientes_indext[c[1]] = c[14]
    if c[1] not in clientes_conyuemp and c[15] != '' and c[15] != 'NA':
        clientes_conyuemp[c[1]] = c[15]
    if c[1] not in clientes_canal_entrada and c[16]    != '' and c[16] != 'NA':
        clientes_canal_entrada[c[1]] = c[16]
    if c[1] not in clientes_indfall and c[17] != '' and c[17] != 'NA':
        clientes_indfall[c[1]] = c[17]
    if c[1] not in clientes_tipodom and c[18] != '' and c[18] != 'NA':
        clientes_tipodom[c[1]] = c[18]
    if c[1] not in clientes_nomprov and c[20] != '' and c[20] != 'NA':
        clientes_nomprov[c[1]] = c[20]
    if c[1] not in clientes_renta and c[22] != '' and c[22] != 'NA':
        clientes_renta[c[1]] = c[22]
    if c[1] not in clientes_segment and c[23] != '' and c[23] != 'NA':
        clientes_segment[c[1]] = c[23]

f.close()
f = open('./Data/train_ver2.csv')
csv_f = csv.reader(f)
headers = csv_f.next()

fo = open('./Data/train_ver2_clean1.csv', 'w')
csv_fo = csv.writer(fo)

csv_fo.writerow(headers)
ind_empleado_recuperados = 0
pais_residencia_recuperados = 0
sexo_recuperados = 0
age_recuperados = 0
fecha_alta_recuperados = 0
indrel_1mes_recuperados = 0
indresi_recuperados = 0
indext_recuperados = 0
conyuemp_recuperados = 0
canal_entrada_recuperados = 0
indfall_recuperados = 0
tipodom_recuperados = 0
nomprov_recuperados = 0
renta_recuperados = 0
segment_recuperados = 0

for c in csv_f:
    c = map(strip, c)
    if c[1] in clientes_indresi and (c[2] == '' or c[2] == 'NA') and c[1] in clientes_pais_residencia and (c[3] == '' or c[3] == 'NA'):
        #Para clientes que se dieron de baja volvieron a contratar. En su primer periodo como clientes se pierden datos de forma sistematica en todos aquellos con esta situacion. Vease 1054429 o 1363761. Se les pone como estaban activos.
        c[7] = '0' #No se considera nuevo
        c[9] = '1' #Primario
        c[12] = 'I'#Dado que son los ultimos meses antes de darse de baja. Lo normal que es no sea activo
        c[21] = '0'
        if(c[1] in clientes_indrel_1mes):
            if(clientes_indrel_1mes[c[1]] in ['3', '3.0']): #Si ex primario
                c[11] = '1' #primario
            else:
                c[11] = '2' #Si ex copropietario enteonces propietario
    if (c[2] == '' or c[2] == 'NA') and c[1] in clientes_ind_empleado:
        c[2] = clientes_ind_empleado[c[1]]
        ind_empleado_recuperados += 1
    if (c[3] == '' or c[3] == 'NA') and c[1] in clientes_pais_residencia:
        c[3] = clientes_pais_residencia[c[1]]
        pais_residencia_recuperados += 1
    if (c[4] == '' or c[4] == 'NA') and c[1] in clientes_sexo:
        c[4] = clientes_sexo[c[1]]
        sexo_recuperados += 1
    if (c[5] == '' or c[5] == 'NA') and c[1] in clientes_age:
        c[5] = clientes_age[c[1]]
        age_recuperados += 1
    if (c[6] == '' or c[6] == 'NA') and c[1] in clientes_fecha_alta:
        c[6] = clientes_fecha_alta[c[1]]
        fecha_alta_recuperados += 1
    if (c[11] == '' or c[11] == 'NA') and c[1] in clientes_indrel_1mes:
        c[11] = clientes_indrel_1mes[c[1]]
    if (c[13] == '' or c[13] == 'NA') and c[1] in clientes_indresi:
        c[13] = clientes_indresi[c[1]]
        indresi_recuperados += 1
    if (c[14] == '' or c[14] == 'NA') and c[1] in clientes_indext:
        c[14] = clientes_indext[c[1]]
        indext_recuperados += 1
    if (c[15] == '' or c[15] == 'NA') and c[1] in clientes_conyuemp:
        c[15] = clientes_conyuemp[c[1]]
        conyuemp_recuperados += 1
    if (c[16] == '' or c[16] == 'NA') and c[1] in clientes_canal_entrada:
        c[16] = clientes_canal_entrada[c[1]]
        canal_entrada_recuperados += 1
    if (c[17] == '' or c[17] == 'NA') and c[1] in clientes_indfall:
        c[17] = clientes_indfall[c[1]]
        indfall_recuperados += 1
    if (c[18] == '' or c[18] == 'NA') and c[1] in clientes_tipodom:
        c[18] = clientes_tipodom[c[1]]
        tipodom_recuperados += 1
    if (c[20] == '' or c[20] == 'NA') and c[1] in clientes_nomprov:
        c[20] = clientes_nomprov[c[1]]
        nomprov_recuperados += 1
    if (c[22] == '' or c[22] == 'NA') and c[1] in clientes_renta:
        c[22] = clientes_renta[c[1]]
        renta_recuperados += 1
    if (c[23] == '' or c[23] == 'NA') and c[1] in clientes_segment:
        c[23] = clientes_segment[c[1]]
        segment_recuperados += 1
    if c[8] == 'NA' or c[8] == '': #Antiguedad
        if(c[6] != 'NA' and c[6] != ''):
            a = datetime.datetime.strptime(c[6], '%Y-%m-%d') #Fecha alta
            b = datetime.datetime.strptime(c[0], '%Y-%m-%d') #Fecha datos
            c[8] = monthdelta(a, b)#diferencia en meses

    csv_fo.writerow(c)

f.close()
fo.close()

from tabulate import tabulate

features = ['ind_empleado', 'pais_residencia', 'sexo', 'age', 'fecha_alta', 'indresi', 'indext', 'conyuemp', 'canal_entrada', 'indfall', 'tipodom', 'nomprov', 'renta', 'segment']
values = [ind_empleado_recuperados, pais_residencia_recuperados, sexo_recuperados, age_recuperados, fecha_alta_recuperados, indresi_recuperados, indext_recuperados, conyuemp_recuperados, canal_entrada_recuperados, indfall_recuperados, tipodom_recuperados, nomprov_recuperados, renta_recuperados, segment_recuperados]

table = zip(features, values)
print tabulate(table, headers = ['Feature', 'Recovered'])
