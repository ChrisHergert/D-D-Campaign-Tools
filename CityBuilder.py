# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 22:56:49 2018

@author: Chris
"""
import random
import pprint

def readIn(fileName):
    '''A Quick reader for the formatted municipality demographics format'''
    f = open(fileName, 'r')
    g = f.read().splitlines()
    f.close()
    return g
#-----------------------------------------------------------------------------
def readInSplit(fileName, c):
    '''The same as the readIn(), but each row is broken down into a list of its own'''
    f = open(fileName, 'r')
    g = f.read().splitlines()
    f.close()
    for i in range(len(g)):
        g[i] = g[i].split(c)
    return g
#-----------------------------------------------------------------------------
def WriteEthns():
    '''Takes user input to create a demographics list'''
    groups = []
    while True:
        print('Give the subrace name. (blank to exit)')
        sub = input()
        if sub == "":
            break
        else:
            if sub not in groups:
                groups.append(sub)
    return groups
#-----------------------------------------------------------------------------

def PopsBuilder(fileName, tot, town):
    '''Adds a column to the demographics file fileName, with the populations of the given town, of total population tot'''
    gs = readIn(fileName)
    ps = [town]
    for i in range(len(gs)):
        ps.append(random.random())
    sumn = sum(ps[1:])
    for i in range(len(ps)-1):
        ps[i+1] = int((ps[i+1]/sumn)*tot)
    if fileName != '':
        f = open(fileName, 'w+')
        for i in range(len(gs)):
            f.write(str(gs[i]) + ',' + str(ps[i]) + '\n')
        f.close()
#-----------------------------------------------------------------------------
def returnPercentages(n, tot):
    '''A stub for breaking down a total 'tot' into n subtotals'''
    p = [0] * n
    for i in range(len(p)):
        p[i] = random.random()
    sm = sum(p)
    for i in range(len(p)):
        p[i] = round(p[i]/sm, 4)
    for i in range(len(p)):
        p[i] = int(round(p[i] * tot, 0))
    return p
#-----------------------------------------------------------------------------
logFile = 'nations.txt'
#PopsBuilder(logFile, 8000, "Neverwinter")
#PopsBuilder(logFile, 1140, "Triboar")
#PopsBuilder(logFile, 730, "Helm's Hold")
#PopsBuilder(logFile, 840, "NVW Army")
#p = readInSplit(logFile, ',')
#pprint.pprint(p)

print(returnPercentages(2, 937))