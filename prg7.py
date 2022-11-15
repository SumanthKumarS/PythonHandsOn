print("Enter the no. of subjects: ")
n = int(input())
if(n<=0):
    print("Invalid no. of subjects")
    exit()
print("Enter the marks")
a = []
for i in range(n):
    a1 = int(input())
    a.append(a1);
    if a[i]<0 or a[i]>100:
        print("Invalid mark")
        exit()
countP = 0
countF = 0
for i in range(n):
    if a[i] <= 50:
        countF +=1
        
    if a[i] > 50:
        countP +=1
        
print("No. of subjects passed: ",countP)
print("No. of subjects Failed: ",countF)
    