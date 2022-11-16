n = int(input("Enter the no of student details to be created : \n"))
if(n<=0):
    print("Invalid Input")
    exit()
dict = {}
for i in range(n):
    dict[i] = {}
    name = input("Name: \n")
    age = int(input("Age: \n"))
    # print(age)
    if(age>10 and age<=20):
        loc = input("Location: \n")
    else:
        print("Invalid Input")
        exit()
    dict[i]["Name"] = name
    dict[i]["Age"] = age
    dict[i]["Location"] = loc
print("Here's the list of student details :")
print(dict[0])
print(dict[1])
print(dict[2])
key = input("Enter the training location: \n")
if key not in dict[i]["Location"]:
    print("Invalid Location")
    exit()
print("Student(s) enrolled in this training location:")
for i in range(n):
    if key == dict[i]["Location"]:
        print(dict[i]["Name"])