def fact(n):
     res = 1
     for i in range(1,n+1):
          res *= i
     return res
def ecalc(n):
     res = 0
     for i in range(0,n):
          div = fact(i)
          res += 1/div
     return res
print(ecalc(6))
