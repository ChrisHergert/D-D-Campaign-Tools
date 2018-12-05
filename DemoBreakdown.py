# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 13:57:46 2018

@author: Chris
"""

import random
import pprint
import math
#-----------------------------------------------------------------------------
def breakOutIntoPercentages(n):
    '''Generates a vector of length n, of decimal-form percentages with 4 digits'''
    percs = [0] * n
    for i in range(n):
        percs[i] = random.random()
    sumn = sum(percs)
    for i in range(n):
        percs[i] = round(percs[i]/sumn, 4)
    return percs
#-----------------------------------------------------------------------------
def split(n,tot):
    '''Given a number n, break it out into p randomly-sized subsets'''
    sub = breakOutIntoPercentages(n)
    for i in range(n-1):
        sub[i] = int(round(sub[i] * tot, 0))
    sub[n-1] = int(tot-round(sum(sub),0))
    return sub
#-----------------------------------------------------------------------------
def breakDownBigList(bigList):
    '''After importing the big list from the txt file as a list of strings, this is to break it out into integer population values.'''
    rows = len(bigList)
    for i in range(rows):
        bigList[i] = bigList[i].split(',')
    cols = len(bigList[1])
    for i in range(rows-1):
        for j in range(cols-1):
            bigList[i+1][j+1] = int(bigList[i+1][j+1])
    return bigList
#-----------------------------------------------------------------------------
def extractCity(bigList, groupCol):
    '''After using breakDownBigList(), this function extracts the city in column index groupCol'''
    city = []
    rows = len(bigList)
    for i in range(rows-1):
        city.append(bigList[i+1][groupCol])
    return city
#-----------------------------------------------------------------------------
def sexSplit(cityCol):
    '''Given a cityCol vector from extractCity(), this breaks that down into M/F'''
    n = len(cityCol)
    l = [[0,0] for i in range(n)]
    for i in range(n):
        l[i][0] = int(round(random.random() * cityCol[i], 0))
        l[i][1] = cityCol[i]-l[i][0]
    return l
#-----------------------------------------------------------------------------
def educationRates(cityCol):
    '''generates a list of length-2 lists for however many races are in the given cityCol, corresponding to the M and F education rates.'''
    n = len(cityCol)
    l = [[0,0] for i in range(n)]
    for i in range(n):
        for j in range(2):
            #l[i][j] = str(round(math.sqrt(random.random() * 100) * 5, 4) * 100) + '%'
            #l[i][j] = str(round(math.sqrt(random.random()*100)*1.5, 1)) + '%'
            l[i][j] = str(round(10 + (random.random() ** 2)*40,1)) + '%'
    return l
#-----------------------------------------------------------------------------
def edAndSexCombined(cityCol):
    '''makes a sexSplit matrix, then an educationRates matrix to match that, then returns a matrix of form [ss,ed]'''
    ss = sexSplit(cityCol)
    ed = educationRates(cityCol)
    n = len(ss)
    combined = [[0 for i in range(4)] for j in range(n)]
    for i in range(n):
        combined[i][0] = ss[i][0]
        combined[i][1] = ss[i][1]
        combined[i][2] = ed[i][0]
        combined[i][3] = ed[i][1]
    return combined
#-----------------------------------------------------------------------------
def generateRate(cityCol):
    '''Generates any needed populations for a given cityCol of populations'''
    n = len(cityCol)
    p = [0 for i in range(n)]
    for i in range(n):
        p[i] = int(round(math.sqrt(cityCol[i] * random.random()) * 7, 0))
    return p
#-----------------------------------------------------------------------------
def buildDemoFile(filename, cityCol, allCols):
    '''Creates a matrix of race names, populations M/F, then education rates M/F, then exports it all to a text file.'''
    rows = edAndSexCombined(cityCol)
    f = open(filename,'w+')
    n = len(rows)
    f.write(allCols[0][0] + ', Pop, M Pop, F Pop, M ed rate, F ed rate \n')
    for i in range(n):
        f.write(str(allCols[i+1][0]) + ',' + str(cityCol[i]) + ',')
        for j in range(4):
            f.write(str(rows[i][j]) + ',')
        f.write('\n')
    f.close()
        
#-----------------------------------------------------------------------------

