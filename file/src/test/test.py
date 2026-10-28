# R.GISPython

import numpy as np
import sys

# Not or for logic test
# Regular expression could look like if x == 1 or x==3.... :
x = 3
if x in (1,2,3,4):
    print('x = %i founded' % (x))
else:
    print('x = %i not founded' % (x))


statusFilter = ['Activa', 'En Mantenimiento']
print(statusFilter[0])

# Time stamp Python 2 - Sample 1
# https://www.codegrepper.com/code-examples/python/python+2.7+datetime+to+timestamp
import time
from datetime import datetime
d = datetime(2022, 1, 1, 11, 30)
print('Unix time: ' + str(int(time.mktime(d.timetuple())*100)))

# Time stamp Python 2 - Sample 2
import time
from datetime import datetime
dTime = datetime.today()
print('Unix time: ' + str(int(time.mktime(dTime.timetuple())*100)))

'''
# Time stamp Python 3
from datetime import datetime
dTime = datetime.today()  # Get timezone naive now
secondsInt = int(dTime.timestamp()*100)
print('Time stamp: '+ str(secondsInt))
'''

'''
# Print an image
import pandas as pd
import matplotlib.pyplot as plt
img = plt.imread('D:\R.GISPython\TableInterpolatedGrid\OutputGrid\GRDM010.tif')
plt.imshow(img)
plt.show()
'''

'''
# Multidimensional array basic operations with print in a file
logAreaEval = open('C:/Temp/ZonificacionAnalisisAreas.txt', 'w+')
evalAreaSZH= [[300,120], [700,180], [900,320], [1100,400], [1300,0], [1500,0], [2000,0], [2500,0], [3500,0], [5000,0], [10000,0], [20000,0], [999999,0]]
evalAreaSZH[4][1] = 1973
cont = 0
for i in evalAreaSZH:
    if cont == 0:
        vTxt = str(i[0]) + ', ' + str(i[1])
        print(vTxt)
        logAreaEval.write(vTxt + '\n' )
    else:
        vTxt = str(i[0]) + ', ' + str(i[1]-evalAreaSZH[cont-1][1])
        print(vTxt)
        logAreaEval.write(vTxt + '\n')
    cont += 1

# Simple array evaluation with numpy
data = np.array([[1,'Alto'],[2,'Medio'],[3,'Bajo']])
print(pd.DataFrame(data,columns=['A','B']))

# Simple array evaluation without numpy
data1 = [[1,'Alto'],[2,'Medio'],[3,'Bajo']]
for i in data1[:]:
    print(i[0])


# Date time basics
from datetime import date
currentDate = date.today()
print(str(currentDate.year)+str(currentDate.month)+str(currentDate.day))

# Basic jenks eval
jenksVal = (2380.173697,9038.960497,20170.29529,65187.50527)
def JenksEval(value, iAux=1):
    for i in jenksVal:
        if value <= i:
            return iAux
        iAux+=1
print('Valor en rango: '+str(JenksEval(175.4)))

# Multiple eval classification
jenksVal = (2380.173697,9038.960497,20170.29529,999999)
equalIntVal = (16308.67596, 32601.61906, 48894.56217, 65187.50527)
quantileVal = (132.666736, 287.448131, 699.363055, 65187.50527)
geoIntVal = (191.655691, 1390.204041, 9555.818893, 65187.50527)
stdDevVal = (2612.35632, 5810.910895, 9009.46547, 65187.50527)
def JenksEval(value, classMethod, iAux=1):
    for i in classMethod:
        if value <= i:
            return iAux
        iAux+=1
print('Valor en rango: '+str(JenksEval(175.4,jenksVal,1)))

# For with internal counter and skip line jump
for i in range(2,12):
    print(' ',i, end = ', ')

'''