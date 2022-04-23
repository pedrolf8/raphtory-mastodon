##Archivo para procesar los datos de las distintas bbdd, habria que poner para que metiendole por consola el nombre de la bbdd abramos una u otra; hacerlo con sys.argv

import csv
import json
import pandas as pd
from subprocess import call
import ast

f = open('cc.csv', 'w')
with open('znark.us.csv', newline='') as File:
    reader = csv.reader(File)
    writer = csv.writer(f)
    
    for row in reader:
        row[44] = row[44].replace("[]","")
        if(row[44] =="mentions"):
            w = []
            w.append(row[36])
            w.append(row[44])
            writer.writerow(w)
        else: 
            if(row[44] != ''):
                row[44] = row[44].replace("[", "")
                row[44] = row[44].replace("]", "")
                x = row[44]
                x = x.replace("u'", "'")
                x = x.replace("{", "")
                x = x.replace("}", "")
                x = x.replace("'username':", '')
                x = x.replace("'url':", '')
                x = x.replace("'id':", '')
                x = x.replace("'acct':", '')
                x = x.replace(" ", "")
                x = x.replace("'", "")
                row[44] =  x.split(",")
                l = len(row[44])
                w = []
                w.append(row[36])
                while (l > 0):
                    w.append(row[44][l-2])
                    l = l-4
                writer.writerow(w)
f.close()

r = open('cc.csv','r')
reader = csv.reader(r)
x = 0
for row in reader:
    if(len(row)>x):
        x = len(row)
r.close()


ll = x
rt = open('cc.csv', 'r')
c = open('cc1.csv', 'w')
wt = csv.reader(rt)
ww = csv.writer(c)
for row in wt:
    if(row[1] == "mentions"):
        rrr = ["created_at", "mentions"]
        while(ll>2):
            rrr.append("mentions")
            ll = ll -1
            print(ll)
        ww.writerow(rrr)  
    else:
        g = row
        li = len(row)
        xx = x
        while(xx>li):
            g.append(-1)
            xx = xx - 1
        ww.writerow(g)
rt.close()
c.close()



#g = load_dataset('cc.csv')
