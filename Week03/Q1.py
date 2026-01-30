# Q1: How to work with Lists?

# Brackets are an indicator of lists.

grades = [85, 92, 78, 95, 88]
grades.append(90) # -> Adds item to the last index
grades.sort()
# Formatted way. Can do math operations and format strings
print(f"Sorted grades: {grades}")
# Traditional way print("Sorted grades:", grades)
print(f"Highest grade: {grades[-1]}")
print(f"Lowest grade: {grades[0]}")
print(f"Total number of grade: {len(grades)}")