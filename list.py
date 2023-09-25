list1=[1,2,3,4,5,"apple"]
list2=[10]
list1.append("orange")
list1.remove(list1[1])
list1.extend(list2)
list1[0],list1[4]=list1[4],list1[0]
for i in range(len(list1)):
    print(list1[i])
