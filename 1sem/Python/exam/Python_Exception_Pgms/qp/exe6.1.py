#exe6.1
def sub(a):
    if(a>2):
        a= a/(a-3)
    return a

try:
    print(sub(5))
except ZeroDivisionError:
    print("Can't divide by zero")

