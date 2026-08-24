x = "aaabbbaaa"
print(x.strip("a"))   # 输出 "bbb"（去掉了首尾的字母 a）
print(x.strip("ab"))  # 输出 ""（首尾的 a 和 b 全去掉了，全空了）

help(str.strip)

x = '  ascsca  '
clean = x.strip
print(clean)
print(clean())