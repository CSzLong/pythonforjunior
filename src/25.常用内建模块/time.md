`time`模块提供了一些与系统时间、操作系统和时间相关的函数，主要用于执行低级别的时间操作，比如等待或者暂停。

## 主要函数

### time()

返回当前时间的时间戳（以秒为单位）。表示从1970年1月1日以来的秒数。具体的起始小时以时区为主.
```python
import time as t
print(t.time())
```

### sleep(seconds)

使程序暂停指定的秒数。在编写程序时常用于模拟延时、等待某些操作。这个函数没有返回值。

```python
import time as t
print("Start")
t.sleep(2)
print("End")
```

### localtime([seconds])

返回当前本地时间的`struct_time`对象。如果给定了`seconds`参数，则将其转换为本地时间，否则返回当前时间。

```python
import time as t
local_time = t.localtime()
print(local_time)
ca_time = t.localtime(1734689541.446833)
print(ca_time)
```