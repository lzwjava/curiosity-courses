# Redis



打开Redis官网，第一句话是说，Redis是一种开源的内存型的数据结构存储，常用于数据库和缓存。`Redis`很常用。



## 安装 Redis



可到官网安装`Redis`。就像`SQLite`一样。安装完毕后，那如何在`Python`使用`Redis`呢。

```shell
pip install redis
```

```shell
>>> import redis
>>> r = redis.Redis(host='localhost', port=6379, db=0)
>>> r.set('foo', 'bar')
True
>>> r.get('foo')
b'bar'
```

Python文档给了一些例子。这里出现了像`pip`的东西。`pip`是包管理工具。包管理工具是什么，可到「熟悉编程环境」一章查阅。`pip`之于`python`，就好像`Homebrew`之于`macOS`系统。



`pip`通常在安装`python`时已经自带了。如果电脑有很多版本的`Python`和 `Pip`，可以在`~/.bash_profile`中加入以下两行：

```shell
alias python=/usr/local/Cellar/python@3.9/3.9.1_6/bin/python3
alias pip=/usr/local/Cellar/python@3.9/3.9.1_6/bin/pip3
```

意思是指定一个版本的`python`和 `pip`。一种方式是可以`Homebrew`来安装。也可以从源代码构建安装。

```shell
make
make test
make install
```

```shell
$ redis-server
87684:C 10 Mar 2021 14:46:06.056 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
87684:C 10 Mar 2021 14:46:06.056 # Redis version=6.2.1, bits=64, commit=00000000, modified=0, pid=87684, just started
87684:C 10 Mar 2021 14:46:06.056 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
87684:M 10 Mar 2021 14:46:06.057 * Increased maximum number of open files to 10032 (it was originally set to 4864).
87684:M 10 Mar 2021 14:46:06.057 * monotonic clock: POSIX clock_gettime
...
Redis 6.2.1 (00000000/0) 64 bit
...
87684:M 10 Mar 2021 14:46:06.058 # Server initialized
87684:M 10 Mar 2021 14:46:06.058 * Ready to accept connections
```

这里节选了一点内容。可见我们已经安装上了。版本号`6.2.1`，是官网最新的。打开另外一个终端窗口。可以试着把玩一下：


```shell
$ redis-cli
127.0.0.1:6379> set a 2
OK
127.0.0.1:6379> get a
"2"
```

运行一下代码。

```python
import redis

r = redis.Redis(host='localhost', port=6379, db=0)
r.set('foo', 'bar')
print(r.get('foo'))
```

输出：

```shell
$ python fib_redis.py
b'bar'
```



## Redis 缓存例子



来实现斐波那契数列`Redis`版本。



```python
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

def f(n):
    nr = r.get(n)
    if nr is not None:
        return int(nr)
    res_n = 0
    if n < 2:
        res_n = n
    else:
        res_n = f(n-1) + f(n-2)
    
    r.set(n, res_n)
    return res_n

print(f(10))
```



这样就搞定啦。



