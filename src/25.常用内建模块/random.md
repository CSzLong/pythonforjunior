
`Python`的`random`模块用于生成伪随机数以及执行随机操作，它提供了多种方法可以处理随机数、随机选择、打乱序列。

## 1. 生成随机数

### 随机浮点数

- **`random()`**: 生成一个`0`到`1`之间的随机浮点数(左闭右开`[0, 1)`区间) 
```python
>>> import random as r
>>> print(r.random())
```

- **uniform(a, b)**: 生成一个范围在`[a, b]`的随机浮点数
```python
>>> print(r.uniform(10, 20))
```

要区分`[]`和函数调用时用到的`()`，一般情况下，`[]`操作符的使用，内部参数用`:`隔开，而函数调用传入参数时，用`,`隔开。
### 随机整数

- **randint(a, b)**： 生成一个范围在`[a, b]`的随机整数
```python
>>> print(r.randint(1, 10)) # 可返回1,2,3,4,5,6,7,8,9,10
```

- **randrange(start, stop, step)**: 从指定的范围内，按步长返回一个随机整数
```python
>>> print(r.randrange(1, 10, 2)) # 可返回1，3，5，7，9
```

## 2. 随机选择

### 从序列中随机选择元素

- **choice(seq)**: 从非空序列`seq`中随机选择一个元素。
```python
>>> items = ['apple', 'banana', 'cherry', 'peach', 'watermelon', 'pear']
>>> print(r.choice(items))
>>> r.choice('abcdefghi')
```

- **sample(population, k)**: 从指定序列中随机选择`k`个不重复的元素，返回的结果是一个列表。这其中所谓的不重复是指索引。

```python
>>> print(r.sample(items, 3))
```

- **choices(population,  k=1)**: 从指定的序列中随机选择`k`个元素，可以指定权重，允许重复。
```python
>>> print(r.choices(items, k=4))
```


## 3.  打印顺序

- **shuffle(x)**：原地打印序列的顺序，无返回值。

```python
>>> deck = [n for n in range(1, 11)]
>>> print(deck) # 输出[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> r.shuffle(deck)
>>> print(deck) # 输出可能为[4, 9, 7, 6, 10, 2, 8, 3, 5, 1]
```