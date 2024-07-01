# 載入 Pandas 模組
import pandas as pd

# 以字典為底，建立 DataFrame
# index 如果不寫，就是採用內建索引
df = pd.DataFrame(
    {
        "name": ["Amy", "Bob", "Charles"],
        "salary": [30000, 50000, 40000]
    }, index = ["a", "b", "c"]
)
print(df)

# 觀察資料
print("資料數列", df.size)
print("資料型態 (列, 欄)", df.shape)
print("資料數列", df.index)

# 取得單維度的列或欄，就是 Series 型態
# 取得列的 Series 資料
print("取得第二列", df.iloc[1], sep="\n") # 根據順序
print("取得第c列", df.loc["c"], sep="\n") # 根據順序

# 取得欄的 Series 型態
print("取得 name 的欄位", df["name"], sep="\n") # 根據順序
names = df["name"]
print("把 name 全部轉大寫", names.str.upper(), sep="\n")

# 計算薪水平均值
salaries = df["salary"]
print("薪水平均值", salaries.mean())

# 建立新的欄位 
df["revenue"] = [500000, 400000, 300000] # df[新欄位名稱] = 列表
df["rank"] = pd.Series([3, 6, 1], index = ["a", "b", "c"]) # df[新欄位名稱] = Series 資料
df["cp"] = df["revenue"] / df["salary"]
print(df)