print("H1, it's a python world !")

import pandas as pd

# 엑셀 파일에서 숫자 데이터 읽기
file_path = "scores.xlsx"  # 엑셀 파일 경로를 입력하세요
column_name = "점수"       # 점수가 저장된 열 이름을 입력하세요

try:
    df = pd.read_excel(file_path)
    if column_name in df.columns:
        scores = df[column_name].dropna()
        if not scores.empty:
            average = scores.mean()
            print(f"{column_name}의 평균은 {average:.2f} 입니다.")
        else:
            print("점수 데이터가 없습니다.")
    else:
        print(f"'{column_name}' 열이 엑셀 파일에 없습니다.")
except FileNotFoundError:
    print("엑셀 파일을 찾을 수 없습니다.")
except Exception as e:
    print(f"오류 발생: {e}")
    