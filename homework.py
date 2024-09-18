list1=[1,2,3,4,5,6,7,8,9,10,12,13]
print("The list is: ")
print(list1)

even=[x for x in list1 if x%2==0]
print("The list of even numbers is: ")
print(even)

odd=[x for x in list1 if x%2!=0]
print("The list of odd numbers is: ")
print(odd)


