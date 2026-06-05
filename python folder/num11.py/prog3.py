num=int(input("Enter a number: "))
for i in range(1,num+2):
    if(i%2!=0):
        print(i)
        print("_"*35)
        for i in range (1,num+1,2):
            print(i)