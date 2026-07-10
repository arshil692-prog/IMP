
# PYTHON LOOP ASSIGNMENTS


print("\n========== Assignment 1 : range() ==========\n")

# Q1
print("Q1")
for i in range(1, 21):
    print(i)

# Q2
print("\nQ2")
for i in range(20, 0, -1):
    print(i)

# Q3
print("\nQ3")
for i in range(2, 51, 2):
    print(i)

# Q4
print("\nQ4")
for i in range(1, 51, 2):
    print(i)

# Q5
print("\nQ5")
for i in range(1, 11):
    print(f"7 x {i} = {7*i}")

# Q6
print("\nQ6")
for i in range(100, 0, -10):
    print(i)

# Q7
print("\nQ7")
for i in range(5, 101, 5):
    print(i)

# ==========================================

print("\n========== Assignment 2 : for Loop ==========\n")

# Q1
print("Q1")
for i in range(10):
    print("Arshil")

# Q2
print("\nQ2")
for i in range(1, 101):
    print(i)

# Q3
print("\nQ3")
for i in range(1, 11):
    print(i, i**2)

# Q4
print("\nQ4")
for i in range(1, 11):
    print(i, i**3)

# Q5
print("\nQ5")
total = 0
for i in range(1, 101):
    total += i
print("Sum =", total)

# Q6
print("\nQ6")
count = 0
for i in range(1, 51):
    if i % 3 == 0:
        count += 1
print(count)

# Q7
print("\nQ7")
for i in range(10, 0, -1):
    print(i)

# Q8
print("\nQ8")
text = "FutureBright"
for ch in text:
    if ch.lower() in "aeiou":
        print(ch)

# Q9
print("\nQ9")
numbers = [25,67,12,98,45]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(largest)

# Q10
print("\nQ10")
marks = [45,78,90,34,88,51]

count = 0
for mark in marks:
    if mark > 50:
        count += 1

print(count)

# ==========================================

print("\n========== Assignment 3 : while Loop ==========\n")

# Q1
print("Q1")
i = 1
while i <= 20:
    print(i)
    i += 1

# Q2
print("\nQ2")
i = 20
while i >= 1:
    print(i)
    i -= 1

# Q3
print("\nQ3")
i = 2
while i <= 50:
    print(i)
    i += 2

# Q4
print("\nQ4")
i = 1
while i <= 10:
    print(f"9 x {i} = {9*i}")
    i += 1

# Q5
print("\nQ5")
i = 10
while i <= 100:
    print(i)
    i += 10

# Q6
print("\nQ6")
i = 10
while i >= 1:
    print(i)
    i -= 1
print("Happy New Year!")

# Q7
print("\nQ7")
balance = 5000
while balance > 0:
    print("Balance =", balance)
    balance -= 500
print("Balance = 0")

# Q8
print("\nQ8")
# password=""
# while password!="python123":
#     password=input("Enter Password : ")
# print("Access Granted")

# ==========================================

print("\n========== Assignment 4 : Lists ==========\n")

marks = [78,56,89,91,45,62,98]

# Q1
print("Q1")
for i in marks:
    print(i)

# Q2
print("\nQ2")
print(sum(marks))

# Q3
print("\nQ3")
print(sum(marks)/len(marks))

# Q4
print("\nQ4")
count = 0
for i in marks:
    if i > 75:
        count += 1
print(count)

# Q5
print("\nQ5")
for i in marks:
    if i % 2 == 0:
        print(i)

# Q6
print("\nQ6")
for i in marks:
    if i % 2 != 0:
        print(i)

# Q7
print("\nQ7")
print(max(marks))

# Q8
print("\nQ8")
print(min(marks))

# Q9
print("\nQ9")
count = 0
for i in marks:
    if i < 50:
        count += 1
print(count)

# Q10
print("\nQ10")
for i in marks:
    if i >= 90:
        grade = "A"
    elif i >= 75:
        grade = "B"
    elif i >= 50:
        grade = "C"
    else:
        grade = "Fail"

    print(i, "->", grade)

# ==========================================

print("\n========== Assignment 5 : Nested Loop ==========\n")

# Q1
print("Q1")
for i in range(4):
    for j in range(4):
        print("*", end=" ")
    print()

# Q2
print("\nQ2")
for i in range(1,6):
    for j in range(i):
        print("*", end=" ")
    print()

# Q3
print("\nQ3")
for i in range(5,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()

# Q4
print("\nQ4")
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

# Q5
print("\nQ5")
for i in range(1,6):
    for j in range(1,6):
        print(i*j,end="\t")
    print()

# Q6
print("\nQ6")
shirts = ["Red","Blue","Black"]
pants = ["Jeans","Formal"]

for s in shirts:
    for p in pants:
        print(s,"-",p)

# Q7
print("\nQ7")
for row in range(1,4):
    for seat in range(1,6):
        print("Row",row,"Seat",seat)

# ==========================================

print("\n========== Assignment 6 : Mixed ==========\n")

# Q1
print("Q1")
numbers=[12,-5,18,-20,34,-7,0]

positive=0
negative=0

for i in numbers:
    if i>0:
        positive+=1
    elif i<0:
        negative+=1

print("Positive =",positive)
print("Negative =",negative)

# Q2
print("\nQ2")
for i in range(1,101):
    if i%3==0 and i%5==0:
        print(i)

# Q3
print("\nQ3")
num=5
fact=1

for i in range(1,num+1):
    fact*=i

print(fact)

# Q4
print("\nQ4")
text="Python"
reverse=""

for ch in text:
    reverse=ch+reverse

print(reverse)

# Q5
print("\nQ5")
numbers=[12,17,24,31,40,55]

total=0

for i in numbers:
    if i%2==0:
        total+=i

print(total)

# Q6
print("\nQ6")
for i in range(1,6):
    for j in range(i):
        print(i,end=" ")
    print()

# Q7
print("\nQ7")
for i in range(5):
    for j in range(i+1):
        print(chr(65+j),end=" ")
    print()

# Q8
print("\nQ8")
numbers=[2,5,7,2,9,5,10]

for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i]==numbers[j]:
            print(numbers[i])

# Q9
print("\nQ9")
prices=[120,450,99,250,180]

total=0

for price in prices:
    print(price)
    total+=price

print("Total =",total)

# Q10
print("\nQ10")
attendance=["Present","Absent","Present","Present","Absent"]

present=0
absent=0

for i in attendance:
    if i=="Present":
        present+=1
    else:
        absent+=1

print("Present =",present)
print("Absent =",absent)

print("\n========== END ==========")