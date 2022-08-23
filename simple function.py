def sum_multiply (x,y):
    multiply=x*y

    if (multiply<=1000):
        return multiply
    else:
        sum = x+y
        return sum
result = sum_multiply(30,20)
print("The result is", result)
result = sum_multiply(40,30)
print("The result is", result)

