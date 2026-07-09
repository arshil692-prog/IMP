# ==========================================
# PYTHON COMPLETE EXAMPLE
# ==========================================

# -------------------------------
# 1. INPUT FUNCTION
# -------------------------------

name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))
salary = float(input("Enter Your Salary: "))

print("\n----- User Information -----")
print("Name:", name)
print("Age:", age)
print("Salary:", salary)

# -------------------------------
# 2. MULTIPLE INPUT
# -------------------------------

city, state = input("\nEnter City and State: ").split()

print("City:", city)
print("State:", state)

# Multiple Integer Input

a, b, c = map(int, input("\nEnter Three Numbers: ").split())

print("Addition:", a + b + c)

# -------------------------------
# 3. PRINT MULTIPLE VALUES
# -------------------------------

print("\n----- Print Multiple Values -----")

print(name, age, city)

print("Python", "Java", "C++")

print("2026", "07", "09", sep="-")

print("Hello", end=" ")
print("World")

# -------------------------------
# 4. ESCAPE CHARACTERS
# -------------------------------

print("\n----- Escape Characters -----")

print("Hello\nWorld")

print("Python\tJava\tC++")

print("C:\\Users\\Arshil")

print("He said \"Hello\"")

print('It\'s Python')

# -------------------------------
# 5. TYPE CASTING / TYPE CONVERSION
# -------------------------------

print("\n----- Type Casting -----")

num = "100"

integer_value = int(num)

float_value = float(num)

string_value = str(integer_value)

boolean_value = bool(integer_value)

print(integer_value)
print(float_value)
print(string_value)
print(boolean_value)

# Implicit Type Casting

x = 10
y = 5.5

print("\nImplicit Type Casting")

print(x + y)

# -------------------------------
# 6. TYPE CONVERSION FUNCTIONS
# -------------------------------

print("\n----- Type Conversion Functions -----")

print(int("25"))

print(float("25"))

print(str(500))

print(bool(1))

print(bool(0))

print(list("Python"))

print(tuple([10,20,30]))

print(set([1,2,2,3,3,4]))

data = [("Name","Arshil"),("Age",21)]

print(dict(data))

# -------------------------------
# 7. STRING FORMATTING
# -------------------------------

print("\n----- String Formatting -----")

# Method 1

print("Name:", name)

# Method 2

print("My Name is %s" % name)

# Method 3

print("My Name is {}".format(name))

print("Name: {} Age: {}".format(name, age))

# Method 4 (Recommended)

print(f"My name is {name}")

print(f"I am {age} years old")

print(f"My salary is {salary}")

# Decimal Formatting

pi = 3.1415926535

print(f"PI Value = {pi:.2f}")

# Alignment

print(f"{'Python':<15}")

print(f"{'Python':>15}")

print(f"{'Python':^15}")

# -------------------------------
# 8. TYPE CHECKING
# -------------------------------

print("\n----- Type Checking -----")

print(type(name))
print(type(age))
print(type(salary))
print(type(integer_value))
print(type(float_value))
print(type(boolean_value))

# -------------------------------
# END
# -------------------------------

print("\nProgram Finished Successfully")