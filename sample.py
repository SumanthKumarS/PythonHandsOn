n = int(input("Enter number of students: \n"))
dict = {}
for i in range(1,n+1):
    print("For student ",i)
    name = input("Enter name: \n")
    score = input("Enter the score: \n")
    dict[name] = score

with open("output_data.txt",'w') as f:
    for key,value in dict.items():
        f.write('Name: %s Score: %s\n' % (key,value))
f.close()
f = open("output_data.txt","r")
print(f.read())