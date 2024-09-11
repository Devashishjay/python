# ---------------------------------- List in Python ----------------------------------------

#A build-in data type that stores set of values.
#It can store elements of different types(integer,float,string,etc)
#It is a collection of Homo,Hetrogenius data inside square braces[ ].

# Homogeneous list- a list contains same kind od individual values,
#  Example-   a=[1,2,3,4,5] => all are integers

# a=[1,2,3]
# print(type(a))   

# output- <class 'list'>          

#Hetrogeneous list- a collection contains mixture of different kind of values
# are known as hetrogeneous list.
#Example- a=[1,5,9,"Hello",3+5j] 

# a=[1,5,9,"Hello",3+5j]
# print(type(a))

# output= <class 'list'>

#Nature of list- List is a collection whose nature is mutable,where you can adddata
#,rowdata or update data.


#----------------------------- List Method -------------------------------------------
#1)Append Method- add one element at the end

# list= [1,2,3]
# list.append(4)
# print(list)

# output= [1, 2, 3, 4]

# 2)Sort Method- Sorts in ascending order

# list= [8,4,9,3,6,2,5]
# list.sort()
# print(list)

# Output= [2, 3, 4, 5, 6, 8, 9]


#3)list.sort(reverse=True) Method- Sorts in decending order.

# list= [8,4,9,3,6,2,5]

# list.sort(reverse=True)
# print(list)

# output= [9, 8, 6, 5, 4, 3, 2]


#4) Reverse Method- Reverses list

# list=[1,2,3,4,5,6,7,8,9,]
# list.reverse()
# print(list)

# output= [9, 8, 7, 6, 5, 4, 3, 2, 1]


#5) Insert Method- Insert element at index   list.insert(idx,el).

# list=[6,3,8,9,0,2,1]
# list.insert(2,5)
# print(list)

# output= [6, 3, 5, 8, 9, 0, 2, 1]

#6) Remove Method- removes first occurrence of element

# list=[2,3,4,5]
# list.remove(4)
# print(list)

# output= [2, 3, 5]  ye element ko he hata deta hai jo v element ka naam likho

#7) POP Method - Removes element at index.

# list=[6,7,3,9,8,5]
# list.pop(2)
# print(list)

# output= [6, 7, 9, 8, 5]

python documentation







