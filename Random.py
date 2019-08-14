#randint: generate random integer numbers
#uniform: generate random float numbers
import os
from random import randint, uniform, random

def Z():
    a = randint(0,100)
    return a

def R():
    b = uniform(0,100)
    return b

os.system("cls")
print("The Z number generate is: ", Z())
print("The R number generate is: ", R())