import os

# Count the number of lines in the document
counter = 0
thefile = open("dom.js", "r")
for lines in thefile:
	counter += 1
print(counter)
# print(file.read())

# Count total number of characters
space = 0
line = 0
charc = 0
thefile = open("dom.js", "r")	
text = thefile.read()			 
		
for i in text:					# reading text character by character
	if(i == " "):
		space += 1
	elif(i == "\n"):
		line += 1
	else:
		charc += 1
 
print (f" Spaces = {space} \n Lines = {line} \n Characters = {charc}")

# Count number of else statements
thefile = open("dom.js", "r")	
word="else"
count = 0
 
for lines in thefile:
	if word in lines.split():
		count += 1
print(word, count)

# List of all files in a directory
print('MY FANCY LIST OF FILES')
path = 'C:\\Users\\evala\\Documents\\EvolveU\\Javascript'
# path2 = 'C:\\Users\\evala\\Documents\\EvolveU\\objects'

# Print every file with its size recursing through dirs

def recurse_dir(directory):
	x = os.path.abspath(directory)
	counterx = 0
	size = 0
	for item in os.listdir(directory):
		item_full_path = os.path.join(directory, item)
		if os.path.isdir(item_full_path):
			counterx += recurse_dir(item_full_path)
		else:
			print(item_full_path,os.stat(item_full_path).st_size, "Bytes" )
			counterx += 1
	return(counterx)

m =recurse_dir(path)

def recurse_dir2(directory):
	x = os.path.abspath(directory)
	size = 0
	for item in os.listdir(directory):
		item_full_path = os.path.join(directory, item)
		if os.path.isdir(item_full_path):
			size +=recurse_dir2(item_full_path)
		else:
			size +=os.stat(item_full_path).st_size
	return(size)

n =recurse_dir2(path)

print(f"There are {m} files in this directory. Total size is {n} bytes.")