# See also https://www.tutorialspoint.com/python3/python_exceptions.htm

try:
    fh = open("testfile", "w")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print("Error: can't find file or read data")
else:
    print("Written content in the file successfully")
    fh.close()

# try:
#    You do your operations here
#    ......................
# except:
#    If there is any exception, then execute this block.
#    ......................
# else:
#    If there is no exception then execute this block.


# try:
#    You do your operations here;
#    ......................
#    Due to any exception, this may be skipped.
# finally:
#    This would always be executed.
#    ......................
