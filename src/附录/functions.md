# 内置函数

## A Series

### abs()

`abs`函数用来返回一个数值的绝对值，参数是整形或浮点型

```python
>>> abs(3)
3
>>> abs(-9.1)
9.1
```

### all()

`all`函数要求传入参数是一个序列或可迭代对象，当这个序列里所有元素都为真值或者这个序列为空，返回`True`，否则返回`False`

```python
>>> lst = [1,2,3,4,5]
>>> all(lst)
True
>>> lst.append(0)
>>> all(lst)
False
>>> all([])
>>> True
```

### any()

`any`函数要求传入参数是一个序列或可迭代对象，当这个序列里有任意一元素为真值返回`True`，否则返回`False`， 当序列为空时，直接返回`False`

```python
>>> s = "abc"
>>> any(s)
True
>>> lst = [0, 0.0, False, "", [], {}]
>>> any(lst)
False
>>> any([])
False
```

## B Series

### bin()

`bin`将一个整数转换为带前缀 "0b" 的二进制数字符串

```python
>>> bin(3)
'0b11'
>>> bin(0xAFE)
'0b101011111110'
```

### bool()

`bool`返回布尔值，即`True`或`False`，也就是说它会检验参数的真假。

## C Series

### chr()

`chr`接收整形参数，返回Unicode (UTF-6)码位为参数值的字符的字符串格式。它是`ord`的逆函数。

```python
>>> chr(65)
'A'
>>> chr(122)
'z'
```

## D Series

### dict()

`dict`创建一个新的字典

```python
>>> dict(a=1,b=2,c=3)
{'a':1, 'b':2, 'c':3}
```

### divmod()

`divmod`接收两个参数`a`和`b`，返回一个元组，这个元组里有两个值，分别为`a//b`和`a%b`.

```python
>>> divmod(10,3)
(3, 1)
>>> divmod(-10, 3)
(-4, 2)
>>> divmod(-10, -3)
(3, -1)
```

## E Series

### enumerate(iterable, start=0)

`enumerate`要求输入的参数必须是可迭代的，即序列。它会返回一个枚举对象，可以通过`next`函数返回一个值，这个值为一个元组，内容为序列参数的索引和值。

```python
>>> lst = ['a', 'b', 'c']
>>> enum = enumerate(lst)
>>> next(enum)
(0, 'a')
>>> next(enum)
(1, 'b')
>>> next(enum)
(2, 'c')
>>> next(enum)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    next(enum)
StopIteration
>>> dit = {'name':"Chris", "age": 10, "gender": "F"}
>>> enum = enumerate(dit)
>>> next(enum)
(0, 'name')
```

### eval(expression, globals=None, locals=None)
`eval`会解析参数 `expression` 并作为 Python **表达式**进行求值

```python
>>> eval("4+5")
9
>>> a = 10
>>> eval("a+5")
15
```

### exec(object, globals=None, locals=None, /, *, closure=None)

`exec`将`object`当成Python语句来执行

```python
>>> a = 10
>>> b = 0
>>> exec("b=a+5")
>>> print(b)
15
```

## F Series

### filter(function, iterable)

`filter`使用 `iterable` 中 `function` 返回真值的元素构造一个迭代器。

```python
>>> lst = [1,2,0,['a','b'], {}, "", 3.14]
>>> ls = list(filter(None, lst))
>>> print(ls)
[1,2,['a','b'],3.14]
```

```python
def is_even(a):
    return a % 2 == 0

lst = [0,1,2,3,4,5,6,7,8,9,10]
ls = list(filter(is_even, lst))

"""
结果为[0, 2, 4, 6, 8, 10]
"""
```

上述可以简写成 `ls = list(filter(lambda a:a%2==0, lst))`


### float(x=0.0)

`float`返回从数字或字符串 x 生成的浮点数。


## H Series

### hex(x)

将整数转换为带前缀`0x` 前缀的小写十六进制数字符串。

## I Series

### input() / input(prompt)

如果存在`prompt`实参，则将其写入标准输出，末尾不带换行符。接下来，该函数从输入中读取一行，将其转换为字符串（除了末尾的换行符）并返回

### int(x, base=10)

返回一个基于数字或字符串 x 构造的整数对象，或者在未给出参数时返回 0。

```python
>>> int(3.4)
3
>>> int('4')
4
>>> int()
0
```

如果 x 不是一个数字或者如果给定了 base，则 x 必须是一个表示以 base 为基数的整数的字符串。

一个以`n`为基数的整数字符串包含多个数位，每个数位代表从`0`到`n-1`范围内的值。 `0-9`的值可以用任何 `Unicode`十进制数码来表示。 `10-35`的值可以用 `a` 到`z`(或`A`到`Z`) 来表示。 默认的`base`为`10`。

