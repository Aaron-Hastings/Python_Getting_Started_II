print("\n\n")
print("Conditional Statements")

# Logical operators ==, !=, <, >, >=, <=

amount = 3590
if amount < 1000:
    print("The value of the variable " + str(amount) + " is small")
elif amount < 5000:
    print("The value of the variable " + str(amount) + " is medium")
else:
    print("The value of the variable " + str(amount) + " is large")
print("\n\n")

a = 1
b = 2

if a == 1 and b == 2:
    print("a = 1 AND b = 2")


if a == 1 or b == 1:
    print("at least one variable equals 1")

if not (a == 2):
    print("a is not equal to 2")
