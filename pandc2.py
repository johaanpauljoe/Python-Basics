a=int(input("Enter a no"))
flag=1
if(a==1):
    print("Np nor c")
elif(a>1):
    for i in range(2,a):
        if(a%i==0):
            #print("Composite")
            flag=2
            break
        #else:
           # print("prime")
           # break
    if flag==2:
        print("composite")
    else:
        print("Prime")
