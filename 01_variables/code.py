#x= 15
from ctypes import pythonapi

price = 9.99

discount = 0.2

result = price * (1 - discount)

print(result)


#string in python
name = 'Rolf'
print(name)
#print(name + name)

# changing variable values
a = 25
b = a
print(b)
print(b)

b = 15

print(a)
print(b)