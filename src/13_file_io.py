"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"
# import os
# path = os.path.abspath('foo.txt')
# print('dir "%s"' % path)

path = 'p:/projects/cs/Unit1/Intro-Python-I/src/foo.txt'

f1 = open(path, 'r')
for x in f1:
  print(x)
f1.close()

# YOUR CODE HERE

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

line1 = "This is Line 1"
line2 = "This is Line 2"
line3 = "This is Line 3"


# YOUR CODE HERE
newpath = 'p:/projects/cs/Unit1/Intro-Python-I/src/bar.txt'
f2 = open(newpath, 'w')

f2.write("%s /n %s /n %s /n" % (line1, line2, line3))

f2.close()
