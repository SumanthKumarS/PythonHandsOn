def find_prime(a,b):
    ain = []
    for num in range(a,b+1):
        if num>1:
            for i in range(2,num):
                if num%i == 0:
                    break
            else:
                ain.append(num)
    for item in ain:
        print(item,end=' ')
    if(len(ain)<=0):
        print("There is no prime numbers in this range")
        exit()

a = int(input())
b = int(input())
if(a == b):
    print("There is no prime numbers in this range")
    exit()
count = 0

if a<0 or b<0 or a>b:
    print("Invalid range")
    exit()
else:
    find_prime(a,b)   
