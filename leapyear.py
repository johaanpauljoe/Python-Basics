def year(a):
    if(a%4==0 and a%100!=0) or (a%400==0):
        return "Leap Year"
    else:
        return "Not a leap year"
    

a=int(input("Enter a year"))
b=year(a)
print(b)
