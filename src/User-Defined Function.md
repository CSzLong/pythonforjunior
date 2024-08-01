# 自定义函数 User-Defined Function

## 语法结构

### 定义

```shell
def function_name(parameters):
    function body
    <return clause>
```

- **def:** 关键字，用来自定义函数时使用，写在最前面。 def 为 define 的简写
- **function_name:** 函数的名字，首先命名规则(naming conversion)同变量的命名规则
- **parameters:** 函数的参数
- **function body:** 函数的实体，具体要执行(execute)的逻辑(logic) 
- **return clause:** 返回值语句，如果有返回值，需要写清楚，return 是关键字(keywords)

例如，定义一个函数，传入两个数值型参数，函数体计算两个数值的和，最后将结果返回

```python
def num_plus(x, y):
    z = x + y
    return z
```

或者：
```python
def num_plus(x:int, y:int)->int:
    z = x + y
    return z
```
第二种写法，`:`和`->`后面的`int`并不是强制要求只能传入或返回整型值，这样写是为了增加代码的可读性。

第二个例子，定义一个函数，传入一个数值型变量，变量的意义为数学成绩，如果成绩大于等于80，则打印`A`，成绩在60和80之间(包含60)，则打印`B`，低于60则打印`C`，如果成绩不是有效成绩，则打印`Invalid`.

```python
def grade(a: int)->None:
    if 80 <= a <= 100:
        print('A')
    elif 60 <= a < 80:
        print('B')
    elif 0 <= a < 60:
        print('C')
    else:
        print('Invalid.')
```


## 函数的参数

在数学中，我们最初学的是解未知数，比如下面的方程：

4x + 8 - 8x= 16  可解出 x 的值为 -2；

在后面的阶段，又学了一元一次方程，二元一次方程，还有一元二次方程，在一元二次方程时，就加入了平面直角坐标系的概念, 如：

y = x^2 + 2x + 1 = (x+1)^2

再后来，这个方程的写法变成了 f(x) = (x+1)^2，

如果我写成 f(x, y, z) = x^2 + y^2 + z^2.

### 参数的类型

1. 位置参数
2. 默认值参数
3. 可变参数
4. 关键字参数

#### 位置参数 positional argument

位置参数是函数定义中按照顺序传递的参数。调用函数时，这些参数根据它们在函数中定义的位置依次传递。

```python
def concatenate(x:str, y:str)->str:
    return x + y
```

其中`x`和`y`为两个位置参数，在传值时，要按顺序传递，如果需要将`hello`和`world`拼接在一起，组成`hello world`，调用时需要：

```python
>>> concatenate('hello', 'world')
helloworld
>>> a = 'hello'
>>> b = 'world'
>>> concatenate(b, a)
worldhello
```

写一个函数，传入两个参数，第一个参数为字符串，第二个参数为数值，函数逻辑为先将数值做平方运算，再将运算的结果和字符串相乘，最后返回

#### 默认值参数 default argument

如果在定义函数时，给位置参数一个默认值，则这个参数就成为了默认值，默认值参数必须写在位置参数后面。默认值参数在调用函数时可以不给其传入新的值

```python
def add(a:float, b:float = 3.14) -> float:
    return a + b
```
如果函数中的参数有默认值参数，那边在调用这个函数时，可以不给默认值参数传值

```python
>>> add(1)
4.14
>>> add(1, 3)
4
```

#### 重新理解参数的传值

假如有如下函数定义：

```python
def add(a,b,c,d,e):
    return a + b + c + d + e
```

正确的调用方式有如下几种：

1. add(1,2,3,4,5)
2. add(1,2,d=4,c=3,e=5) 或者 add(1,2,c=3,d=4,e=5)
3. add(e=5, a=1, c=3, b=2, d=4)

#### 可变参数

在 Python 中，可变参数允许函数接受任意数量的参数

```python
def add(*args):
    return sum(args)

def add(*args):
    summ = 0
    for i in args:
        summ += i
    return summ
```

调用的方式：

```python
>>> add(1,2,4,53,53,2,6,4,24,36,743,42,245,42,131,313,3,43543,54343,64343,31)
163964
>>> tp = (1,2,4,53,53,2,6,4,24,36,743,42,245,42,131,313,3,43543,54343,64343,31)
>>> add(*tp)
163964
```

#### 关键字参数

Python允许传入不定数量的带有参数名的参数，参数的名字没有强制的要求


```python
def person(name, age, gender='Male', **kwargs):
    print(name, age, gender, kwargs)
```

调用

```python
>>> person("Michael", 30, height=180,weight=75)
Michael 30 Male {'height': 180, 'weight': 75}
>>> person("Michelle", 24, 'Female', job='IT Developer', postion="Senior IT Archtecture", salary="$30K/mon")
Michelle 24 Female {'job': 'IT Developer', 'postion': 'Senior IT Archtecture', 'salary': '$30K/mon'}
```

还有一个比较特殊的关键字参数，叫做命名关键字参数，也就是说这种关键字参数要求有明确的参数名字：

```python
def person(name, age, gender='Male', *, city, job):
    print(name, age, gender, city, job)
```

调用时，命名关键字参数一定要传入参数名：

```python
>>> person('Jack', 20, city='Shanghai', job='Engineer')
Jack 20 Male Shanghai Engineer
>>> person('Jack', 20, 'Male', 'Shanghai', 'Engineer')
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    person('Jack', 20, 'Male', 'Shanghai', 'Engineer')
TypeError: person() takes from 2 to 3 positional arguments but 5 were given

>>> mydict = {'city':'Beijing', 'job': 'Teacher'}
>>> person('Tina', 31, 'Female', **mydict)
Tina 31 Female Beijing Teacher
```

#### 组合参数类型

如果一个函数中，有上述四种参数的类型，在定义时要遵循的顺序:

```text
位置参数 -> 默认值参数 -> 可变参数 -> 命名关键字参数 -> 关键字参数
```