# 第1题：变量与运算符（难度 ⭐）
# ========================================================
"""
已知：
  单价 = 28.5 元，数量 = 4 件
  支付了 200 元

请计算：应找零多少元？
要求：
  1. 用变量存储单价、数量、支付金额
  2. 计算总价和找零
  3. 用 print() 输出 "总价：xxx 元，找零：xxx 元"（保留一位小数）
"""


price = 28.5
num = 4
pay  = 200
print(f'应该找钱{pay-num*price:.1f}元，总价{num*price:.1f}元')


# ========================================================
# 第2题：类型判断与转换（难度 ⭐）
# ========================================================
"""
已知字符串："score = 92.5"
请编写代码：
  1. 提取出其中的数字部分（用字符串切片或 split）
  2. 转换为 float 类型
  3. 判断该分数属于哪个等级（>=90: A, >=80: B, >=70: C, >=60: D, <60: E）
  4. 输出 "原始分数 92.5 分，等级为 A"
"""
x = 'score = 92.5'
score = x.split('=')[1].strip()
print(score)
fscore = float(score)
print(type(fscore))

if fscore >=90:
    print('你是A级别')
elif fscore >=80:
    print('你是B级别')
elif fscore >=70:
    print('你是C级别')
elif fscore >=60:
    print('你是D级别')
else:
    print('你没及格，是E级别')


x = 'score = 92.5'
score = x.split('=')[1].strip()
print(score)
fscore = float(score)
print(type(fscore))

match fscore:
    case S if S>=90:
        grade = 'A'
    case S if S>=80:
        grade = 'B'
    case S if S>=70:
        grade = 'C'
    case S if S>=60:
        grade = 'D'
    case _:
        grade = 'E'
print(f'你是{grade}等级')

# ========================================================
# 第3题：字符串格式化（难度 ⭐）
# ========================================================
"""
现有患者信息：
  name = "王建国"
  age = 58
  department = "心内科"
  bed_no = "12A"

请分别用三种方式格式化输出（每种一行）：
  1. % 格式化："患者 王建国，58岁，心内科 12A 床"
  2. format() 方法
  3. f-string
"""
name = "王建国"
age = 58.55
department = "心内科"
bed_no = "12A"
print("患者 %s，%.1f岁，%s %s 床" % (name, age, department, bed_no))
# 1. % 格式化
print("患者 %s，%d岁，%s %s 床" % (name, age, department, bed_no))

# 2. format() 方法
print("患者 {}，{}岁，{} {} 床".format(name, age, department, bed_no))

# 3. f-string
print(f"患者 {name}，{age}岁，{department} {bed_no} 床")



做第五题