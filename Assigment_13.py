#!/usr/bin/env python
# coding: utf-8

# 1.	What advantages do Excel spreadsheets have over CSV spreadsheets?

# XLS files support adding charts and graphs to the file, whereas CSV files only offer a plain text representation of the data.

# 2. What do you pass to csv.reader() and csv.writer() to create reader and writer objects?

# In[1]:


import csv
with open('protagonist.csv', 'w', newline='') as file:
    writer = csv.writer(file)


# In[2]:



with open('protagonist.csv', 'r', newline='') as file:
    reader = csv.reader(file)


# Q3. What modes do File objects for reader and writer objects need to be opened in?

#  Reading a file
# f = open(__file__, 'r')# read mode 
# #read()
# text = f.read(10)
# print(text)
# 
#  Reading a file
# f = open(__file__, 'w')# read mode 
# #read()
# text = f.write(10)
#  
#  Reading and Writing a file
# f = open(__file__, 'r+')#or 'w+'
# lines = f.read()
# f.write(lines)
#  
#  Appending a file
# f = open(__file__, 'a')
# lines = 'Hello world\n'
# f.write(lines)
#  
#  Appending and reading a file
# f = open(__file__, 'a+')
# lines = f.read()
# f.write(lines)

# Q4.What method takes a list argument and writes it to a CSV file?

# .writerows(data)---> method use to include the list of data in the file
# data to be written row-wise in csv file
# data = [['Kom'], [is], ['great !']]
#  
#  opening the csv file in 'w+' mode
# file = open('kom.csv', 'w+', newline ='')
#  
#  writing the data into the file
# with file:   
#     write = csv.writer(file)
#     write.writerows(data)

# Q5. What do the keyword arguments delimiter and line terminator do?
# 
# The delimiter is the character that appears between cells on a row. By default, the delimiter for a CSV file is a comma. The line terminator is the character that comes at the end of a row. By default, the line terminator is a newline

# Q6.  What function takes a string of JSON data and returns a Python data structure?
# 
# loads() method return Python data structure of JSON string or data.

# 7. What function takes a Python data structure and returns a string of JSON data?
# 
# Answer->If you have a Python object, you can convert it into a JSON string by using the json. dumps() method.

# In[ ]:




