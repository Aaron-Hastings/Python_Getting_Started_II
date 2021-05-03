# Variables and Data Structures
# See, e.g. https://www.tutorialspoint.com/python3/python_variable_types.htm
#
#    Numbers
#    String
#    List
#    Tuple
#    Dictionary

int_var = 100  # Integer
flt_var = 100.0  # Float
cpx_var = complex(1.0, 0.0)  # Complex Number
str_var = "abc"  # String -- somewhat immutable
lst_var = ["abc", 123, 3.14]  # List
tpl_var = ("abc", 123, 3.14)  # Tuple -- Immutable
dct_var = {"one": 1, 2: "This is two"}  # Dictionary

print(int_var)
print(flt_var)
print(cpx_var)
print(str_var)
print("")

# slice operator ([ ] and [:] ) with indexes starting at 0 in the beginning
# of the string and working their way from -1 to the end
print(str_var[0:3])  # 0 based index, : up to but not including THIS element
print(str_var[0])
print(str_var[1])
print(str_var[2])
print(str_var[1:])  # Prints the 2nd element to the end of the string
print("")
print(str_var + str_var)  # Concatenates strings
print(str_var * 3)  # Repeats string

print(lst_var)
print(lst_var[2])
print("")

print(tpl_var)
print(tpl_var[2])
print("")

print(dct_var)
print(dct_var["one"])
print(dct_var[2])
