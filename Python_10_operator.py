# Operations in Python
'''
operation symbols for each category of operators in Python:
1. **Arithmetic Operators:**
   - Addition: `+`
   - Subtraction: `-`
   - Multiplication: `*`
   - Division: `/`
   - Modulus: `%`
   - Exponentiation: `**`
   - Floor Division: `//`

2. **Assignment Operators:**
   - Assignment: `=`
   - Addition Assignment: `+=`
   - Subtraction Assignment: `-=`
   - Multiplication Assignment: `*=`
   - Division Assignment: `/=`
   - Modulus Assignment: `%=`
   - Exponentiation Assignment: `**=`
   - Floor Division Assignment: `//=`

3. **Comparison Operators:**
   - Equal to: `==`
   - Not equal to: `!=`
   - Greater than: `>`
   - Less than: `<`
   - Greater than or equal to: `>=`
   - Less than or equal to: `<=`

4. **Logical Operators:**
   - Logical AND: `and`
   - Logical OR: `or`
   - Logical NOT: `not`

5. **Identity Operators:**
   - Identity equality: `is`
   - Identity inequality: `is not`

6. **Membership Operators:**
   - Membership: `in`
   - Negated membership: `not in`

7. **Bitwise Operators:**
   - Bitwise AND: `&`
   - Bitwise OR: `|`
   - Bitwise XOR: `^`
   - Bitwise NOT: `~`
   - Left shift: `<<`
   - Right shift: `>>`

'''
'''
1. **Arithmetic Operators:**
   - Addition: `+`
   - Subtraction: `-`
   - Multiplication: `*`
   - Division: `/`
   - Modulus: `%`
   - Exponentiation: `**`
   - Floor Division: `//`
'''
# 5+10 = 15
x = 5 + 10
print(5 + 10)
print(5 - 10)
print(5 / 10)
print(5 % 10)
print(5 ** 10) # 5*5*5*5.. 10 times
print(5 // 10)

'''
2. **Assignment Operators:**
   - Assignment: `=`
   - Addition Assignment: `+=` x = x+5 | x +=5
   - Subtraction Assignment: `-=`
   - Multiplication Assignment: `*=`
   - Division Assignment: `/=`
   - Modulus Assignment: `%=`
   - Exponentiation Assignment: `**=`
   - Floor Division Assignment: `//=`
'''

x =10
x = x+ 5 # x += 5
print(x) #15




'''
3. **Comparison Operators:**
   - Equal to: `==`
   - Not equal to: `!=`
   - Greater than: `>`
   - Less than: `<`
   - Greater than or equal to: `>=`
   - Less than or equal to: `<=`
'''
print("---------")
print( 10 == 5) # False
print( 10 != 5) # True
print( 10 > 5)  # True
print( 10 < 5)  # False
print( 10 >= 5) # True
print( 10 <= 5) # False

'''
4. **Logical Operators:**
   - Logical AND: `and`
   - Logical OR: `or`
   - Logical NOT: `not`
'''

print( 10 != 5 and 10 > 5) #True
print( 10 != 5 or 10 > 5) #True
print(not (10 != 5 or 10 > 5)) # False