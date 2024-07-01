# 載入 pandas 模組
import pandas as pd

# 篩選- Series
# 數字
dataSum = pd.Series([30, 15, 20])
condition = dataSum > 18
print(condition) # List (元素是 True 和 False)
filteredDataSum = dataSum[condition] 
print(filteredDataSum)

# 字串 
dataStr = pd.Series(["您好", "Python", "Pandas"])
condition = dataStr.str.contains("P")
print(condition)
filteredDataStr = dataStr[condition]
print(filteredDataStr)

# 篩選- DataFrame
df = pd.DataFrame({
    "name": ["Amy", "Bob", "Chales"],
    "salary": [30000, 50000, 40000]
})
condition = df["salary"] >= 40000 
filterDF = df[condition]
print(filterDF)
