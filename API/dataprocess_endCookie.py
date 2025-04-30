import pandas as pd

# food.csv 파일 전체 읽기
df = pd.read_csv('food.csv')

# '식품명' 컬럼 처리 함수 정의
def rearrange_name(name):
    if '_' in str(name):
        front, back = name.split('_', 1)
        return back + front
    else:
        return name

# '식품명' 컬럼에 함수 적용
df['식품명'] = df['식품명'].apply(rearrange_name)

# 결과를 새로운 CSV 파일로 저장
df.to_csv('food_modified.csv', index=False)
