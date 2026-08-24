"""
测试题 1：数据存储与运算 + 流程控制 + 数据容器
==============================================
说明：每道题写完后运行验证，确认无误后喊我检查。
如果卡住超过 15 分钟，先跳过做后面的，回头再补。
"""

# ========================================================
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
# 在这里写代码
price = 28.5
num = 4
pay = 200
print(f'总价:{price*num:.1f}元，找零{pay-price*num:.1f}元')
k = '  aaa '
print(k)
k.strip()
print(k)
# 输出：总价:37.5元，找零12.5元

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
a = 'score = 92.5'
b=float(a.split('=')[1].strip())
if b>=90:
    print(f'原始分数{b}分,等级为A')
elif b>=80:
    print(f'原始分数{b}分,等级为B')
elif b>=70:
    print(f'原始分数{b}分,等级为C')
elif b>=60:
    print(f'原始分数{b}分,等级为D')
else:
    print(f'原始分数{b}分,等级为E')
#第二种写法
a = 'score = 92.5'
score = float(a.split('=')[1].strip())

match score:
    case s if s >= 90:
        grade = 'A'
    case s if s >= 80:
        grade = 'B'
    case s if s >= 70:
        grade = 'C'
    case s if s >= 60:
        grade = 'D'
    case _:
        grade = 'E'

print(f'原始分数 {score} 分，等级为 {grade}')
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
# 第4题：条件分支（难度 ⭐⭐）
# ========================================================
"""
BMI 计算公式：体重(kg) / (身高(m))^2

请写一个程序：
  1. 定义变量 weight = 75, height = 1.78
  2. 计算 BMI
  3. 根据以下标准判断并输出结果：
     - BMI < 18.5 → "偏瘦"
     - 18.5 <= BMI < 24 → "正常"
     - 24 <= BMI < 28 → "偏胖"
     - BMI >= 28 → "肥胖"
  4. 使用 if-elif-else 结构

输出格式："您的 BMI 为 23.7，属于 正常"
"""
weight,height = 75,1.78
BMI = weight/height**2
match BMI:
    case B if B < 18.5:
        type = '偏瘦'
    case B if 18.5 <= B < 24:
        type = '正常'
    case B if 24 <= B < 28:
        type = '偏胖'
    case B if B >= 28 :
        type = '肥胖'
    case _:
        print('您输入的信息有误，请检查')
print(f'您的BMI为{B:.1f}。属于{type}')

weight,height = 75,1.78 
BMI = weight/height**2
if BMI <18.5:
    type = '偏瘦'
elif 18.5 <= BMI < 24:
    type = '正常'
elif 24 <= BMI < 28:
    type = '偏胖'
elif  BMI >= 28:
    type = '肥胖'
else :
    print('您输入的信息有误')
print(f'您的BMI为{BMI:.1f}。属于{type}')



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
    prefix = code.split('-')[0]
    match prefix:
        case "NEU":
            dept = "神经外科"
        case "CAR":
            dept = "心外科"
        case "ORT":
            dept = "骨科"
        case "OFT":
            dept = "眼科"
        case _:
            dept = "未知科室"
    print(f'"{code} → {dept}"')


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
for i in range(1,21):
    if i%3 == 0:
        print(i)
k=0   
i=1
while i <101:
    k+=i
    i+=1
print(k)  
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{j}×{i}={i*j}", end="\t")
    print()
       
# ========================================================
# 第7题：列表操作综合（难度 ⭐⭐⭐）
# ========================================================
"""
patients = [
    "赵敏", "钱磊", "孙丽", "周强", "吴昊",
    "郑爽", "王芳", "冯磊", "陈静", "褚健",
]
scores =   [88,    55,    92,    73,    61,
            47,    85,    66,    95,    58]

请完成以下操作，每步一行注释说明在做什么：
  1. 用 zip() 将 patients 和 scores 合并成列表，每个元素是 (姓名, 分数) 元组
  2. 用列表推导式筛选出分数 >= 60 的及格学生名单
  3. 对合并后的列表按分数从高到低排序（用 sorted + lambda）
  4. 输出分数最高和最低的学生姓名
  5. 计算平均分（保留一位小数）
  6. 用切片取出前 3 名学生的信息
"""
# 在这里写代码
# 1.
patients = ["赵敏", "钱磊", "孙丽", "周强", "吴昊","郑爽", "王芳", "冯磊", "陈静", "褚健",]
scores =   [88,55,92,73,61,47,85,66,95,58]
p_s = list(zip(patients,scores))
print(p_s)
# 2.
print(list(p for p,s in p_s if s>=60))
#3
# p_s.sort(key=lambda x:(-x[1],x[0]))
# print(p_s)
p_s_sorted = sorted(p_s,key=lambda x:(-x[1],x[0]))
print(p_s_sorted)
#4
print(f'成绩最高的学生名字叫：{p_s_sorted[0][0]}')
print(f'成绩最低的学生名字叫：{p_s_sorted[-1][0]}')
#5
k = [i[1] for i in p_s]
print(f'平均成绩为：{sum(k)/len(k):.1f}')
#6
a = p_s_sorted[0:3]
print(a)

