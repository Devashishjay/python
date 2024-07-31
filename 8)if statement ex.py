# if 5>2:
#     print("Greater")

# if 5<2:
#         print("Greater")

# yenha hm lg clearly dekh sakte hai agar 5>2 hai toh condition true hai,aur jo print wala part hai wo exicute ho jayega

# ,wanhi 5<2 kiye toh code exicute nii ho raha hai kuki ye false hai

# aur indent v maintaid krna jruri hai means print se pehle 4 space dena must h(vs code m ye khud ho jaata hai python m)

# example-
# if 5>2:
# print("Greater")

# space nii diye hai print se pehle to exicute nii ho rha hai error aa rha hai

# if 5>2:print("Greater")
# ye single line m v exicute hoga,lekin bs ek he print hona chaiye.if 5>2:print("Greater") print("jai mata ki"),aisa chij ni exicute hoga.
# multiple statement k liye nii h,single statement hai toh esko ek line m likh sakte h


# if 5>2:
#     print("Greater")
# print("rest of the code")

# yenha pe greater aur rest of the code uske baad print ho rha hai,greater pehle print ho rha kuki condition true h

# if 5<2:
#     print("Greater")
# print("rest of the code")

# here condition is false essiliye greater nii print ho rhi

# if 5>2:
#     print("Greater")
#     print("5 is greater than 2")
# print("rest of the code")

# yenha ek se jyada statement ka example h condition true hai toh serial wise code exicute ho rha.
# agar false rehta toh bss rest of the code wala part exicute hota.


# Ab dekhte hai user se input leke kaise hm aisa program bna sakte hai.lets see with exaple,aur user se input lene k liye input use krte hai

a=int(input("Enter number greater than 2:"))
if(a>2):
    print("you have entered", a)
print("2 se kum type kro yaar")

    # int use krna hoga input se pehle nii toh wo string samjhega aur error dega.soo int function se input ko inclose krna hota h




