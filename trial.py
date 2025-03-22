"""
Create an empty list called my_list.
Append the following elements to my_list: 10, 20, 30, 40.
Insert the value 15 at the second position in the list.
Extend my_list with another list: [50, 60, 70].
Remove the last element from my_list.
Sort my_list in ascending order.
Find and print the index of the value 30 in my_list.
"""
#note -> append only adds an element to a list at the end of the list and is only added one at a time

#emty list 
my_list = []
print(my_list)
#append elements to an array
my_list.append(10)
my_list.append(20)
my_list.append(30)
print(my_list)
#insert 15 at the second position
my_list.insert(1, 15)
print(my_list)
#extend my_list with another list
my_list2 = [50, 60, 70]
my_list.extend(my_list2)
print(my_list)
#remove the last element
my_list.pop()
print(my_list)
#sort my_list in ascending order
my_list.sort()
print(my_list)

# #descending 
# my_list.sort(reverse = 1) #reverse value 1 means true boolean value
# print(my_list)

# Find and print the index of the value 30 in my_list.

find_30 = my_list.index(30)
print(find_30)