# ========================================================
# 第8题：字典操作（难度 ⭐⭐⭐）
# ========================================================
"""
现有一个嵌套字典存储药房库存：

pharmacy = {
    "心内科": {
        "阿司匹林": {"规格": "100mg", "库存": 200, "价格": 15.5},
        "美托洛尔": {"规格": "25mg",  "库存": 150, "价格": 22.0},
    },
    "呼吸科": {
        "阿莫西林": {"规格": "250mg", "库存": 300, "价格": 8.5},
        "布洛芬":   {"规格": "200mg", "库存": 80,  "价格": 12.0},
    }
}

请完成：
  1. 给呼吸科新增药品"左氧氟沙星"，规格 500mg，库存 100，价格 18.0
  2. 心内科"美托洛尔"消耗了 30 盒，更新库存
  3. 遍历 pharmacy，输出格式：
     心内科 - 阿司匹林(100mg) - ¥15.5 - 库存:200
     （每个药品一行）
  4. 找出全药房库存最少的药品名称和库存量
"""
#1
pharmacy = {
    "心内科": {
        "阿司匹林": {"规格": "100mg", "库存": 200, "价格": 15.5},
        "美托洛尔": {"规格": "25mg",  "库存": 150, "价格": 22.0},
    },
    "呼吸科": {
        "阿莫西林": {"规格": "250mg", "库存": 300, "价格": 8.5},
        "布洛芬":   {"规格": "200mg", "库存": 80,  "价格": 12.0},
    }
}
pharmacy['呼吸科']["左氧氟沙星"] = {"规格": "500mg","库存": 100,"价格": 18.0}
print(pharmacy)
#2
pharmacy['心内科']["美托洛尔"]['库存'] = pharmacy['心内科']["美托洛尔"]['库存'] - 30
print(pharmacy)
#3
for i,k,in pharmacy.items():
    for k1,k2 in k.items():
        spec,stock,price = k2['规格'],k2['库存'],k2['价格']
        print(f'{i} - {k1}({spec}) - ¥{price} - 库存：{stock}')
#4找出全药房库存最少的药品名称和库存量
min_stock = []
for i,k,in pharmacy.items():
    for k1,k2 in k.items():
        stock = k2['库存']
        min_stock.append(stock)
min_med = min(min_stock)
for i,k,in pharmacy.items():
    for k1,k2 in k.items():
        if k2['库存'] == min_med:
            print(f'库存最少的药品名称为{k1},库存量为{min_med}')
