##Archivo para procesar los datos de las distintas bbdd, habria que poner para que metiendole por consola el nombre de la bbdd abramos una u otra; hacerlo con sys.argv

import csv
import json
import sys
from subprocess import call
import ast
import os
import pandas as pd


os.chdir('./csv')
os.system('ls > lista.txt')
l = open('lista.txt', 'r')
a = []
for row in l:
    if "lista" in row:
        print("")
    else:
        a.append(row)

l.close()
b = []
for i in a:
    i = i.replace("\n", "")
    b.append(i)
uu = 0
for i in b:
    cccc = str(str(i).replace(".csv", ""))
    print(cccc)
    call(['sudo','rm', '-r', 'csv/' + cccc])
    if (uu>0):
        os.chdir('../../')
    print(i)
    f = open('ini' + str(i), 'w')
    with open(str(i), newline='') as File:
        reader = csv.reader(File)
        writer = csv.writer(f)
        iniii = 0
        for row in reader:
            for ce in row:
                if(ce == "mentions"):
                    print(iniii)
                    res = iniii
                    yyy = ce
                    print(yyy)
                    print(iniii)
                if(ce == "created_at"):
                    print(iniii)
                    date = iniii
                if(ce == "account.acct"):
                    print(iniii)
                    user = iniii
                if(ce == "account.username"):
                    print(iniii)
                    us = iniii
                if(ce == "account.id"):
                    print(iniii)
                    usid = iniii
                iniii = iniii + 1
            
            row[res] = row[res].replace("[]","")
            if(row[res] =="mentions"):
                w = []
                w.append(row[date])
                w.append(row[res])
                writer.writerow(w)
            else: 
                if(row[res] != ''):
                    row[res] = row[res].replace("[", "")
                    row[res] = row[res].replace("]", "")
                    x = row[res]
                    x = x.replace("u'", "'")
                    x = x.replace("{", "")
                    x = x.replace("}", "")
                    x = x.replace("'username':", '')
                    x = x.replace("'url':", '')
                    x = x.replace("'id':", '')
                    x = x.replace("'acct':", '')
                    x = x.replace(" ", "")
                    x = x.replace("'", "")
                    row[res] =  x.split(",")
                    l = len(row[res])
                    w = []
                    r = row[user].replace(row[us] + "@", "")
                    w.append(row[date])
                    w.append(row[usid])
                    w.append(r)
                    while (l > 0):
                        w.append(row[res][l-2])
                        p = row[res][l-1].replace(row[res][l-4] + "@", "")
                        w.append(p)
                        l = l-4
                    writer.writerow(w)
    f.close()

    r = open('ini'+str(i),'r')
    reader = csv.reader(r)
    x = 0
    for row in reader:
        if(len(row)>x):
            x = len(row)
    r.close()
    
    
    call (['mkdir', cccc])
    call (['cp', '-r', '../Mastodon', './'+cccc])
    call (['cp', './ini'+ str(i), './'+cccc])


    ll = x
    rt = open('ini'+str(i), 'r')
    c = open('./'+  cccc + '/' + str(i), 'w')
    wt = csv.reader(rt)
    ww = csv.writer(c)
    for row in wt:
        if(row[1] == "mentions"):
            rrr = ["created_at", "userid", "server"]
            while(ll>4):
                rrr.append("mentions")
                rrr.append("server")
                ll = ll -2
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

    call (['cp', './'+ cccc + '/' + str(i), './' + cccc + '/Mastodon/src/main/scala/com/raphtory/mastodon/data' ])
    call (['rm', '-r', './' + cccc + '/Mastodon/src/main/scala/com/raphtory/mastodon/Runner.scala'])

    h2 = open('./' + cccc + '/Mastodon/src/main/scala/com/raphtory/mastodon/Runner.scala', 'a')

    h2.write('package com.raphtory.mastodon;\n\n')
    h2.write('import com.raphtory.mastodon.graphbuilders.MastUserGraphBuilder\n')
    h2.write('import com.raphtory.core.build.server.RaphtoryGraph\n')
    h2.write('import com.raphtory.algorithms.{ConnectedComponents, Degree}\n')
    h2.write('import com.raphtory.spouts.FileSpout\n\n')
    h2.write('object Runner extends App{\n')
    h2.write('        val builder   = new MastUserGraphBuilder()\n')
    h2.write('        val source    = new FileSpout("src/main/scala/com/raphtory/mastodon/data", "' + str(i) + ') \n')
    h2.write('        val rg        = RaphtoryGraph[String](source,builder)\n')
    h2.write('        rg.rangeQuery(Degree(path="/Users/pedrollorenteflores/Desktop/TFG/'+ cccc +'/Degree"), start = 1482404531000L, end = 1525723247000L, increment = 3600000L, windows = List(3600000L, 86400000L, 604800000L, 2592000000L, 31536000000L))\n')
    h2.write('        }')
    h2.close()


    call(['rm', '-r', './' + cccc + '/Mastodon/src/main/scala/com/raphtory/mastodon/graphbuilders/MastUserGraphBuilder.scala'])
    j2 = open('./' + cccc + '/Mastodon/src/main/scala/com/raphtory/mastodon/graphbuilders/MastUserGraphBuilder.scala', 'a')

    j2.write('package com.raphtory.mastodon.graphbuilders\n\n')
    j2.write('import com.raphtory.core.components.graphbuilder.GraphBuilder\n')
    j2.write('import com.raphtory.core.implementations.generic.messaging._\n')
    j2.write('import com.raphtory.core.model.graph.{ImmutableProperty, Properties, Type}\n')
    j2.write('import java.text.SimpleDateFormat\n')
    j2.write('class MastUserGraphBuilder extends GraphBuilder[String]{\n\n')
    j2.write('    override def parseTuple(tuple: String) = {\n')
    j2.write('        val fileLine = tuple.split(",").map(_.trim)\n')
    j2.write('        val sourceNode = fileLine(1).toInt\n')
    lo = 1
    y = 3
    loo = 1
    while(lo<(x/2-1)):
        z = '        val targetNodement'+str(lo)+'= fileLine('+str(y)+').toInt\n'
        j2.write(z)
        lo = lo + 1
        y = y + 2
    while(loo<(x/2-1)):
        j2.write('            if (targetNodement'+ str(loo) +'> 0 && targetNodement'+ str(loo) +'!= sourceNode) {\n')
        j2.write('                val creationDate = dateToUnixTime(timestamp = fileLine(0).slice(0, 23))\n')
        j2.write('                addVertex(creationDate, sourceNode, Type("User"))\n')
        j2.write('                addVertex(creationDate, targetNodement'+ str(loo) +', Type("User"))\n')
        j2.write('                addEdge(creationDate, sourceNode, targetNodement'+ str(loo) +', Type("User to User"))\n')
        j2.write('            }\n\n')
        loo = loo + 1
    j2.write('    }\n')
    j2.write('    def dateToUnixTime (timestamp: => String): Long = {\n')
    j2.write('        val sdf   = new SimpleDateFormat("yyyy-MM-dd\'T\'HH:mm:ss")\n')
    j2.write('        val dt    = sdf.parse(timestamp)\n')
    j2.write('        val epoch = dt.getTime\n')
    j2.write('        epoch\n')
    j2.write('    }\n\n\n')
    j2.write('}')

    j2.close()
    call(['mkdir', './'+str(cccc)+'/grafo'])
    os.chdir('./'+str(cccc)+'/grafo')
    call (['cp', '../'+str(i), '.'])
    g = open(str(i), 'r')
    g1 = open('enlace.csv', 'w')
    h = []
    reader = csv.reader(g)
    writer = csv.writer(g1)
    for row in reader:
        if "server" in row[2]:
            h = ["source", "target"]
            writer.writerow(h)
        else:
            h = [row[2], row[4]]
            writer.writerow(h)
        h = []
    g.close()
    g1.close()
    uu = uu +1
    g2 = pd.read_csv("enlace.csv")
    w = g2["source"].unique()
    xxx = g2["target"].unique()
    xxx = xxx.tolist()
    for ii in w:
        if not ii in xxx:
            xxx.append(ii)
    g1 = open('nodo.csv', 'w')
    
    writer = csv.writer(g1)
    uuu = 0
    for iii in xxx:
        if(uuu == 0):
            writer.writerow(["Id", "Label"])
        else:   
            writer.writerow([uuu, iii])
        uuu = uuu + 1
    g1.close()


    
    


#os.chdir(sys.argv[1] + '/Mastodon')
#call(['sbt', 'compile'])
#call(['sbt', 'run'])



        