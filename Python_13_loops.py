# '''
# In Python, loops are used to execute a block of code repeatedly. 
# The two main types of loops in Python are the `for` loop and the `while` loop. 
# '''

# '''
# 1. for Loop:
# The `for` loop is used to iterate over a sequence (such as a list, tuple, string, or range) or any iterable object.
# '''


# # Example 1: Iterate over a list
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# # Output:
# # apple
# # banana
# # cherry





# # Example 2: Iterate over a string
# for char in "Python":
#     print(char)

# # Output:
# # P
# # y
# # t
# # h
# # o
# # n

# # Example 3: Iterate over a range of numbers
# for i in range(5):
#     print(i)

# # Output:
# # 0
# # 1
# # 2
# # 3
# # 4


# '''

# 2. while Loop:
#    The `while` loop is used to repeatedly execute a block of code as long as a specified condition is true.
# '''

# # Example: Print numbers from 1 to 5 using a while loop
# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# # Output:
# # 1
# # 2
# # 3
# # 4
# # 5
 
'''
3. Loop Control Statements:
   Python also provides loop control statements like `break`, `continue`, and `pass` to modify the behavior of loops.
'''

# Example: Use of break and continue in a loop
for i in range(1, 11):
    if i == 5:
        break  # Exit the loop when i equals 5
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)

# Output:
# 1
# 3
