#!/usr/bin/env python3
# -*- coding: utf-8 -*-



"""
Created on Sun Nov 27 09:04:33 2016

@author: papapep
"""
#%%
from __future__ import print_function
def average(llista):
    accu=0
    compta =0
    for num in llista:
        accu = accu + num
        compta += 1
        print(num)
    mitjana = float(accu/compta)
    print("average is",mitjana,"its count is",compta)

#%%
from __future__ import print_function
def average1(numlis):
    sum_ = 0
    for ite in numlis:
        sum_ = sum_ + ite
        print(ite, end=" ")
    average = sum_/len(numlis)
    print("average is",average,"its count is",len(numlis))

#%%

def print_list(lis):
    for item in lis:
        print(item)

#%%

