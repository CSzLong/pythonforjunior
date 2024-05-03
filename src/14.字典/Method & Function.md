# 内置函数

### len(iterable)

`len`返回传入的 `iterable`的长度，即元素的个数，`iterable`可以是序列、集合或者映射。

### max(iterable)/min(iterable)

`max`和`min`分别返回`iterable`的最大值和最小值，要求`iterable`里元素的类型要一致。

### str(x)

将`x`转换成字符串，并返回这个字符串, 如果没有传参数则返回空字符串`"""`。

```python
>>> str(1)
'1'
>>> str([1,2,3])
'[1,2,3]'
```

### list(iterable)

返回将`iterable`转换之后生成的列表, 如果没有传参数则返回空列表`[]`。

```python
>>> list("abcdefg")
['a','b','c','d','e','f','g']
>>> list(1)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    list(1)
TypeError: 'int' object is not iterable

>>> list()
[]
>>> list({1:2,3:4,5:6})
[1, 3, 5]
```

### tuple(iterable)

返回将`iterable`转换之后生成的元组，如果没有传参数则返回空元组`()`。

```python
>>> tuple([1,2,3,4,5,6,7])
(1, 2, 3, 4, 5, 6, 7)
>>> tuple("abcdefg")
('a', 'b', 'c', 'd', 'e', 'f', 'g')
>>> tuple()
()
```

### set(iterable)

返回将`iterable`转换之后生成的集合，如果没有传参数则返回空集合`set()`。

```python
>>> set([1,2,3,4,5,5,6,1,4])
{1, 2, 3, 4, 5, 6}
>>> set()
set()
```

### dict(**kwargs)

new dictionary initialized with the name=value pairs in the keyword argument list.  For example:  dict(one=1, two=2)
返回一个字典，字典内每个键值对由关键字参数中一对`参数名=值`组成，无参数则返回一个空字典`{}`。

```python
>>> dict(one=1, two=2, three=3, F=1111)
{'one': 1, 'two': 2, 'three': 3, 'F': 1111}
```


```python

# 执行语句
eval() exec()

# 检查空值
any() all()

# 输入输出
input() print()

# 数学运算
round() abs() divmod() pow()

# 字符与码位转换
chr()/ord()

# 进制转换
bin()/oct()/hex()

# 类型转换
int() float() bool() str() list() tuple() set() dict()

# 批量处理迭代对象
filter() map()
```