file = open("0627.txt")

# readlines() 方法一次性讀取所有行，並返回一個列表，這樣可以方便地對文件中的所有行進行處理。但缺點是可能造成 RAM 太滿
print(file.readlines())

file.seek(0)
for line in file.readlines():
    print(line)