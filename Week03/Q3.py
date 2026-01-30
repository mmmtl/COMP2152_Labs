# Q3: Tuples - Creation and Unpacking

# Tuples use parenthesis "()" as indicator

point1 = (3,5)
point2 = (7,2)
x1, y1 = point1
x2, y2 = point2
print(f"X1 = {x1}, Y1 = {y1}")
print(f"X2 = {x2}, Y2 = {y2}")
distance = ((x2 - x1) ** 2 + (y2-y1) ** 2) ** 0.5
print("Distance between points:", distance)

# Notes:
# Tuples are represented by the parenthesis "()"
# Tuple unpacking:
#   var = (4, 5, 6) => this is a tuple
#   var1, var2, var3 = var => this is unpacking
#   We are basically saying:
#   var1 = 4, var2 = 5, var3 = 6