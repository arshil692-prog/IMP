a = 15
b = 4

print("----------------------------")
print("Arithmetic Operators: ")
print("----------------------------")

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b) 

#comparision operators

print("----------------------------")
print("Comparison Operators: ") 
print("----------------------------")


print(5 == 5)
print(10 != 20)
print(15 > 10)
print(5 < 10)
print(15 >= 15)
print(5 <= 10)


print("----------------------------")
print("Logical Operators: ")
print("----------------------------")


print(5 > 3 and 10 > 5)
print(5 > 3 or 10 < 5)
print(not(5 > 3 and 10 > 5))


# ============================================
# 1. IDENTITY OPERATORS
# ============================================

print("===== Identity Operators =====")

a = [10, 20, 30]
b = a
c = [10, 20, 30]

print("a:", a)
print("b:", b)
print("c:", c)

print("a is b =", a is b)          # True
print("a is c =", a is c)          # False
print("a == c =", a == c)          # True
print("a is not c =", a is not c)  # True


# ============================================
# 2. LOGICAL OPERATORS
# ============================================

print("\n===== Logical Operators =====")

age = 20
citizen = True

print("Age >=18 and Citizen =", age >= 18 and citizen)

marks = 45
sports_quota = True

print("Marks >=50 or Sports Quota =", marks >= 50 or sports_quota)

logged_in = False

print("Not Logged In =", not logged_in)


# ============================================
# 3. MEMBERSHIP OPERATORS
# ============================================

print("\n===== Membership Operators =====")

fruits = ["Apple", "Banana", "Mango"]

print("Banana in fruits =", "Banana" in fruits)
print("Orange not in fruits =", "Orange" not in fruits)

text = "Python Programming"

print("'Python' in text =", "Python" in text)

student = {
    "name": "John",
    "age": 20
}

print("'name' in student =", "name" in student)
print("'John' in student =", "John" in student)


# ============================================
# 4. ASSIGNMENT OPERATORS
# ============================================

print("\n===== Assignment Operators =====")

x = 10
print("Initial x =", x)

x += 5
print("After += 5 :", x)

x -= 3
print("After -= 3 :", x)

x *= 2
print("After *= 2 :", x)

x /= 4
print("After /= 4 :", x)

x //= 2
print("After //= 2 :", x)

x %= 3
print("After %= 3 :", x)

x **= 2
print("After **= 2 :", x)


# ============================================
# 5. REAL LIFE EXAMPLE
# ============================================

print("\n===== Real Life Example =====")

users = ["Alice", "Bob", "Charlie"]

username = "Alice"
logged_in = True

if username in users and logged_in:
    print("Access Granted")
else:
    print("Access Denied")

# --------------------------------------------
# PYTHON BITWISE OPERATORS - COMPLETE PROGRAM
# --------------------------------------------

# Taking Input
a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))

print("\n-------- BITWISE OPERATORS --------\n")

# Bitwise AND
print("1. Bitwise AND (&)")
print(f"{a} & {b} = {a & b}")
print()

# Bitwise OR
print("2. Bitwise OR (|)")
print(f"{a} | {b} = {a | b}")
print()

# Bitwise XOR
print("3. Bitwise XOR (^)")
print(f"{a} ^ {b} = {a ^ b}")
print()

# Bitwise NOT
print("4. Bitwise NOT (~)")
print(f"~{a} = {~a}")
print(f"~{b} = {~b}")
print()

# Left Shift
print("5. Left Shift (<<)")
print(f"{a} << 1 = {a << 1}")
print(f"{a} << 2 = {a << 2}")
print(f"{b} << 1 = {b << 1}")
print(f"{b} << 2 = {b << 2}")
print()

# Right Shift
print("6. Right Shift (>>)")
print(f"{a} >> 1 = {a >> 1}")
print(f"{a} >> 2 = {a >> 2}")
print(f"{b} >> 1 = {b >> 1}")
print(f"{b} >> 2 = {b >> 2}")