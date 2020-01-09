no_of_time= int(input("Enter number of time pattern print :  "))
no = int(input("Enter a number"))

for i in range(no):
    for m in range(no_of_time):
        for c in range(no-i):
            print(end=" ")
        for j in range(i*2-1):
            print("*",end ="")
        for c in range(no-i):
            print(end=" ")
    print()