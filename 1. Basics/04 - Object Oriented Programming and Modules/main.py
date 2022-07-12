'''Method 1'''
# import calculator
# print(type(calculator))

# print(calculator.CONSTANT)
# print(calculator.add(1,2))
# print(calculator.sub(1,2))
# print(calculator.mul(1,2))
# print(calculator.div(1,2))
# a = calculator.A()
# print(type(a))

'''Method 2'''
# from calculator import add,sub
# print(add(1,2))

'''Method 3'''
# from calculator import * # not recommended
# print(add(1,2))
# print(sub(1,2))
# print(globals())

'''Method 4'''
# from ast import Add
# from calculator import (
#     add,
#     sub,
#     mul,
#     div
# )

# print(add(1,2))
# print(div(1,2))

'''Aliases'''
'''Method 1'''
# import calculator as lib
# def calculator (a,b):
#     print(a,b)

# print(lib.add(3,4))

'''Method2'''
# from calculator import (
#     add as addition,
#     sub as difference
# )

# print(addition(1,2))


'''IMPORTING PACKAGE'''
# when we directly import math , the info inside __init__ file is imported
# import maths
# print(maths.a) #=> 1

from maths import (
    simple,
    complex
)

# from math import *

print(simple.add(1,2))
print(complex.cube(4))