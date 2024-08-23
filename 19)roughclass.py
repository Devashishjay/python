# write a program to check string is palindrom using looping
# a="nayan"
# out=''
# i=len(a)-1
# while i>=0:
#     out+=a[i]
#     i-=1
#     if a==out:
#         print('pallindron')
#     else:
#         print("not pallidron")


# a='aaabcbbcc'
# op='a3b1c2b2c2'

a='aaabcbbcc'
out=''
i=0
while i<len(a)-1:
    if a [i]==a[i+1]:
      c+=1
    else:
     out+=a[i]+str(c)
     c=1
    i+=1
out+=a[-1]+str(c)
print(out)
    
        