class Ex(Exception):
    pass

try:
    raise Ex()
except Ex:
    print("own exc")
except:
    print("standard Ex")

