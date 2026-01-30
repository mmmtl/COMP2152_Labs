# Q4: How to work with Sets

# Similar to Lists, but its indicator are curly brackets "{}"

monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}
monday_class.add("Grace")
print(f"Monday class: {monday_class}")
print(f"Wednesday class: {wednesday_class}")
print(f"Attended both classes: {monday_class & wednesday_class}") # shift 7 = &, This is an Intersection
print(f"Attented either classes: {monday_class | wednesday_class}") # shift \ = |, This is a Union
print(f"Only Monday: {monday_class - wednesday_class}")
print(f"Only one class: {monday_class ^ wednesday_class}") # ^ = caret, shift 6
allStudents = monday_class | wednesday_class
print("Is Monday subset of all students?", monday_class <= allStudents) # True

# Notes:
# .add() => adds a value to a set
# & => Intersection, ampersand, returns all common values between sets
# | => Union, pipe, returns all values from both sets, without duplicating the duplicated values (so they appear once)
# - => Minus sign, returns all values from a set that don't appear in another set
# ^ => Caret sign, returns all values that appear in one set, but no in both of them
# <= => Subset, returns a boolean checks if a set is a subset of a union
