# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 16:22:27 2018

@author: Chris
"""
import DemoBreakdown as demobd

filename = 'nations.txt' #The name of the cities and demographics file
f = open(filename,'r')  #Open the cities file
big = f.read().splitlines() #create a macro-list of all of the rows from the demo file
f.close()   #Close the fstream
groupCol = 1 #The index of the column for the city you're looking to break down.

gib = demobd.breakDownBigList(big)
#pprint.pprint(gib)
nvw = demobd.extractCity(gib,groupCol)
demobd.buildDemoFile('NvwDemos3.txt',nvw,gib)