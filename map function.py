num1=[1,2,3]
num2=[4,5,6]
result=map(lambda x,y:x+y , num1 , num2)
print("The sum of the lists is: ")
print(list(result))

num=[1,2,3,4,5]
def square(n):
    return n*n
    
result1=list(map(square,num))
print("The square of the numbers are: ")
print(result1)
