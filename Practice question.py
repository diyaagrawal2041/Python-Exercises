mystr=[54,84,2,14,20]
print("original list is: ",mystr)
mystr.sort()
print("sorted list is: ",mystr)
mystr.reverse()
print("reversed list is: ",mystr)
a1 = {"A": "Pink","B": "Red", "C":"Blue"}
a1["F"]="Purple"
a1["G"]="Green"
print("a1 dictionary= ",a1)
del a1["F"]
print("a1 dictionary after deletion: ",a1)
a2=a1.copy()
print("a2 dictionary: ",a2)
del a2["B"]
print("a2 dictionary after deletion: ",a2)
a1.update({"D":"White","E":"Black"})
print ("a1 dictionary after update: ",a1)


