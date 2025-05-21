# -*- coding: UTF-8 -*-
# Script name: ColorMapStyle.py, ColorMapStyleValue.py
# Description: Color ramp style generator
# Requirements: Python 3+

# Libraries
import ColorMapStyleValue as cmsv
import sys
from datetime import datetime
import matplotlib
import matplotlib.pyplot as plt

# Python rgb color changing text function
def colorrgb(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

# Markdown header separator table function
def tableseparatormarkdown(n=2):
    lineSep = '|---'
    printlog(lineSep * n + '|', True)

# Print and or show log in screen
def printlog(txtPrint, onScreen=True):
    if onScreen: print(txtPrint)
    fileLog.write(txtPrint + '\n')

# Variables
baseRGBColors = cmsv.ColorMap13  # ✓✓✓ User can change ✓✓✓ - Style values from ColorMapStyleValue.py
styleNumber = 13  # ✓✓✓ User can change ✓✓✓
numColor = 256  # ✓✓✓ User can change ✓✓✓
filePath = r'D:/R.GISPython/ColorMapStyle'  # r'.' for relative path
fileName = 'ColorMapArcGIS'+str(numColor)+'s'+str(styleNumber)
fileNameOutput = filePath+'/Output/'+fileName+'.clr'
fileLog = open(filePath+'/Output/'+fileName+'.md', 'w+')
urlGitHub = 'https://github.com/rcfdtools/R.GISPython/blob/main/ColorMapStyle'
fileColorName = open(fileNameOutput, 'w+')
cutRamp = len(baseRGBColors)-1
discreteCutValue = int(numColor/cutRamp)
moduleEval = numColor % cutRamp
xVal, yVal, pyRBG = [], [], []
rgbSampleResolution = 96
printCutOnScreen = False  # Only for code review and not for print
printPyRGBOnScreen = True
printPlotOnScreen = True

# Header
printlog('## Color ramp style generator - Reference style # ' + str(styleNumber))
printlog('![' + str(fileName) + '.png](' + urlGitHub + '/Output/' + str(fileName) + '.png)', True)
printlog('* Execution date & time: ' + str(datetime.now()) +
         '\n* Script compatibility: Python 3'
         '\n* Python version: ' + str(sys.version) +
         '\n* Python path: ' + str(sys.path[0:5]) +
         '\n* matplotlib version: ' + str(matplotlib.__version__) +
         '\n* Repository: https://github.com/rcfdtools/R.GISPython/tree/main/ColorMapStyle'
         '\n* License and conditions: https://github.com/rcfdtools/R.GISPython/wiki/License'
         '\n* Credits: r.cfdtools@gmail.com\n')

# Parameters
printlog('### General parameters')
printlog('\n* Reference style #: ' + str(styleNumber) +
         '\n* Colors: ' + str(numColor) +
         '\n* Cuts: ' + str(cutRamp) +
         '\n* Module operator: ' + str(numColor % cutRamp) +
         '\n* Colors per cut: ' + str(discreteCutValue) +
         '\n* Output file: ' + str(fileNameOutput) +
         '\n* GitHub: ' + urlGitHub + '/Output/' + str(fileName) + '.clr' +
         '\n* GitHub sample: ' + urlGitHub + '/Output/' + str(fileName) + '.png\n')

printlog('### Reference RGB with ' + str(len(baseRGBColors)) + ' color values\n')
printlog('| #    | R   | G   | B   |')
tableseparatormarkdown(4)
iAux = 0
for i in baseRGBColors:
    printlog('| ' + str(iAux) + ' | ' + str(i[0]) + ' | ' + str(i[1]) + ' | ' + str(i[2]) + ' |')
    iAux += 1
printlog('\n')

# Calculation
printlog('### Generated RGB color values table\n')
i = 0
iAux = 0
printlog('| #    | R    | G   | B   | Cut |', False)
print('| #    | R    | G   | B   | Sample')
tableseparatormarkdown(5)
while i < cutRamp:
    redColorFrom = baseRGBColors[i][0]
    redColorTo = baseRGBColors[i+1][0]
    redColorJump = abs((redColorFrom-redColorTo)/discreteCutValue)
    redColorRampValue = redColorFrom
    greenColorFrom = baseRGBColors[i][1]
    greenColorTo = baseRGBColors[i+1][1]
    greenColorJump = abs((greenColorFrom-greenColorTo)/discreteCutValue)
    greenColorRampValue = greenColorFrom
    blueColorFrom = baseRGBColors[i][2]
    blueColorTo = baseRGBColors[i+1][2]
    blueColorJump = abs((blueColorFrom-blueColorTo)/discreteCutValue)
    blueColorRampValue = blueColorFrom
    if printCutOnScreen: # Only for code review and not for print
        print('Red color from ' + str(redColorFrom) + ' To ' + str(redColorTo) + ' with ' + str(redColorJump) + ' variation')
        print('Green color from ' + str(greenColorFrom) + ' To ' + str(greenColorTo) + ' with ' + str(greenColorJump) + ' variation')
        print('Blue color from ' + str(blueColorFrom) + ' To ' + str(blueColorTo) + ' with ' + str(blueColorJump) + ' variation')
    for j in range(1, discreteCutValue+1):
        if iAux < numColor:
            if iAux == numColor-1:
                printTxt = '| ' + str(iAux).zfill(4) + ' |  ' + str(int(redColorTo)).zfill(3) + ' | ' + str(int(greenColorTo)).zfill(3) + ' | ' + str(int(blueColorTo)).zfill(3) + ' |'
                printTxtMd = str(iAux) + ' ' + str(int(redColorTo)) + ' ' + str(int(greenColorTo)) + ' ' + str(int(blueColorTo))
            else:
                printTxt = '| ' + str(iAux).zfill(4) + ' |  ' + str(int(redColorRampValue)).zfill(3) + ' | ' + str(int(greenColorRampValue)).zfill(3) + ' | ' + str(int(blueColorRampValue)).zfill(3) + ' |'
                printTxtMd = str(iAux) + ' ' + str(int(redColorRampValue)) + ' ' + str(int(greenColorRampValue)) + ' ' + str(int(blueColorRampValue))
            printSample = ' ■■■■■■■■■■■'
            print(colorrgb(0,0,0, printTxt) + colorrgb(int(redColorRampValue), int(greenColorRampValue), int(blueColorRampValue), printSample))
            printlog(printTxt, False)
            fileColorName.write(printTxtMd + '\n')
            if redColorFrom < redColorTo:
                redColorRampValue += redColorJump
                if redColorRampValue > redColorTo:
                    redColorRampValue = redColorTo
            else:
                redColorRampValue -= redColorJump
                if redColorRampValue > redColorFrom:
                    redColorRampValue = redColorFrom
            if greenColorFrom < greenColorTo:
                greenColorRampValue += greenColorJump
                if greenColorRampValue > greenColorTo:
                    greenColorRampValue = greenColorTo
            else:
                greenColorRampValue -= greenColorJump
                if greenColorRampValue > greenColorFrom:
                    greenColorRampValue = greenColorFrom
            if blueColorFrom < blueColorTo:
                blueColorRampValue += blueColorJump
                if blueColorRampValue > blueColorTo:
                    blueColorRampValue = blueColorTo
            else:
                blueColorRampValue -= blueColorJump
                if blueColorRampValue > blueColorFrom:
                    blueColorRampValue = blueColorFrom
            pyRBG.append((abs(redColorRampValue / 255.00000001), abs(greenColorRampValue / 255.00000001),
                          abs(blueColorRampValue / 255.00000001)))
            iAux += 1
    if moduleEval >= 1 and iAux < numColor:
        if iAux == numColor - 1:
            printTxt = '| ' + str(iAux).zfill(4) + ' |  ' + str(int(redColorTo)).zfill(3) + ' | ' + str(int(greenColorTo)).zfill(3) + ' | ' + str(
                int(blueColorTo)).zfill(3) + ' |'
            printTxtMd = str(iAux) + ' ' + str(int(redColorTo)) + ' ' + str(int(greenColorTo)) + ' ' + str(
                int(blueColorTo))
        else:
            printTxt = '| ' + str(iAux).zfill(4) + ' |  ' + str(int(redColorRampValue)).zfill(3) + ' | ' + str(int(greenColorRampValue)).zfill(3) + ' | ' + str(int(blueColorRampValue)).zfill(3) + ' |'
            printTxtMd = str(iAux) + ' ' + str(int(redColorRampValue)) + ' ' + str(int(greenColorRampValue)) + ' ' + str(int(blueColorRampValue))
        printSample = ' ■■■■■■■■■■■'
        print(colorrgb(0,0,0, printTxt) + colorrgb(int(redColorRampValue), int(greenColorRampValue), int(blueColorRampValue), printSample) + str(i+1) + ' cut')
        printlog(printTxt + str(i+1) + ' cut |', False)
        fileColorName.write(printTxtMd + '\n')
        pyRBG.append((abs(redColorRampValue / 255.00000001), abs(greenColorRampValue / 255.00000001),
                      abs(blueColorRampValue / 255.00000001)))
        iAux += 1
    i += 1
fileColorName.close()
print('\n')

# Matplotlib sample
printlog(colorrgb(0,0,0,'### Matplotlib color style sample'))
if printPyRGBOnScreen:
    printlog(colorrgb(0,0,0,'\nPython value conversion'))
    printlog(colorrgb(0,0,0,'| #    | pyR   | pyG   | pyB   |'))
    tableseparatormarkdown(n=4)
    iAux = 0
    for i in pyRBG:
        # printlog('| ' + str(iAux) + ' | ' + str(round(i[0],3)) + ' | ' + str(round(i[1],3)) + ' | ' + str(round(i[2],3)) + ' |')  # Python 2 y 3
        printlog(colorrgb(0,0,0, '| ' + str(iAux) + ' | ' + (f'{round(i[0], 3):.3f}') + ' | ' + str(f'{round(i[1], 3):.3f}') + ' | ' + str(f'{round(i[2], 3):.3f}') + ' |'))  # Python 3
        iAux += 1
for i in range(1,numColor+1):
    xVal.append(-i)
    yVal.append(1)
matplotlib.rcParams.update({'font.size': 8})
plt.figure(figsize=(5, 6), dpi=rgbSampleResolution)
plt.box(False)
plt.xticks([])
plt.title(fileName+'.clr' + '\n' + urlGitHub)
plt.tight_layout(pad=1.5)
plt.yticks([0, -numColor/4, -numColor/2, -numColor*3/4, -numColor])
plt.barh(xVal, yVal, color=pyRBG, height=1, align='center')
plt.savefig(filePath+'/Output/'+fileName+'.png')
if printPlotOnScreen: plt.show()
fileLog.close()
