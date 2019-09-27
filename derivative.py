import math
from math import e

a=float(input("Enter the 'a' value:"))
x=0.1


def f(x):
    if x>=1:
        return 1-(e**-(a*x))
    else:
        return (e**(a*x))-1
    
def exactValue(x):
    if x>=1:
        return a*((e)**(-a*x))    
    else:
        return a*(e**(a*x))

    

def central(function, value,h):    
    
    top = function(value+h ) - function(value - h)
    bottom =2*h
    slope = top / bottom 
    print("\t   Central Divided Difference")
    print()
    print("Approximate value with CDD is ",slope)

    True_error=abs(slope-exactValue(x))
    print("True error with CDD is","%.9f" % True_error)
    Rte=True_error/exactValue(x)*100
    print("Relative true error with CDD is :",Rte)

    c=1
    while Rte>0.005:
       
        h=h/2
        top = function(value+h)-function(value)
        bottom = h
        slope = top / bottom
        True_error=abs(slope-exactValue(x))
        c+=1
        Rte=True_error/exactValue(x)*100


   
    print("Iterarion time for CDD is",c)
    print("Relative true error with CDD after minimized :",Rte)


    
def backward(function, value,h):
    
    top = function(value)-function(value-h)
    bottom = h
    slope = top / bottom
    print("\t   Backward Divided Difference")
    print()
    print("Approximate value with BDD is ",slope)

    True_error=abs(slope-exactValue(x))
    print("True error with BDD is","%.9f" % True_error)

    Rte=True_error/exactValue(x)*100
    print("Relative true error with BDD is :",Rte)

    b=1
    while Rte>0.005:
       
        h=h/2
        top = function(value+h)-function(value)
        bottom = h
        slope = top / bottom
        True_error=abs(slope-exactValue(x))
        b+=1
        Rte=True_error/exactValue(x)*100


   
    print("Iterarion time for BDD is",b)
    print("Relative true error with BDD after minimized :",Rte)
   

def forward(function, value,h):
   
        
    top = function(value+h)-function(value)
    bottom = h
    slope = top / bottom 
    print("\t   Forward Divided Difference")
    print()
    print("Approximate value with FDD is ",slope)

    True_error=abs(slope-exactValue(x))
    print("True error with FDD is","%.9f" % True_error)

    Rte=True_error/exactValue(x)*100
    print("Relative true error with FDD is :",Rte)
    f=1
    while Rte>0.005:
       
        h=h/2
        top = function(value+h)-function(value)
        bottom = h
        slope = top / bottom
        True_error=abs(slope-exactValue(x))
        f+=1
        Rte=True_error/exactValue(x)*100
        
    print("Iterarion time for FDD is",f)
    print("Relative true error with FDD after minimized :",Rte)

def main():

    h=0.05
    print("----------------------------------------------------")
    print("True value is ",exactValue(x))
    print("----------------------------------------------------")
    central(f,x,h)
    print("----------------------------------------------------")
    backward(f,x,h)
    
    print("----------------------------------------------------")
    forward(f,x,h)



main()
