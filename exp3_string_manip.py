print("-------- STRING MANIPULATION --------")

# Concatenation
s1 = input("\nEnter first string: ")
s2 = input("Enter second string: ")
print(f"Concatenated String: {s1 + s2}")

# Reversal
s = input("\nEnter a string to reverse: ")
print(f"Reversed String: {s[::-1]}")

# Slicing
s = input("\nEnter a string for slicing: ")
try:
    start = int(input("Enter start index: "))
    end = int(input("Enter end index: "))
    print(f"Sliced String: {s[start:end+1]}")
except ValueError:
    print("Error: Indices must be whole numbers.")
