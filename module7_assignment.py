# 1) What are the types of Applications?
# There are **five** main types of applications:  

# 1. **Web Applications** – Runs on browsers (e.g., Gmail, Facebook).  
# 2. **Mobile Applications** – Runs on smartphones (e.g., WhatsApp, Instagram).  
# 3. **Desktop Applications** – Installed on PCs (e.g., MS Word, Photoshop).  
# 4. **Enterprise Applications** – Used by businesses (e.g., ERP, CRM).  
# 5. **Embedded Applications** – Runs on hardware devices (e.g., ATMs, smart TVs). 


# 2) What is programing? 
# Programming involves using languages like Python, Java, or C++ to create software, websites, and applications. 
# It helps automate tasks, solve problems, and build technology-driven solutions.


# 3) What is Python? 
### **What is Python?**  

# Python is a high-level, interpreted, and easy-to-learn programming language** created by Guido van Rossum in 1991. 
# It is widely used for **web development, data science, AI, ML, and automation due to its simple syntax and vast libraries.


# 4) Write a Python program to check if a number is positive, negative or zero. 
# number = int(input("enter a number :"))
# if(number >0):
#     print("The number is positive")
# elif(number <0):
#     print("The number is negative")
# else:
#     print("The number is zero")
    
#5) Write a Python program to get the Factorial number of given numbers.

# n=5
# fact=1
# i=1
# while i<=n:
#     fact*=i
#     i+=1
# print("Total of FActorila",fact)


# n=5
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print("total of factorial",fact)
# 6)Write a Python program to get the Fibonacci series of given range.
# n=int(input("enter your number:"))
# a=0
# b=1
# print(a,b,end=" ")
# for i in range(n):
#     c=a+b
#     a=b
#     b=c
#     print(c,end=" ")

#7)How memory is managed in Python? 
# Python manages memory using private heap space, garbage collection, and memory
# pools (PyMalloc) for efficient allocation and deallocation. 

#8)What is the purpose continuing statement in python? 
# The continue statement in Python skips the current iteration
# of a loop and moves to the next iteration. 

#9) Write python program that swap two number with temp variable and without temp variable. 
# a=5
# b=10
# temp=a
# a=b
# b=temp
# print(a,b)

# a=5
# b=10
# a,b=b,a
# print(a,b)
 
#10) Write a Python program to find whether a given number is even
# or odd, print out an appropriate message to the user.
# n=int(input("enter number : "))
# if(n%2==0):
#     print(n,"is even")
# else:
#     print(n,"is odd")

#11) Write a Python program to test whether a passed letter is a vowel or not.
# c=input("enter your character :")
# vowels=0
# consonents=0
# for char in c:
#     if char in "AEIOUaeiou":
#         vowels+=1
#     elif char.isalpha():
#         consonents+=1
# print("total vowels:", vowels)
# print("total consonents :", consonents)

# char=input("enter a letter :")
# if char in "AEIOUaeiou":
#     print(char,"is vowel:")
# else:
#     print(char ,"is not vowel")

#12) Write a Python program to sum of three given integers. However, if two values are equal sum will be zero
# a=int(input("enter your first number :"))
# b=int(input("enter your second number :"))
# c=int(input ("enter your third number :"))
# sum=0
# if a==b or b==c or a==c:
#     print(sum)
# else:
#     sum=a+b+c
#     print(sum)

#13) Write a Python program that will return true if the two given 
# integer values are equal or their sum or difference is 5.
# a=int(input("enter your first number :"))
# b=int(input("enter your second number :"))
# sum=0
# if a==b or b==a:
#     print(sum)
# else:
#     sum=a+b
#14) Write a python program to sum of the first n positive integers.
# n=int(input("enter your number: "))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print("sum of first number",n,"sum of positive number",sum)    
# 15) Write a Python program to calculate the length of a string. 
# string=input("enter your string :")
# length=len(string)
# print("total of string",length)

# string="Hello World"
# count=0
# for  char in string:
#     count+=1
# print("count of string", count)

#16) Write a Python program to count the number of characters (character frequency) in a string 
# string = input("Enter a string: ")
# char_count = {}

# for char in string:
#     char_count[char] = char_count.get(char, 0) + 1  # Count each character

# print("Character Frequency:", char_count)

#17) What are negative indexes and why are they used?
# In Python, negative indexing allows you to access elements from the end of a sequence
# (like strings, lists, or tuples).

