# 元组：tuple。 有序列表
# tuple 一旦初始化就不能修改
t = (1, 2)
print(t)
print(t[0])
print(t[1])
t = (1, 2, 3)
print(t)
print(t[0])
print(t[1])

# 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
t = (1,)
print(t)

# 数组元组
t = ('a', 'b', ['A', 'B'])
print(t)
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)