"""
a = 10
print("Type of a: ", type(a))

b = 10.5
print("Type of b: ", type(b))

c = 2 + 3j
print("Type of c:", type(c))

string1 = "Hello"
string2 = 'World'
string3 = '''
Where's
Mars
'''

print(string1 + string2 + string3)
print(type(string1))
print(type(string3))

print("First character", string1[0])

#Create a list by declaring
list = ['Geeks', 'For', 'Geeks']
print(list)
print("The First element:", list[0])
print("The Last element:", list[-1])

"""
"""
Tuple1 = ()
print(type(Tuple1))
Tuple1 = (1, "Greek", 2)
print(Tuple1)
print(Tuple1[0])

Tuple2 = tuple("First")
print(Tuple2)
print(Tuple2[-1])

Tuple3 = (Tuple1, Tuple2)
print(Tuple3)

"""
"""
"""
"""
Set1 = set("Initial blank set")
print(Set1)
print(type(Set1))
Set2 = set([1, "Set", True])
print(Set2)
print(type(Set2))

for i in Set1:
  print(i)
  """
"""
Dictionary1 = {1: "Geeks", 2: "For", 3: "Geeks"}
Dictionary2 = {"Name": "Allan", "Age": 20, "Gender": "Male", "Enrolled": True}
print(Dictionary2["Name"])
"""
"""
n = input("Enter a number: ")
print = (n)
"""

#Basic If Statement to check if a number is positive or negative
'''
num = 8
if (num >= 0):
  if num == 0:
    print("Zero")
elif num > 0:
  print(num, "is a positve number")
else:
  print(num, "is a negative number")
'''
"""
#Program for calculating sum in a list
sum = 0
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in list:
  sum += i  #instead of sum = sum + i
  print("The sum of the list is", sum)
"""
#Demo of Range function
#Range starts from 0 by default and increments by 1
#range does not store values,we have to call a list()
"""
print(range(10))
alist = (list(range(10)))
print(alist)
print("The fourth item in the list is", alist[3])

#Range can take 2 parameters
range(2, 8)
listb = (list(range(2, 8)))
print("The whole listb:", listb)

#Range can take 3 parameters
range(0, 10, 2)
listc = (list(range(0, 10, 2)))
print("The whole listc:", listc)
"""

#combining for and range
"""
sum = 0
for var in range(1,11):
  sum += var
  print("var = ",var, "and sun =", sum)
  
  print(sum)
"""
"""
music = ["rock", "pop", "jazz", "classical", "country"]

for i in range(len(music)):
  print("Index:", i, "I like", music[i])
"""
#while loop by adding natural numbers
"""
n = int(input("Enter how many natural numbers you want to add: "))
sum = 0  #initialize sum to 0
i = 1  #initialize i to 1

#while loop to add natural numbers
while i <= n:
  sum += i  #sum = sum + i
  print("The sum of the", i, "natural numbers is", sum)
  i += 1
"""

#A simple python program to demo the use of break statement
"""
for val in "string":
   print("in loop", val)
   if val == "i":
     break
     print("out of loop", val)
"""
#A simple python program to demo the use of continue statement
"""
for char in "string":
  print("in for loop", char)
  if char == "i":
    print("I found", char)
    continue  # The continue statement should be before the print statement
  print("The end!")
  """
#A simple python program to demo the use of pass statement
"""
sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for val in sequence:
  pass

print("The end!")
"""

#Functions
"""
def greet(name):
"""
# This function greets to the person passed in as a parameter
"""
  print("Hello, ", name)


greet("Allan")
print(greet.__doc__)  #How to print the docstring of a function
"""
'''
def ad(a, b):
  """
  A simple program for adding two numbers passed as two parameters returms the sum
  """
  return a + b


print(ad, __doc__)
print(ad(2, 3))
'''
