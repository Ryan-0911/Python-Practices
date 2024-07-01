file = open("0627.txt")

# readline() 方法每次只讀取文件中的一行，並且每次調用會依次讀取下一行，直到文件結尾。
while True:
    line = file.readline()
    if not line:
        break
    else:
        print(line)