##Archivo para procesar los datos de las distintas bbdd, habria que poner para que metiendole por consola el nombre de la bbdd abramos una u otra; hacerlo con sys.argv

import csv
import json
import sys
import pandas as pd
from subprocess import call
import ast

f = open('cc.csv', 'w')
with open(sys.argv[1] + '.csv', newline='') as File:
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

call(['rm', '-r', sys.argv[1] ])
call (['mkdir', sys.argv[1]])
call (['cp', '-r', 'Mastodon', './'+sys.argv[1]])
call (['cp', './cc.csv', './'+sys.argv[1]])




ll = x
rt = open('cc.csv', 'r')
c = open('./'+sys.argv[1] + '/' + sys.argv[1] +'.csv', 'w')
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

call (['cp', './'+sys.argv[1] + '/' + sys.argv[1] +'.csv', './' + sys.argv[1] + '/Mastodon/src/main/scala/com/raphtory/mastodon/data' ])

h1 = open('./' + sys.argv[1] + '/Mastodon/src/main/scala/com/raphtory/mastodon/Runner.scala', 'r')
h2 = open('./' + sys.argv[1] + '/Mastodon/src/main/scala/com/raphtory/mastodon/Runner2.scala', 'w')

for line in h1:
    if("val source" in line):
        h2.write('        val source    = new FileSpout("src/main/scala/com/raphtory/mastodon/data", "' + sys.argv[1] +'.csv") \n')
    else:
        h2.write(line)

h2.close()
h1.close()

call(['rm', './' + sys.argv[1] + '/Mastodon/src/main/scala/com/raphtory/mastodon/Runner.scala'])
call(['mv', './' + sys.argv[1] + '/Mastodon/src/main/scala/com/raphtory/mastodon/Runner2.scala', './' + sys.argv[1] + '/Mastodon/src/main/scala/com/raphtory/mastodon/Runner.scala'])
call(['rm', '-r', './' + sys.argv[1] + '/Mastodon/src/main/scala/com/raphtory/mastodon/graphbuilders/MastUserGraphBuilder.scala'])

j2 = open('./' + sys.argv[1] + '/Mastodon/src/main/scala/com/raphtory/mastodon/graphbuilders/MastUserGraphBuilder.scala', 'a')

j2.write('package com.raphtory.mastodon.graphbuilders\n\n')
j2.write('import com.raphtory.core.components.graphbuilder.GraphBuilder\n')
j2.write('import com.raphtory.core.implementations.generic.messaging._\n')
j2.write('import com.raphtory.core.model.graph.{ImmutableProperty, Properties, Type}\n')
j2.write('import java.text.SimpleDateFormat\n')
j2.write('class MastUserGraphBuilder extends GraphBuilder[String]{\n\n')
j2.write('    override def parseTuple(tuple: String) = {\n')
j2.write('        val fileLine = tuple.split(";").map(_.trim)\n')
j2.write('        val sourceNode = fileLine(1).toInt\n')
lo = 0
loo = 0
while(lo<(x-2)):
    y= lo+2
    z = '        val targetNodement'+str(lo)+'= fileLine('+str(y)+').toInt\n'
    j2.write(z)
    lo = lo + 1
while(loo<(x-2)):
    j2.write('            if (targetNodement'+ str(loo) +'> 0 && targetNodement'+ str(loo) +'!= sourceNode) {\n')
    j2.write('                val creationDate = dateToUnixTime(timestamp = fileLine(0).slice(0, 23))\n')
    j2.write('                addVertex(creationDate, sourceNode, Type("User"))\n')
    j2.write('                addVertex(creationDate, targetNodement'+ str(loo) +', Type("User"))\n')
    j2.write('                addEdge(creationDate, sourceNode, targetNodement'+ str(loo) +', Type("User to User"))\n')
    j2.write('            }\n\n')
    loo = loo + 1
j2.write('    def dateToUnixTime (timestamp: => String): Long = {\n')
j2.write('        val sdf   = new SimpleDateFormat("yyyy-MM-dd\'T\'HH:mm:ss")\n')
j2.write('        val dt    = sdf.parse(timestamp)\n')
j2.write('        val epoch = dt.getTime\n')
j2.write('        epoch\n')
j2.write('    }\n\n\n')
j2.write('}')
j2.write('')



