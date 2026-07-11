text = "Python Programming"

print("Original String:", text)

# 1. Indexing
print("\n1. Indexing")
print(text[0])      # P
print(text[3])      # h
print(text[-1])     # g

# 2. Slicing
print("\n2. Slicing")
print(text[0:6])    # Python
print(text[7:])     # Programming
print(text[:6])     # Python
print(text[::2])    # Every second character
print(text[::-1])   # Reverse string

# 3. split()
print("\n3. split()")
fruits = "Apple,Mango,Banana,Grapes"
print(fruits.split(","))

# 4. strip()
print("\n4. strip()")
name = "   Muktar   "
print(name.strip())

# 5. replace()
print("\n5. replace()")
print(text.replace("Python", "Java"))
