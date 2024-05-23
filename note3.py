'''
This is a note for Module 2 of Python Basics. 
This is a Multi-line String comment. 

LESSON 3: Python Lists
'''
#creating lists
potions = ["Healing", "Invisibility", "Strength", "Healing", "Strength"]
print(potions)

empty_list = []
print(empty_list)

#index helps you access, modify, or remove a list
for i in potions:
    print(i)
print(potions[0])

#a list can include integers, strings, and even other lists
#count method returns number of times an item occurs in a list
#remove method removes the first occurance of an item from a list
#append method adds an item to a list

heal_count = potions.count("Healing")
print(heal_count)

potions.remove(potions[0])
print(potions)

potions.append("Healing")
print(potions)

#insert method adds an item in the middle of the list
potions.insert(0, "Healing")
print(potions)

#modify existing values
potions[0] = "Wisdom"
print(potions)

#.pop() method removes the last item or a specific item by position
potions.pop()
print(potions)

#index and position
position_paint = potions.index("Healing")
print(position_paint)

# .clear() method removes/cleans the method completely

# .sort() method arranges in an alphabethic order

# to find the length of list use -- len()
count = len(potions)
print(count)

# .reverse() method turns the method around

# The built-in methods of list can be found here ---> https://www.w3schools.com/python/python_lists_methods.asp 



#Identity Operators 

# -- 'is' operator
# -- 'is not' operator

# -- 'in' operator
# -- 'not in' operator


# .copy() method creates a new identical list.

# .extend(list) method allows one list to include the items of another list. 

#Joining Strings
# join_s = " "+ join(potions) 

#forms




