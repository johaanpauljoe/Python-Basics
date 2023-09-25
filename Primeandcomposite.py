a=int(input("Enter a no"))
flag=False
if(a==1):
    print("Np nor c")
elif(a>1):
    for i in range(2,a):
        if(a%i==0):
            #print("Composite")
            flag=True
            break
        #else:
           # print("prime")
           # break
    if flag:
        print("composite")
    else:
        print("Prime")
