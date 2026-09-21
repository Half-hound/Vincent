# File: homework1.py
# --- Variables and Data Types ---
a = 10
print(a)
print(type(a)) # a is an integer, a whole number with no decimals
b = 10
print(b)
print(type(b)) # b is an float, a number with decimals
c = 3j
print(c)
print(type(c)) # c is a complex number, a number with an imaginary part
d = "hello"
print(d)
print(type(d)) # a is a string, a sequence of characters
e = [1, 2, 3]
print(e)
print(type(e)) # e is a list, a group of variables
f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dictionary, a group of variables where each is assigned a corresponding key
g = (1, 2)
print(g)
print(type(g)) # g is a tuple, a group of variables in which each position is fixed
h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a list, a group of variables
i = True
print(i)
print(type(i)) # i is a boolean, a true or false statement
j = None
print(j)
print(type(j)) # j is a nonetype, a type of variable that represents the absence of a value
k = [True, "blue", 12]
print(k)
print(type(k)) # k is a list, a group of variables
l = str(14)
print(l)
print(type(l)) # l is a string, a sequence of characters
m = 1e4
print(m)
print(type(m)) # m is a float, a number containing decimals
# nine kinds
# String, Boolean, List, Tuple, Float, Nonetype, Dictionary, Integer, Complex Number,
# b and m, a and l, e and h and k
# it's a string; its not an integer because the Str() command converts it into a string
# A set. A set cannot contain duplicates, unlike a list

print(10 > 9) # True
print(10 == 9) #False
print(10 <= 9) #False
print(bool("abc")) # True
print(bool(123)) # True
print(bool(["apple", "cherry", "banana"])) # True
print(bool(True)) # True
print(bool(False)) #False
print(bool(0)) #False
print(bool("")) #False
print(bool(" ")) # True
print(bool(())) #False
print(bool([])) #False
print(bool({})) #False
print(bool(True and False)) #False
print(bool(True and True)) # True
print(bool(False and False)) #False
print(bool(True or False)) # True
print(bool(True or True)) # True
print(bool(False or False)) #False
print(bool(not(False))) # True
print(bool(not(True))) #False

# when a data type is blank, it returns false, and when it contains information, returns true
# the "" returning false and the " " returning true; on the surface, they seem the same
# 1==1, returns true because one is indeed one
# 2>3, returns false because 2 is not larger than 3

print(10 + 5) # 15, performs addition
print(10 - 5) # 5, performs subtraction
print(2 * 4) # 8, performs multiplication
print(6 / 3) # 2.0, performs division
print(5 % 2) # 1, shows the remanent 
print(3 ** 2) # 9, performs to the power of
print(15 // 2) # 7, shows the answer with remainder
print(5 == 2) # False
print(10 != 10) # False
print(2 < 5) # True
print(12 > 5) # True
print(5 <= 6) # True
print(1 >= 10) # False
x=5
print(x + 5) # 10
print(x - 4) # 1
print(x * 3) #15

# it checks if both are true and if so returns true; otherwise flase. e.g. bool(4==4 and 5==5) returns true, bool(4==3 and 5==5) returns false
# it checks if either of them are true; if true, returns true, otherwise false. e.g. bool(4==4 and 5==4) returns true, bool(4==3 and 5==4) returns false
# it gives the opposite of the value detected. e.g. bool(not(True)) returns false, bool(not(False)) returns true
# / gives the number divided to the end, with decimals etc, whereas // gives an integer 
# % gives the remainder of the things divided while // gives the result of the division as an integer
# use %
# assigns the variable on the left hand to a value on the right side
my_string = "hello"
print(my_string) # Prints: hello
print(my_string[0]) # Prints: h
print(my_string[1]) # Prints: e
print(my_string[2]) # Prints: l
print(my_string[3]) # Prints: l
print(my_string[4]) # Prints: o
print(my_string[-1]) # Prints: o
print(my_string[1:3]) # Prints: el
print(my_string[0:5:2]) # Prints: hlo
print(len(my_string)) # Prints: 5
print(my_string + "goodbye") # Prints: hellogoodbye
print(my_string * 7) # Prints: hellohellohellohellohellohellohello
# Slicing is picking out characters from a string; it was used for all of the commands save for the last three
name = "Oski"
print("Hello, my name is", name) # Hello, my name is Oski
name = "Oski"
print(f"Hello, my name is {name}") # Hello, my name is Oski
# There is no difference between the two outputs. The f-string is an easier way to insert variables into a string

# cd
# Changes directories. Use it to move from one folder to another
# Example: cd Desktop
# ls
# Lists everything under the directory
# Example: ls
# ls -a
# lists everything under the directory, including hidden files
# Example: ls -a
# mkdir
# Makes a new directory under the current one
# Example: mkdir pineapple
# cat
# Create and manipulate text files
# Example: cat > applebees.txt
# pwd
# Prints the whole pathway of where you are in
# Example: pwd  
# cd ..
# Moves into the parent file of where you are
# Example: cd ..
# cd .
# Keeps you in the directory you are in
# Example: cd .
# cd ∼
# Brings you into your home directory
# Example: cd ~
# cp
# Copies a file
# Example: cp dog.txt cat.txt
# mv
# Moves a file from one directory into another
# Example: mv cat.txt /felines/
# rm (be careful with this one)
# Deletes a file
# Example: rm cat.txt
# clear
# Clears the terminal window of all previous commands
# Example: clear
# grep
# searches for lines within a file
# Example: grep "dog" canid.txt
#1) !! reruns the last command, e.g. !! 2)df -h checks disk space, e.g. df -h 3) !$ reuses the last argument, e.g. !$
# the latter shows hidden files
# files whose filename starts with a . and are thus hidden from user view
# -l shows detailed info, -f forces a command, -h displays a help manual