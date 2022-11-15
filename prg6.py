print("Enter the total no.of plots: ")
n = int(input())
if (n<0 or n>20):
    print("Invalid Input")
else:
    a = []
    sumeve = 0
    sumodd = 0
    print("Enter the numbers of each plot:")
    for i in range(n):
        a1 = int(input())
        a.append(a1)
        if a[i]<0:
            print("Invalid Input")
            exit()
    for i in range(n):
        if a[i]%2 == 0:
            sumeve += a[i]
        else:
            sumodd += a[i]
    avg = sumeve+sumodd
    avg = avg/2
    print("The password for the file is: "+f'{avg:.2f}')