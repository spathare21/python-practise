# Create a new file
fo = open ("foo.txt","w+")
fo.write ("Hey welcome to the file tutorials\nstart reading and writing file in python\n")
print ("file name : ",fo.name)
fo.close()

# Read file
fo = open("foo.txt","r+") 
str = fo.read(20)
print (str)

#Rename file 
import os
os.rename("foo.txt","bar.txt")
print ("file name after rename : ",fo.name)

# Delete file 
os.remove("bar.txt")

print ("Done with files operations")

print ("\n Directory operations")

# Create direcotry 
os.mkdir("test_dir")

#Change the dir
os.chdir("/home/spathare/python-practise/test_dir")

# get current dir
print("current dir path : ",os.getcwd())

# Chage directory
os.chdir("/home/spathare/python-practise")

# Remove the dir
os.rmdir("test_dir")


