
cities = ("Mumbai", "Pune", "Nashik", "Delhi", "Hyderabad")

print("1. Cities:", cities)



print("\n2. First City:", cities[0])
print("Last City:", cities[-1])


print("\n3. Last City using Negative Index:", cities[-1])



print("\n4. Middle Three Cities:", cities[1:4])


empty_tuple = ()

print("\n5. Empty Tuple:", empty_tuple)


single = ("Python",)

print("\n6. Single Element Tuple:", single)
print("Type:", type(single))


#
student = ("Arshil", 20, 89.5, "Nashik")

print("\n7. Student Details")
print(student)



nested = (
    ("Rahul", 90),
    ("Sneha", 95),
    ("Amit", 85)
)

print("\n8. Nested Tuple")
print(nested)

print("Access Inner Element:", nested[1][0])   # Sneha



numbers = (10, 20, 30)

# Uncomment to see the error
# numbers[0] = 100

print("\n9. Tuples are Immutable")
print("numbers =", numbers)
print("Trying numbers[0]=100 gives TypeError")



languages = ["Python", "Java", "C", "C++"]

language_tuple = tuple(languages)

print("\n10. List:", languages)
print("Tuple:", language_tuple)



tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

result = tuple1 + tuple2

print("\n11. Concatenated Tuple:", result)



colors = ("Red", "Green")

print("\n12. Repeated Tuple")
print(colors * 4)



languages = ("Python", "Java", "C++", "Go")

print("\n13. Check Element")

if "Python" in languages:
    print("Python Exists")
else:
    print("Python Not Found")



print("\n14. Using For Loop")

for city in cities:
    print(city)



print("\n15. Using While Loop")

i = 0

while i < len(cities):
    print(cities[i])
    i += 1



marks = (85, 92, 78, 65, 99)

print("\n16. Student Marks:", marks)

print("Maximum:", max(marks))
print("Minimum:", min(marks))
print("Total:", sum(marks))
print("Average:", sum(marks) / len(marks))



prices = (150, 200, 300, 450, 250)

print("\n17. Product Prices:", prices)

print("Total Bill:", sum(prices))



roles = ("Admin", "Manager", "HR", "Employee")

user_role = "Manager"

print("\n18. User Role Check")

if user_role in roles:
    print(user_role, "is a Valid Role")
else:
    print(user_role, "is Not Valid")


# ==========================================
# MINI PROJECT
# Employee Salary Report
# ==========================================

employees = (
    ("Rahul", 50000),
    ("Amit", 65000),
    ("Sneha", 72000),
    ("Pooja", 58000)
)

print("\n===============================")
print(" Employee Salary Report")
print("===============================")

# 1. Print Employee Name and Salary
print("\nEmployee Details")

for name, salary in employees:
    print(name, ":", salary)

# 2. Create Tuple of Salaries
salaries = tuple(salary for name, salary in employees)

print("\nSalary Tuple")
print(salaries)

# 3. Salary Statistics
print("\nHighest Salary :", max(salaries))
print("Lowest Salary  :", min(salaries))
print("Total Salary   :", sum(salaries))
print("Average Salary :", sum(salaries) / len(salaries))




import sys


fruits = ("Apple", "Banana", "Mango", "Apple", "Orange", "Apple")

print("1. Fruits:", fruits)
print("Apple appears:", fruits.count("Apple"), "times")



print("\n2. Index of Mango:", fruits.index("Mango"))



numbers = (5, 10, 20, 5, 30, 40, 5, 50)

print("\n3. Numbers:", numbers)
print("5 appears:", numbers.count(5), "times")



colors = ("Red", "Green", "Blue")

print("\n4. Finding Index of Yellow")

try:
    print(colors.index("Yellow"))
except ValueError:
    print("Error: tuple.index(x): x not in tuple")


employees = ("Rahul", "Amit", "Sneha", "Pooja", "Kiran")

employee = input("\nEnter Employee Name: ")

if employee in employees:
    print(employee, "Found at Index:", employees.index(employee))
else:
    print(employee, "Not Found")



list_data = [10, 20, 30, 40, 50]
tuple_data = (10, 20, 30, 40, 50)

print("\n6. Memory Comparison")
print("List Memory :", sys.getsizeof(list_data), "bytes")
print("Tuple Memory:", sys.getsizeof(tuple_data), "bytes")



months = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
)

print("\n7. Index of July:", months.index("July"))



marks = (
    85,
    90,
    85,
    78,
    90,
    85
)

print("\n=================================")
print("    Student Result Analysis")
print("=================================")

# 1. Count 85
print("\n1. 85 appears:", marks.count(85), "times")

# 2. Index of first 90
print("2. First Index of 90:", marks.index(90))

# 3. Total number of marks
print("3. Total Elements:", len(marks))

# 4. Maximum, Minimum and Average
print("4. Maximum Marks:", max(marks))
print("   Minimum Marks:", min(marks))
print("   Average Marks:", sum(marks) / len(marks))