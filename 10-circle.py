print("==============for 循环==============")
names = ["Michael", "Bob", "Tracy"]
for name in names:
    print(name)

print("==============range 循环==============")
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

print("==============while 循环==============")
n = 1
sum = 0
while n < 101:
    sum = sum + n
    n = n + 1
print(sum)
print("==============break 循环==============")
n = 1
sum = 0
while n <= 11:
    if n > 10:
        break
    sum = sum + n
    n = n + 1
print(f"END {sum}")
print("==============continue 循环==============")
n = 0
sum = 0
while n < 4:
    n = n + 1
    if n % 2 == 0:
        continue
    sum = sum + n
print(f"END {sum}")
