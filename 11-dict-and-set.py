print("=================dict=================")
d = {"Michael": 95, "Bob": 75, "Tracy": 85}
print(d["Michael"])
d["Adam"] = 67
print(d)
print(d.get("Thomas"))
print(d.get("Thomas", -1))
print(d.pop("Bob"))
print(d)

print(
    "============在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：========="
)
a = 'abc'
b = a.replace('a', 'A')
print(a)
print(b)
# key = [1, 2, 3]
# d[key] = 'a list' # TypeError: unhashable type: 'list'


print("=================set=================")
s1 = set([1, 2, 2, 2, 3])
print(s1)
s1.remove(2)
print(s1)

print("=================set 交并操作=================")
s2 = set([2, 4])
print(s2)
print(s1 & s2)
print(s1 | s2)
