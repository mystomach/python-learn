"""
测试题 2：函数进阶 + 模块 + 面向对象
==============================================
说明：每道题写完后运行验证，确认无误后喊我检查。
如果卡住超过 15 分钟，先跳过做后面的，回头再补。
"""

# ========================================================
# 第1题：函数定义与参数类型（难度 ⭐⭐）
# ========================================================
"""
完成三个函数：

1.1 位置参数 + 默认参数
  def create_doctor(name, specialty, hospital="卫宁健康"):
      返回 f"{name} 医生，{specialty}，就职于 {hospital}"

1.2 不定长参数 *args
  def avg_score(*scores):
      计算传入的所有分数的平均值
      如果没有传入任何分数，返回 0.0

1.3 关键字不定长参数 **kwargs
  def patient_info(name, **kwargs):
      输出格式：
        患者：张三
        年龄：45
        科室：心内科
      （kwargs 里的键值对逐行输出，不预设有哪些键）

测试代码：
  print(create_doctor("李华", "心内科"))
  print(create_doctor("王芳", "神经外科", "华山医院"))
  print(avg_score(85, 90, 78, 92))   # 应为 86.25
  print(avg_score())                   # 应为 0.0
  patient_info("张三", age=45, dept="心内科", bed="12A")
"""
def create_doctor(name,specialty,hospital = '卫宁健康'):
    return (f'{name} 医生，{specialty}，就职于 {hospital}')
print(create_doctor('李华','心内科'))
print(create_doctor("王芳", "神经外科", "华山医院"))

def avg_score(*args):
    if not args:
       return 0.0
    return sum(args)/len(args) 
print(avg_score(85, 90, 78, 92))   # 应为 86.25
print(avg_score())                   # 应为 0.0

def patient_info(name, **kwargs):
    """输出患者信息，包括姓名和任意数量的关键字参数。"""
    print(f"患者：{name}")
    for key, value in kwargs.items():
        print(f"{key}：{value}")

patient_info("张三", age=45, dept="心内科", bed="12A")
# ========================================================
# 第2题：变量作用域（难度 ⭐⭐）
# ========================================================
"""
观察并理解以下代码的输出。先写出你的预期，然后运行验证。

global_count = 0

def visit():
    global global_count
    local_count = 0
    global_count += 1
    local_count += 1
    return f"第 {global_count} 次访问，本地计数 {local_count}"

请回答（写注释）：
  1. 连续调用 visit() 三次，输出分别是什么？为什么 global_count 每次都增加，
     而 local_count 始终为 1？
  2. 如果把 global global_count 这行注释掉，运行会怎样？为什么？
"""
#global_count增加是因为在函数内部已经通过global的方法，将之给全局变量了，也就是在这个函数运行后，会根据函数的变化来变化global_count的数值，但是local_count
#没有修改过全局变量，函数一停，立马回退到原味。三次输出一次如下，第1次访问，本地计数1；第2次访问，本地计数1；第3次访问，本地计数1
#注释掉函数的第一行，那就会不断输出第1次访问，本地计数1，因为每次运行，内部的局部变量会覆盖掉外面设定好的全局变量，在结束后回退。
global_count = 0

def visit():
    # global global_count
    local_count = 0
    global_count += 1
    local_count += 1
    return f"第 {global_count} 次访问，本地计数 {local_count}"
print(visit())
print(visit())
print(visit())
# ========================================================
# 第3题：lambda + 高阶函数（难度 ⭐⭐⭐）
# ========================================================
"""
现有数据：
  medicines = [
      {"name": "阿莫西林", "price": 8.5, "stock": 300},
      {"name": "布洛芬",   "price": 12.0, "stock": 80},
      {"name": "头孢克肟", "price": 25.0, "stock": 150},
      {"name": "奥美拉唑", "price": 32.0, "stock": 45},
  ]

请用 lambda + 内置函数完成：
  1. 按价格从高到低排序，输出药品名列表
  2. 用 filter() 筛选出库存 < 100 的药品（需补货的）
  3. 用 map() 提取所有药品名称，加后缀 "（处方药）"
     输出 ["阿莫西林（处方药）", "布洛芬（处方药）", ...]
  4. 用 max() 配合 lambda 找出总价最高的药品(price * stock)
"""
# 在这里写代码


