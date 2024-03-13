class NetworkError(RuntimeError):
    def __init__(self,arg):
        self.arg=arg
try:
    raise NetworkError("Bad hostname")
except (NetworkError,e):
    print(e.arg)
