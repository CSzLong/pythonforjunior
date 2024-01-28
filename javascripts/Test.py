if __name__ == '__main__':
    print("请教官说出一个1-9之间任意数字")
    n = int(input("数字为:"))
    print("开始报数")
    for i in range(1, 151):
        if i % 10 == n or i % n == 0:
            continue
        print(i, end=' ')