import csv
import json
import sys
import pandas as pd
from subprocess import call

call(['rm', '-r', 'dat.csv'])
a = open('partition-0', 'r')
b = open('partition-1', 'r')
c = open('partition-2', 'r')
d = open('partition-3', 'r')
e = open('partition-4', 'r')
f = open('partition-5', 'r')
g = open('partition-6', 'r')
h = open('partition-7', 'r')
i = open('dat.csv', 'a')

i.write('date, window, userid, in-degree, out-degree, degree \n')
for line in a:
    i.write(line)
for line in b:
    i.write(line)
for line in c:
    i.write(line)
for line in d:
    i.write(line)
for line in e:
    i.write(line)
for line in f:
    i.write(line)
for line in g:
    i.write(line)
for line in h:
    i.write(line)

a.close()
b.close()
c.close()
d.close()
e.close()
f.close()
g.close()
h.close()
i.close()