s=set()                     #empty set
s=set([1,5,3,8,4])          #adding elements from list
print("s: ",s)
s.add(9)
s.add(5)                    #adding elements in the set
print("s after adding elements: ",s)

s1=s.union({2,4,6,8})
print('UNION')
print("s1: ",s1)
s2=s.intersection({1,5,3})
print("INTERSECTION")
print("s2: ",s2)
s3={0,6}
print("DISJOINT")
print(s.isdisjoint(s3))
s.remove(5)
print("s after removing 5: ",s)