# In Python, indexing starts from 0 for the first element
# Negative indexing starts from -1 for the last element
# string="TOPS"
# print(string[-1])
# print(string[-2])

#  To access elements from the end without knowing the exact length
#  Useful in slicing operations

#18) Write a Python program to count occurrences of a substring in a string.
# string = input("Enter the main string: ")
# substring = input("Enter the substring to count: ")

# count = string.count(substring)  # Count occurrences
# print(f"Occurrences of '{substring}': {count}")

#19) Write a Python program to count the occurrences of each word in a given sentence
# sentence = input("Enter a sentence: ")
# words = sentence.split()

# for word in set(words): 
#     print(f"'{word}': {words.count(word)}")


#20) Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. 

# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")

# print(str2[:2] + str1[2:], str1[:2] + str2[2:])

# 21) Write a Python program to add 'in' at the end of a given string (length 
# should be at least 3). If the given string already ends with 'ing' then 
# add 'ly' instead if the string length of the given string is less than 3, 
# leave it unchanged. 

# word = input("Enter a string: ")

# if len(word) < 3:
#     print(word)
# elif word.endswith("ing"):
#     print(word + "ly")
# else:
#     print(word + "ing") 
 
# 22) Write a Python function to reverses a string if its length is a multiple 
# of 4. 
# word = input("Enter a string: ")
# check=(word[::-1] if len(word) % 4 == 0 else word)
# print(check)


# 23) Write a Python program to get a string made of the first 2 and the last 
# 2 chars from a given a string. If the string length is less than 2, return 
# instead of the empty string. 
# s = input("Enter a string: ")

# if len(s) < 2:
#     print("")
# else:
#     print(s[:2] + s[-2:])


# 24) Write a Python function to insert a string in the middle of a string. 
# main = input("Enter the main string: ")
# insert = input("Enter the string to insert: ")

# mid = len(main) // 2
# print(main[:mid] + insert + main[mid:])

# 25) What is List? How will you reverse a list? 

# In Python, a list is a collection of ordered, mutable (changeable) items. 
# It can hold elements of different data types, such as integers, strings, or even other lists.
# There are several ways to reverse a list in Python:
# a) 
# my_list = [1, 2, 3, 4, 5]
# my_list.reverse()
# print(my_list)
# b) 
# my_list = [1, 2, 3, 4, 5]
# reversed_list = my_list[::-1]
# print(reversed_list)

# 26) How will you remove last object from a list? 
# using th pop remove last object from a list 
# my_list = [10, 20, 30, 40, 50]
# my_list.pop()   
# print(my_list)

# 27) Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?  
# list1 = [2, 33, 222, 14, 25]
# list=list1[-1]
# print(list)
# list1[-1] means the last element of the list. so output = 25


# # 28) Differentiate between append () and extend () methods? 
# Append= append() is a list method used to add a single element at the end of the list.
# Extend=extend() is a list method used to add multiple elements from an iterable (like list, tuple, etc.) to the end of the list.

# 29) Write a Python function to get the largest number, smallest num and sum of all from a list. 
# def list(numbers):
#     largest=max(numbers)
#     smallest=min(numbers)
#     total=sum(numbers)

#     print("largest number is :",largest)
#     print("smallest number is :", smallest)
#     print("total of number is :",total)

# numbers=[25,56,21,45,72]
# list(numbers)    


# 30) How will you compare two lists? 
# You can compare two lists in Python using the equality operator ==.
# for example:-
# list1=[1,2,3]
# list2=[1,2,3]
# if(list1==list2):
#     print("lists are equal")
# else:
#     print("list are not equal")


# 31) Write a Python program to count the number of strings where the string  
# length is 2 or more and the first and last character are same from a given list of strings. 

# strings = ['aba', 'xyz', '121', 'madam', 'aa', 'ab']
# count = 0

# for s in strings:
#     if len(s) >= 2 and s[0] == s[-1]:
#         count += 1

# print("Count:", count)


# 32) Write a Python program to remove duplicates from a list. 

# A=[1, 2, 2, 3, 4, 4, 5]
# print(list(set(A)))


# 33) Write a Python program to check a list is empty or not.
# list = []

# if not list:
#     print("The list is empty")
# else:
#     print("The list is not empty")


# 34) Write a Python function that takes two lists and returns true if they have at least one common member. 
# def common():
#     a=[1,2,3]
#     b=[3,4,5]
#     print(set(a) & set(b))
# common()

