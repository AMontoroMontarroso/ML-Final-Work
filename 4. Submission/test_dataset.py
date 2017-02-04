"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
The goal of this script is prepare the test dataset for the prediction and the 
future submission.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


import csv
from string import strip

#Headers of products
products_h = ["ind_ahor_fin_ult1","ind_aval_fin_ult1","ind_cco_fin_ult1","ind_cder_fin_ult1","ind_cno_fin_ult1","ind_ctju_fin_ult1","ind_ctma_fin_ult1","ind_ctop_fin_ult1","ind_ctpp_fin_ult1","ind_deco_fin_ult1","ind_deme_fin_ult1","ind_dela_fin_ult1","ind_ecue_fin_ult1","ind_fond_fin_ult1","ind_hip_fin_ult1","ind_plan_fin_ult1","ind_pres_fin_ult1","ind_reca_fin_ult1","ind_tjcr_fin_ult1","ind_valo_fin_ult1","ind_viv_fin_ult1","ind_nomina_ult1","ind_nom_pens_ult1","ind_recibo_ult1"]
past_products_headers = map(lambda x: x + '_past', products_h)

#Open the output file
fo = open('../Data/test_submission.csv', 'w')
csv_out = csv.writer(fo)
csv_out.writerow(['ncodpers'] + products_h + past_products_headers + ['age'])

#Save the current products
products = dict()
f = open('../Data/train_ver2_clean2.csv')
csv_f = csv.reader(f)
csv_f.next()
for line in csv_f:
    line = map(strip, line)
    if line[0] == '2016-05-28':
        products[line[1]] = line[22:]

f.close()

#Save the past products
f = open('../Data/product_past.csv')
csv_f = csv.reader(f)
past = dict()

for line in csv_f:
    past[line[0]] = line[1:]

f.close()

#Save the results
f = open('../Data/test_ver2.csv')
csv_f = csv.reader(f)
csv_f.next()

for line in csv_f:
    line = map(strip, line)
    ps = [line[1]]
    if line[1] in products:
        ps.extend(products[line[1]])
    else:
        print 'ERROR: No tiene productos'
        break

    if line[1] in past:
        ps.extend(past[line[1]])
    else:
        ps.extend([0]*len(products_h))

    ps.append(line[5])
    csv_out.writerow(ps)
