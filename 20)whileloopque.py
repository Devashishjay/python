# 1write a program to print deepak sir is a good man 10 tyme

# name="Deepak sir is a good man"
# i=1
# while i<=10:
#   print("name=",name, i)
#   i+=1  

# i=1
# while i<=10:
#     print(i,"Deepeak sir is a good man")
#     i+=1

#q) print a reportcard in which you have to give marks to students according to grades
# if marks greater than 90 give grade A 
# if marks =<80 and >=90 give grade B 
# if marks=<70 and >=80 give grade C 
# other wise fail 

# wap to print first 10 natural number

# i=1
# while i<=10:
#     print(i)
#     i+=1

# Wap to print all even number less than 100.

# i=0
# while i<100:
#     if i%2==0:
#       print(i)
#     i+=1

# Q Wap to print square of first 10 natural number
# i=1
# while i<=10:
#     print(i**2)
#     i+=1
   
#q1. wap to print product of first  5 number.

# i=1
# while i<=5:
#     print(i*2)
#     i+=1

# i=1
# while i<=5:
#     print(i**2)
#     i+=1

# Wap to print sqauare of a number if the number is odd

# i=1
# while i<=10:
#     if i%3==0:
#       print(i**2)
#       i+=1

#--------------------------------------------- loop in python(in details)-----------------------------------
# Loops are used to repeat instructions
# There are two types of loops in python
# 1) While loop
# 2) for loop

################################### while loop

# while condition: (means jb tk  condition sach rehti hai)

      #some work (tb tk uss kaam ko repeat krte rho)
      

# for example=

# Q) print hello 5 times

# i=1                  #(iteration 1 hai means 1 se ginti start kr rhe)
# while i<=5:          # (ginti kanha tk karna hai 5 tk condition diye)
#     print(i,"hello")         # (print karwaye i ko taaki gitni print ho)
#     i=i+1             # (i=i+1 hai means loop run karwa rhe loop upar condition jb tk true hai tb tk chalega)

######################## QUESTIONS

#1) Print numbers from 1 to 100

# i=1
# while i<=100:
#     print(i)
#     i+=1

#2) Print numbers from 100 to 1

# i=100
# while i>=1:
#     print(i)
#     i-=1

# 3) print multipplication table of a number

# i=1
# while i<=10:
#     print(7*i)
#     i+=1


# i=1
# while i<=10:
#     print(3*i)
#     i+=1


# 4) Print the elements of the following list using a loop:
# [1,4,9,16,25,36,49,64,81,100]

# list=[1,4,9,16,25,36,49,64,81,100]
# index=0
# while index<len(list):
#     print(list[index])
#     index+=1                                           //unsolved

# 6) Print  the elements of the following list using loop:
#[orange,mango,apple,kela,banana]

# fruits=[orange,mango,apple,kela,banana]
# index=0
# while                                                  // unsolved

#Q) Write a program to calculate the area of a triangle

# base=10
# height=7

# area=(0.5)*base*height
# print(area)

#take input from user and run example is below

# height = float(input("enter the height: "))
# base = float(input("enter the base: "))

# area = (0.5)*base*height
# print(area)


#Q) Wap to check Email.id and password credintals using nested loop.

# email=input("Enter your email: ")
# password=input("Enter your password: ")

# if '@' in email:
#     if '.' in email:
#         if len(password)>=8:
#             if any(char.isdigit() for char in password):
#                 if any(char.isupper() for char in password):
#                     if any(char.islower() for char in password):
#                         print("Email and password are valid")
#                     else:   print("The character must contain at least one lower character")
#                 else:   print("must contain one upper character")
#             else:    print("The contain one digit")
#         else: print("length should be atleast of 8 character")
#     else: print("must contain one dot")
# else: print("must contain @")

# #@) WAP to check the middle term is capital of a string

# string=input("enter the string")
# if any(char.iscapital() for char in string):
#     print("The character",string,"is capital")
# else:
#     print("Their is no capital letter in string")          //Unsolved

