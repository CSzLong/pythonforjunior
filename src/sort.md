## 排序算法

常见的排序算法有：冒泡排序，选择排序，插入排序。

### 数据准备

```python
import random as r
n = int(input("请输入列表元素的个数："))
lst = []
for i in range(n):
    a = r.randint(-200, 200)
    while a in lst:
        a = r.randint(-200, 200)
    lst.append(a)
```

### 冒泡排序

冒泡排序（Bubble Sort）是一种简单直观的排序算法。它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢"浮"到数列的顶端。

```python
def bubble_sort(ls, reverse=False):
    n = len(ls)
    for i in range(n-1):
        for j in range(n-1-i):
            if reverse:
                if ls[j] < ls[j+1]:
                    ls[j], ls[j+1] = ls[j+1], ls[j]
            else:
                if ls[j] > ls[j+1]:
                    ls[j], ls[j+1] = ls[j+1], ls[j]
            print(ls)

if __name__ == '__main__':
    print(lst)
    bubble_sort(lst, True)
    print(lst)

"""
请输入列表元素的个数：10
[-125, 92, 6, 23, -147, 161, -20, 121, 127, 148]
[161, 148, 127, 121, 92, 23, 6, -20, -125, -147]
"""
```         

### 选择排序

选择排序（Selection sort）是一种简单直观的排序算法。它的工作原理如下。首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。

步骤：
1. 首先默认第一个位置的值最小(大)；
2. 再依次和后面的数进行比较，如果有比当前最小值还要小(大)的数，则重新定义最小值的位置，直到最后一个位置判断结束；
3. 将最小值位置上的数和第一个位置上的数交换；
4. 依次对后面的位置进行上述操作。

```python
def selection_sort(ls, reverse=False):
    n = len(ls)
    for i in range(n - 1):
        flag = i
        for j in range(i + 1, n):
            if reverse:
                if ls[flag] < ls[j]:
                    flag = j
            else:
                if ls[flag] > ls[j]:
                    flag = j
        ls[i], ls[flag] = ls[flag], ls[i]
        print(ls)
```         

选择排序有另外一种写法，效率会低于上面一种：
```python
def selection_sort(ls, reverse=False):
    n = len(ls)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if reverse:
                if ls[i] < ls[j]:
                    ls[i], ls[j] = ls[j], ls[i]
            else:
                if ls[i] > ls[j]:
                    ls[i], ls[j] = ls[j], ls[i]
        print(ls)
```   


### 二分法查找

二分法查找要求要查找的序列`seq`先排序，再根据起始位置(`start`和`end`)确定一个中间位置`mid`(mid=(start + end)//2)，根据要查找的关键字`key`和中间位置的元素做比较:

如果`key` > `seq[mid]`，则将start = mid + 1,再重新计算出`mid`
如果`key` < `seq[mid]`，则将end = mid - 1,再重新计算出`mid`

直到找到`key`或者`start`==`end`结束