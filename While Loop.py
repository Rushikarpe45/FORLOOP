# natural number
# n=int(input("enter the num: "))
# i=1
# while i<=n:
#     print(i)
#     i=i+1

# even num
# n=int(input("enter the num: "))
# i=1
# while i<50:
#     if i%2==0:
#       print(i)
#     i=i+1

# multiple of 5
# n=int(input("enter the num: "))
# i=1
# while i<n:
#     if i%5==0:
#       print(i)
#     i=i+1

# table creation
# n=int(input("enter the num: "))
# i=1
# while i<11:
#     print(n*i)
#     i=i+1

# print n num
# n=int(input("enter the num: "))
# i=n
# while n>=1:
#     print(n)
#     n=n-1

# reverse the num
n=int(input("enter the num: "))
i=0
while n>0:
    a=n%10 
    i=i*10
    i=i+a
    n=n//10
print(i)

# sum of num  
# n=int(input("enter the num: "))
# i=0
# while n>0:
#     a=n%10 
#     i=i+a
#     n=n//10
# print(i)


# mul of num between num
# n=int(input("enter the num: "))
# i=1
# while n>0:
#     r=n%10
#     if r%2==0:
#         i=i*r
#     n=n//10
# print(i)
 
# sum of natural num
# n=int(input("enter the num: "))
# i=0
# while n>0:
#     i=i+n
#     n=n-1
# print(i)

# factorial
# n=int(input("enter the num: "))
# i=1
# while n>0:
#     i=i*n
#     n=n-1
# print(i)

#  assignment 
# separate given string
# string=input("enter the string: ")
# i=0
# while i<len(string):
#      print(string[i],end=" ")
#      i=i+1                              
    
# extract lowercase
# a=input(" enter the string: ")
# i=0
# while  i<len(a):
#     if 'a'<=a[i]<='z':
#         print(a[i],end=" ")
#     i=i+1                               

     # extract integer from list
# s=eval(input("enter the list: "))
# i=0
# while i<len(s):
#     if type(s[i])==int:
#         print(s[i],end=" ")
    # i=i+1                               # done


     # extract uppercase from string
# a=input(" enter the string: ")
# i=0
# while  i<len(a):
#     if 'A'<=a[i]<='Z':
#         print(a[i],end="")
#     i=i+1                              

       # int from list and print sum
# li=eval(input("enter the list: "))
# i=0
# s=0
# while i<len(li):
#     if type(li[i])==int:
#         s=s+li[i]
#     i=i+1
# print(s)                               

# a=eval(input("enter the tuple: "))
# i=0
# s=1
# while i<len(a):
#     if type(a[i])==float and  a[i]%2!=0:
#      s=a[i]%2!=0
#      s=s*a[i]
#     i=i+1
# print(s)                               

         # convert lowercase to uppercase and vice versa
# a=input(" enter the string: ")
# i=0
# while  i<len(a):
#     if 'a'<=a<='z':
#         print(chr(ord(a[i])-32),end="")
#     else:
#         print(chr(ord(a[i])+32),end="")
#     i=i+1
                                                             
    #   convert lowercase to uppercase
# a=input(" enter the string: ")                                                       
# i=0
# while  i<len(a):  
#     if 'a'<=a<='z':
#         print(chr(ord(a[i])-32),end="")
#     i=i+1
# print()                                                          

#  print fabonacci series
# s=int(input("enter the num: "))   
# i=0
# a=0
# b=1
# while i<s:
#      print(a,end=" ")
#      i=i+1
#      n=a+b
#      a=b
#      b=n

# a=int(input("enter the no.: "))
# i=1
# while i<=a:
#      print(i,end=" ")
     # i+=1
     
# a=int(input("enter the no.: "))
# i=0
# while i<a:
#      if i%2==0:
#       print(i,end=" ")
#      i+=1

# check armstrong no.
# a=int(input("enter the no.: "))
# s=0
# temp=a
# while a!=0:
#     r=a%10
#     s=s+r**3
#     a=a//10
# print(s)
# if s==temp:
#     print("armstrong no.")
# else:
#     print("not armstrong no.")       
     
