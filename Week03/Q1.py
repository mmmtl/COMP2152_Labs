# Q1: How to work with Lists?

# Brackets are an indicator of lists.

grades = [85, 92, 78, 95, 88]
grades.append(90)
grades.sort()
print(f"Sorted grades: {grades}")
print(f"Highest grade: {grades[-1]}")
print(f"Lowest grade: {grades[0]}")
print(f"Total number of grade: {len(grades)}")


# Notes:
# .append(value) => Adds items to the last index
# .sort() => Sorts items in from desc to asc
# array[-1] => Index of last item
# array[0] => Index of first item
# len(array) => Length of array

# Print formatted way => print(f"String string string {variable:.2f}")
#   - Can do math operations
#   - Can add string formatting
#   - Includes variables inside the quotes

# Print traditional way => print("String string string", variable)
#   - Extra space is added by default after a string
#   - Varibles and strings are joined by commas
#   - Using plus sign only works between strings. In this case, numbers have to be string type casted
#       Ex: "String" + string + "String" => Correct
#       Ex: "String" + num => Incorrect
#       Ex: "String" + str(num) => Correct