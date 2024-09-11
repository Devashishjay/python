#----------------------------------------- Functions in python--------------------------------------

# Block of statements that perform a specific task.
#Function is a block of code which takes input as parameter and returns output.

#                          _______________
#                         |              |
#         input      -->  |              | --> output
#         parameter       |______________|
# syntax=

# def func_name(param1,param2..):       #Function defination
#     some work
#     return val 

# func_name(arg1,arg2..)                #function call

# Example=lets make a function to do addition of any two numbers

# def calc_sum(a,b):              #Function defination
#     sum=a+b
#     print(sum)
#     return sum



# suppose if i have to do addition of 10 and 20

# a=10
# b=20

# sum=a+b
# print(sum)

# so it will give 30 as output, but we dont have to do addition like this our code become very long
# .so as a shortcut or to do this whole thing in a single line we use function.
# We simply call our function to do addition 

# example

# calc_sum(10,20)       #and here 10 and 20 are arguments which is geting stored in parameter a,b of our function

# output=30


# example2

# calc_sum(2000,3000)

# output=5000

# example3

# calc_sum(70,90)

# output=160

#So this was few sum example that we seen in function,we can do the sum of any numbers in a single line of code.
#What are the steps we have to follow
# 1) We maked our function to do addition of any numbers

# def calc_sum(a,b):               #Function defination
#     sum=a+b
#     print(sum)
#     return sum

# 2) Then we simply called it, whenever we have to do addition of two numbers
# 3) By the help of "calc_sum(a,b)"
# 4) In 'a' we writtten our first number and in 'b' in writen our 2nd number, which we have to add
# 5) We got our output.
# Important note-we make our function so that we can do redundancy of our code
#Redundancy(unnecessary jyada lamba aur complex dikhne wala code line ko kum karna).

# In summarised way we can write this same function in short way also. 

# Example=

# def calc_sum(a,b):
#     return a+b                      #This is my function defination

# sum = calc_sum(1,2)                 # Here we called our function
# print(sum)

# sum= calc_sum(900,600)               # Here we called our function
# print(sum)

# outputs=3        # for (1,3)
#         1500     #for(900,600)


#--------------------------------------Now we will see some more easy function

# Like if we have to print "hello" ,and we want to call it whenever you have to print "hello"
# So here we will see it,

# def print_hello():                #Function Defination
#     print("Hello")


# print_hello()                      #Function call
# print_hello()
# print_hello()
# print_hello()
# print_hello()
# print_hello()

# output=Hello, is printed 6 times
# Note=as many time we call our this function "print_hello" , Hello will print in output
# We can make function without parameters also,means it will not give any output.
#Just like this print function

# def print_hello():               # Not have any parameters
#     print("Hello")              


#------------------------------------------------- Average of 3 numbers

# def calc_average(a,b,c):                               #Function Defination
#     sum=a+b+c
#     average=sum/3
#     print(average)
#     return(average) 

# Function Calls...........

# calc_average(1,2,3)                                   #Function  Calls
# calc_average(56,78,67)
# calc_average(500,400,800)
# calc_average(40000,60009,4356)



#-------------------------------------- Types of Function --------------------------------------

###############################3 1) Built-in Functions                    
                                       
#  > print()             #we can hover to this function to see how it is defined                    
#  > len()
#  > type()
#  > range()

# Built it functions are the functions which is already written in python like the examples above
# and we are using it frequently also

#Example=
# print("Dev Ashish Jay")        #this print we are using always is a function call,which is inbuilt in python
                               #and "Dev ashish jay" which i am written is a argument which is
                               #storing under defination of print function.

#Note- Seperator(" ",)=   It seperates the string,It is done by giving coma(,) after any string
#                        ,Like 
# 
# print("Dev Ashish","is a good boy","and handsome also")  
#  Output=Dev Ashish is a good boy and handsome also  

#print("Dev Ashish",             "is a good boy",          "and handsome also.") 
#Ouput=Dev Ashish is a good boy and handsome also.

# Example1)
# print("Dev Ashish Jay", end=" ") 
# print("He is a good boy")

