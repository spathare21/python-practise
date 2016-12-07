#read write file first example

fo = open("foo.txt","w+")
fo.write("Hey how are you \n we are testing this file for write to file!!\n")
print ("Name of the file : ", fo.name)
print ("Is this file closed ? : ",fo.closed )
print ("Opening mode :",fo.mode)
fo.close()
print ("reading from file")
fo1 = open("foo.txt","r+")
str = fo1.read(10)
print ("Read string from file is :",str )
fo1.close()




