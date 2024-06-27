"""
打印出1000-9999之间的所有四叶草数:
即 千位四次方+百位四次方+十位四次方+个位四次方等于这个数

"""

for i in range(1000, 10000):
    s = str(i)
    qw, bw, sw, gw = int(s[0]), int(s[1]), int(s[2]), int(s[3])
    if i == qw ** 4 + bw ** 4 + sw ** 4 + gw ** 4:
        print(i)

"""
判断一个数是不是回文数，回文数就是将这个数反过来之后，和原数是相等的
12321是回文数
12345不是回文数
"""

n = input('Input a number:')
if n == n[::-1]:
    print('Yes')
else:
    print('No')