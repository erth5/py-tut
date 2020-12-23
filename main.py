v = [2, 4, 'meow, "Maskierung": I\'m']
en = 0
de = 1
fr = 2
ch = 4
while v[0] > 0:
    v[0] = v[0] - 1
    print(v[0])

for w in v:
    print(2 ** 3 == 8)  # potent

for i in range(5, 8, 2):
    v.append("hi")
    print(i)

def fkt(l):
    if l == 1:
        return "deutsch"
print(fkt(de))

import module
print(module.x)

if __name__ == "__main__":
    print("text, der nur ausgeführt wird, wenn main nur direkt gestartet wird")

# global var
t = "me"
def fu():
    def inner():
        nonlocal var    # first option
        global var      # second option
        var = "inner"
        print(var)
    var = "fu"
    print(var)
    inner()
var = "globalvar"
print(var)
fu()

# errors
all = de / 0