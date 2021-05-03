# While Loops are slower than For Loops
# in Python, because more of the process
# is handled in C for for loops

# break - is used for premature termination of the current loop.
# continue - returns the control to the beginning of the current loop.
#            When encountered, the loop starts next iteration without
#            executing the remaining statements in the current iteration.
# pass - used when a statement is required syntactically but you do not
#        want any command or code to execute. Useful for break points

print("\n\n")

count = 0
while count < 9:
    print("The count is: ", count)
    count = count + 1

print("\n\n")

lst_var = list(range(5))
for var in lst_var:
    print(var)

print("\n\n")

for letter in "abcdefg":
    print(letter)

print("\n\n")

lst_var = ["abcd", 123, 3.14]
for idx in range(len(lst_var)):
    print(idx)
    print(lst_var[idx])
