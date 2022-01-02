#python is mainly used for automation purposes, web-apps, and data science.
#Big companies like instagram/facebook/amazon use python in different parts of thier products
#when downloading python it comes with it's own python shell, type idle3 in terminal to pop it up, or type python3.9 to use personal teminal
#Ex: process images
#everything in python is an object
#Division in python always returns a floating point number
""" print(hello)""" #another form of commenting in python iss with triple qoutes

# len function returns the length of a string
fruit = 'grapes'
fruit_len = len(fruit) #if you print the output you will get  6,, which the length of 'grapes'
#Variable tpes in python are implicit and not explicit, dont need to identify with int/String/Char?etc like Java
#semi-colon is not necessarry in python
day_hours = 24
week_days = 7
week_hours = week_days * day_hours
print(week_hours)

print(type(day_hours)) # type is used to check/class variable type

print('{} {} {}'.format('I',"love",'Python'))

##List
student_grades = [9.1,8.8,7.5] #each item in list is an object

#you can create a list of numbers using a "range"
#list(range(1,10)) , the output will be [1,2,3,4,5,6,7,8,9]
#you can also specify a third argument list(range(1,10,2)), the output will be [1,3,5,7,9]

temperature = [32.3, 44, "It's cold"] #each object in list does not need to be same data type

guava =[3.4, 34, "sam",temperature]#you can also plas a list within a list

#splice a list or string 

# we can accss a portion of the list, guava[3:5] will give items 3-4
#guave[-2] will give you the last two items
# you can also splice stings

mystring = ' hello'
mystring[1] #will return th lettr e
mystring[:3] #will return letters 0-2 so hel

guava[2][2] #will return item 2 then return sa

guava[:-2] #prints out everything but last two
guava[-3:] #prints out last three

## Exception Handiling
# try : 
#    except: block is used instead of try and catch in java
## IMPORTANT INFO BELOW
#to find out what you can do with a specific type use dir() in shell CL
#if you want further explination in dir() use help
#example: dir(str) -> help(str.upper) then press 'q' to go back
#dir(__builtins__) gives you a list of all the built in functions in python

#Dictionaries

# Dictionary types =  use {} instead of []. Items in dictionry are made of keys and values.
# list is more appropriate to store an array of values
# list.sort() sorts the list
#range() can be used to get the range of a list

student_grades = {"Marry" : 9.1, "Sim": 8.8, "Jhon": 7.5 }
print(student_grades.get("Marry"))

#Tuple

# tuple (3,4,3) a tuple is like a list but with parenthesis. 
#tuples are inmutable, list are mutable
#in list you can add and subtract to list with .appen(), but you cant in a tupple
#tuples ar a bit faster then list

## From Tuple to List

# data = (1,2,3) -> list(data) = [1,2,3]

# Tuple is immutable , List arent

#From List to Tuple

# data = [1,2,3] -> tuple(data) = (1,2,3)

#From List to Dictionary

# data = [["name","Jhon"], ["surname","smith"]]
# dict(data) {'name': 'Jhon','surname':'smith'}

# th original data type needs to be structured in a way the new data type can understand it

#Functions

# to create functions you use the def keyword

def mean(mylist): #python automatically knows whats part of function based on indent
    the_mean = sum(mylist) / len(mylist)
    return the_mean
print(mean([1,2,3]))

def foo(*args):
    h = 7 #accepts many arguments
def foo(**Kwargs): 
    hi = ''     #accepts many key word arguments. Ex: foo(x=9,y=10)

# if statements use and , or, ==. < or > Instead of < or >, &&, ||, == like java
# isinstance() can be used with if statement to check type(), type() can be used to but isinstance() is perferrable


## File
# To open a file we use the built in open(path_to_file_) function
# absolute path includes the root, relative path starts with current working directory
#read() method posts string method of contents in file
# on windows you stat path with "C:"
# when reading in the file python keeps track of the current position in the file
# seek(number) method changes the current position in the file
# tell() - determinse the current position in the file
# close() - like java it's important to close the file.
# open(path_to_file, mode) - mode allows us to do different functions with a file
# Different modes, r: open for reading(default), w:Open for writing, truncating first, x: Create a new file and open it for writing, a: Open for writing, appending to file.
# Extra modes, +: Open a file for updating (read/write), b: binary mode, t:text mode (default)
# modes can be combined together. Ex: rb, rt
# rstrip(), removes any white spaces in file
# best way to open file is using 'with'
with open('bear.txt') as myFile:
    content = myFile.read()
print(content)
    
###Function vs Method
# when you write a function inside a class it is a  method
# outside of a class it is a function
# functions can be called directly, in class  method can be called with object
# def __init__(self): , is equal to a constructor in java and is called in every initilization of an object
# *self* is a reference to the new object being created. you can then add arguments
# self.field_name = field_name is equal to this.field_name = field_name in java

## Modules
#modules are like libraries in java
#python modules are files that  have an '.py' extension 
#can be used with import module_name
#Builtin modules come with python when downloaded
import time
import os

while True: 
    if os.path.exists('files/fruit.txt'):
        with open("files/fruit.txt") as myFile:
            print(myFile.read())
    else:
        print("File does not exist")
    time.sleep(10)

## PANDAS
# is a data structure or a data library that provides data structures and data analysis tools
# 'pip' is another library that comes installed in python
# 'pip' is used to install other third part libraries
# 'pip' command is different depending on different operating system but all us 'pip'
# 'pip3.9 install pandas' - panda is a bunch of modules which is called a package. 

import pandas

while True: 
    if os.path.exists('files/tmp_today.csv'):
        with open("files/fruit.txt") as myFile:
            data = pandas.read_csv('files/tmp_today.csv')
            print(data.mean()['st1'])
    else:
        print("File does not exist")
    time.sleep(10)
6121

#df1 = pandas.DataFrame<[[2,4,6],[10,20,30]]> #create data table
#df1 = pandas.DataFrame< [[2,4,6],[10,20,30]] >#Create data tablewith columns


## String Format 

name = input("Enter Your Name:")
surname = input("Enter your surname:")

message = "Hello %s %s" %(name, surname)
message = f"Hello {name} {surname}"
print(" Hi {} {}".format(name,surname))

## For-Loops
monday_temperatures = [9.1,45.5,323,32.4]
for temperature in monday_temperatures:
    print(round(temperature))

for letter in 'hello':
    print(letter.title())

# for loops can be done in one statement and returned in a function

def foo(num):
    return [temp for temp in num if type(temp) is int]

def foo(num):
    return [ temp for temp in num if type(temp) is not str]

def foo(ans):
    return [ temp if not isinstance(temp,str) else 0 for temp in ans]

## Fun Fact
## Python comes pre-installed on Linux and Mac systems!
## Windows 10 and up have it pre-installed



