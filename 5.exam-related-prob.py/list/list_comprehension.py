#print 10 number in a list
lst =[x for x in range(10)]
print(lst)

lst = [x for x in range(1, 11)]
print(lst)

#get the square of a list of number
my_num =[10, 20]
lst = [x**2 for x in my_num]
print(lst)


#print the square of 10 numbers
squares = [x**2 for x in range(10)]

#get the only odd number from a list
myLst =[1,3,6,8,9,2,3,6]
lst =[x for x in myLst if x%2 !=0]
print(lst)


#get the max of odd number from a list 
lst = [2,4,5,8,3,0,8,12,3,56,78]
new_list = max([x for x in lst if x%2!=0])
print(new_list)