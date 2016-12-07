#try and finally block example
try :
 fo = open("testfile","w")
 fo.write("This is my test file for exception handling")
finally:
 print ("Error : can\'t find file")
 fo.close()
 print ("file is closed :",fo.closed)
