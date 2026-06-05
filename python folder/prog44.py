str="scott@oracle.in"
a=str.split('@')
d=str.find('.')
print(str[0:a])
print(str[a+1:d])