# Output=Dev Ashish Jay He is a good boy

#Example2)
# print("Dev Ashish Jay", end="$") 
# print("He is a good boy")

# Output=Dev Ashish Jay$He is a good boy   #we can anything inside ("")


# Example3)
# print("Dev Ashish Jay", end="\n")         #\n means line break 
# print("It is a good boy")

# Output=Dev Ashish Jay
#        It is a good boy


####################################### 2)User defined Function

# Functions which we make to perform some task after calling it are user defined function.
#This are not inbuilt.



#------------------------------------- Default Parameter----------------------------------------

# Assigning a default value to parameter,which is used when no argument is passed.

# Example=

# def calc_product(a=8,b=9):
#     print(a*b)
#     return a*b


# calc_product()                        Output=72
# calc_product()                        Output=72
# calc_product()                           "
# calc_product()                           "
# calc_product()                           "


# if we will not assign anything in "a" it will assume "a" as 1 and it will multiply 1 by value of b.
#But we have to assign some value in "b" 
#If we will assign some value in "a" and we will not assign some value in "b" it will show error.
#mtlb shuru m jo hai usme kuch nii v denge toh chalega lekin uske baad wale ko value dena he hoga.these is the rule.



#----------------------------------------------- Questions --------------------------------------------------------

#Question) Write a function to print length of a list.(list is the parameter).

# cities=["ranchi","dhanbad","Bokaro","japan","sahibganj"]
# cricketers=["dhoni sir","viru","chicku","jaddu","gautam sir coach","Dev Ashish Jay"]

# def calc_length(list):                      #function defination
#     print(len(list))


# calc_length(cities)                       #output=5                 #function call
# calc_length(cricketers)                   #output=6


#Question) Write a function to print the element of a list in a single line.(list is the parameter)

# cricketers=["dhoni sir","viru","chicku","jaddu","gautam sir coach","Dev Ashish Jay"]

# def calc_element(list):                            #function defination
#     for item in list:
#         print(item,end=" ")


# calc_element(cricketers)                            #function call

# output=dhoni sir viru chicku jaddu gautam sir coach Dev Ashish Jay 


# Question) write a function to find the factorial of n.(n is the parameter)


# def calc_factorial(n):
#     factorial=1
#     for i in range(1,n+1):
#         factorial*=i
#     print(factorial)


# calc_factorial(5)

# output=120

# question) write a function to convert USD to INR.

# def calc_converter(usd_value):                             #Function Defination
#     inr_value=usd_value*83
#     print(usd_value,"USD=", inr_value,"INR")


# calc_converter(61.91)                                  #Function call
    

# Quesrtion= Write a function which takes input fron user and if the input is even number
#            print "EVEN" and if the input is odd number print "ODD"


# number=int(input("Enter a number: "))       #function defination
# def calc_function(n):
#     if n%2==0:
#         print("EVEN")
#     else:
#         print("ODD")


# calc_function(10)                         #function call




#------------------------------------ Recursion-----------------------------------------

# When a function calls itself repeatedly
#jo sara kaam loop se kiya jaata hai wo recursion se v kr sakte hai
#Aur jo kaam recursion se kiya jaata hai wo loops se v kr sakte hai
#bss kuch cases m hm loops ko prefare karte hai,jo begineers level k codeing hote usme maximim. 
#aur baad m agar data algo sikhne nikle toh usme kuch cases honge jisme recursion simple code deega as compare to loops. 

# Example= 

# def show(n):                          Recursion defination
#     if(n==0):        #base case
#         return
#     print(n)
#     show(n-1)



# show(9)                                #Recursion call

# output=it will print 1 to 9 in reverse order
#here we can see that "n==0" it means n zero k brabar hai
#but we called function inside our function only by using 'n-1' and this is working like a loop
#It means that we have to move from 0 to 9 because at last we used "n-1" means we have to move backward


#Jb hm ek function k upar dusre functions ko ek pe ek add krte hai toh usko functions ka stack kehte hai 





a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

sum=(a+b)
print(sum)

sub=(a-b)
print(sub)

mul=(a*b)
print(mul)





















    



