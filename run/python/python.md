#  试用 Python 编程



可能大家早已听过 Python 这门编程语言。查了下维基百科，发现它是1991年发布的。想不到已经30年。



让我们把Python编译器安装起来。官网是 https://www.python.org 。找到 `Getting Started`部分。这里说有2.x编译器和3.x编译器。就是说Python编程语言又分为两种主要的版本，Python2和Python3。它们的语法或别的可能不同，它们无法兼容。也就是在「解谜计算机科学」上所说的，对于一些概念，有些模型在两者中的符号表达不一样。至于为什么会这样，我们暂时不去了解。



我们这里用3.x。目前最新的版本是 [Python 3.9.2](https://www.python.org/downloads/release/python-392/)。来把它下载下来。接下来进行安装。我早之前装的是 Python 3.9.0。3.9.0和3.9.2版本应该差别不大。本文以3.9.0来讲述。这里只是演示运行一些基本简单的程序，几乎用所有的版本都应该差不多的。



安装完成后，便可在命令行输入`python`来进入 Python的实时交互编程命令行。



```shell
$ python
Python 3.9.0 (default, Oct  8 2020, 11:54:28)
[Clang 12.0.0 (clang-1200.0.32.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>>
```

这里打印了当前Python编译器的一些基本信息和帮助信息。



试试输入一些命令。

```python
>>> 2+3
5
```

```python
>>> 8*(2+3)
40
```

是不是这又很像终端命令行。

```python
>>> 2+
  File "<stdin>", line 1
    2+
      ^
SyntaxError: invalid syntax
```

出错了。告诉我们这是无效的语法。 在文件 stdin 的第一行出错了。这是什么意思。可能这个交互编程环境，Python把每一行命令封装成一个文件，然后提供一些基本的依赖库，接着来运行。stdin是standard input 的意思，即是标准输入的意思。



继续玩。

```python
>>> a=3
>>> a+5
8
```

说明它支持变量。



怎么退出这个交互命令行呢。这样来：

```python
>>> exit()
```



那能不能先写成一个文件，再运行呢。试试看。我们用VSCode来写几行代码。



创建一个`main.py`的文件。随便写点啥吧。

```python
2+3
```

那怎么运行呢。



试试看在终端用`python`运行这个文件，也就是把这个文件名当做参数传递给Python编译器，看看如何。

```shell
$ python main.py
```

什么也没有，什么也看不到。再改一改。



main.py：

```python
println(2+3)
```

```shell
$ python main.py
Traceback (most recent call last):
  File "/Users/lzw/curious-courses/run/python/hello-python/main.py", line 1, in <module>
    println(2+3)
NameError: name 'println' is not defined
```

出错了。println是我在其它语言看到的。这里也可能是我们网上查到的。总之随便试一试。错误信息是说，`println`没有被定义。



再试试改改。



main.py：

```
print(2+3)
```

```
$ python main.py
5
```

成功了！继续玩玩。



main.py：

```python
print("hello")
```

```
$ python main.py
hello
```



嗯。我们用Python语言写了一些代码，接着用Python编译器来执行了这些代码。可以说我们在用Python编程了。



### 练习

* 试着像本文一样，学生在自己电脑上试用Python编程。
* 作业提交形式为一百字以内的总结。也可以是对本文内容的补充知识。

