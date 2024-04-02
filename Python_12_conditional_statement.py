'''
Conditional statements in Python allow you to execute different blocks of code based on whether a certain condition is true or false. The primary conditional statements in Python are `if`, `elif` (short for "else if"), and `else`. Here's an overview of how they work:

1. **if Statement:**
   The `if` statement is used to execute a block of code if a specified condition is true.
'''

x = 1
if x > 5:
    print("x is greater than 5")


'''
2. **if...else Statement:**
   The `if...else` statement allows you to execute one block of code if the condition is true, and another block of code if the condition is false.
'''
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")


'''
3. **if...elif...else Statement:**
   The `if...elif...else` statement allows you to test multiple conditions and execute a block of code corresponding to the first true condition. You can have multiple `elif` blocks, but only one `else` block (if needed).
'''
x = 10
if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is equal to 10")
else:
    print("x is less than 10")

'''
4. **Nested if Statements:**
   You can also nest `if` statements within other `if`, `elif`, or `else` blocks to create more complex conditional logic.
'''
x = 10
if x > 5:
    print("x is greater than 5")
    if x == 10:
        print("x is equal to 10")

'''
5. **Ternary Conditional Operator:**
   Python also supports a shorter form of the `if...else` statement known as the ternary conditional operator, which is used to assign a value to a variable based on a condition.
'''

x = 2
message = "x is greater than 5" if x > 5 else "x is not greater than 5"
print(message)
