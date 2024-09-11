############################### For loop in python

# Syntax

# for var_name in sequence:      //  var can can be anything but try it should be meaningful. And sequence means anything list tuple dict 
    # statements                 // statements can be one or multiple


# Example-

# list=['laddu','iphonewala','Rishav','Devashish']
# for name in list:
#     print(name)
# output=laddu
#        iphonewale
#        Rishav
#        Devashish

# Example-2
# list='laddu','iphonewala','Rishav','Devashish'
# for name in list:
#     print(name)
# output=laddu
#        iphonewale
#        Rishav
#        Devashish

#example-3
# name='Dev Ashish Jay'
# for i in name:
#     print(i)

# Output-
# D 
# e 
# v 

# A 
# s 
# h 
# i 
# s 
# h 

# J 
# a 
# y 


# same example with different varable name

# name='Dev Ashish Jay'
# for letters in name:
#     print(letters)

# output=same as above

# Here letter is a iterator insted of letter we can write 'i' also

# Example-4

# list='laddu','iphonewala','Rishav','Devashish'
# for name in list:
#     print(name)
#     if name=='Devashish':
#         print("hey its meah")

# output=laddu
#        iphonewale
#        Rishav
#        Devashish
#      hey its meah

# Q) calculate the square of each item in the list. list1[2,3,5,-6,20]

# list1=[2,3,5,-6,20]
# out=[]
# for i in list1:
#     square=i**2
#     out.append(square)
# print(out)

# Output-[4,9,25,36,400]

#Q)
# tuple1=(2,25,34,3,5,-1)
# for i in tuple1:
#     print(i)
# else:
#     print("You have successfully completed")

# output-
# 2
# 25
# 34
# 3
# 5
# -1
# you have successfully completed

# Q) same question but we will see what 'break' statement do 

# tuple1=(2,25,34,3,5,-1)
# for i in tuple1:
#     print(i)
#     if i==3:
#         break
# else:
#     print("You have successfully completed")

# Output-
# 2
# 25
# 34
# 3

############################# use of Range in for loop

# Range functions returns a sequence of numbers,starting from 0 by default,and 
# increments bt 1(by default), and stops before a specified number. 

# Range(start?,stop,step?)
      
# example range(2,8,2)
# means 2 se start kr rhe h,question marks diya hua h mtlb puch rha h kanha 
# se start krna chah rhe ho.stop means kanha rukna h jo ki question m diya 
# hua rehta h.Aur step means kitna ka gap rahega ye v pta ni rehta essiliye que
# marks diya hua h Example se samajhte 

# example-

# for i in range(2,8,2):
#     print(i)

# Output=
# 2
# 4
# 6

# means 2 se start hua stop 6 pe hua kuki 2 ka gap rakhe h 8 print nii hoga 
# kuki last m ek step jo h usme ek step pehle na print hota h 
  
# Example-2

# for i in range(2,8):
#     print(i)
 
#  Output= 
# 2
# 3
# 4
# 5
# 6
# 7

# Example-3

# for i in range(5):
#     print(i)

# output=
# 0
# 1
# 2
# 3
# 4

#Question=Print even number from 2 to 20

# for i in range(2,20,2):
#     print(i)

# output= even numbers column wise print ho jayega 18 tk

#print numbers from 100 to 1 

# for i in range(100,0,-1):
#     print(i)

# Output=100 se 1 tk colomn wise print ho jayega

#Question=print a multiplication table of any number
# for i in range(1,55):
#     if i%5==0:
#       print(i,":is multiplication of 5")

# another example by taking input from user show user can print any table

# n=int(input("Enter the number for table: "))

# for i in range(1,11):
#     print(n*i)

# output=koi v number daalo table print ho k aa jayega

# yenha i matlb hai ki 1-11 starting ek se hua aur 11 essilye daale taaki 10 m 
# ruke toh 10 tk table print hoga koi v chij ka

# Question=WAP to find the sum of first n numbers(using while)

# num=int(input("Enter the number: "))
# sum=0
# i=1
# while i<=num:
#     sum+=i
#     i+=1
# print(sum)

#Question=WAP to find the sum of first n number(using for)

# n=int(input("Enter the number: "))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(sum)

#WAP to find the factorial of first n numbers.(using for)

# factorial means multiply krna janha tk num h example
# factorial of 5=1*2*3*4*5=120

# n=int(input("Enter the number: "))

# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)


#---------------------------------------------sir class--------------------------------------------
#a'hiee nitin is ava'
# output='nitin ava'

# a='hii nitin to ava'.split()
# out=''
# for i in a:
#     if i==i[::-1]:
#      out+=i
#      out+=''
# print(out)


# a=[10,'Hello',3+5j,{1,2,3},[1,2,3,'Helo']]
# output=[1,5,1,3,4]

# a=[10,'Hello',3+5j,{1,2,3},[1,2,3,'Helo']]
# out=[]
# for i in a:
#     if type(i) in [int,float,complex,bool]:
#         out+=[1]
#     else:
#         out+=[len(i)]
# print(out)

# output=as excepted


    







