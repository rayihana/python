start = 25
end = 50

print("Prime numbers between", start, 'and',end)
for num in range(start,end+1,1):
    if num>1:
        for i in range (2,num):
            if (num%i)==0:
                break
        else:
            print(num)