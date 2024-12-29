
`Python`的`random`模块用于生成伪随机数以及执行随机操作，它提供了多种方法可以处理随机数、随机选择、打乱序列。

## 1. 生成随机数

### 随机浮点数

- **`random()`**: 生成一个`0`到`1`之间的随机浮点数(左闭右开区间) 
```python
>>> import random as r
>>> print(r.random())
```

- **uniform(a, b)**: 生成一个范围在`[a, b]`的随机浮点数
```python
>>> print(r.uniform(10, 20))
```

### 随机整数

- **randint(a, b)**： 生成一个范围在`[a, b]`的随机整数
```python
>>> print(r.randint(1, 10))
```

- **randrange(start, stop, step)**: 从指定的范围内，按步长返回一个随机整数
```python
>>> print(r.randrange(1, 10, 2))
```