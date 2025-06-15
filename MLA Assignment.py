#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Q1: What is the output of following expression 5 + 4 * 9 % (3 + 1) / 6 - 1

exp =  5 + 4 * 9 % (3 + 1) / 6 - 1
print(exp)


# In[10]:


# Q2: Write a program to check if a Number is Odd or Even. Take number as a input from user at runtime.

num = int(input("Enter Number : "))
if(num%2==0):
    print("Even")
else:
    print("odd")


# In[16]:


# Q3: Write a program to display the multiplication table by taking a number as input. [Hint : Use print statement inside of a loop]
num = int(input("Enter Number : "))
for i in range(0, 10):
    print(num, 'x', i, '=', num * i)


# In[19]:


# Write a program which will find all numbers between 2000 and 3200 which are divisible by 7 but are not a multiple of 5. Note: The numbers obtained should be printed in a comma-separated sequence on a single line.

for i in range(2000, 3200):
    if(i%7==0 and i%5!=0):
        print(i, end=',')


# In[30]:


# Count the elements of each datatype inside the list and display in output [2, 3, 'Py', '10', 1, 'SQL', 5.5, True, 3, 'John', None, 7]

import collections as c
list = [2, 3, 'Py', '10', 1, 'SQL', 5.5, True, 3, 'John', None, 7]  
c = c.Counter(type(x) for x in list)
print(dict(c))


# In[32]:


# Add all values from the list with numeric datatypes [2, 3, 'Py', '10', 1, 'SQL', 5.5, True, 3, 'John', None, 7]

import collections as c
list = [2, 3, 'Py', '10', 1, 'SQL', 5.5, True, 3, 'John', None, 7]
ans = sum(filter(lambda i: isinstance(i,int),list))
newans = ans + sum(filter(lambda j: isinstance(j,float),list))
print(newans)


# In[36]:


# Q7: Concat all str datatypes with hyphen as a delimiter [2, 3, 'Py', '10', 1, 'SQL', 5.5, True, 3, 'John', None, 7]

list = [2, 3, 'Py', '10', 1, 'SQL', 5.5, True, 3, 'John', None, 7]
''.join(filter(lambda x: type(x)==str,list))


# In[37]:


# Q8: Write a UDF that takes list as input and returns sum of all numbers (exclude bool) and count of all str [2, 3, 'Py', '10', 1, 'SQL', 5.5, True, 3, 'John', None, 7] Hint: ----- def my_func: # your code my_func(l1) # output --> {'Sum': xxx, 'Count_of_Strs': xxx}

# Declaring list
list1 = [2, 3, 'Py', '10', 1, 'SQL', 5.5, True, 3, 'John', None, 7]

def my_func(l):
    dict1 = {}
     
    dict1['sum of all numbers (exclude bool)'] = sum([float(i) for i in l if type(i)== int or type(i)== float])
    dict1['count of all str'] = len([str(i) for i in l if type(i)== str])
    return dict1

my_func(list1)


# In[40]:


# Q9: Get only odd numbers from the following list and store the numbers in new list li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] i. Use loops to get the answer ii. Use list comprehensions iii. Use lambda function with filter

list = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

# i. Use loops to get the answer
odd_list = []
for x in list:
    if x % 2 != 0:
        odd_list.append(x)
print('Using loops to get the answer :',odd_list)
        
# ii. Use list comprehensions

odd_list = [x for x in li if x % 2 !=0]
print('list comprehensions :',odd_list)


# In[52]:


# Q10: Write a UDF to return the descriptives [sum, count, min, mean, max] for a list of n number of input numbers.

import numpy as np

list = []

n = int(input("Enter Number Of Elements: "))

for i in range(0, n):
    elem = int(input())
    
    list.append(elem)
    
print("List is", list)


# Calculate the descriptives
total_sum = sum(list)
print("Sum is", total_sum)
count = len(list)
print("Length is", count)
minimum_value = min(list)
maximum_value = max(list)
print("Maximum Value is: ", maximum_value)
print("Minimum numer is", minimum_value)
print("Mean is: ", np.mean(list))


# In[53]:


# Q11: Write an udf to calculate the area of different shapes Take shape and dimensions as arguments to udf as follows : 1. square which has side 2. rectangle which has length and width 3. circle which has radius The shape should be a positional
# argument and it's dimensions are taken as kwargs Perform proper validation for the user inputs and then calculate area. E.g. if shape is square, ensure kwargs has "side" and if so, then you may return the area, else display appropriate error message
# like "Please enter 'side' for a square"

name_shape = input('Enter Name of Shape : ')

