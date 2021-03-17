# 实战：抓取网站内容

已经有很多现成的工具可以抓取网站的内容。然而如果使用它们，我们没法更好地理解背后的过程。如果在工作中遇到复杂或特别一些的网站，使用它们可能并不能得到想要的结果。我们需要造轮子，为了更好地学习它们和更好地运用它们。

也来看看现成的一些工具。

## Data Miner

![miner](./img/miner.png)

`Data Miner`是Chrome上的很方便的一个插件。可以来很方便地抓取链接和内容。



## getbook

`getbook`是一个很方便的制作电子书工具。

```powershell
pip install getbook
```

`book.json`:

```json
{
  "uid": "book",
  "title": "Hello World",
  "author": "Armin",
  "chapters": [
    "http://lucumr.pocoo.org/2018/7/13/python/",
    "http://lucumr.pocoo.org/2017/6/5/diversity-in-technology",
  ]
}
```

```shell
getbook -f ./book.json --mobi
```

这样就方便地把一些链接做成了电子书。通过使用 `Data Miner`和`getbook`，一个爬取链接，一个把链接变成电子书，就能很方便制作电子书。



## 费曼物理讲义

![fl](./img/fl.png)

在「项目实战：将费曼物理讲义网页做成电子书」章节中，我们学会如何把一个用`mathjax`渲染的`html`网页做成电子书。这里继续这个项目，来看看如何获取到所有的网页。费曼物理讲义有三卷。上图是第一卷的的目录。

