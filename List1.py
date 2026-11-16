#creating list 
#syntax
# my_list = ["element1", "element2", "element3", ...]
# print(my_list)

#basic example
# fruits = ["apple", "banana", "cherry"]
# numbers = [1, 2, 3, 4, 5]
# mixed = ["apple", 3, True]
# print(fruits)
# print(numbers)
# print(mixed)

#Accessing the list elements
#syntax
# list_name[index]

#example
# fruits = ["apple", "banana", "cherry"]
# print(fruits[0])  # Output: apple
# print(fruits[2])  # Output: cherry

# # negative indexing 
# print(fruits[-1])  # Output: cherry
# print(fruits[-2])  # Output: banana

#adding the elements
# append() - adds an element to the end of the list
# insert() - adds an element at a specific index
# extend() - adds multiple elements to the end of the list

fruits = ["apple", "banana", "cherry"]
# fruits.append("date")
# print(fruits)  # Output: ["apple", "banana", "cherry", "date"]

# fruits.insert(1, "blueberry")
# print(fruits)  # Output: ["apple", "blueberry", "banana", "cherry", "date"]

# more_fruits = ["grape", "kiwi"]
# fruits.extend(more_fruits)
# print(fruits)  # Output: ["apple", "blueberry", "banana", "cherry", "date", "grape", "kiwi"]

# removing the elements
# remove() - removes a specific element from operator import index

# from the list
# pop() - removes an element at a specific index
# clear() - removes all elements from the list

# fruits.remove("banana")
# print(fruits)  # Output: ["apple", "blueberry", "cherry", "date", "grape", "kiwi"]

# fruits.pop(1)
# print(fruits)  # Output: ["apple", "cherry", "date", "grape", "kiwi"]

# fruits.clear()
# print(fruits)  # Output: []

#slicing lists
#syntax
#list_name[start:stop:step]

# numbers = [0, 1, 2, 3, 4, 5, 6]
# print(numbers[1:4])  # Output: [1, 2, 3] (from index 1 to 3)
# print(numbers[:4])  # Output: [0, 1, 2, 3] (from start to index 3)
# print(numbers[2:5])  # Output: [2, 3, 4] (from index 2 to 4)
# print(numbers[::2])  # Output: [0, 2, 4, 6] (every 2nd element)

# #list function methods
# print(len(fruits))  # Output: 3

# numbers = [5, 2, 9, 1]
# print(sorted(numbers))  # Output: [1, 2, 5, 9]
# print(numbers)  # Original list remains unchanged: [5, 2, 9, 1]

# numbers = [1, 2, 3, 4]
# print(sum(numbers))  # Output: 10



# #common methods
# print(max(numbers))  # Output: 9
# print(fruits.index("apple"))  # Output: 0
# numbers = [1, 2, 3, 1, 1]
# print(numbers.count(1))  # Output: 3
# fruits.reverse()
# print(fruits)  # Output: ['cherry', 'orange', 'apple']
# numbers = [5, 2, 9, 1]
# numbers.sort()
# print(numbers)  # Output: [1, 2, 5, 9]

#Nested list // A nested list contains other list element its called nested list
#examole 
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements in a nested list
print(matrix[0])  # Output: [1, 2, 3] (first row)
print(matrix[1][2])  # Output: 6 (element in the second row, third column)