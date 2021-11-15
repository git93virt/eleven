import numpy as nu
from numpy.core.fromnumeric import shape, size
# import pygame as py

# a=py

a = nu.array([7, 3, 5], nu.int32)
a.size

print(a)
print(size(a))
print(type(a))

b = nu.array([5, 9, 6])
print(b)
print(a*b)
b.shape
print(b)

print(a)
