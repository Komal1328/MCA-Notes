try:
    raise NameError("hi")

except NameError:
    print("an exception")
    raise
