#!/usr/bin/python

#Creating of string variables
a='Hello'
b="Python"

#Accessing of variabbles in python
print("Accessig of Variable i.e a : ",a)
print("Accessig of Variable i.e b : ",b)

print("Left to right index:",a[1])
print("")
print("Right to left index :",a[-4])

print(a[1:5])
print(a[0:4])
print(a[0:])

print("My name is %s and I born in %d" % ('Python',1981))
var1='Python'
var2=1981
print("My name is %s and I born in %d" % (var1,var2))

print("My name is {} and I born in {}".format('Guido',1981))
print("My name is {} and I born in {}".format(var1,var2))
print("My name is {var3} and I born in {var4}".format(var3='python',var4=1981))
print("My name is {} and I born in {}".format(var1,var2))
print("My name is {0} and I born in {1}".format(var1,var2))
print("My name is {1} and I born in {0}".format(var1,var2))

firstname='Guido'
lastname='Rossum'

Fullname=firstname + lastname
print(Fullname)
Fullname1=firstname + "&" + lastname
FullName2= firstname[0] + " & " + lastname[0]
print(Fullname1)
print(FullName2)
print(firstname*5)

str1="Hello World!"
str2='This is an example string'
alphabets='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num='0123456789'
print(str1[0])
print(str1[-1])
print(str1[2:6])
print(str1[:5])
print(str1[5:])
print (str1*3)

print(alphabets[0::6])
print(num[0::3])

print("updating string ",str1[:6] + "planet")