# ========================================================
# 第4题：递归（难度 ⭐⭐⭐）
# ========================================================
"""
4.1 写一个递归函数 factorial(n) 计算 n!（n 的阶乘）
    要求：包含递归终止条件，n < 0 时返回 None

4.2 写一个递归函数 fibonacci(n) 返回第 n 个斐波那契数
    （改进：思考如果 n 很大比如 40 会怎样？效率问题？）

4.3 思考题（写注释回答）：
    递归和循环都可以解决的问题，什么场景下优先用递归？
    递归有什么风险？
"""
# 在这里写代码


# ========================================================
# 第5题：类型注解（难度 ⭐⭐）
# ========================================================
"""
给以下函数补全类型注解：

# 示例：
def add(a: int, b: int) -> int:
    return a + b

def get_patient(name: ____, age: ____, diagnosis: ____) -> ____:
    return {"name": name, "age": age, "diagnosis": diagnosis}

def process_scores(scores: ____) -> ____:
    # scores 是整数列表，返回 (平均分, 最高分, 最低分) 元组
    avg = sum(scores) / len(scores)
    return (avg, max(scores), min(scores))

def find_medicine(pharmacy: ____, keyword: ____) -> ____:
    # pharmacy 是 {科室名: [药品名列表]}，keyword 是字符串
    # 返回包含 keyword 的药品名列表
    result = []
    for meds in pharmacy.values():
        for med in meds:
            if keyword in med:
                result.append(med)
    return result

测试：
  print(get_patient("赵敏", 45, "高血压"))
  print(process_scores([85, 90, 78, 92]))
  print(find_medicine({"内科": ["阿司匹林", "美托洛尔"]}, "阿"))
"""
# 在这里写代码


# ========================================================
# 第6题：模块与包（难度 ⭐⭐）
# ========================================================
"""
请创建一个包结构如下：

mymedical/
    __init__.py    （可以为空，或写一些导入）
    utils.py       （放工具函数）
    models.py      （放数据模型类）

utils.py 要求：
  - 函数 calculate_bmi(weight, height) → float
  - 函数 check_blood_pressure(sbp, dbp)
    sbp>=140 或 dbp>=90 返回 "高血压"
    sbp<90 或 dbp<60 返回 "低血压"
    否则返回 "正常"

models.py 要求：
  - 类 Patient，有 name, age, diagnosis 三个属性
  - 有一个 info() 方法返回 "姓名：xxx | 年龄：xx | 诊断：xxx"

然后在当前文件用以下代码测试：
  from mymedical.utils import calculate_bmi, check_blood_pressure
  from mymedical.models import Patient

  print(calculate_bmi(75, 1.78))
  print(check_blood_pressure(145, 95))
  p = Patient("李华", 58, "冠心病")
  print(p.info())
"""
# 请先创建 mymedical 目录和文件，然后取消下面的注释运行测试：
# from mymedical.utils import calculate_bmi, check_blood_pressure
# from mymedical.models import Patient


# ========================================================
# 第7题：面向对象——类与对象（难度 ⭐⭐）
# ========================================================
"""
创建一个 Doctor 类：
  - 类属性：hospital = "卫宁健康"
  - 实例属性：name, department, patients（已接诊患者列表，默认为空列表）
  - 实例方法：
    def admit(self, patient_name):    // 接诊患者，添加到 patients 列表
    def discharge(self, patient_name): // 出院，从列表移除
    def summary(self):                 // 返回 "王医生（心内科）已接诊 3 位患者"

测试代码：
  d1 = Doctor("王强", "心内科")
  d1.admit("赵敏")
  d1.admit("钱磊")
  d1.admit("孙丽")
  print(d1.summary())
  d1.discharge("钱磊")
  print(d1.summary())
  print(f"所属医院：{Doctor.hospital}")
"""
class Doctor:
    hospital = "卫宁健康"

    def __init__(self, name, department):
        self.name = name
        self.department = department
        self.patients = []  # 已接诊患者列表

    def admit(self, patient_name):
        self.patients.append(patient_name)

    def discharge(self, patient_name):
        if patient_name in self.patients:
            self.patients.remove(patient_name)

    def summary(self):
        return f"{self.name}医生（{self.department}）已接诊 {len(self.patients)} 位患者"


