no = int(input("Enter the  no of student details to be created : "))
dict = {}
for i in range(no):
    dict[i] = {}
    name = input("Name: ")
    age = input("Age: ")
    loc = input("Location: ")
    dict[i]["Name"] = name
    dict[i]["Age"] = age
    dict[i]["Location"] = loc

print("Here's the list of student details :")
print(dict[1])