# 35) Write a Python program to generate and print a list of first and last 5 
# elements where the values are square of numbers between 1 and 30.
# square=[]
# for i in range(1,31):
#     square.append(i*i)
# print("First 5:", square[:5])
# print("Last 5:", square[-5:])

# 36) Write a Python function that takes a list and returns a new list with 
# unique elements of the first list.
# def get_unique(lst):
#     return [] if not lst else list(dict.fromkeys(lst))
 
# my_list = [1, 2, 2, 3, 4, 4, 5]
# print(get_unique(my_list))

# 37) Write a Python program to convert a list of characters into a string. 
# Step 1: Character list
# char_list = ['H', 'e', 'l', 'l', 'o']
# result = " "
# for ch in char_list:
#     result = result + ch
# print("String:", result)

# 38) Write a Python program to select an item randomly from a list. 
# import random

# items = [1, 2, 3, 4, 5, 'apple', 'banana', 'cherry']
# random_item = random.choice(items)
# print("Random item:", random_item)

# 39) Write a Python program to find the second smallest number in a list. 
# numbers=[5, 1, 9, 3, 7]
# numbers.sort()
# second_smallest=numbers[1]
# print(second_smallest)

# 40) Write a Python program to get unique values from a list 
# List with duplicate values
# my_list = [1, 2, 2, 3, 4, 4, 5]
# unique_values = list(set(my_list))
# print("Unique values:", unique_values)

# 41) Write a Python program to check whether a list contains a sub list 

# def is_sublist(main_list, sub_list):
#     return str(sub_list)[1:-1] in str(main_list)

# main = [1, 2, 3, 4, 5]
# sub = [3, 4]

# if is_sublist(main, sub):
#     print("Yes")
# else:
#     print("No")

# 42) Write a Python program to split a list into different variables. 
# Example list

# my_list = [10, 20, 30, 40, 50]
# var1, var2, var3, var4, var5 = my_list
# print(var1, var2, var3, var4, var5)
# print(var1)

# 43) What is tuple? Difference between list and tuple. 
### Tuple:
# tuple is an ordered, immutable collection of elements, defined with round brackets ().

### Difference between List and Tuple:
# List: Mutable (can be changed), defined with [].
# Tuple: Immutable (cannot be changed), defined with ().
# List: Slower, more methods.
# Tuple: Faster, fewer methods.
# Use Case: Use list when data changes; use tuple for constant data.

# 44) Write a Python program to create a tuple with different data types. 

# my_tuple = (10, "Hello", 3.14, True, [1, 2, 3])
# print("Tuple with different data types:", my_tuple)

# 45) Write a Python program to unzip a list of tuples into individual lists. 
# List of tuples

# pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
# x, y = zip(*pairs)
# print("List 1:", list(x))
# print("List 2:", list(y))

# 46) Write a Python program to convert a list of tuples into a dictionary. 

# my_list = [("a", 1), ("b", 2), ("c", 3)]
# my_dict = dict(my_list)
# print("Dictionary:", my_dict)

# 47) How will you create a dictionary using tuples in python? 

# data = [("name", "Swapnil"), ("age", 25), ("city", "Bhopal")]
# my_dict = dict(data)
# print(my_dict)

# 48) Write a Python script to sort (ascending and descending) a dictionary by value. 

# d = {'a': 3, 'b': 1, 'c': 5, 'd': 2}
# # Ascending
# print(dict(sorted(d.items(), key=lambda x: x[1])))
# # Descending
# print(dict(sorted(d.items(), key=lambda x: x[1], reverse=True)))

# 49) Write a Python script to concatenate following dictionaries to create a new one. 

# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'd': 4}
# dict1.update(dict2)
# print("New Dictionary:", dict1)

# 50) Write a Python script to check if a given key already exists in a dictionary. 

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# Check = 'b'

# if Check in my_dict:
#     print(Check,"exist in my_dict")
# else:
#     print(Check,"dosesn't exist")

# 51) How Do You Traverse Through a Dictionary Object in Python? 
### Traversing a Dictionary in Python

# 1. Iterating over keys: You can iterate through the dictionary's keys using a simple `for` loop.
# 2. Using `items(): The `items()` method allows you to traverse both keys and values.
# 3. Using `keys(): The `keys()` method allows you to iterate over only the dictionary's keys.
# 4. Using `values(): The `values()` method allows you to iterate over only the dictionary's values.

