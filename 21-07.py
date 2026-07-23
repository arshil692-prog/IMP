# basic 
# 1///
fruits = {"apple","mango","banana","orange"}
print(fruits)

# 2///
fruits1 = {"apple","mango","banana","orange"}
print("origanal",fruits1)
fruits.add("apple")
print("duplicate",(fruits))

# 3///
set1 = set()
print(type(set1))

#4///
num1 = [1,2,3,4,5]
print("orignal list",num1)
set_num = set(num1)
print("set",set_num)

# 5///
# print(fruits[1])
#TypeError: 'set' object is not subscriptable


# intermediate
# 6///
student = {"arshil","rehan","fazal","vahid","aliyan"}
print("student set;",student)
print(len(student))

#7///
city = {"nashik","niphad","puna","jalgaon"}
if "puna" in city:
    print("city find")
else:
    print("city Not find")

# 8///
#num3 = {11,[22],33}
#print(num3)
#TypeError: unhashable type: 'list'


# mini challenge
#9///
registrations = [
    "Rahul",
    "Amit",
    "Rahul",
    "Sneha",
    "Pooja",
    "Amit",
    "Rahul"
]
# 1. Convert the list into a set
unique_students = set(registrations)
# 2. Print all unique student names
print("Unique Student Names:")
print(unique_students)
# 3. Print the total number of unique students
print("\nTotal Unique Students:", len(unique_students))
# 4. Check whether "Sneha" is registered
if "Sneha" in unique_students:
    print("\nSneha is registered.")
else:
    print("\nSneha is not registered.")
# 5. Display the original list count versus the unique student count
print("\nOriginal Student Count:", len(registrations))
print("Unique Student Count:", len(unique_students))


# set questions (10)
# level 1 
# 1///
student_ids = [101,102,103,102,104,101,105,106,105]
unique_students_ids = set(student_ids)
print("unique student ids:",unique_students_ids)


#2///
student1 = {"Python","sql","Java","c++"}
print("student1 know:",student1)
student2 = {"Python","JavaScript","sql","html"}
print("student2 know:",student2)
print("commen subject student knows:",student1.intersection(student2))


#3///
print("subject known by student1:",student1.symmetric_difference(student2))


#4///
backend = {"Python","Django","sql"}
print("backend skills:",backend)
frontend = {"html","css","JavaScript"}
print("frondend skills:",frontend)
print("combine skiils:",backend.union(frontend))


# lvel 2
# 5///
Company_A = {"Rahul","Sneha","Amit","Pooja"}
Company_B = {"Amit","Pooja","Rohan","Karan"}
both_selected = Company_A.intersection(Company_B)
only_company_A = Company_A.difference(Company_B)
only_company_B = Company_B.difference(Company_A)
total_selected = Company_A.union(Company_B)
print("student selected in both companys:")
print(both_selected)
print("\nstudent selected in company A:")
print(only_company_A)
print("\nstudent selected in company B:")
print(only_company_B)
print("\ntotal student selected in both company:")
print(total_selected)
print("\ntotal unique student selcted :")
print(len(total_selected))

#6///

sentence = "python is easy and python is powerful"

banned = {"is","and"}

words = sentence.split()

for word in words:
    if word not in  banned:
        print(word, end = " ")
        
# 7///
required = {"Python","SQL"}

candidate = {"Python","SQL","Pandas","NumPy"}
if required.issubset(candidate):
    print("candidate  satisfy required with all skills:")
else:
    print("Candidate does not satisfy all required skills:")


# 8///
store1 = {"rohan","arshil","rehan","fazal"}
store2 = {"arshil","rehan","fazal","ali"}
store3 = {"fazal","arshil","rehan","rohan"}
commen = store1.intersection(store2,store3)
print("commen visitor is:",commen)

# 9///
user_A = {"avengers","godfather","king","doomslayes"}
user_B = {"tiger3","sikender","king"}
recommend_movie = user_A.difference(user_B)
print("recommend movies:",recommend_movie)

# 10///
numbers = [1,2,3,4,2,1,5,3,6,7,8,9,10]

unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
print("original list",numbers)
print("list without duplicates",unique)

# dictionary questions (15)
# level 1
# 1///
students = {
    "Rahul":85,
    "Amit":72,
    "Sneha":94,
    "Pooja":67
}
print("students scoring above 80:")
for name,marks in students.items():
    if marks > 80:
        print(name,":",marks)
    
# 2///
# 2.1
students = {
    "Rahul":85,
    "Amit":72,
    "Sneha":94,
    "Pooja":67
}
for name,marks in students.items():
    if marks > 80:
        print("higgest marks",name,marks)
    elif marks > 50:
        print("average marks",name,marks)
    elif marks > 30:
        print("lowest marks",name,marks)    
    else:
        print("fail ",name,marks)

# 2.2
students = {
    "Rahul": 85,
    "Amit": 72,
    "Sneha": 94,
    "Pooja": 67
}

marks = students.values()

print("Highest Marks :", max(marks))
print("Lowest Marks  :", min(marks))
print("Average Marks :", sum(marks) / len(marks))

# 3///
word = "programming"
frequnacy = {}
for ch in word:
    if ch in frequnacy:
        frequnacy [ch] += 1
    else :
        frequnacy [ch] = 1
        print(frequnacy)

# 4///
sentence = "python is easy python is powerful"

words = sentence.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print(frequency)


