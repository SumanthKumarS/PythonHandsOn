print("Enter the number of names :")
n = int(input())
if n<=0:
    print("Invalid Input")
    exit()
print("Enter the names:")
a = []
for i in range(n):
    name = input()
    a.append(name)

print("The sorted name list is:")
print(sorted(a,key=lambda x:(len(x),x),reverse=True))