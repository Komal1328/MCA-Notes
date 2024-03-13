# Program to handle multiple #errors with one except #statement
def fun(a):
    if a < 4:
        # throws ZeroDivisionError 	#for a = 3
        a = a/(a-3)
        print(a)
        # throws NameError
    if a >= 4:
        print("Value of b = ", b)
try:
    fun(2)
    fun(5)
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")
