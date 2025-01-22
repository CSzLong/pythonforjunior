
`os`模块提供了与操作系统交互的功能，能够处理文件和目录的创建、删除、路径操作等。

## 常用功能

- **os.name**： 获取操作系统的名称。`posix`表示类`Unix`系统，`nt`表示`Windows`系统。
```python
>>> import os
>>> print(os.name)
```

- **os.getcwd()**：获取当前工作目录。

```python
>>> print(os.getcwd())
```

- **os.chdir(path)**：改变当前的工作目录，`chdir`即`change directory`.

```python
>>> os.chdir('/Users/chris/Downloads')
```

- **os.listdir(path)**：列出指定路径下的文件和目录。

```python
>>> print(os.listdir('/Users/chris/Downloads'))
```

- **os.mkdir(path)和 os.makedirs(path)**：创建单个目录和创建级联目录（递归创建）

```python
>>> os.mkdir("ABC")
>>> os.makedirs("A/B/C")
```

- **os.remove(path)和os.rmdir(path)**：`os.remove`用于删除文件，`os.rmdir`用于删除空目录

```python
>>> os.remove('C/testing.txt')
>>> os.rmdir('C')
```

- **os.rename(old_name, new_name)**：重命名文件或目录

```python
>>> os.rename('ABC', 'DEF')
```

- **os.system(command)**：执行操作系统的命令。返回值是命令的退出状态码。

```python
>>> os.system("shutdown -h")
>>> os.system("echo Hello World")
>>> os.system("mkdir HIJ")
```

- **os.path** 模块
`os.path`模块是`os`模块的子模块，提供了处理路径的函数。
	-`os.path.join()`: 拼接路径。
	-`os.path.exists()`：检查路径是否存在。
	-`os.path.isdir()`：检查路径是否为目录。
	-`os.path.isfile()`：检查路径是否为文件。
	-`os.path.abspath()`：获取绝对路径。