import random

print("==================简单使用=====================")
# 生成一个指定范围内的随机整数
random_int = random.randint(1, 6)
print(random_int)

match random_int:
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("three")
    case _:
        print("large than 3")

print("==================条件判断====================")
# 生成一个指定范围内的随机整数
age = random.randint(1, 40)
print(age)
match age:
    case x if x < 10:
        print(f"< 10 years old: {x}")
    case 10:
        print("10 years old.")
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
        print("11~18 years old.")
    case 19:
        print("19 years old.")
    case _:
        print("not sure.")

print("==================列表匹配=====================")
print('-- match list --')

args = ['gcc', 'hello.c', 'world.c', 'haha.c', 'maya']
# args = ['clean']
# args = ['gcc']

match args:
    # 如果仅出现gcc，报错:
    case ['gcc']:
        print('gcc: missing source file(s).')
    # 出现gcc，file1 为第二个变量, files 为其余变量:
    case ['gcc', file1, *files]:
        print('gcc compile: ' + file1 + ', ' + ', '.join(files))
    case _:
        print('invalid command.')