#5///
data = {
    "A": 1,
    "B": 2,
    "C": 3
}

reverse = {}

for key, value in data.items():
    reverse[value] = key

print(reverse)

# 7///
phonebook = {}

while True:

    print("\n1 Add Contact")
    print("2 Delete Contact")
    print("3 Search Contact")
    print("4 Update Contact")
    print("5 Display")
    print("6 Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        name = input("Enter Name: ")
        number = input("Enter Number: ")

        phonebook[name] = number

    elif choice == 2:
        name = input("Enter Name: ")

        if name in phonebook:
            del phonebook[name]

    elif choice == 3:
        name = input("Enter Name: ")

        if name in phonebook:
            print(phonebook[name])
        else:
            print("Contact Not Found")

    elif choice == 4:
        name = input("Enter Name: ")

        if name in phonebook:
            phonebook[name] = input("Enter New Number: ")

    elif choice == 5:
        print(phonebook)

    elif choice == 6:
        break


# 8///
employees = {
    "Rahul": {"Salary": 70000, "Department": "HR"},
    "Amit": {"Salary": 55000, "Department": "IT"},
    "Sneha": {"Salary": 90000, "Department": "Finance"},
    "Pooja": {"Salary": 45000, "Department": "Admin"}
}

print("Employees earning above ₹60,000\n")

for name, details in employees.items():

    if details["Salary"] > 60000:

        print(name)

        print("Salary:", details["Salary"])

        print("Department:", details["Department"])

        print()


# 9///
dict1 = {
    "A": 1,
    "B": 2
}

dict2 = {
    "C": 3,
    "D": 4
}

dict1.update(dict2)

print(dict1)

# 10 ///
students = {
    "Rahul": "Python",
    "Amit": "Python",
    "Sneha": "Java",
    "Pooja": "Java"
}

group = {}

for name, course in students.items():

    if course not in group:
        group[course] = []

    group[course].append(name)

print(group)

# 11 ///
votes = {}

while True:

    candidate = input("Vote (type Exit to stop): ")

    if candidate.lower() == "exit":
        break

    if candidate in votes:
        votes[candidate] += 1
    else:
        votes[candidate] = 1

print("\nResult")

for name, count in votes.items():
    print(name, ":", count)



# 12///
library = {
    "Python": 5,
    "Java": 4,
    "SQL": 3
}

while True:

    print("\n1 Issue")
    print("2 Return")
    print("3 Display")
    print("4 Exit")

    ch = int(input("Choice: "))

    if ch == 1:

        book = input("Book Name: ")

        if book in library and library[book] > 0:
            library[book] -= 1

    elif ch == 2:

        book = input("Book Name: ")

        if book in library:
            library[book] += 1

    elif ch == 3:

        print(library)

    elif ch == 4:
        break

# 15 ///
employees = {
    "Rahul": 70000,
    "Amit": 55000,
    "Sneha": 90000,
    "Pooja": 45000,
    "Rohan": 80000
}

salaries = list(employees.values())

salaries.sort(reverse=True)

second = salaries[1]

for name, salary in employees.items():

    if salary == second:

        print("Second Highest Salary")

        print(name, ":", salary)

# arrray questions (10)
# 1 ///
from array import array

numbers = array('i', [10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("Array:", numbers)

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))
print("Average:", sum(numbers) / len(numbers))

# 2///
from array import array

numbers = array('i', [10, 20, 30, 40, 50])

element = int(input("Enter element to search: "))

if element in numbers:
    print("Index:", numbers.index(element))
else:
    print("Element not found")

# 3///
from array import array

numbers = array('i', [10, 20, 30, 40, 50])

reverse_array = array('i')

for i in range(len(numbers)-1, -1, -1):
    reverse_array.append(numbers[i])

print("Original Array:", numbers)
print("Reversed Array:", reverse_array)

# 4///
from array import array

numbers = array('i', [10, 21, 35, 44, 56, 77])

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even Numbers:", even)
print("Odd Numbers:", odd)


# 5///
from array import array

numbers = array('i', [10, 20, 30, 20, 40, 20])

delete_num = int(input("Enter number to delete: "))

new_array = array('i')

for num in numbers:
    if num != delete_num:
        new_array.append(num)

print("Updated Array:", new_array)

# 6///
from array import array

numbers = array('i', [10, 20, 90, 40, 70])

largest = max(numbers)

second = numbers[0]

for num in numbers:

    if num != largest and num > second:
        second = num

print("Second Largest:", second)

# 7///
from array import array

array1 = array('i', [10, 20, 30])

array2 = array('i', [40, 50, 60])

merged = array('i')

merged.extend(array1)
merged.extend(array2)

print("Merged Array:", merged)

# 8///
from array import array

months = [
    "Jan","Feb","Mar","Apr",
    "May","Jun","Jul","Aug",
    "Sep","Oct","Nov","Dec"
]

sales = array('i', [
    12000,
    15000,
    18000,
    20000,
    25000,
    30000,
    28000,
    27000,
    32000,
    29000,
    31000,
    35000
])

highest = max(sales)

lowest = min(sales)

average = sum(sales) / len(sales)

total = sum(sales)

index = sales.index(highest)

print("Highest Sale:", highest)

print("Lowest Sale:", lowest)

print("Average Sale:", average)

print("Month with Highest Sale:", months[index])

print("Total Annual Sales:", total)

# no 9,8