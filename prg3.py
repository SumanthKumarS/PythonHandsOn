print("Dead Count:")
dead = int(input())
if(dead<0):
    print("Invalid input")
else:
    print("Injured Count:")
    injured = int(input())
    if(injured<0):
        print("Invalid input")
    else:
        print("Safe Count:")
        safe = int(input())
        if(safe<0):
            print("Invalid input")
        else:
            print("TSUNAMI REPORT OF JAPAN")
            print("The number of people")
            print("Dead :",dead,"\nInjured :",injured,"\nSafe :",safe)
            print("Please help the people who are suffering!!!")