
empty_list = []


students = ["Arshil", "Ayan", "Rahul", "Priya", "Sneha"]


marks = [85, 90, 78, 88, 95]


my_details = ["Arshil", 20, "Nashik", 89.5]


matrix = [
    [1, 2],
    [3, 4]
]


print("Empty List:", empty_list)
print("Student Names:", students)
print("Marks:", marks)
print("My Details:", my_details)
print("2x2 Matrix:", matrix)


print("\nLength of Empty List:", len(empty_list))
print("Number of Students:", len(students))
print("Number of Marks:", len(marks))
print("Length of My Details List:", len(my_details))
print("Rows in Matrix:", len(matrix))


languages = ["Python", "Java", "C", "C++", "JavaScript"]

print("Favorite Programming Languages:", languages)
print("Number of Programming Languages:", len(languages))


cities = ["Mumbai", "Pune", "Nashik", "Delhi", "Hyderabad"]

print("Cities List:", cities)


print("Third City:", cities[2])


print("Last City:", cities[-1])


print("First Four Cities:", cities[:4])


print("Reversed List:", cities[::-1])


print("Every Second City:", cities[::2])


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("3x3 Matrix:")
print(matrix)

# Print the center element
print("Center Element:", matrix[1][1])



list1 = [10, 20, 30]
list2 = list1      # Both variables refer to the same list

list2.append(40)

print("\nUsing Assignment")
print("list1:", list1)
print("list2:", list2)

# Copy
list3 = [100, 200, 300]
list4 = list3.copy()   # Creates a separate copy

list4.append(400)

print("\nUsing copy()")
print("list3:", list3)
print("list4:", list4)

# ==========================================
# LIST UPDATE ASSIGNMENT
# ==========================================


numbers = [10, 20, 30, 40, 50]

print("1. Before Update:", numbers)

numbers[2] = 99

print("After Update:", numbers)


cities = ["Mumbai", "Pune", "Nashik"]

print("\n2. Before Append:", cities)

cities.append("Delhi")

print("After Append:", cities)



students = ["Rahul", "Sneha", "Aman"]

print("\n3. Before Insert:", students)

students.insert(1, "Arshil")

print("After Insert:", students)



list1 = [1, 2, 3]
list2 = [4, 5, 6]

print("\n4. Before Extend:", list1)

list1.extend(list2)

print("After Extend:", list1)



fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

print("\n5. Before Slice Assignment:", fruits)

fruits[-2:] = ["Kiwi", "Pineapple"]

print("After Slice Assignment:", fruits)


cart = ["Milk", "Bread", "Eggs"]

print("\n6. Before Insert:", cart)

cart.insert(0, "Butter")

print("After Insert:", cart)




# append()
list_a = [10, 20, 30]
list_a.append([1, 2])

print("\n7. Using append():")
print(list_a)

# extend()
list_b = [10, 20, 30]
list_b.extend([1, 2])

print("\nUsing extend():")
print(list_b)



employee_list1 = ["Rahul", "Aman", "Sneha"]
employee_list2 = ["Priya", "Rohan", "Kiran"]

employee_list1.extend(employee_list2)

print("\n8. Merged Employee List:")
print(employee_list1)


# ==========================================
# 9. MINI PROJECT
# Student Management System
# ==========================================

students = []

