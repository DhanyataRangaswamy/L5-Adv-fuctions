s1={1,2,3,4}
s2={2,4,6,8}
s3=list(zip(s1,s2))
print(s3)

list1=[100,200,300]
list2=[1,2,3]
for x,y in zip(list1,list2[::-1]):
    print(x,y)

stocks=['relience','infosys','tcs']
price=[1000,2500,3000]
new_dict={stocks:price for stocks,price in zip(stocks,price)}
print('\n{}'.format(new_dict))
