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
        #nonlocal var1   first option
        global var2  # second option
        var = "inner"
        print(var)

    var = "fu"
    print(var)
    inner()


var = "globalvar"
print(var)
fu()


# Klassen mit Klassenvars in java static vars
class uf:
    time = 1937
    sentence = "ha qu"

    def funct(self, other_vars):
        sentence = "qu hi"

class uf_child(uf):
    bonus = 42

child = uf_child()
print(child.time == child.bonus)

instanz = uf() #instanzierung muss sein
print(instanz.time)

# konstruktoren mit instanzvars aolso local
def __init__(self, other_warz):
    self.varia = other_warz

# exceptions = Klassen
try:
    all = de / 0
except:
    print("Zero Devision Error")



# dates
import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))
print(x.date())

y = x - 33
print(x, y)