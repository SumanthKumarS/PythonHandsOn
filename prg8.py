print("Enter number of courses: ")
n = int(input())
if n<1:
    print("Invalid no. of courses")
    exit()
dict = {}
for i in range(n):
    print("Enter name of the subject and marks respectively: ")
    name = input()
    marks = int(input())
    if marks<0 or marks>100:
        print("Invalid mark")
        exit()
    else:
        dict[name] = marks
print("The courses you have cleared are:")
for key,value in dict.items():
    if value>=80:
        print(key,value)

        
