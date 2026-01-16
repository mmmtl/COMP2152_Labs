# Sample Coding Question 01 Week 01
# Maria Tai


# Question 2: defining an array (list)
my_array = [1, 4, 7, 9]


# Question 3: Order of Operations
# Variables
a = 1
b = 2
c = 3
d = 4

# Fully-Bracketed Version of: e = a - b ** c // d + a % c
e = (a - ((b ** c) // d)) + (a % c)
print("Question 3 result: ", e)


# Question 4: String Formatting
temp = 32.6
print("The temperature today is: {:.3f} degrees Celsius".format(temp))


# Question 5: User Input
userAge = int(input("Enter your age: "))
userAge = userAge + 22
print("Now showing the shop items filtered by age: ", userAge)