# 测试代码
d1 = Doctor("王强", "心内科")
d1.admit("赵敏")
d1.admit("钱磊")
d1.admit("孙丽")
print(d1.summary())
d1.discharge("钱磊")
print(d1.summary())
print(f"所属医院：{Doctor.hospital}")


# ========================================================
# 第8题：魔法方法（难度 ⭐⭐⭐）
# ========================================================
"""
实现一个 Medication（药品）类，要求：

  __init__(self, name, price, stock):
    初始化药品名、单价、库存

  __str__(self):
    返回 "阿莫西林(¥8.5) 库存:300"

  __repr__(self):
    返回 "Medication(name='阿莫西林', price=8.5, stock=300)"
    （方便调试时看到完整信息）

  __eq__(self, other):
    两个药品如果 name 相同则视为相等

  __lt__(self, other):
    按价格比较（用于排序）

  def value(self):
    返回总价值 price * stock（库存总价值）

测试代码：
  m1 = Medication("阿莫西林", 8.5, 300)
  m2 = Medication("布洛芬", 12.0, 80)
  m3 = Medication("阿莫西林", 8.5, 200)  # 和 m1 同名不同库存

  print(m1)                     # __str__
  print([m1, m2])               # 会触发 __repr__
  print(m1 == m3)               # 应为 True（同名即相等）
  print(m1 == m2)               # 应为 False
  print(m1 < m2)                # 应为 True（8.5 < 12.0）
  print(m1.value())             # 2550.0
"""
# 在这里写代码


# ========================================================
# 第9题：实例属性 vs 类属性（难度 ⭐⭐）
# ========================================================
"""
完成以下代码并回答注释中的问题：

class Employee:
    hospital = "卫宁健康"      # 类属性
    count = 0                   # 类属性

    def __init__(self, name):
        self.name = name        # 实例属性
        Employee.count += 1     # 每创建一个实例 count+1

e1 = Employee("张三")
e2 = Employee("李四")

print(Employee.hospital)   # 输出？
print(e1.hospital)         # 输出？
print(Employee.count)      # 输出？

# 思考题（写注释回答）：
# 1. 如果把 Employee.count += 1 改成 self.__class__.count += 1，效果一样吗？
# 2. e1.hospital = "华山医院" 之后，e1.hospital 和 Employee.hospital 分别是什么？为什么？
# 3. 类属性和实例属性在内存中存储的位置有什么不同？
"""
# 在这里写代码


# ========================================================
# 第10题：综合实战——简易教务系统（难度 ⭐⭐⭐⭐）
# ========================================================
"""
实现一个学生管理系统（面向对象版）。

要求：

1. Student 类
   - 属性：stu_id, name, scores（字典，如 {"python": 85, "math": 90}）
   - 方法：total() 返回总分
   - 方法：avg() 返回平均分（保留一位小数）
   - __str__ 返回 "S001-张三(Python:85, 数学:90)"

2. StudentSystem 类
   - 属性：students（字典，key 是 stu_id，value 是 Student 对象）
   - 方法：
     def add_student(self, stu_id, name):
        添加学生（初始成绩为空字典）

     def add_score(self, stu_id, course, score):
        给学生添加一门课的成绩

     def remove_student(self, stu_id):
        删除学生

     def search(self, keyword):
        按 stu_id 或 name 搜索（keyword 可能是 id 或部分姓名）
        返回匹配的学生列表

     def top(self, n=3):
        返回总分排名前 n 的学生列表（从高到低）

     def summary(self):
        返回系统统计：
        {
            "total_students": 总人数,
            "avg_score_all": 所有学生所有课程的总平均分,
            "top_student": 总分最高的学生姓名和总分,
            "course_count": 共有多少门不同的课程,
        }

3. 主流程演示（写在 if __name__ == "__main__": 里）：
   - 创建 StudentSystem 实例
   - 添加至少 5 个学生，每个学生有 2-3 门课的成绩
   - 搜索功能展示
   - 输出总分前三名
   - 输出系统统计
"""
# 在这里写代码
