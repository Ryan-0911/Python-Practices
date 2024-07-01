# 定義一個包含字符串的列表
names = ["John", "Jane", "Alice", "Bob"]

# 使用 sort() 方法按字母逆序排序
names.sort(key=lambda x: x[::-1])

# 打印按字母逆序排序後的列表
print("按字母逆序排序後的列表:", names)
# 輸出: 按字母逆序排序後的列表: ['John', 'Jane', 'Alice', 'Bob']