# ========================================================
# 第9题：集合与元组（难度 ⭐⭐）
# ========================================================
"""
两个科室的用药清单：
  internal = {"阿司匹林", "美托洛尔", "阿莫西林", "奥美拉唑"}
  surgical = {"布洛芬", "阿莫西林", "头孢克肟", "奥美拉唑"}

请计算并输出：
  1. 两个科室都使用的药品（交集）
  2. 内科使用但外科不使用的药品（差集）
  3. 两个科室的所有药品并集（去重后，按字母排序输出）
  4. (元组操作) 现有数据 point = (3, 7, 2, 9, 5)，用元组解包取出第一个和最后一个元素
"""
# 在这里写代码
#1
internal = {"阿司匹林", "美托洛尔", "阿莫西林", "奥美拉唑"}
surgical = {"布洛芬", "阿莫西林", "头孢克肟", "奥美拉唑"}
print(internal.intersection(surgical))
#2
print(internal-surgical)
#3
k = sorted(internal.union(surgical))
print(k)
#4
point = (3, 7, 2, 9, 5)
first,*_,last = point
print(f'第一个元素是{first},最后一个是{last}')
# ========================================================
# 第10题：综合实战（难度 ⭐⭐⭐⭐）
# ========================================================
"""
模拟简单的门诊叫号系统。

已有数据：
  queue = [
      {"name": "赵敏", "dept": "内科", "arrival": 1},
      {"name": "钱磊", "dept": "外科", "arrival": 2},
      {"name": "孙丽", "dept": "内科", "arrival": 3},
      {"name": "周强", "dept": "儿科", "arrival": 4},
      {"name": "吴昊", "dept": "外科", "arrival": 5},
      {"name": "郑爽", "dept": "内科", "arrival": 6},
  ]

请实现以下功能（每题在同一个程序中依次完成，用空行或注释分隔）：

  a) 显示当前所有排队患者（格式："1号-赵敏(内科)"）

  b) 叫号函数 call_next(queue)：按 arrival 顺序叫号，
     叫到的人从列表中移除，并返回其信息。
     输出 "请 赵敏 到 内科 诊室就诊"
     如果队列为空，输出 "当前没有候诊患者"

  c) 统计函数 stats(queue)：统计并返回每个科室的候诊人数，
     如 {"内科": 3, "外科": 2, "儿科": 1}

  d) 插队函数 cut_in(queue, name, dept, position=1)：
     在指定位置插入一个患者（arrival 按顺序重新编号）

  e) 批量过号函数 skip_patients(queue, names)：
     传入一个姓名列表，将这些患者从队列移除（模拟过号）
     返回移除的患者列表

  f) 主流程：用以上函数模拟以下场景：
     - 显示初始队列
     - 叫号 2 次
     - 插队一个新患者"冯磊(内科)"到第 2 位
     - 叫号 1 次
     - 跳过"周强"和"郑爽"
     - 显示最终队列和每个科室的统计
"""

queue = [
    {"name": "赵敏", "dept": "内科", "arrival": 1},
    {"name": "钱磊", "dept": "外科", "arrival": 2},
    {"name": "孙丽", "dept": "内科", "arrival": 3},
    {"name": "周强", "dept": "儿科", "arrival": 4},
    {"name": "吴昊", "dept": "外科", "arrival": 5},
    {"name": "郑爽", "dept": "内科", "arrival": 6},
]

def display(queue):
    if not queue:
        print("当前队列为空")
    else:
        for i, p in enumerate(queue, start=1):
            print(f"{i}号-{p['name']}({p['dept']})")

def call_next(queue):
    if not queue:
        print("当前没有候诊患者")
        return None
    patient = queue.pop(0)
    print(f"请 {patient['name']} 到 {patient['dept']} 诊室就诊")
    renumber(queue)
    return patient

def stats(queue):
    dept_count = {}
    for p in queue:
        dept_count[p['dept']] = dept_count.get(p['dept'], 0) + 1
    return dept_count

def cut_in(queue, name, dept, position=1):
    new_patient = {"name": name, "dept": dept, "arrival": 0}
    idx = position - 1
    if idx < 0:
        idx = 0
    elif idx > len(queue):
        idx = len(queue)
    queue.insert(idx, new_patient)
    renumber(queue)
    print(f"插队成功：{name}({dept}) 插入到第 {position} 位")

def skip_patients(queue, names):
    removed = []
    for i in range(len(queue) - 1, -1, -1):
        if queue[i]['name'] in names:
            removed.append(queue.pop(i))
    removed.reverse()
    renumber(queue)
    return removed

def renumber(queue):
    for i, p in enumerate(queue, start=1):
        p['arrival'] = i

print("=" * 30)
print("初始队列：")
display(queue)
print()

print("呼叫第1次：")
call_next(queue)
print("呼叫第2次：")
call_next(queue)
print()

print("插队：冯磊(内科) 到第2位")
cut_in(queue, "冯磊", "内科", position=2)
print("当前队列：")
display(queue)
print()

print("呼叫第3次：")
call_next(queue)
print()

print("跳过患者：周强、郑爽")
skipped = skip_patients(queue, ["周强", "郑爽"])
print(f"被过号的患者：{[p['name'] for p in skipped]}")
print()

print("最终队列：")
display(queue)
print()

print("科室统计：")
dept_stats = stats(queue)
for dept, count in dept_stats.items():
    print(f"{dept}: {count}人")