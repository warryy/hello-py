print("===========内置函数============")
print(abs(-1))
print(max(1, 2))
print(float(1))
print(int(1.2312435))
print(str(1.2312435))
print(bool(1.2312435))

print("===========函数定义============")
from functions.cust_abs import cust_abs


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-1))
print(cust_abs(-1))


print("===========函数参数============")
print("===========默认参数必须指向不变对象============")


def add_end(L=[]):
    L.append("END")
    return L


def add_end2(L=None):
    if L is None:
        L = []
    L.append("END")
    return L


print(add_end())
print(add_end())
print(add_end2())
print(add_end2())
print("===========可变参数(扩展元祖)============")


def calc(*numbers):
    print("numbers", numbers)
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2, 3))
print(calc(*[1, 2, 3]))
print(calc(*(1, 2, 3)))


print("===========关键参数(扩展对象)============")


def person(name, age, **kw):
    print("name:", name, "age:", age, "other:", kw)


person("Jack", 24, city="Beijing")
person("Jack", 24, city="Beijing", gender="male")
person("Jack", 24, **{"city": "Beijing", "gender": "male"})


print("===========命名关键字参数============")
print(
    "===========命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错============"
)


def person2(name, age, *, city="beijign", gender):
    print("name:", name, "age:", age, "city:", city, "gender:", gender)


person2("Jack", 24, gender="male")


print("===========参数组合============")


def f1(a, b, c=0, *args, **kw):
    print("a =", a, "b =", b, "c =", c, "args =", args, "kw =", kw)


def f2(a, b, c=0, *, d, **kw):
    print("a =", a, "b =", b, "c =", c, "d =", d, "kw =", kw)


f1(1, 2)
f1(1, 2, 3)
f1(1, 2, 3, "a", "b")
f1(1, 2, 3, "a", "b", x=99)
f2(1, 2, d=99, ext=None)


print("===========递归函数============")
print("===========递归函数============")
print("===========递归函数============")
