# Q1 create an empty list called my_list
my_list = []
print(my_list)

# Q2 append the following elements to my_list: 10, 20, 30, 40.
my_list.append([10, 20, 30, 40])
print(my_list)

# Q3 insert the value 15 at the second position in the list
my_list.insert(len(my_list),15 )
print(my_list)

# Q4 extend my list with another list [50, 60 , 70]
my_list.extend([50, 60, 70])
print(my_list)

# Q5 remove the last element from my list
my_list.pop()
print(my_list)

# Q6 sort my list in assending order
filtered_list = [item for item in my_list if isinstance(item, int)]
filtered_list.sort()
print(filtered_list)

# Q7 Find and point the index 30 in my list
try:
    index_of_30 = my_list.index(30)
    print(f"The index of 30 is: {index_of_30}")
except ValueError:
    print("30 is not in the list.")