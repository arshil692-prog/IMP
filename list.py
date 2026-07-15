# ==========================================
# PYTHON LIST - COMPLETE EXAMPLES
# ==========================================

print("=" * 50)
print("1. CREATING LIST")
print("=" * 50)

# Creating Lists
fruits = ["Apple", "Mango", "Banana"]
numbers = [10, 20, 30, 40]
mixed = ["Arshil", 22, 85.5, True]

print("Fruits :", fruits)
print("Numbers :", numbers)
print("Mixed :", mixed)


print("\n" + "=" * 50)
print("2. ACCESSING LIST ELEMENTS")
print("=" * 50)

print("First Fruit :", fruits[0])
print("Second Fruit :", fruits[1])
print("Last Fruit :", fruits[-1])

print("Slice [0:2] :", fruits[0:2])
print("Slice [1:] :", fruits[1:])
print("Whole List :", fruits[:])


print("\n" + "=" * 50)
print("3. UPDATING LIST")
print("=" * 50)

print("Original :", fruits)

fruits[1] = "Orange"

print("Updated :", fruits)

numbers = [10,20,30,40,50]
numbers[1:4] = [100,200,300]

print("Updated Multiple :", numbers)


print("\n" + "=" * 50)
print("4. APPEND")
print("=" * 50)

colors = ["Red", "Green"]

print("Before :", colors)

colors.append("Blue")

print("After :", colors)


print("\n" + "=" * 50)
print("5. EXTEND")
print("=" * 50)

colors.extend(["Black", "White"])

print(colors)


print("\n" + "=" * 50)
print("6. INSERT")
print("=" * 50)

colors.insert(1, "Yellow")

print(colors)


print("\n" + "=" * 50)
print("7. REMOVE")
print("=" * 50)

colors.remove("Black")

print(colors)


print("\n" + "=" * 50)
print("8. POP")
print("=" * 50)

removed = colors.pop()

print("Removed :", removed)
print("Remaining :", colors)


print("\n" + "=" * 50)
print("9. DEL")
print("=" * 50)

marks = [50,60,70,80]

print("Before :", marks)

del marks[1]

print("After :", marks)


print("\n" + "=" * 50)
print("10. CLEAR")
print("=" * 50)

data = [1,2,3,4]

print("Before :", data)

data.clear()

print("After :", data)


print("\n" + "=" * 50)
print("11. APPEND vs EXTEND")
print("=" * 50)

a = [1,2]

a.append([3,4])

print("append() :", a)

b = [1,2]

b.extend([3,4])

print("extend() :", b)


print("\n" + "=" * 50)
print("12. LIST COMPREHENSION")
print("=" * 50)

numbers = [1,2,3,4,5]

square = [x*x for x in numbers]

print("Squares :", square)


print("\nEven Numbers")

even = [x for x in numbers if x % 2 == 0]

print(even)


print("\nOdd Numbers")

odd = [x for x in numbers if x % 2 != 0]

print(odd)


print("\nNames in Uppercase")

names = ["arshil","rahul","priya"]

upper = [name.upper() for name in names]

print(upper)


print("\n" + "=" * 50)
print("13. SORTING")
print("=" * 50)

numbers = [40,10,90,20,60]

print("Original :", numbers)

numbers.sort()

print("Ascending :", numbers)

numbers.sort(reverse=True)

print("Descending :", numbers)


print("\nUsing sorted()")

numbers = [40,10,90,20]

new_list = sorted(numbers)

print("Original :", numbers)

print("Sorted :", new_list)


print("\n" + "=" * 50)
print("14. FILTERING")
print("=" * 50)

numbers = [10,15,20,25,30,35,40]

even = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)

print("Even :", even)


odd = []

for num in numbers:
    if num % 2 != 0:
        odd.append(num)

print("Odd :", odd)


greater = []

for num in numbers:
    if num > 20:
        greater.append(num)

print("Greater Than 20 :", greater)


print("\nFiltering using List Comprehension")

even = [x for x in numbers if x % 2 == 0]

print(even)

odd = [x for x in numbers if x % 2 != 0]

print(odd)

greater = [x for x in numbers if x > 20]

print(greater)


print("\n" + "=" * 50)
print("15. USEFUL LIST METHODS")
print("=" * 50)

numbers = [5,3,8,2,5,5]

print("List :", numbers)

print("Count of 5 :", numbers.count(5))

print("Index of 8 :", numbers.index(8))

numbers.reverse()

print("Reverse :", numbers)

print("Length :", len(numbers))

print("Maximum :", max(numbers))

print("Minimum :", min(numbers))

print("Sum :", sum(numbers))


print("\n" + "=" * 50)
print("16. ITERATING THROUGH LIST")
print("=" * 50)

fruits = ["Apple","Mango","Banana"]

for fruit in fruits:
    print(fruit)


print("\nUsing Index")

for i in range(len(fruits)):
    print(i, fruits[i])


print("\n" + "=" * 50)
print("17. NESTED LIST")
print("=" * 50)

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix)

print("First Row :", matrix[0])

print("Element :", matrix[1][2])


print("\n" + "=" * 50)
print("18. COPYING LIST")
print("=" * 50)

a = [10,20,30]

b = a.copy()

print(a)

print(b)


print("\n" + "=" * 50)
print("19. CONCATENATION")
print("=" * 50)

a = [1,2]

b = [3,4]

print(a + b)


print("\n" + "=" * 50)
print("20. REPETITION")
print("=" * 50)

print(["Python"] * 5)


print("\n" + "=" * 50)
print("END OF LIST PROGRAM")
print("=" * 50)