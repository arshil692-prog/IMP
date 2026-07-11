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
# 6. find()
print("\n6. find()")
print(text.find("Programming"))
print(text.find("Java"))

# 7. upper()
print("\n7. upper()")
print(text.upper())

# 8. lower()
print("\n8. lower()")
print(text.lower())

# 9. capitalize()
print("\n9. capitalize()")
print("python".capitalize())

# 10. title()
print("\n10. title()")
print("python programming".title())

# 11. count()
print("\n11. count()")
print(text.count("m"))

# 12. startswith()
print("\n12. startswith()")
print(text.startswith("Python"))

# 13. endswith()
print("\n13. endswith()")
print(text.endswith("Programming"))

# 14. len()
print("\n14. len()")
print(len(text))

# 15. in operator
print("\n15. in operator")
print("Python" in text)
print("Java" in text)

# 16. Escape Characters
print("\n16. Escape Characters")

print("Hello\nWorld")
print("Name\tAge")
print("C:\\Users\\Muktar")
print("He said \"Hello\"")
print('It\'s Python')