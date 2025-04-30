import pandas as pd
import glob
import os

os.chdir("./trand_files")
all_filenames = glob.glob("*.csv")

dfs = []
for f in all_filenames:
    try:
        df = pd.read_csv(f, encoding='utf-8')
    except UnicodeDecodeError:
        df = pd.read_csv(f, encoding='cp949')
    dfs.append(df)

combined_csv = pd.concat(dfs)
combined_csv.to_csv("combine_trend.csv", index=False, encoding='utf-8-sig')
