# -*- coding: utf-8 -*-

from string import strip
import csv

def diff(a, b):
    a = map(int, a)
    b = map(int, b)
    r = [0]*len(a)
    for i in range(len(a)):
        r[i] = a[i] - b[i]
    return r

def sumar(a, b):
    a = map(int, a)
    b = map(int, b)
    r = [0]*len(a)
    for i in range(len(a)):
        r[i] = (a[i] + b[i]) % 1
    return r


f = open('./Data/train_ver2_clean2.csv')
fo = open('./Data/train_ver2_product_added.csv', 'w')
csv_f = csv.reader(f)
headers = csv_f.next()
csv_o = csv.writer(fo)

products = ["ind_ahor_fin_ult1","ind_aval_fin_ult1","ind_cco_fin_ult1","ind_cder_fin_ult1","ind_cno_fin_ult1","ind_ctju_fin_ult1","ind_ctma_fin_ult1","ind_ctop_fin_ult1","ind_ctpp_fin_ult1","ind_deco_fin_ult1","ind_deme_fin_ult1","ind_dela_fin_ult1","ind_ecue_fin_ult1","ind_fond_fin_ult1","ind_hip_fin_ult1","ind_plan_fin_ult1","ind_pres_fin_ult1","ind_reca_fin_ult1","ind_tjcr_fin_ult1","ind_valo_fin_ult1","ind_viv_fin_ult1","ind_nomina_ult1","ind_nom_pens_ult1","ind_recibo_ult1"]

past_products_headers = map(lambda x: x + '_past', products)
csv_o.writerow(headers + past_products_headers + ['product'])

clientes_products_anterior = dict()
clientes_past_products = dict()

for c in csv_f:
    c = map(strip, c)
    ncodpers = c[1]
    if ncodpers not in clientes_products_anterior:
        clientes_products_anterior[ncodpers] = c[22:]
    else:
        if clientes_products_anterior[ncodpers] != c[22:]:
            dife = diff(c[22:], clientes_products_anterior[ncodpers])
            products_added = []
            products_past = [0] * len(dife)
            for x in range(len(dife)):
                if dife[x] == 1:#Nuevo producto adquirido
                    products_added.append(products[x])
                if dife[x] == -1:#Producto eliminado
                    products_past[x] = 1
            #Actualizamos con los productos que tuvo en el pasado el cliente
            if ncodpers not in clientes_past_products:
                clientes_past_products[ncodpers] = products_past
            else:
                clientes_past_products[ncodpers] = sumar(clientes_past_products[ncodpers],  products_past)
            #Si se ha añadido algun producto se añade al conjunto de entrenamiento
            if products_added:
                #Informacion demografica + estado de productos adquiridos + productos de los que se dio de baja + productos añadidos
                n_added = c[:22] + clientes_products_anterior[ncodpers] + clientes_past_products[ncodpers] + [' '.join(sorted(products_added))]
                csv_o.writerow(n_added)

        clientes_products_anterior[ncodpers] = c[22:]
