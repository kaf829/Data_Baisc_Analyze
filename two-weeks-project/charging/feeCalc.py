import pandas as pd

fp_simple_detail = {
    "입력(EI)": 3,
    "출력(EO)": 4,
    "조회(EQ)": 3,
    "내부 논리 파일(ILF)": 7,
    "외부 인터페이스 파일(EIF)": 5
}

fp_counts_detail = {
    "입력(EI)": 3,
    "출력(EO)": 4,
    "조회(EQ)": 2,
    "내부 논리 파일(ILF)": 2,
    "외부 인터페이스 파일(EIF)": 2
}

fp_result_detailed = {
    k: {
        "수량": fp_counts_detail[k],
        "단위점수": fp_simple_detail[k],
        "총점수": fp_counts_detail[k] * fp_simple_detail[k]
    } for k in fp_counts_detail
}

total_fp_detailed = sum([v["총점수"] for v in fp_result_detailed.values()])
total_mm_detailed = round(total_fp_detailed * 0.175, 2)

# 결과 출력
df_detailed = pd.DataFrame(fp_result_detailed).T
df_detailed.loc["총합"] = ["-", "-", total_fp_detailed]

print(df_detailed)
print(f"총 기능점수: {total_fp_detailed}")
print(f"총 개발 공수 (MM): {total_mm_detailed}")