# Q) WAP to check the number is divisible by 5 and it should be a even number

# num=int(input("Enter the number: "))
# if (num%5==0 & num%2==0):
#     print("The number is divisible by 5 and number is even")
# else:
#     print("The num does not match the cretaria")

#Q) WAP to check the character is vowel or a consonants using nested method.
#Hint- vowels are a,e,i,o,u we have 5 vowels and rest of the alphabets are consonants

# char='g'

# if (char=='a' or char=='e' or char=='i' or char=='o' or char=='u'):
#     print("Vowel")
         
# else:
#     print("consonants")

#By taking input from user and do the same question

# char=(input("Enter the character: "))
# if (char=='a' or char=='e' or char=='i' or char=='o' or char=='u'):
#     print("Vowel")
         
# else:
#     print("consonants")


#Lets try to solve it using nested loop

# char=(input("Enter the character: "))
# if (char=='a'): 
#     print("Vowel")
#     if (char=='e'):  
#         print("Vowel")
#         if (char=='i'):
#             print("Vowel")
#             if (char=='o'):
#                 print("Vowel")
#                 if (char=='u'):
#                     print("Vowel")
#                 else:
#                      print("Consonants")
#             else:
#                  print("Consonants")
#         else: 
#              print("Consonants")
#     else: 
#          print("Consonants")
# else:
#      print("Consonants")                                 // Unsolved


# Q) WAP to check the collection is single value data type or multivaluedata type but it length
#should be more than 3

# Ans- example of single value data type- age=25 , name="Devashish"
#      example of multivalue data type- list, tuple, dictionary etc

#Q output should {'python':6,'hello':5,'apple':5}

# a=['python',3+5j,3.8,[1,2,3],'hello','ab','apple']
# i=0
# while i<len(list):
#     print(i)
#     i+=1


# a=['python',3+5j,3.8,[1,2,3],'hello','ab','apple']
# out={}
# i=0
# while i<len(a):
#     if type(a[i]==str and len(a[i])>2):
#         out[]



#Q  output should [171,777,939]
# a=[171,23,'Hello',777,939,127,'puthon']
# out=[]
# i=0
# while i<len(a):
#     if type(a[i])==int and str(a[i])==str(a[i])[::-1]:
#         out+=[a[i]]
#     i+=1
# print(out)


#Q output  [10,'Hello',3,27,3+5j]

# a=[10,'Hello',10,3,27,3+5j,3,10]
# out=[]
# i=0
# while i<len(a):
#     if a[i] not in out:
#         out+=[a[i]]
#     i+=1
# print(out)


#Q OUTPUT=1
# a='(()))(())'
# i=0
# c=0
# c1=0
# while i<len(a):
#     if a[i]==')':
#         c+=1
#     else:
#         c1+=1
#     i+=1
# print(abs(c1-c))

#Q
#Wap to check the number is perfect number or not

# num=int(input("Enter the number: "))
# sum=0
# i=1
# while i<num:
#     if num%i==0:
#         sum+=i

#     i+=1
# if num==sum:
#     print("perfect number")
# else:
#      print("not perfect")


#Q
#a='Hai Hello'
#Output={'Hai':['Hai',b,'iaH3'],'Hello':['Hello',10,'olleHs']}

# a='Hai Hello'.split()
# out={}
# i=0
# while i<len(a):
#     out[a[i]]=[a[i],len(a[i])*2,a[i][::-1]+str(len(a[i]))]
#     i+=1
# print(out)

#Q
# a='Hello'
# b='bye'
# output='Hbeylelo'

a='Hello'
b='bye'
out =''
i=0

while i<max(len(a), len(b)):
    if i<len(a):
        out+=a[i]
    if i<len(b):
        out+=b[i]
    i+=1
print(out)


  

    

        
       


                                                              
         

        
            



 

      
        
                    

            










    
