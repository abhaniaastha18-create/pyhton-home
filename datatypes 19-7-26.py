#collection datatypes
#mutable
#immutable

 #list and tuple (basics & mutablity)
#list_mutable
#fruits=["apple","orange","banana"]
#fruits=[1]="apple"
#print(fruits)

print("-"*20)
print("built-in")
print("-"*20)
number=(10,22,34,56,78)
print(number)
print(len(number))
print(max(number))
print(min(number))
print(sorted(number))
print(type(number))
print(sum(number))

print("-"*20)
print("udf function")
print("-"*20)
def factorial(n):
 if n ==1:
    return 1
 return n *factorial(n-1)


print("-"*20)
print("recursion function")
print("-"*20)


print("-"*20)
print("square list using list comprehension")
print("-"*20)
def square_list(lst):
       return[i**2 for i in lst]
data=[1,2,3,4,5,6]
print(data)
print(square_list(data))


#adding element :
my_list = [10, 20, 30]
my_list.append(40)

print(my_list)

#remove element:
my_list =[10,20,30]
my_list.remove(30)

print(my_list)

#tuples:
 #tuple -immutable
my_tuple = (10, 20, 30)

my_list = list(my_tuple)
my_list[0] = 100
my_list[1] = 100

my_tuple = tuple(my_list)

print(my_tuple)

#collection of data:
#set of data
#type costing constrution and keyword


number=(1,2,3,4,5,6)
print(number)
print(type(number))

list_1=[1,2,3,4,4,6,6,5,5]
set_1=set(list_1)
list_2=list(set_1)
print(set_1)


#union intersection & diffrence:

set_a = {1 , 2 , 3 , 4}
set_b = {3 , 4 , 5 , 6}

print("Union :" , set_a.union(set_b))

print("Intersection :" , set_a.intersection(set_b))

print("Difference:" , set_b.difference(set_a))
