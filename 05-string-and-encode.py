# ========================================================
# python3 中字符串用 Unicode 字符集保存, 即 2 个字节一个字符
# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
print(ord("A"))
print(chr(65))
print("\u4e2d\u6587")

# 这样可以让 ABC 只占 3 个字节
print(b"ABC")

print("ABC".encode("ascii"))
print("中文".encode("utf-8"))
print(b"\xe4\xb8\xad\xe6\x96\x87".decode("utf-8", errors="ignore"))

# 字符长度和字节长度
print(len("ABC"))
print(len("中文"))
print(len("中文".encode("utf-8")))

# ========================================================
# 格式化字符串
print("Hello, %s" % "world")
print("Hi, %s, you have $%d." % ("warryy", 1000000))
print("Age: %s. Gender: %s" % (25, True))
print("进度: %d%%" % 100)

# format()
print("Hello, {0}, 成绩提升了 {1:.2f}%".format("小明", 17.3587))

# f-string
var1 = 2
var2 = var1 * 1.1 ** 2
print(f'{var1}, {var2:.2f}')