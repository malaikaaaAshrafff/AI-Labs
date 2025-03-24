
c=0
while(c<3):
    c=c+1
    print("hyy")    
    
#single statement while block
c=0
while(c==0): print("infinite")


# 3. for in loop
# print list iteration
l=["geeks" , "for" ,"geeeks"]
for i in l:
    print(i)

 #Har word ko ek ek kar ke print karega.

# 4. iterating over a tupple (immuteable)
t=("geeks" , "for" , "geeks")
for i in t:
    print(i) 
   
# 5. iterating over a string
s="saiha"
for i in s: print (i)

#6 iterating by index (index based iteration)
list=["good" , "girl"]
for i in range(len(list)):
    print (list[i])

#7 Loop control statements continue ststements
for letter in 'malaika' :
    if letter=='a':
        continue
    print("current letter:" , letter)
#8 Break statement

for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        break
    print("Current Letter:", letter)

#9. simple function
def aiman_function():
    print("Aiman Ashraf")

aiman_function()

#10. function with parameters
def greet(name):
    print("Work Hard, " + name)

greet("Malaika")
greet("Aiman")

#11. Return a value
def square(num):
    return num * num

result = square(5)
print(result)  # Output: 25
 
#11. default parameter
def square(no=5):
    return no * no * no

print(square())  # Output: 125
print(square(3))  # Output: 27

#12. list as  a parameter
fruits_list = ["apple", "banana", "cherry"]
def print_fruits(fruits):
    for fruit in fruits:
        print(fruit)

print_fruits(fruits_list)

#13. OOP class and object
class MyClass:
    name = "malaika ashraf"

p1 = MyClass()
print(p1.name) 

#14. constructor
class Person:
    def __init__(self, name, age):  # Pehla parameter 'self' hona chahiye
        self.name = name  # Attributes ko initialize karte hain
        self.age = age

p1 = Person("Malaika", 21)
print(p1.name)  # Output: Ali
print(p1.age)   # Output: 25

#15.Object methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name)

p1 = Person("malaika", 22)
p1.greet()  





    
