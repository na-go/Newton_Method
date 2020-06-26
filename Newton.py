# coding: utf-8
import numpy as np

Nmax = 100
epsilon = 10**-10

def f(x):
    return x**3 - 4*x**2 + 13*x/4 - 3/4

def f_def(x):
    return 3*x**2 - 8*x + 13/4

def Newton_Method(x_0,x_t,N = Nmax,epsilon = epsilon):
    absolute_error = []
    i=0
    while(i != Nmax):
        absolute_error.append(abs(x_0 - x_t))
        x_0 = x_0 - f(x_0)/f_def(x_0)
        if abs(f(x_0)) < epsilon:
            break
        i+= 1
    # 絶対誤差
    print(abs(x_0 - x_t))
    # 近似解と反復回数
    print(x_0,i) 
    # 残差
    print(abs(f(x_0)))
    return absolute_error
    



error_list_1 = Newton_Method(6.0,3.0, Nmax, epsilon)
print(error_list_1)
error_list_2 = Newton_Method(-6.0, 3.0, Nmax, epsilon)
print(error_list_2)