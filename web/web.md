# Web 编程



继续 Web 开发的话题，让我们稍稍重构一下代码。

```python
from http.server import SimpleHTTPRequestHandler, HTTPServer
from fib import f
from urllib.parse import urlparse,parse_qs

class Handler(SimpleHTTPRequestHandler):

    def parse_n(self, s):
      parsed = urlparse(s)
      qs = parse_qs(parsed.query)
      if len(qs) > 0:
        ns = qs['n']
        if len(ns) > 0:
          n = int(ns[0])
          return n
      return None
      
    def do_GET(self):
      self.send_response(200)
      self.send_header('Content-type', 'text')
      self.end_headers()

      result = ""
      n = self.parse_n(self.path)
      if n is not None:
        result = str(f(n))
              
      self.wfile.write(bytes(result, "utf-8"))
      self.wfile.write(bytes(result, "utf-8"))

server = HTTPServer(("127.0.0.1", 8000), Handler)

server.serve_forever()
```



引入 `parse_n`的函数来把从请求路径中解析得到`n`封装在一块。



现在程序有这样的问题。小王请求了斐波那契数列的第10000位，过了一些天，小明又请求了斐波那契数列的第10000位。两次，小王和小明都等待了半天，才得到结果。我们该如何提高这个`Web服务的`效率呢。



注意到如果`n`相同，`f(n)`的值总是一样的。我们进行了一番实验。



```shell
127.0.0.1 - - [10/Mar/2021 00:33:01] "GET /?n=1000 HTTP/1.1" 200 -
----------------------------------------
Exception occurred during processing of request from ('127.0.0.1', 50783)
Traceback (most recent call last):
    ...
    if v[n] != -1:
IndexError: list index out of range
```

原来数组不够大，那就把v数组改成10000吧。

```python
v = []
for x in range(10000):
   v.append(-1)
```

然而当n为`2000`时，出现了递归深度溢出错误：

```shell
127.0.0.1 - - [10/Mar/2021 00:34:00] "GET /?n=2000 HTTP/1.1" 200 -
----------------------------------------
Exception occurred during processing of request from ('127.0.0.1', 50821)
Traceback (most recent call last):
    ...
    if v[n] != -1:
RecursionError: maximum recursion depth exceeded in comparison
```

然而这一切都还挺快的。



为什么。因为`f(1)`到`f(1000)`，都只需要算一次。这意味着当在算`f(1000)`的时候，`+`运算也许只被执行了1000次左右。我们知道`Python`的递归深度大约在1000左右。这意味着我们可以这样优化程序，如果要算`2000`，那我先算`1000`的。不，这样还是可能会出现`递归深度溢出错误`。如果要算2000，先算1200吧。如果要算1200，先算400吧。



这样算完400和1200之后，再算2000，递归深度大概在800左右，就不会出现递归深度溢出错误了。

```python
v = []
for x in range(1000000):
   v.append(-1)

def fplus(n):
   if n > 800:         
      fplus(n-800)
      return f(n)
   else:
      return f(n)

def f(n):
   if v[n] != -1:
      return v[n]
   else:
      a = 0
      if n < 2:
         a = n
      else:
         a = f(n-1) + f(n-2)
      v[n] = a
      return v[n]
```

增加了`fplus`函数。



然而不禁让人想，`fplus`被递归调用`1000`次怎么样。1000 * 800 = 800000。当我把n设为80万之后，又出现递归深度错误了。继续试探了一下，发现事情更复杂。然而这样优化之后，算2000是非常轻松的了。



似乎把话题岔开了。回到Web开发的话题上。第一次请求`f(400)`，第二次请求`f(600)`。那么第二次请求时，第一次请求所产生的`v`数组的值，我们是能用上的。然而当我们把程序退出。再启动就用不上了。按我们的方法，斐波那契数列计算是很快的。然而设想，如果很慢怎么办。尤其就如当我们没有引入v数组的时候，有着大量重复的计算。这时我们希望能把好不容易得到的结果保存起来。



这时，就引入`缓存`的概念了。`v`数组这里就是一个缓存。不过它只存在于程序生命周期里。程序关闭后，它就没了。怎么办呢。很自然，我们会想到存到文件里去。



如何把v数组保存到文件呢。

```shell
0 0
1 1
2 1
3 2
4 3
...
```

我们的`v`数组可以这样保存。每一行保存为`n f(n)`。既然`n`是自然增长的。或许我们可以只保存`f(n)`值。

```shell
0
1
1
2
3
...
```

