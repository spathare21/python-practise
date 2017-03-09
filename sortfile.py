names = open('file.txt')
line=names.readline()
while len(line)!=0:
    print(line, end ='')
    line=sorted(names.readline())
names.close()
