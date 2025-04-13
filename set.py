# s={10,20,20,10,'neeraj',30,10,30}
# print(s)
# inbuilt functions
# print(len(s))
# l={10,20,30,10,20,30}
# print(max(l))
# print(min(l))
# print(sum(l))
# print(type(l))
# print(id(l))
# methods in set 
# s.add('ok')
# print(s)
# s.update(1,2,3) this code will get error because
# for using update,the arguements that are passed must be iterable i,e. they must be a collection.
# s.update('ijh','dfg')
# print(s)
# l1=[23,45,7]
# l2=[67,99,87]
# s.update(l1,l2)
# s.update([23,3,45,55],[56,34,78])
# print(s)
# pop removes any element randomly from the set
# s.pop()
# print(s)
# print(s.pop())
# never use pop for set,we use remove in general
# s.remove('neeraj')
# print(s)
# s.remove('Neeraj')
# if the element is not in the set then remove givrs keyerror,better method is discard
# s.discard('Neeraj')
# if element is not in the set,discard doesnt throw keyerror
# s1=s.copy()
# print(s)
# print(s1)
# print(id(s))
# print(id(s1))
# s.clear()
# print(s)
# printing empty set
# x=set()
# print(x)
# print(type(x))
# union is returning a new set
# s1={1,2,3,4,5,6}
# s2={4,5,6,7,8,9}
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.difference(s2))
# print(s2.difference(s1))
# print(s2.symmetric_difference(s1))
# s1.intersection_update(s2)
# print(s1)
# s1.difference_update(s2)
# print(s1)
# s1.symmetric_difference_update(s2)
# print(s1)
# print(s1.isdisjoint(s2))
# l1={1,2,3}
# l2={4,5,6}
# print(l1.isdisjoint(l2))
# s1={1,2,3,4,5,6}
# s2={4,5,6}
# print(s1.issubset(s2))
# print(s2.issubset(s1))
# print(s1.issuperset(s2))

