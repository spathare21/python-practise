#open a file
fo = open("foo.txt","r+")
str = fo.read(15)
print ("Read String is :",str)

# Check the current position 
pos = fo.tell()
print ("current position is :",pos)

#Read the file before reposition of pointer
str = fo.read(10)
print ("Read the String before reposition is :" , str)

# Reposition pointer at the begining once again
pos = fo.seek(0,0)
str = fo.read(10)
print ("Again read string is :",str)

fo.close()
