# 사회·과학탐구 영역 중 일부 과목(예시: 생활과 윤리, 윤리와 사상, 한국지리)을 수작업으로 구성
import pandas as pd

df_tankoo = pd.DataFrame({
    '등급': list(range(1, 10)),

    '국어_등급구분점수': [133, 125, 116, 106, 95, 84, 73, 63, '63미만'],
    '국어_인원(명)': [18015, 32787, 56275, 78603, 86708, 73569, 51976, 28597, 16560],
    '국어_비율(%)': [4.07, 7.40, 12.70, 17.74, 19.57, 16.60, 11.73, 6.45, 3.74],


    '수학_등급구분점수': [133, 126, 118, 107, 94, 80, 74, 70, '70미만'],
    '수학_인원(명)': [17910, 32921, 50248, 69816, 85517, 76134, 50532, 29913, 13634],
    '수학_비율(%)': [4.20, 7.72, 11.78, 16.36, 20.05, 17.85, 11.84, 7.01, 3.20],

    '생활과 윤리_등급구분점수': [65, 63, 59, 54, 48, 42, 36, 32, '32미만'],
    '생활과 윤리_인원(명)': [6357, 11087, 16020, 23980, 25796, 22737, 18047, 9260, 4074],
    '생활과 윤리_비율(%)': [4.63, 8.08, 11.67, 17.40, 18.49, 16.56, 13.15, 6.74, 2.97],

    '윤리와 사상_등급구분점수': [63, 61, 58, 55, 46, 41, 37, 33, '33미만'],
    '윤리와 사상_인원(명)': [4241, 6617, 5717, 4645, 8017, 5433, 4548, 2233, 1258],
    '윤리와 사상_비율(%)': [11.75, 18.34, 15.84, 12.87, 22.21, 14.80, 12.60, 6.46, 3.48],

    '한국지리_등급구분점수': [65, 63, 61, 54, 45, 40, 38, 36, '36미만'],
    '한국지리_인원(명)': [2350, 2817, 2438, 5271, 6902, 6275, 3486, 1552, 795],
    '한국지리_비율(%)': [7.37, 8.83, 7.65, 16.53, 21.65, 19.68, 10.93, 4.87, 2.49],

    # 동아시아사
    '동아시아사_등급구분점수': [66, 63, 60, 55, 46, 40, 37, 34, '34미만'],
    '동아시아사_인원(명)': [1522, 1792, 2755, 4487, 5157, 5512, 2307, 1523, 646],
    '동아시아사_비율(%)': [5.92, 6.97, 10.72, 17.46, 20.07, 21.45, 8.98, 5.93, 2.51],

    # 세계지리
    '세계지리_등급구분점수': [63, 60, 57, 52, 45, 42, 37, 35, '35미만'],
    '세계지리_인원(명)': [1293, 745, 2095, 3500, 3500, 2843, 2143, 842, 651],
    '세계지리_비율(%)': [7.45, 4.29, 12.07, 20.16, 20.16, 16.38, 14.00, 4.85, 3.75],

    # 세계사
    '세계사_등급구분점수': [66, 62, 60, 55, 46, 45, 41, 36, '36미만'],
    '세계사_인원(명)': [1402, 955, 1794, 2167, 2970, 2863, 1686, 923, 370],
    '세계사_비율(%)': [6.30, 4.29, 11.83, 14.82, 19.58, 19.58, 11.11, 6.08, 2.70],

    # 경제
    '경제_등급구분점수': [68, 63, 59, 52, 46, 41, 37, 36, '36미만'],
    '경제_인원(명)': [207, 429, 550, 987, 783, 840, 717, 193, 182],
    '경제_비율(%)': [4.23, 8.78, 11.25, 20.19, 16.02, 17.18, 14.67, 3.95, 3.72],

    # 정치와 법
    '정치와 법_등급구분점수': [67, 64, 59, 53, 46, 41, 37, 33, '33미만'],
    '정치와 법_인원(명)': [1259, 1458, 3389, 4003, 4783, 4786, 2101, 1825, 822],
    '정치와 법_비율(%)': [5.15, 5.97, 13.87, 16.39, 19.58, 19.59, 8.60, 7.47, 3.37],

    # 사회문화
    '사회문화_등급구분점수': [66, 63, 59, 54, 47, 41, 36, 33, '33미만'],
    '사회문화_인원(명)': [5374, 9399, 16667, 19492, 23591, 20265, 16235, 8405, 2234],
    '사회문화_비율(%)': [4.42, 7.73, 13.70, 16.39, 19.96, 16.66, 13.34, 6.91, 1.84],

    # 지구과학Ⅰ
    '지구과학Ⅰ_등급구분점수': [65, 63, 58, 54, 47, 40, 36, 30, '33미만'],
    '지구과학Ⅰ_인원(명)': [11098, 9512, 24228, 21634, 29779, 31963, 14248, 10586, 4213],
    '지구과학Ⅰ_비율(%)': [7.08, 6.07, 15.46, 13.81, 19.01, 20.35, 9.09, 6.73, 2.69],

    # 물리학Ⅱ
    '물리학Ⅱ_등급구분점수': [71, 66, 58, 50, 45, 42, 40, 37, '37미만'],
    '물리학Ⅱ_인원(명)': [159, 331, 508, 696, 810, 691, 311, 277, 126],
    '물리학Ⅱ_비율(%)': [4.18, 8.70, 10.57, 18.30, 21.30, 18.17, 8.18, 7.23, 3.31],

    # 화학Ⅱ
    '화학Ⅱ_등급구분점수': [70, 64, 58, 50, 45, 42, 40, 36, '36미만'],
    '화학Ⅱ_인원(명)': [257, 378, 601, 686, 818, 753, 452, 300, 101],
    '화학Ⅱ_비율(%)': [7.11, 10.45, 16.63, 18.98, 22.64, 20.84, 12.51, 8.34, 2.79],

    # 생명과학Ⅱ
    '생명과학Ⅱ_등급구분점수': [69, 65, 59, 52, 45, 42, 38, 37, '37미만'],
    '생명과학Ⅱ_인원(명)': [234, 422, 701, 878, 1361, 704, 974, 88, 221],
    '생명과학Ⅱ_비율(%)': [4.19, 7.56, 12.56, 15.73, 24.33, 12.61, 17.43, 1.58, 3.96],

    # 지구과학Ⅱ
    '지구과학Ⅱ_등급구분점수': [70, 65, 58, 50, 45, 42, 39, 35, '37미만'],
    '지구과학Ⅱ_인원(명)': [178, 295, 480, 706, 782, 696, 415, 285, 139],
    '지구과학Ⅱ_비율(%)': [4.33, 7.18, 11.68, 17.19, 19.37, 17.23, 10.27, 6.93, 3.38],

    # 물리학Ⅰ
    '물리학Ⅰ_등급구분점수': [67, 63, 60, 53, 48, 40, 38, 35, '35미만'],
    '물리학Ⅰ_인원(명)': [2959, 6230, 5550, 8290, 11126, 12769, 5059, 4696, 1944],
    '물리학Ⅰ_비율(%)': [4.68, 9.86, 8.79, 20.31, 17.62, 20.22, 8.01, 7.43, 3.08],

    # 화학Ⅰ
    '화학Ⅰ_등급구분점수': [67, 62, 59, 54, 48, 40, 37, 32, '33미만'],
    '화학Ⅰ_인원(명)': [2767, 6090, 5756, 8225, 12223, 10480, 6067, 4868, 1065],
    '화학Ⅰ_비율(%)': [4.73, 10.27, 11.54, 14.16, 20.89, 17.91, 10.37, 4.32, 3.08],

    # 생명과학Ⅰ
    '생명과학Ⅰ_등급구분점수': [66, 62, 59, 53, 48, 42, 36, 32, '32미만'],
    '생명과학Ⅰ_인원(명)': [7274, 16101, 15117, 32266, 21221, 26171, 12611, 10404, 4333],
    '생명과학Ⅰ_비율(%)': [4.94, 10.93, 10.27, 21.91, 17.44, 17.77, 10.22, 7.06, 2.94],
})

# 저장
excel_path = "data_make.xlsx"
df_tankoo.to_excel(excel_path, index=False)


