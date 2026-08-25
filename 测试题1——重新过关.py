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



# ========================================================
# 第5题：match 模式匹配（难度 ⭐⭐）
# ========================================================
"""
手术编码前缀对应科室：
  "NEU" → 神经外科
  "CAR" → 心外科
  "ORT" → 骨科
  "OFT" → 眼科
  其他  → "未知科室"

已知手术编码列表：
  codes = ["NEU-001", "ORT-023", "CAR-045", "DER-001", "OFT-012"]

请用 match-case 判断每个编码对应的科室，并输出：
"NEU-001 → 神经外科"
"ORT-023 → 骨科"
......（每个编码一行）
"""
codes = ["NEU-001", "ORT-023", "CAR-045", "DER-001", "OFT-012"]

for code in codes:
    eksbm = code.split('-')[0].strip()
    no = code.split('-')[1].strip()
    match eksbm:
        case 'NEU':
            b = '神经外科'
        case 'CAR':
            b = '心外科'
        case 'ORT':
            b = '骨科'
        case 'OFT':
            b = '眼科'
        case _:
            b = '未知科室'
    print(f'"{eksbm}-{no}→{b}"')

    # ========================================================
# 第6题：循环结构（难度 ⭐⭐）
# ========================================================
"""
1. 用 for 循环打印 1 到 20 中所有 3 的倍数（每行一个数字）

2. 用 while 循环计算 1 + 2 + 3 + ... + 100 的和，并输出

3. 打印九九乘法表（嵌套循环），输出格式：
   1x1=1  1x2=2  ...  1x9=9
   2x2=4  2x3=6  ...  2x9=9
   ...（三角形形式）
"""
for i in range (1,21):
    if i%3 == 0:
        print(i)

total = 0
i = 1
while i<101:
    total +=i
    i+=1

print(total)

# /	除法（真除法）	计算商，保留小数	10 / 3 = 3.333...	浮点数 (float)
# //	整除（地板除）	计算商，只保留整数部分（向下取整）	10 // 3 = 3	整数 (int)
# %	取模（求余）	计算除法后的余数	10 % 3 = 1 （因为 3x3=9，剩 1）	整数 (int)
for i in range(1,10):
    for j in range(1,i+1):
        print(f'{i}x{j}={i*j}',end = "\t")
    print()


print("Hello\nWorld")  # 输出：Hello 换行  World
print("Hello\tWorld")  # 输出：Hello     World （中间有一大段空格间隔）
print("Hello\\World")  # 输出：Hello\World