# These methods help in efficiently accessing the elements of a dictionary.

# 52) How Do You Check the Presence of a Key in A Dictionary? 

### Checking the Presence of a Key in a Dictionary

# 1. Using the `in` keyword: The `in` keyword checks if a key exists in the dictionary. 
# It returns `True` if the key is present and `False` if not.
# 2. Using the `get()` method: The `get()` method returns the value of the key if it exists. 
# If the key is not found, it returns `None` (or a default value if specified).
# Both methods allow you to check if a key is present in the dictionary efficiently. 
# The `in` keyword is commonly used for its simplicity.

# 53) Write a Python script to print a dictionary where the keys are numbers between 1 and 15. 

# my_dict = {i: i for i in range(1, 16)}
# print(my_dict)

# 54) Write a Python program to check multiple keys exists in a dictionary 
 
# 55) Write a Python script to merge two Python dictionaries 

# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'd': 4}
# dict1.update(dict2)
# print(dict1)

# 56) Write a Python program to map two lists into a dictionary 
# Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}). 

# keys = ['a', 'b', 'd', 'c']
# values = [400, 400, 400, 300]
# mapped_dict = dict(zip(keys, values))
# print(mapped_dict)

# 57) Write a Python program to find the highest 3 values in a dictionary 

# my_dict = {'a': 400, 'b': 100, 'c': 300, 'd': 200, 'e': 500}
# H= sorted(my_dict.values(), reverse=True)[:3]
# print("Highest 3 values:",H)

# 58) Write a Python program to combine values in python list of dictionaries. 
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 
# 300}, o {'item': 'item1', 'amount': 750}] 

# data = [
#     {'item': 'item1', 'amount': 400},
#     {'item': 'item2', 'amount': 300},
#     {'item': 'item1', 'amount': 750}
# ]
# result = {}
# for d in data:
#     result[d['item']] = result.get(d['item'], 0) + d['amount']
# print(result)



# 59) Write a Python program to create a dictionary from a string. 
# Note: Track the count of the letters from the string. 

# def letter_count(string):
#     count_dict = {}
#     for char in string.lower():
#         if char.isalpha():
#             count_dict[char] = count_dict.get(char, 0) + 1
#     return count_dict
# input_string = "Hello World"
# print(letter_count(input_string))


# 60) Sample string:
#  'w3resource'

# def letter_count(string):
#     count_dict = {}
#     for char in string:
#         count_dict[char] = count_dict.get(char, 0) + 1
#     return count_dict

# input_string = 'w3resource'
# print(letter_count(input_string))


# 61) Write a Python function to calculate the factorial of a number (a 
# nonnegative integer) 

# def factorial():
#     n=int(input("enter your number\n"))
#     fact=1
#     sum=0
#     for i in range(1,n+1):
#         fact*=i
#     print(fact)

# factorial()


# 62) Write a Python function to check whether a number is in a given range 

# def is_in_range(number, start, end):
#     return start <= number <= end

# print(is_in_range(5, 1, 10)) 


# 63) Write a Python function to check whether a number is perfect or not. 

# def is_perfect_number(num):
#     divisors_sum = 0
#     for i in range(1, num):
#         if num % i == 0:
#             divisors_sum += i
#     return divisors_sum == num

# print(is_perfect_number(6))  


# 64) Write a Python function that checks whether a passed string is palindrome or not 

# def is_palindrome(s):
#     return s == s[::-1]

# print(is_palindrome("madam"))  
# print(is_palindrome("hello"))  

# 65) How Many Basic Types of Functions Are Available in Python? 

# There are 2 basic types of functions in Python:
# 1.Built-in Functions: Predefined functions like print(), len(), max(), etc.
# 2.User-defined Functions: Functions that you create using the def keyword.
# def greet(name):
#     print(f"Hello, {name}!")

# 66) How can you pick a random item from a list or tuple? 

# import random
# print(random.choice([1, 2, 3, 4, 5]))
# print(random.choice(('apple', 'banana', 'cherry')))

# 67) How can you pick a random item from a range? 

# import random
# item = random.choice(range(1, 11))
# print(item)

# 68) How can you get a random number in python ? 
# import random
# number=random.randint(1,10)
# print(number)

# 69) How will you set the starting value in generating random numbers? 

# import random

# random.seed(20)
# print(random.randint(1, 100))
 
