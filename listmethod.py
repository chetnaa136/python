l=[1,2,3,4,5]
# adds single element at the last
l.append(9)
print(l)
# clears out all the elements in the list 
# print(l.clear())
# copy the elements in another list
x=l.copy()
print(x)
print(l)
# agr double underscore se start hogi toh usko magic method 
print(id(x))
print(id(l))
print(id(x)==id(l))
# copy is used for creating another object of same element i.e. same content but different addresses
# count
# used to find the frequency of a particular element in the list
a=[1,2,3,2,4,2,3]
print(l.count(3))
print(a.count(2))
# extend
# adds multiple elements at last
# takes only single argument i.e u can add another list 
l1=[1,2,3]
l.extend(l1)
print(l)
l1.extend(l)
print(l1)
# index
# index returns int thats why we can directly return it.
print(l.index(2))
# insert
# Syntax:collection.insert(position,element)
l.insert(0,'jai')
l.insert(3,'chetna')
print(l)
#pop removes the last element
print(l.pop())
print(l)
# remove
# remove removes a particular element
print(l.remove('jai'))
print(l)
# reverse
print(l.reverse())
print(l)
# sort
# print(l.sort())
# print(l)
l2=[1,3,5,2,4,8,9,5]
print(l2.sort())
print(l2)
# to print in reverse order
l2.sort(reverse=True)
print(l2)