def area_shape(name):
    name = name.lower()
    
    if(name == 'square'):
        s = int(input("Enter Length of Square: "))
        square = s * s
        print(f'Area of Square is {square}.')
    elif(name == 'retangle'):
        l = int(input("Enter Length : "))
        b = int(input("Enter Bredth : "))
        area = l * b
        print(f'Area of Retangle is {area}.')
    elif(name == 'circle'):
        r = int(input("Enter Radius of Circle: "))
        pie = 3.14
        area = pie * r * r
        print(f'Area of Circle is {area}.')
        
area_shape(name_shape)


# In[4]:


# Q12: Write a UDF to reconcile the values within two lists. l1 = ['January', 'February', 'March', 'May', 'June', 'September', 'December'] l2 = ['January', 'February', 'April', 'June', 'October', 'December'] Hint: ----- def func(l1, l2): your code here... Output:
# {'Matched': ['January', 'February', 'June', 'December'], 'Only in l1': ['March', 'May', 'September'], 'Only in l2': ['April', 'October']}


l1 = ['January', 'February', 'March', 'May', 'June', 'September', 'December']
l2 = ['January', 'February', 'April', 'June', 'October', 'December']

def func_of_reconcile(l1, l2):
    x = set(l1)
    y = set(l2)
    result = {}
    result['Matched'] = list(x.intersection(y))
    result['Only in l1'] = list(x-y)
    result['Only in l2'] = list(y-x)
    return result
func_of_reconcile(l1, l2)


# In[23]:


# Q13: write a UDF to check if a number is prime or not.

def test_num(x):
    num = int(input("Enter number: "))

    flag = False

    if num == 1:
        print(num, "is not a prime number")
    elif num > 1:
        for i in range(2, (num-1)):
            if (num % i) == 0:
                flag = True
                break

        if flag:
            print(num, "is not a prime number")
        else:
            print(num, "is a prime number")
            
test_num(num)


# In[24]:


# Q14. Write a program which can compute the factorial of a given numbers. # The results should be printed in a comma-separated sequence on a single line. # input() function can be used for getting user(console) input #Suppose the input is supplied to
# the program: 8 #Then, the output should be: 40320 #Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

num = int(input('Enter a number : '))
fact = 1
if num < 0:
    print('factorial does not exist for negative numbers')
elif num == 0:
   print('The factorial of 0 is 1')
else:
    for i in range(1, num + 1):
        fact = fact * i
    print('Factorial of',num ,'is',fact)


# In[28]:


# Q15. With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary. #Suppose the following input is supplied
# to the program: 8 #Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64} #Hints: In case of input data being supplied to the question, it should be assumed to be a console input. Consider using dict()

num = int(input('Enter a number : '))
dict1 = {i: i * i for i in range(1, num + 1)}
print(dict1)


# In[30]:


# Q16. Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number. Suppose the following input is supplied to the program: 34,67,55,33,12,98 Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input. you may use tuple() method to convert list to tuple

numbers = input('Enter a sequence of comma-separated numbers : ' )

numbers_split = numbers.split(',')

number_tuple = tuple(numbers_split)

print(numbers_split , end = ' ')
print(number_tuple)


# In[ ]:


# Q17. Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

# Suppose the following input is supplied to the program: without,hello,bag,world Then, the output should be: bag,hello,without,world

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

words = input('Enter a comma separated sequence of words : ')
words_split = words.split(',')
words_split.sort()
print ((', ').join(words_split))


# In[31]:


# Q18. Write a program that accepts a sequence of whitespace separated words # as input and prints the words after removing all duplicate words and sorting them alphanumerically. # Suppose the following input is supplied to the program: hello world
# and practice makes perfect and hello world again # Then, the output should be: again and hello makes perfect practice world #Hints: In case of input data being supplied to the question, it should be assumed to be a console input. #We use set container
# to remove duplicated data automatically and then use sorted() to sort the data.

words = input('Enter a sequence of whitespace separated words : ')
words1 = words.split(' ')
words1 = set(words1)
sorted_words = sorted(words1)
print((' ').join(sorted_words))


# In[32]:


# Q19. Write a program that accepts a sentence and calculate the number of upper case # letters and lower case letters. #Suppose the following input is supplied to the program: Hello world! #Then, the output should be: UPPER CASE 1 LOWER CASE 9
# #Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

sentense = input('Enter a sentence : ')
sentense = list(sentense)

upper,lower = 0 , 0

for i in sentense:
    if i.isupper():
        upper = upper + 1
        
    if i.islower():
        lower = lower + 1
    else:
        pass
        
print('UPPER CASE ',upper,'LOWER CASE ',lower)


# In[33]:


# Q20. Write a program that takes a string and returns reversed string. i.e. if input is "abcd123" output should be "321dcba"

str1 = input('Enter a string : ')
str1 = str1[::-1]
print(str1)

