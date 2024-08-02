#if elif statement
# a=10
# b=20
# if a>b:
#     print("a is greater than b")
# elif a<b:
#     print("a is smaller than b")
# elif a==b:
#     print("a is equal to b")

#means elif ka use multiple decisions k liye krte h,mtlb if agar false hua toh elif m jayega wo elif false hua toh dusra elif m jayega aise krte krte saara conditions jo v ho sakta h usko likh lenge
#aur jo condition true ho ga wo run kr jayega,janha true mill gya wanha stop ho jayega

#ab iss chij ko user se input le k karte h  (baad ka task home work)

#ab iss m if elif else statement krte(kuch change ni hua h bss else aa gya aur else ka mtlb toh pta he hai tumko,false aane pe jo chij run karwana chahte ho wo likha)
#example

# day="Friday"
# if day=="monday":
#     print("Today is monday")
# elif day=="Tuesday":
#     print("Today is tuesday")
# elif day=="Wednesday":
#     print("Today is Wednesday")
# else:
#     print("Today is holiday")

    #jub saare if and elif false ho jayenge tb ye else wala result dega

#ab esko user se input le k sikhte h..saara code same rahega bss input daalne ka jarurat h

day=input("Enter Day: ")
if day=="monday":
    print("Today is monday")
elif day=="Tuesday":
    print("Today is Tuesday")
elif day=="Wednesday":
    print("Today is Wednesday")
else:
    print("Today is holiday")

#yaad rakhe days m capital small letter jaise likha h waise he same lihe nii toh holiday wala dikha dega,aur ye essiliye hota hai kuki python case sensive hota h
#ya ni toh logical operator use kro ex-'if day=="Monday" or day=="monday":' aise or laga k likhne se fir dono run karega  

    










