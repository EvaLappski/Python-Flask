print("Hello World from Python")

# NUMBERS
# Integer - whole numbers like 1, 200, 9
a=10
a= a+a
print(a)
# Floating Point - decimal point such as 9.0 or 100.0
a=1.0
b=2.9
print(a)
print(b)

# VARIABLES
# RULES - cannot start with a number, no spaces, use _ instead, no special charachters
# BEST PRACTICES - PEP8 - all lower case and _, don't use words already built into Python
# Python uses DYNAMIC TYPING = meaning you can reassign variables to different data types
# unlike other languages which throw an error , called STATICALLY TYPED
my_dogs = 2
my_dogs = ["Rudy", "Oscar"]
puppies = 6
weight = 2
total = (puppies * weight)
print(total)

# STRINGS - in "" or '' or use both ex: "don't" - IMMUTABLE
# Ordered Sequences which you can index and slice to grab subsections of
a = 'Eva is awesome'
b = "So it Python"
c = "don't forget it"
print(a)
print(b)
print(c)
print(len(a)) 
# returns 14 as the length of the string including the spaces and characters
# INDEX
my_string = "Eva"
print(my_string[0])
print(my_string[-2])
print(my_string[2])
# SLICING
my_string = "abcdefghijklmnop"
# [start:stop;step] starting index: up to but not including index: size of jump
print(my_string[:3]) 
print(my_string[4:7])
print(my_string[0:7:2])
print(my_string[::-1])
# Concat
print(my_string+my_string)
print("Hello "+"World")
print(my_string.upper())
print(my_string.lower())
print(my_string.split('g'))
# Print formatting
username = "Eva"
color = "Pink"
print("The girl named {} likes the color {}".format(username, color))
# f string literals, only Python 3.6 or higher
print(f"The girl named {username} likes {color}")

# LISTS
# Ordered sequence which can hold a variety of object types
# supports slicing and indexing
# BE CAREFUL to use the word 'list' to name your list 
first_list = [1,2,3]
print(len(first_list))
second_list = [1, 2.9, 3, 9.1, 'Eva']
print(second_list[4])
print(second_list[1:4])
second_list.append("Lapp")
print(second_list[4:])
second_list.insert(5,"Marta")
print(second_list[4:])
popped_item = second_list.pop(0)
print(second_list)
print(popped_item)
# Nested Lists
mega_list = [first_list, second_list]
print(mega_list)
print(len(mega_list))
print(mega_list[0][1])

# DICTIONARIES
# Unordered mappings for storing objects, used a key:value pairing, does not need index
# Syntax uses {'key1':'value1', 'key2':'value2'}
# The objects are retrieved based on the value name
# Can not be ordered or sorted in anyway
d = {'key1':'value1', 'key2':'value2'}
print(d)
print(d['key1'])
salaries = {'Shane':100000, 'Eva':100500, 'Dima':200000}
print(salaries['Shane'])
# New Employee
salaries['Greg'] = 40000
# Eva gets a raise
salaries["Eva"] = salaries["Eva"] = 10500
# Link lists into dictionaries
people = {'Eva':[1,2,3], 'Shane':[7,8,9]}
print(people['Eva'])
print(people['Eva'][1])
people2 = {'Eva':{'Age':34, 'Salary': 0}, 'Shane':{'Age':30, 'Salary': 9}}
print(people2['Eva']['Age'])
# Some Usefule methods
d2 = {'k1':45, 'k2':77, 'k3':98}
print(d2)
print(d2.keys())
print(d2.values())
print(d2.items())

# TUPLES
# Similar to lists, but are IMMUTABLE, cannot reassign
# Syntax (1,2,3), can use index/slice, can have mixed data types
t = (1,2,3, 'Eva', 9.9)
print(t[1])

# SETS
# Unordered collection of Unique elements. uses {}, but no key:value pairs
x = set()
print(x)
x.add(1)
x.add(2)
x.add(3)
print(x)
# Can't add the same value again b/c it's not unique
# x.add(3) again won't do anything.
mylist = [1,2,4,5,6,3,44,2,1,1,2,3,4,66,8,5,6]
print(set(mylist))

# BOOLEANS
# returns true or false. Must be capital T True F False
a = True
print(a)
b = False
print(b)
c = None

