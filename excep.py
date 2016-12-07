# Example of exception handeling.
try :
 fh = open("testfile.txt","r")
 fh.write("This is my test file for exception handling!!\n")
except IOError :
 print ("Error:can\'t find file or read data")
else :
 print ("written content in file successfully\n")
