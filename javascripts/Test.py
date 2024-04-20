if __name__ == '__main__':
    f = open("list_helper.txt", 'w', encoding='utf-8')
    a = list()
    print(help(a), file=f)
    f.close()