n = int(input("Enter the no of student details to be created : \n"))
data = []
subdict = {}
if n>0:
    for i in range(n):
        name = input("Name: ")
        age = int(input("Age: "))
        if age<10 or age>20:
            print("Invalid Input")
            exit()
        location = input("Location: ")
        subdict.update({'Name':name,'Age':age,'Location':location})
        data.append(subdict)
        subdict = {}
    print("Here's the list of student details :")
    for i in data:
        print(i)
    sn = input("Enter the training location: \n")
    res = [sub['Name'] 
    for sub in data if sub['Location'] == sn]
    if not res:
        print("Invalid location")
    else:
        print("Student(s) enrolled in this training location:")
        for i in res:
            print(i)
else:
    print("Invalid Input")