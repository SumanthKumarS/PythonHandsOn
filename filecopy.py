f1 = open("file_in.txt",'r')
f2 = open("file_out.txt",'a')
for line in f1:
    f2.write(line)
f1.close()
f2.close()
f = open("file_out.txt",'r')
print(f.read())