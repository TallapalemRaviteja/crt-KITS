num=int(input("Enter the number"))
count=0
res=0
while(num!=0):
    res=num%10
    count+=1
    num=num/10
    print(f"count of digits is {count}")