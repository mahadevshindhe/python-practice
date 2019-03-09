# 1. python syntax

#Print "Hello World"
print ("Hello world")
#comments
#docstrings
"""This is a 
multiline docstring."""

# 2. Python Variables
#create a variable
x  = 5
y = "Jhon"
print(x)
print(y)
#Output both text and a variable
x = "awsome"
print("Python is "+x)
#Add a variable to another variable
x = "Python is "
y = "awsome"
z = x + y
print(z)

# 3. Python Numbers
# verify the type of an object
x = 1
y = 2.8
z = 1j
print(type(x))
print(type(y))
print(type(z))
# create integers
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))
# create floating point numbers
x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))
# create scientific numbers with an "e" io indicator the power of 10
x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))
# create complex numbers
x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))

#4. Python Casting
#casting - Integers
x = int(1)
y = int(2.8)
z = int("3")
print(x)
print(y)
print(z)

#casting - Floats
x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x)
print(y)
print(z)
print(w)

#casting - Strings
x = str("s1")
y = str(2)
z = str(3.0)
print(x)
print(y)
print(z)

#5. Python Strings
#Get the character at position 1 of a string
a = "Hello, World!"
print(a[1])
#substring, Get the character from position 2 to position 5 (not included)
b = "Hello, World!"
print(b[2:5])

# Remove whitespace from the beginning or at the end of a string
a = "Hello, World! "
print(a.strip())

#Return the length of a string
a = "Hello, World!"
print(len(a))

#convert a string to lower case
a = "Hello, World!"
print(a.lower())
#convert a string to upper case
a = "Hello, World!"
print(a.upper())

#Replace a stirng with another string
a = "Hello, World!"
print(a.replace("H", "J"))
#split a string into substrings
a = "Hello, World!"
b = a.split(",")
print(b)

#6. Python operators
#Addition
x = 5
y = 3

print(x + y)

#substraction
x = 5
y = 3

print(x - y)

#Multiplication

x = 5
y = 3

print(x * y)

#Division operators

x = 12
y = 3

print(x / y)

#Modulus
x = 5
y = 2

print(x % y)

#Assignment
x = 5

print(x)


