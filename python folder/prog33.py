std={
    101:'Scott',103:'Adams',104:'James,',105:'David'
}
print(std)
std[106]='ravi'
print(std)
del std[101]
del std[106]
print(std)
#check 101,103,105
check=101 in std
print(check)
check=103 in std    
print(check)
