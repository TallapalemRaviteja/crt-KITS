scores = [85,90,78,92,88]
for i in range(len(scores)):
    print(f"scores [{i}]={scores[i]}")
for score in scores: print(score)    

#metod 3
for idx, val  in enumerate(scores):
    print(f"Index {idx} ->{val}")
doubled = [x*2 for x in scores]    
arr=[10,20,30,40]
arr.append(50)
arr.insert(2,55)
arr.insert(2,5)
arr.extend([60,70,80])
new_arr = arr + [80,90]
print(arr)
print(new_arr)