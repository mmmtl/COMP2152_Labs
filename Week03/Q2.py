# Q2: List methods

cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]
app_count = cart.count("apple")
print(f"Number of apples: {app_count}") # Output: Number of apples: 2
milk_position = cart.index("milk")
print(f"Position of milk: {milk_position}") # Output: Position of milk: 2
cart.remove("apple")
removed_item = cart.pop()
print(f"Remove item using pop: {removed_item}") # Output: Remove item using pop: eggs
print("Is banana in cart?", "banana" in cart) # Output: True

# Notes:
# .count(value) => Counts the number of appearences of such item in a list
# .index(value) => Returns the index of a value from a list
# .remove(value) => Removes a value from a list
# .pop() => By default deletes the last item in the list
# value in list => keyword "in" 
#   - Returns a boolean value
#   - Find if a value is found in a list
#   - Typically used in for loops 