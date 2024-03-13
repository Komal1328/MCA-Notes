def cal(a):
    if(a>3):
        a=a/0
    else:
        print(a)

try:
    cal(4)

except ZeroDivisionError:
    print("Can't divide ny zero")
except SyntaxError:
    print("unindented error")
