class Patient:
    def __init__(self, name: str, age: int, diagnosis: str):
        self.name = name
        self.age = age
        self.diagnosis = diagnosis

    def info(self) -> str:
        return f"姓名：{self.name} | 年龄：{self.age} | 诊断：{self.diagnosis}"
