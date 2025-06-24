# for i in '123':
#     print(i)

# for i in 'Rushikesh':
#     print(i,end=" ")

# for i in (2,3,4,5,6):
#     print(i,end=" ")
    
# for i in {2,3,4,5,6}:
#     print(i,end=" ")

# for i in {2:'ee',3:'tt',4:'ff',5:'tt','a':'hh'}:
#     print(i,end=" ")

# for i in range(1,51):
#     if i%2!=0:
#       print(i,end=" ")

# for i in range(1,51):
#     if i%2==0:
#         print(i,end=" ")
        
# s='this is python class'
# c=0
# for i in s:
#     c+=1
# print(c)


# to extract vowels form the given str
# s=input("enter the str:")
# for i in s:
#     if i in "aeiouAEIOU":
#         print(i)

# to replace space by _ in a given str
# s=input("enter the str: ")
# c=""
# for i in s:
#     if i==" ":
#         c+="_"
#     else:
#         c+=i
# print(c)     
   
# to check whether the given str is palindrome
# s=input("enter the str: ")
# a=""
# for i in range(len(s)-1,-1):
#     a+=s[i]
# if a==s:
#     print("palindrome") 
# else:
#     print("not palindrome")
  
# extract all the int which are multiple of 5 having 3 digit
# l=eval(input("enter the list: "))
# for i in l:
#     if i%5==0 and 99<i<1000:
#         print(i,end="")
        
#  program to remove the duplicate value form the given list without using typecasting
# l=eval(input("enter the list: "))
# s = []
# for i in l:
#     if i not in s:
#         s.append(i) 
# print(s)

# to create a str from a to z
# a=""
# for i in range(ord('a'),ord('z')+1):
#     a+=chr(i)   
# print(a ,end=" ")




# Print even numbers between 1 and 20.
# n=20
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         print(i, end=" ")       

# Print the characters of a string one by one.
# s="hello world"
# for i in s:
#     print(i, end=" ")

# Print the square of numbers from 1 to 5.
# n=5
# for i in range(1,n+1):
#     print(i * i, end=" ")
    
# Count vowels in a given string.
# s="hello world"
# vowels = "aeiouAEIOU"
# count = 0
# for i in s:
#     if i in vowels:
#         count += 1
# print("Number of vowels:", count)

# Print all elements of a list.
# l = [1, 2, 3, 4, 5]
# for i in l:
#     print(i, end=" ")

# Sum all numbers in a list.
# l = [1, 2, 3, 4, 5]
# s=0
# for i in l:
#     s += i  
# print("Sum of list:", s)

# # Print multiplication table of a number (e.g., 5).
# num = int(input("enter the num: "))
# for i in range(1,11):
#     i*=num
#     print(i,end=" ")

# Print all items with their index using a loop.
# l = ['apple', 'banana', 'cherry']
# for i in range(len(l)):
#     print( i, l[i], sep=":")


# Print numbers from 10 to 1 (reverse order).
# n=10
# for i in range(10,0,-1):
#     print(i,end=" ")
    
# Print only the palindromes from a list of strings without .
# s=['naman',"iiij" , "nayan", ]
# for i in s:
#     rev = ""
#     for j in range(len(i)-1,-1,-1):
#         rev+=i[j]
#         if i==rev:
#             print(i,end=" ")

# Count how many times a word appears in a list.


# Remove all duplicates from a list using a loop. 
# l = [1, 2, 2, 3, 4, 4, 5]
# a=[]
# for i in l:
#     if i not in a:
#         a.append(i)
# print(a)

# Create a dictionary from two lists (keys and values).
# l = [1, 2, 3, 4, 5]
# m = ['a','b','c','d','e']
# b={}
# for i in l:
#         b.add     

# Loop through a nested list and print each item.
# l=[1,2,3,4,5,[33,22,44],33]
# for i in l[5]:
#     print(i,end=" ")

# Find prime numbers between 1 and 50.
# a=int(input("enter the num: "))
# count=0
# for i in range(0,a):
#     if %i==0:
#         count+=1  
# if count<2:
#     print(i)

# i=1
# count=0
# while i<a:
#     if a%i==0:
#         count+=1
#     i+=1
# if count<2:
#     print("it is a prime num")
# else:
#     print("it is not prime")

# FOR LOOP///////

# PRINT OR FIND THE LENGTH OF GIVEN COLLECTION WITHOUT USING LEN FUNCTION 
# a=eval(input(" enter the collection: "))
# c=0
# for b in a:
#     c+=1
# print("length of collection: ",c)

# to extract vowels from string
# a=input("enter the string: ")
# for b in a:
#     if b in 'aeiouAEIOU':
#         print(b,end=" ")

# to replace space from given string    
# a=input("enter the string: ")
# c=""
# for b in a:
#     if b==" ":
#         c+="_"
#     else:
#         c+=b
# print(c)        
         
# TO CHECK OME WITHOUT USING SLICING
# a=input("enter the string: ")
# b=''
# for i in a:
#     b=i+b
# if a==b:
#     print("the given string is palindrome")
# else: 
#     print("the given string is not palindrome")
    
# TO EXTRACT INT WHICH ARE MULTIPLE OF 5 AND 3
# a=eval(input("enter the list: "))
# for b in a:
#     if type(a)==int:
#         if a%5==0 and a%3==0:
#             print(b,end=" ")

# TO REMOVE DUPLICATE FROM THE LIST WITHOUT TYPECASTING
# a=eval(input("enter the list: "))
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)

# CONVERT THE TUPLE INTO DICT
# a=eval(input("enter the tuple: "))
# i=0  
# s={}
# while i<len(a):
#     if type(a[i])==str:
#         s[a[i]]=len(a[i])
#     i+=1
# print(s)

#  To get the following output:
# 1=[12,3.4, 'data', 'science'] output=('data': 'da', 'science': 'se')
# a=eval(input("enter the list: "))
# i=0
# s={} 
# while i<len(a):
#     if type(a[i])==str:
#      s[a[i]]=a[i][0:2]   
#     i+=1
# print(s)

# To get the following output
# a=input("enter the string: ")
# s={}
# i=0
# while i<len(a):
#     if a[i]  in s:
#         s[a[i]]== 'A'<=a[i]<='Z'
#         print(chr(ord(a[i])+32),end="")
#     else:
#          print(chr(ord(a[i])-32),end="")
# i+=1


# 10. To create the string with uppercase character from A to Z.
# a=input("enter the string: ")
# s=""
# i=0
# while i<len(a):
#     if 'A'<=a[i]<='Z':
#         s+=a[i]
#     i+=1
# print(s)

# SPLIT FUNCTION
# z='hey hello how are you'
# print(z.split("h"))

# a=eval(input("enter the string: "))
# i=0
# s={}
# for i in a.split(' '):
#     s[i]=len(i)
# print(s)

# to get the following outputp
# p=["python.py","web.html","google.com"]
# # output=["py","html","com"]
# i=0
# l=[]
# for i in p:
#     l.append(i.split(".")[1])
# print(l)

# to get the following outputp
# p=["python.py","web.html","google.com"]
# output={"py.python,html.web,com.google"}
# s={}
# for i in p:
#    n=i.split(".")
#    s[n[len(n)-1]]=n[0]
# print(s)

# a='Do code  by yourself'
# # output='oD edoc yb flesruoy'
# s=''
# i=0  
# for i in a.split(' '):
#     s+=i[::-1]+" "
# print(s)



    