# COMPARISON AND LOGICAL OPERATORS
print(1 > 2)
print(2 > 1)
print(3 <= 2)
print(3 >= 2)
print(3 == 3)
print(3 != 3)
print(1 == 1 and 2>3)
print(1 == 2 or 5>3)
username = "Admin"
check = "Admin"
permission = False
print(username == check and permission)

#CONTROL FLOW - execute code when a condition is met, uses indentation

if username == check and 1==1: 
	print('Access Granted')
elif permission == True:	
	print('You do not have permission')
else:
	print('Access Denied')

# LOOPS
# allows you to itterate over items in a list, characters in a string or key in a dictionary
# FOR LOOP - itterates through each item in the loop
seq = [1,2,3,4,5]
for item in seq:
	print(item*2)
seq2 = 'KOWALEWSKI'
for char in seq2:
	print(char)
salaries = 	{'Shane':100000, 'Eva':100500, 'Dima':200000}
for key in salaries:
	print(key)
	print(salaries[key])

mypairs = [(1, 'a'),(2, 'b'),(3, 'c')]
for pair in mypairs:
	print(pair)
for (num, letter) in mypairs:
	print(num)
	print(letter)
	# This is called 'Unpacking the tuples'

# WHILE LOOP
i = 1
while i < 5:
    print('i is: {}'.format(i))
    i = i+1
# OTHER HANDY THINGS
range(5)

list(range(5))

for i in range(5):
    print(i)

print('d' in 'fnlsahglajglsnjklsglkdldbndbdh' )

# FUNCTIONS
def my_func():
	print('Hello from my_func')

my_func() 

def my_name_func(name):
	print('Hello my name is ' + name)

my_name_func("Eva")	

def add(n1,n2):
    print(n1+n2)

add(2,3)

result = add(2,3)

print(result)
print(type(result))

# FUNCTIONS PART 2
print(max([1,2,4,8,999,]))
print(min(-1, -4, 8, 0, -700))


for letter in ['a', 'b', 'c']:
	print(letter)

my_list = ['a', 'b', 'c']
index = 0

for letter in my_list:
	print(letter + ' is at index:{}'.format(index))
	index = index +1
	# or you can use enumerate
for index,letter in enumerate(my_list):
	print(letter + ' is at index:{}'.format(index))

my_list = ['a', 'b', 'c', 'd']
print('--'.join(my_list))

# SECRET FUNCTION
def secret_checker(message):
	if 'secret' in message:
		print('This is top secret')
		return True
	else:
		print('This is not a secret')
		return False

secret_checker('Shhh this is a secret')
secret_checker('You can tell everyone if you want')

# Simpler version of the above
def secret_checker_better(message):
	return 'secret' in message.lower()


print(secret_checker_better('this is top SECRET'))

# CODE MAKER FUNCTION
def code_maker(mystring):
    output = list(mystring)
    for i,letter in enumerate(mystring):
        for vowel in 'aeiou':
            if letter.lower() == vowel:
                output[i] = 'x'

    output = ''.join(output)
    return output

print(code_maker('Edward'))
print(code_maker('John'))

# TESTING
def add(x,y):
	return x + y

def sub(x,y):
	return x - y

def multiply(x,y):
	return x * y

def divide(x,y):
	if y == 0:
		raise ValueError('Error, cannot divide by 0')
	return x / y

def email(fname,lname):
	return(f'{fname.lower()}.{lname.lower()}@evolveu.ca')

email('Eva', 'Lapp')

# TAX CALCULATOR
maxamount = [0, 7145, 9764,13626,18184];
taxrate = [0, 0.15, 0.205, 0.26, 0.29, 0.33]
maxbracket = [0,11809, 47630, 95259, 147667, 210371];

def tax_calc(income):
	if income <= maxbracket[1]: 	
	 	return  income * taxrate[0];
	elif income > maxbracket[1] and income <= maxbracket[2]:
		return  (income * taxrate[1])
	elif income > maxbracket[2] and income <= maxbracket[3]:
		return  ((income-maxbracket[2])*taxrate[2] + maxamount[1])
	elif income > maxbracket[3] and income <= maxbracket[4]:
		return  (((income-maxbracket[3])*taxrate[3] )+ maxamount[1] + maxamount[2])
	elif income > maxbracket[4] and income <= maxbracket[5]:
		return  (((income-maxbracket[4])*taxrate[4] )+ maxamount[1] + maxamount[2] + maxamount[3])
	else: 
		return  (((income-maxbracket[5])*taxrate[5] )+ maxamount[1] + maxamount[2] + maxamount[3]+maxamount[4]);