```python
>>> int('743279', 10)
743279
>>> int('743279', 2)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    int('743279', 2)
ValueError: invalid literal for int() with base 2: '743279'
>>> int('743279', 16)
7615097
>>> int('10', 8)
8
>>> int('10', 36)
36
```

## L Series

### len(s)

返回对象的长度（元素个数）。实参可以是序列（如 `string`、`bytes`、`tuple`、`list` 或 `range` 等）或集合（如 `dictionary`、`set`等）。

## M Series

### map(function, iterable)

返回一个将 function 应用于 iterable 的每一项，并产生其结果的迭代器。 如果传入了额外的 iterables 参数，则 function 必须接受相同个数的参数并被用于到从所有可迭代对象中并行获取的项。 当有多个可迭代对象时，当最短的可迭代对象耗尽则整个迭代将会停止。

```python
>>> lst = [1,2,3,4,5]
>>> g = map(str, lst)
>>> next(g)
'1'
>>> next(g)
'2'
>>> p = map(lambda x:x*x, lst)
>>> next(p)
1
>>> next(p)
4
```

## N Series

### next(iterable)


## O Series

### oct(x)
将整数转换为带前缀 "0o" 的八进制数字符串。

### open()

`open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)`
打开文件

### ord(c)

对表示单个 Unicode 字符的字符串，返回代表它 Unicode 码点的整数。这是 chr() 的逆函数。

```python
>>> ord('A')
65
>>> ord("王")
29579
```

## P Series

### pow(base, exp, mod=None)

返回 base 的 exp 次幂；如果 mod 存在，则返回 base 的 exp 次幂对 mod 取余（比 pow(base, exp) % mod 更高效）。 两参数形式 pow(base, exp) 等价于乘方运算符: base**exp。

```python
>>> pow(4,3)
64
>>> pow(4,3,10)
4
>>> 
```

## R Series

### reversed(seq)
返回一个反向的迭代器。
```python
>>> lst = [2,4,1,52,302,23,22]
>>> reversed(lst)
<list_reverseiterator object at 0x00000151CDD7E4C0>
>>> list(reversed(lst))
[22, 23, 302, 52, 1, 4, 2]
>>> 
```

### round(number, ndigits=None)

返回 number 舍入到小数点后 ndigits 位精度的值。 如果 ndigits 被省略或为 None，则返回最接近输入值的整数。

```python
>>> round(3.1415926,2)
3.14
>>> round(3.1415926)
3
>>> round(3.1415926, -1)
0.0
>>> round(1789,-1)
1790
>>> 
```

## S Series

### set(iterable)

返回一个新的`set`对象，可以选择带有从`iterable`获取的元素。 

```python
>>> lst = [1,2,4,23,5,12,4,6,7,2,42,5,62,1,42,4,2,1,23,5,0]
>>> st = set(lst)
>>> new_lst = list(st)
>>> print(new_list)
[0, 1, 2, 4, 5, 6, 7, 42, 12, 23, 62]
```
也可以用来为创建一个空集合`set()`，注意不是`{}`，`{}`是一个空字典。

```python
>>> st = set()
>>> print(st)
set()
```

### sorted(iterable, reverse=False)

根据`iterable`中的项返回一个新的已排序列表。默认按元素大小升序排列，当传值`True`给`reverse`之后，则按元素大小降序排列。

```python
>>> lst = [1,2,4,23,5,12,4,6,7,2,42,5,62,1,42,4,2,1,23,5,0]
>>> sorted(lst)
[0, 1, 1, 1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 6, 7, 12, 23, 23, 42, 42, 62]
>>> tp = (2,24,1,2438,27809,108,490,80,-984,940,26896)
>>> sorted(tp)
[-984, 1, 2, 24, 80, 108, 490, 940, 2438, 26896, 27809]
>>> sorted(tp, reverse=True) # `reverse`是关键字参数，`reverse=`不能省略。
[27809, 26896, 2438, 940, 490, 108, 80, 24, 2, 1, -984]

>>> dit = {1:2, 5:6, 4:56, 10:422, 15:0}
```

### str(object)

`str`返回`object`的字符串格式。

```python
>>> str(1)
'1'
>>> str([1,2,3,4,5])
'[1,2,3,4,5]'
```

### sum(iterable, start=0)

从`start`开始自左向右对`iterable`的项求和并返回总计值。 `iterable`的项通常为数字，而`start`值则不允许为字符串。

```python
>>> sum([1,2,3,4,5])
15
>>> sum(1,2,3,4,54,56,6)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    sum(1,2,3,4,54,56,6)
TypeError: sum() takes at most 2 arguments (7 given)

>>> sum([1,2,3,4,5], start=10)
25
```

## T Series

### tuple(iterable)

返回由`iterable`中元素组成的元组。

```python
>>> tuple([1,2,3,4,5])
(1, 2, 3, 4, 5)
```


### type(object)

返回`object`的类型。

```python
>>> type(1)
<class 'int'>
>>> type([1,2,3,4,5])
<class 'list'>
```

