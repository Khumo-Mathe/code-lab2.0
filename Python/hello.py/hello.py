from calendar import week
from math import pi



print('hello, world!')
print(32)
print()
print(1+1)

name = "brian"
print('hello\nmy\nname\nis\nkamogelo')
print('1\t2\t3\t4\t5')
print('c:\\users\\timbukcha\\notes.exe') 

print(type(11))
print(type(name))
print(name[0:4]) #slincing strigs


 #numeric values 

a = 12
b = 3

print(a+b)
print(a-b)
print(a%b)
print(a*b)
print(a/b)  

#backward slicing

letters = "khumo"
backwards = letters[4::-1]
print(backwards)

#sequence operators

print("my " "name " "is " "khumo ")
print("ha "* 7)

age= 25
print("you are {0} years old ".format(age))  #string replacement
print("in a {0} you work in {1}, {2}, {3}, {4}, {5}"
      .format("week", "monday", "tuesday", "wednesday","thursday", "friday"))
 

#advanced string formatting
print("_" *40)
print("\tmultiples of Two.")
print("_" *40)

for i in range(1, 11):
     print("2 Times {:2}  is {:4}".format( i, 2* i)) #aligning values {:x}


#string interpolation
age=25
print("you are %d years old" %age)




#program tha calculates the area of a circle based om the entered radius

radius = float(input("enter radius: "))
area = pi * radius**2 # type: ignore

print("r:" + str(radius) + "\narea : " + str(area))

#input fileds and control flow

name= input("what is your name? ")
age= int (input("hi {0}, how old are you? " .format(name)))
print( "you are {}" .format(age))