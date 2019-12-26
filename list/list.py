
"""
 PYTHON COLLECTION OF (ARRAY)
    this are the four collection date types in the python programming language:
    > list: is a collection which is ordered and changeable allows duplication  members
    > Tuple is a collection which is ordered and unchangeable . Allow duplication members

    >set is collection which is unordered and unindeed . No duplication members
    >Dictionary is collection which is unordered and changeable
"""
thislist = ["apple","banana","cherry"]
print(thislist)

# access Items
print(thislist[1])

#change item value
thislist[2] = "blackberry"
print(thislist[2])

#loop through list
for x in thislist:
    print(x)

#list lenght
print(len(thislist))

#add item
thislist.append("Orange")
print(thislist)


thislist.insert(1, "orange")
print(thislist)

# remove items
thislist.remove("banana")
print(thislist)

#Copy list
"""
You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2."""

mylist = thislist.copy()
print(mylist)

# another way of making copy is to use the built in method list()

mylist = list(thislist)
print(mylist)

"""
 it is also pissble to make new list by using 
 list constarctor
 
"""
thislist = list(("apple", "banna", "Cherry"))# note the double round- brackets

print(thislist)
