from calendar import week


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
print("\tmultiples of Two.")

for i in range(1, 11):
     print("2 Times {}  is {}".format( i, 2* i))
