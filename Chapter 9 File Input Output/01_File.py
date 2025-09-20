'''
a = " a very long string with emails "

emails = []
3 seconds

The random-access memory is voilatile, and all its contents are lost once a program terminates in order to persist the data 
forever, we use files.

A file is data stored in a storage device. a python program can talk to the file by reading content
from it and writing content to it.

TYPES OF FILES.

1. Text Files. (.txt, .c etc.)
2. Binary Files. (.jpg, .dat etc.)

'''

# Text file. ( Open/ Read/ Print/ Close)

f = open("file.txt")
data = f.read()
print(data)
f.close()
