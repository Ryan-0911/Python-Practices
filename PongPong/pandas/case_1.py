import pandas as pd

# 讀取資料
df = pd.read_csv("googleplaystore.csv") # 把 csv 格式檔案讀成一個 DataFrame
print(df)

# 觀察資料- 評分的各種統計資料
print("資料數量", df.shape)
print("資料欄位", df.columns)

# 分析資料- 評分的各種統計數據
print("平均數", df["Rating"].mean())
print("中位數", df["Rating"].median())
print("前一百個應用程式的平均數", df["Rating"].nlargest(100).mean())

# 因為前一百個應用程式的平均數是 5.14，超過了 5 分，所以檢查是哪些資料有問題
condition = df["Rating"] > 5
df = df[condition]
print(df)

# 分析資料- 評分的各種統計數據
df = pd.read_csv("googleplaystore.csv") # 把 csv 格式檔案讀成一個 DataFrame
condition = df["Rating"] <= 5
df = df[condition]
print("平均數", df["Rating"].mean())
print("中位數", df["Rating"].median())
print("前一百個應用程式的平均數", df["Rating"].nlargest(1000).mean())

# 分析資料- 安裝數量的各種統計數據
df = pd.read_csv("googleplaystore.csv") # 把 csv 格式檔案讀成一個 DataFrame
# 資料清理後轉換型態
df["Installs"] = pd.to_numeric(df["Installs"].str.replace("[,+]", "", regex=True).replace("Free", ""))
print(df)
print("平均數", df["Installs"].mean())
condition = df["Installs"] > 100000
print("安裝數大於 100000 的應用程式有幾個", df[condition].shape[0])

# 基於資料的應用- 關鍵字搜尋應用程式名稱
keyword = input("請輸入關鍵字： ")
condition = df["App"].str.contains(keyword, case=False)
print(df[condition]["App"])
print("包含關鍵字的應用程式數量: ", df[condition]["App"].shape[0])