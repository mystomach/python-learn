def calculate_bmi(weight: float, height: float) -> float:
    return weight / (height ** 2)


def check_blood_pressure(sbp: int, dbp: int) -> str:
    if sbp >= 140 or dbp >= 90:
        return "高血压"
    if sbp < 90 or dbp < 60:
        return "低血压"
    return "正常"
