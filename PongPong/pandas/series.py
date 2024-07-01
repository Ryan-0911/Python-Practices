# 載入 pandas 模組
import pandas as pd

# 資料索引 (要跟資料數量一樣)
dataNum = pd.Series([5, 4, -2, 3, 7], index = ["a", "b", "c", "d", "e"])
print(dataNum)

# 觀察資料
print("資料型態", dataNum.dtype)
print("資料數量", dataNum.size)
print("資料索引", dataNum.index)

# 取得資料: 根據數字、根據索引
print(dataNum[2], dataNum[0])
print(dataNum["e"], dataNum["d"])


# 數字運算: 基本、統計、順序
print("最大值", dataNum.max())
print("總和", dataNum.sum())
print("標準差", dataNum.std())
print("中位數", dataNum.median())
print("最大三位數", "\n", dataNum.nlargest(3))
print("最小兩位數", "\n", dataNum.nsmallest(2))

#-----------------------------------------------------------------------
# 字串運算: 基本、串接、搜尋、取代
dataStr = pd.Series(["您好", "Python", "Pandas"])
print(dataStr.str.lower()) # 全部轉小寫
print(dataStr.str.len()) # 算出每個字串長度
print(dataStr.str.cat(sep=",")) # 將字串串起來
print(dataStr.str.contains("P")) # 確認是否包含指定字串 (回傳 True 或 False)
print(dataStr.str.replace("您好", "Hello")) # 將參數1取代成參數2