while True:

    print("\n==============================")
    print(" Student Management System")
    print("==============================")
    print("1. Add Student")
    print("2. Insert Student")
    print("3. Update Student")
    print("4. Display Students")
    print("5. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        name = input("Enter Student Name: ")
        students.append(name)
        print("Student Added Successfully!")

    elif choice == 2:
        index = int(input("Enter Index: "))
        name = input("Enter Student Name: ")
        students.insert(index, name)
        print("Student Inserted Successfully!")

    elif choice == 3:
        index = int(input("Enter Index to Update: "))

        if index >= 0 and index < len(students):
            new_name = input("Enter New Student Name: ")
            students[index] = new_name
            print("Student Updated Successfully!")
        else:
            print("Invalid Index!")

    elif choice == 4:

        if len(students) == 0:
            print("No Students Available.")
        else:
            print("\nStudent List")
            for i in range(len(students)):
                print(i, ":", students[i])

    elif choice == 5:
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Please Try Again.")


        # ==========================================
# LIST DELETE OPERATIONS
# ==========================================

# ------------------------------------------
# 1. Remove "Banana" from a list of fruits
# ------------------------------------------
fruits = ["Apple", "Banana", "Mango", "Orange"]

print("1. Before Remove:", fruits)

fruits.remove("Banana")

print("After Remove:", fruits)


# ------------------------------------------
# 2. Remove the last element using pop()
# ------------------------------------------
numbers = [10, 20, 30, 40, 50]

print("\n2. Before Pop:", numbers)

numbers.pop()

print("After Pop:", numbers)


# ------------------------------------------
# 3. Store the removed value from pop()
# ------------------------------------------
marks = [85, 90, 75, 60]

print("\n3. Before Pop:", marks)

removed = marks.pop()

print("Removed Value:", removed)
print("Updated List:", marks)


# ------------------------------------------
# 4. Delete the third element using del
# ------------------------------------------
cities = ["Mumbai", "Pune", "Nashik", "Delhi", "Goa"]

print("\n4. Before del:", cities)

del cities[2]

print("After del:", cities)


# ------------------------------------------
# 5. Delete elements from index 2 to 5
# ------------------------------------------
numbers = [10, 20, 30, 40, 50, 60, 70]

print("\n5. Before Slice Delete:", numbers)

del numbers[2:6]

print("After Slice Delete:", numbers)


# ------------------------------------------
# 6. Empty a list using clear()
# ------------------------------------------
languages = ["Python", "Java", "C", "C++"]

print("\n6. Before clear():", languages)

languages.clear()

print("After clear():", languages)


# ------------------------------------------
# 7. Difference between clear() and del
# ------------------------------------------

# clear()
list1 = [1, 2, 3]

print("\n7. clear() Example")
print("Before:", list1)

list1.clear()

print("After:", list1)


# del
list2 = [10, 20, 30]

print("\ndel Example")
print("Before:", list2)

del list2

# Uncomment the line below to see the error
# print(list2)

print("After del: Variable Deleted")


# ------------------------------------------
# 8. Remove first occurrence of duplicate value
# ------------------------------------------
values = [10, 20, 30, 20, 40, 20]

print("\n8. Before:", values)

values.remove(20)

print("After Removing First 20:", values)


# ==========================================
# MINI PROJECT
# TO-DO LIST MANAGER
# ==========================================

tasks = []

while True:

    print("\n==========================")
    print("      TO-DO LIST")
    print("==========================")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Remove Last Task")
    print("4. Display Tasks")
    print("5. Clear All Tasks")
    print("6. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        task = input("Enter Task: ")
        tasks.append(task)
        print("Task Added Successfully!")

    elif choice == 2:
        task = input("Enter Task to Remove: ")

        if task in tasks:
            tasks.remove(task)
            print("Task Removed Successfully!")
        else:
            print("Task Not Found!")

    elif choice == 3:

        if len(tasks) > 0:
            removed = tasks.pop()
            print("Removed Task:", removed)
        else:
            print("Task List is Empty!")

    elif choice == 4:

        if len(tasks) == 0:
            print("No Tasks Available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    elif choice == 5:
        tasks.clear()
        print("All Tasks Cleared!")

    elif choice == 6:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")



        # ==========================================
# LIST SEARCHING & CALCULATIONS
# ==========================================

# ------------------------------------------
# 1. Find the length of a list
# ------------------------------------------
numbers = [10, 20, 30, 40, 50]

print("1. List:", numbers)
print("Length of List:", len(numbers))


# ------------------------------------------
# 2. Count how many times 10 appears
# ------------------------------------------
numbers = [10, 20, 10, 30, 10, 40, 10]

print("\n2. List:", numbers)
print("10 appears", numbers.count(10), "times")


# ------------------------------------------
# 3. Find the index of "Python"
# ------------------------------------------
languages = ["Java", "Python", "C", "C++", "JavaScript"]

print("\n3. Languages:", languages)
print("Index of Python:", languages.index("Python"))


# ------------------------------------------
# 4. Check if "Java" exists using in
# ------------------------------------------
languages = ["Python", "Java", "C++", "Go"]

print("\n4. Languages:", languages)

if "Java" in languages:
    print("Java exists in the list.")
else:
    print("Java does not exist.")


# ==========================================
# INTERMEDIATE
# ==========================================

# ------------------------------------------
# 5. Find the maximum and minimum marks
# ------------------------------------------
marks = [85, 92, 76, 68, 95, 81]

print("\n5. Marks:", marks)
print("Maximum Marks:", max(marks))
print("Minimum Marks:", min(marks))


# ------------------------------------------
# 6. Calculate the total salary of employees
# ------------------------------------------
salary = [25000, 30000, 28000, 35000, 40000]

print("\n6. Employee Salaries:", salary)
print("Total Salary:", sum(salary))


# ------------------------------------------
# 7. Calculate the average temperature of a week
# ------------------------------------------
temperature = [30, 32, 31, 29, 33, 34, 30]

print("\n7. Weekly Temperature:", temperature)

total = sum(temperature)
average = total / len(temperature)

print("Total Temperature:", total)
print("Average Temperature:", average)


# ------------------------------------------
# 8. Count how many 'Present' values exist
# ------------------------------------------
attendance = [
    "Present",
    "Absent",
    "Present",
    "Present",
    "Absent",
    "Present",
    "Present"
]

print("\n8. Attendance:", attendance)
print("Total Present:", attendance.count("Present"))


# ==========================================
# LIST SORTING
# ==========================================

# ------------------------------------------
# 1. Sort a list of integers in ascending order
# ------------------------------------------
numbers = [45, 12, 78, 23, 5]

print("1. Original List:", numbers)

numbers.sort()

print("Ascending Order:", numbers)


# ------------------------------------------
# 2. Sort a list in descending order
# ------------------------------------------
numbers = [45, 12, 78, 23, 5]

print("\n2. Original List:", numbers)

numbers.sort(reverse=True)

print("Descending Order:", numbers)


# ------------------------------------------
# 3. Reverse a list using reverse()
# ------------------------------------------
numbers = [10, 20, 30, 40, 50]

print("\n3. Before Reverse:", numbers)

numbers.reverse()

print("After reverse():", numbers)


# ------------------------------------------
# 4. Reverse a list using reversed()
# ------------------------------------------
numbers = [10, 20, 30, 40, 50]

print("\n4. Original List:", numbers)

reverse_list = list(reversed(numbers))

print("Using reversed():", reverse_list)

print("Original List:", numbers)


# ==========================================
# INTERMEDIATE
# ==========================================

# ------------------------------------------
# 5. Sort a list of names alphabetically
# ------------------------------------------
names = ["Rahul", "Aman", "Sneha", "Arshil", "Priya"]

print("\n5. Before Sorting:", names)

names.sort()

print("Alphabetical Order:", names)


# ------------------------------------------
# 6. Sort words by their length
# ------------------------------------------
words = ["Python", "C", "Java", "JavaScript", "Go"]

print("\n6. Original Words:", words)

words.sort(key=len)

print("Sorted by Length:", words)


# ------------------------------------------
# 7. Sort names ignoring case
# ------------------------------------------
names = ["rahul", "Aman", "sneha", "Arshil", "priya"]

print("\n7. Original:", names)

names.sort(key=str.lower)

print("Case-Insensitive Sort:", names)


# ------------------------------------------
# 8. Difference between sort() and sorted()
# ------------------------------------------
numbers = [50, 20, 40, 10, 30]

print("\n8. Original List:", numbers)

sorted_list = sorted(numbers)

print("sorted() Result:", sorted_list)
print("Original List:", numbers)

numbers.sort()

print("sort() Result:", numbers)


# ==========================================
# LIST TRAVERSING
# ==========================================

# ------------------------------------------
# 9. Print all elements using for loop
# ------------------------------------------
numbers = [10, 20, 30, 40, 50]

print("\n9. Using For Loop")

for num in numbers:
    print(num)


# ------------------------------------------
# 10. Print all elements using while loop
# ------------------------------------------
numbers = [10, 20, 30, 40, 50]

print("\n10. Using While Loop")

i = 0

while i < len(numbers):
    print(numbers[i])
    i += 1


# ------------------------------------------
# 11. Display index and value using enumerate()
# ------------------------------------------
cities = ["Mumbai", "Pune", "Nashik", "Delhi"]

print("\n11. Using enumerate()")

for index, city in enumerate(cities):
    print(index, ":", city)


# ------------------------------------------
# 12. Print the square of every number
# ------------------------------------------
numbers = [1, 2, 3, 4, 5]

print("\n12. Squares")

for num in numbers:
    print(num, "=", num ** 2)


# ==========================================
# INTERMEDIATE
# ==========================================

# ------------------------------------------
# 13. Print student names with marks using zip()
# ------------------------------------------
students = ["Rahul", "Sneha", "Arshil", "Priya"]
marks = [85, 90, 95, 80]

print("\n13. Students and Marks")

for name, mark in zip(students, marks):
    print(name, ":", mark)


# ------------------------------------------
# 14. Print all elements of a 3×3 nested list
# ------------------------------------------
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("\n14. Matrix Elements")

for row in matrix:
    for value in row:
        print(value, end=" ")
    print()


# ------------------------------------------
# 15. Calculate the sum of each row
# ------------------------------------------
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print("\n15. Sum of Each Row")

for row in matrix:
    print("Row:", row, "Sum =", sum(row))


# ------------------------------------------
# 16. Print only even numbers
# ------------------------------------------
numbers = [11, 22, 33, 44, 55, 66, 77, 88]

print("\n16. Even Numbers")

for num in numbers:
    if num % 2 == 0:
        print(num)



        # ==========================================
# LIST COMPREHENSION
# ==========================================

# ------------------------------------------
# 1. Create a list containing "Pass" or "Fail"
# ------------------------------------------
marks = [85, 45, 72, 30, 90, 55]

result = ["Pass" if mark >= 35 else "Fail" for mark in marks]

print("1. Marks:", marks)
print("Result:", result)


# ------------------------------------------
# 2. Create a list containing "Even" or "Odd"
# ------------------------------------------
numbers = list(range(1, 21))

even_odd = ["Even" if num % 2 == 0 else "Odd" for num in numbers]

print("\n2. Numbers:", numbers)
print("Even/Odd:", even_odd)


# ------------------------------------------
# 3. Convert words longer than 4 characters
# ------------------------------------------
words = ["python", "java", "go", "apple", "cat", "computer"]

new_words = [word.upper() if len(word) > 4 else word.lower() for word in words]

print("\n3. Original Words:", words)
print("Updated Words:", new_words)


# ------------------------------------------
# 4. Replace negative numbers with 0
# ------------------------------------------
numbers = [10, -5, 20, -15, 30, -1]

positive = [num if num >= 0 else 0 for num in numbers]

print("\n4. Original:", numbers)
print("Updated:", positive)


# ==========================================
# INTERMEDIATE
# ==========================================

# ------------------------------------------
# 5. Flatten a matrix
# ------------------------------------------
matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

flat = [value for row in matrix for value in row]

print("\n5. Flatten Matrix")
print(flat)


# ------------------------------------------
# 6. Remove None while flattening
# ------------------------------------------
nested = [
    [1, None],
    [2, 3],
    [None, 4],
    [5, None]
]

flat = [value for row in nested for value in row if value is not None]

print("\n6. Remove None")
print(flat)


# ------------------------------------------
# 7. Create a 4×4 matrix filled with 1s
# ------------------------------------------
matrix = [[1 for j in range(4)] for i in range(4)]

print("\n7. 4x4 Matrix")

for row in matrix:
    print(row)


# ------------------------------------------
# 8. Temperature Status
# ------------------------------------------
temperature = [25, 30, 35, 28, 40, 29, 32]

status = ["Hot" if temp >= 30 else "Normal" for temp in temperature]

print("\n8. Temperature:", temperature)
print("Status:", status)


# ==========================================
# MINI PROJECT
# Employee List Comprehension
# ==========================================

employees = [
    ("Rahul", 45000),
    ("Amit", 62000),
    ("Sneha", 75000),
    ("Pooja", 39000)
]

# Employee Names
employee_names = [name for name, salary in employees]

# Salaries
employee_salaries = [salary for name, salary in employees]

# Tax Applicable
tax = [
    "Tax Applicable" if salary > 50000 else "No Tax"
    for name, salary in employees
]

# Salary with Bonus
bonus_salary = [salary + 5000 for name, salary in employees]

print("\n========= Employee Details =========")

print("Employee Names:")
print(employee_names)

print("\nEmployee Salaries:")
print(employee_salaries)

print("\nTax Status:")
print(tax)

print("\nSalary After Bonus:")
print(bonus_salary)