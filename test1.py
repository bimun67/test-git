print("Hi, it's a wonderful world!")

# 성적 계산 프로그램

def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

try:
    score = float(input("점수를 입력하세요 (0~100): "))
    if 0 <= score <= 100:
        grade = calculate_grade(score)
        print(f"당신의 성적은 {grade} 입니다.")
    else:
        print("점수는 0에서 100 사이여야 합니다.")
except ValueError:
    print("유효한 숫자를 입력하세요.")