# 70) How will you randomize the items of a list in place? 
# import random
# my_list = [1, 2, 3, 4, 5]
# random.shuffle(my_list)
# print(my_list) 

 
# 71) What is File function in python? What are keywords to create and write file. 
# In Python, the file function refers to the open() function, which is used to create, open, read, write, or append files.
# It takes two main arguments:
# Filename – the name of the file.
# Mode – the operation to perform ('r', 'w', 'a', etc.).

# 72) Write a Python program to read an entire text file. 
# f=open("test.text1",'w')
# f.write("Hello world\n")
# f.close()

# 73) Write a Python program to append text to a file and display the text. 
# f=open("test.text1",'a')
# f.write(" Hello Python\n")

# 74) Write a Python program to read first n lines of a file.

# f=open("test.text1",'r')
# data=f.read()
# print(data)
# f.close()

#  75) Write a Python program to read last n lines of a file.

# file = open("test.text1", "r")  
# lines = file.readlines()        
# file.close()                    
# for line in lines[-1:]:         
#     print(line, end='') 

# 76) Write a Python program to read a file line by line and store it into a list 

# file = open("test.text1", "r")  
# lines = file.readlines()        
# file.close()                   
# print("Lines stored in list:\n",lines)

# 77) Write a Python program to read a file line by line store it into a variable. 

# file = open("test.text1", "r")   
# lines = file.readlines()         
# file.close()                     
# data = "".join(lines)            

# print("File content stored in variable:\n",data)

# 78) Write a python program to find the longest words. 

# file = open("test.text1", "r") 
# words = file.read().split()     
# file.close()                    
# longest_word = max(words, key=len)  
# print("Longest word in the file:", longest_word)

# 79) Write a Python program to count the number of lines in a text file. 

# file = open("test.text1", "r")   
# lines = file.readlines()         
# file.close()                     
# line_count = len(lines)          
# print("Number of lines in the file:", line_count)

# 80) Write a Python program to count the frequency of words in a file. 

# from collections import Counter

# with open("test.text1", "r") as file:
#     word_count = Counter(file.read().split())
# print(word_count)

# 81) Write a Python program to write a list to a file. 
# my_list = ["Python", "is", "awesome", "and", "fun"] 

# with open("test.text1", "w") as file:  
#     for item in my_list:
#         file.write(item + "\n")
#         print(my_list)

# 82) Write a Python program to copy the contents of a file to another file.

# file = open("test.text1", "r")
# data = file.read()
# destination = open("destination.txt", "w")
# destination.write(data)
# file.close()
# destination.close()
# print("Copied content:\n", data) 

# 83) Explain Exception handling? What is an Error in Python? 
# Exception handling is a way to handle runtime errors gracefully so that the program doesn’t crash.
# An error is a problem in a program that causes it to stop running.
# Types of errors:
# Syntax Error: Wrong code structure (e.g., missing :)
# Runtime Error: Error while program is running (e.g., division by zero)

# 84) How many except statements can a try-except block have? Name Some built-in exception classes:
 
# A try block can have multiple except blocks.
# Some built-in exception classes:
# ValueError,TypeError,ZeroDivisionError,IndexError,FileNotFoundError

# 85) When will the else part of try-except-else be executed? 

# Else part in try-except-else runs only if no exception occurs in the try block.

# 86) Can one block of except statements handle multiple exception?
#  Yes, one except block can handle multiple exceptions using a tuple.
# Example:-
# try:
#     x = int("abc")
# except (ValueError, TypeError):
#     print("Handled multiple exceptions")

# 87) When is the finally block executed? 

# The finally block is always executed, regardless of whether:
# An exception is raised or not,
# The exception is caught or not,
# There is a return statement in the try or except block.

# 88) What happens when „1‟== 1 is executed? 

# The expression "1" == 1 compares:
# "1" → a string
# 1 → an integer

# 89) How Do You Handle Exceptions with Try/Except/Finally in Python? Explain with coding snippets. 

# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
#     print("Result:", result)
# except ZeroDivisionError:
#     print("You cannot divide by zero.")
# finally:
#     print("Execution complete.")

# 90) Write python program that user to enter only odd numbers, else will raise an exception. 

# try:
#     num = int(input("Enter an odd number: "))
#     if num % 2 == 0:
#         raise ValueError("This is not an odd number!")
#     print(num)
# except ValueError as ve:
#     print("Error:", ve)





























