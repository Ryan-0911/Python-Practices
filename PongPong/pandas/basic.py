# 載入 pandas 模組
import pandas as pd

# 建立 Series (一維)
data = pd.Series([20, 10, 15])
print(data)

# 各種運算
print("Max", data.max())
print("Mediun", data.median())
print(data * 2)
print(data == 20)

# 建立 DataFrame
df = pd.DataFrame({"name": ["Amy", "John", "Bob"],
                     "salary": [30000, 50000, 40000]})
print(df)

# 取得特定的欄
print(df["name"])

# 取得特定的列
print(df.iloc[1])