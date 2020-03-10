# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 21:36:32 2020

@author: ASUS
"""

def fact(n):
    if(n==0):
        return 1
    else:
        return (fact(n-1)*n)
a=int (input("enter a number"))
print(fact(a))