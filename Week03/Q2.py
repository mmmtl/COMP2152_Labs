# Q2: List methods

cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]
app_count = cart.count("apple") # .count Counts the number of "apple"
print(f"Number of apples: {app_count}") # Output: Number of apples: 2
milk_position = cart.index("milk")
print(f"Position of milk: {milk_position}") # Output: Position of milk: 2
cart.remove("apple") # remove the first encounter of "apple"
removed_item = cart.pop() # It will by default delete the last item in the list
print(f"Remove item using pop: {removed_item}") # Output: Remove item using pop: eggs
print("Is banana in cart?", "banana" in cart) # Output: True