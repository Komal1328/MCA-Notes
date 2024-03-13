def fact(num):
    fact = 1
    for i in range(1,num+1):
        fact *= i
    return fact

def combination(num, r):
    return fact(num)/(fact(r)*fact(num-r))

print(combination(5,1))

