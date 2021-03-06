# 试用 Java 编程



Java 诞生于1995年，有着25年的历史。Java 的官网是 https://www.java.com 。



如果在 Windows上，可能有下载Java的编译器。下载JDK，即`Java Development Kit`（Java开发环境工具）。在macOS上，通常已经自带了 `javac`编译程序。这里将在 macOS 上试用 Java 来编程。



试试在终端运行`javac`。

```shell
$ javac
Usage: javac <options> <source files>
where possible options include:
  -g                         Generate all debugging info
  -g:none                    Generate no debugging info
  -g:{lines,vars,source}     Generate only some debugging info
  -nowarn                    Generate no warnings
  -verbose                   Output messages about what the compiler is doing
  -deprecation               Output source locations where deprecated APIs are used
  -classpath <path>          Specify where to find user class files and annotation processors
  -cp <path>                 Specify where to find user class files and annotation processors
  -sourcepath <path>         Specify where to find input source files
  -bootclasspath <path>      Override location of bootstrap class files
  -extdirs <dirs>            Override location of installed extensions
  -endorseddirs <dirs>       Override location of endorsed standards path
  -proc:{none,only}          Control whether annotation processing and/or compilation is done.
  -processor <class1>[,<class2>,<class3>...] Names of the annotation processors to run; bypasses default discovery process
  -processorpath <path>      Specify where to find annotation processors
  -parameters                Generate metadata for reflection on method parameters
  -d <directory>             Specify where to place generated class files
  -s <directory>             Specify where to place generated source files
  -h <directory>             Specify where to place generated native header files
  -implicit:{none,class}     Specify whether or not to generate class files for implicitly referenced files
  -encoding <encoding>       Specify character encoding used by source files
  -source <release>          Provide source compatibility with specified release
  -target <release>          Generate class files for specific VM version
  -profile <profile>         Check that API used is available in the specified profile
  -version                   Version information
  -help                      Print a synopsis of standard options
  -Akey[=value]              Options to pass to annotation processors
  -X                         Print a synopsis of nonstandard options
  -J<flag>                   Pass <flag> directly to the runtime system
  -Werror                    Terminate compilation if warnings occur
  @<filename>                Read options and filenames from file
```

这一串的英文信息可以忽略。然而说明已经跑起来了。如果出错了，提示没有命令。那可能要更改终端运行的环境变量。



来创建java文件，尝试写点什么，编译一下。

```java
2+3
```

```java
$ javac hello.java
hello.java:1: error: class, interface, or enum expected
2+3
^
hello.java:1: error: class, interface, or enum expected
2+3
 ^
hello.java:1: error: class, interface, or enum expected
2+3
  ^
```

结果很有意思。报了三个错，分别指向三个字符。告知说，编译程序希望这是`class`、`interface`或`enum`，中文上通常叫类、接口和枚举。

```java
class Happy{ 
  public static void main(String args[]){  
   System.out.println("Hello Java");  
  }  
}
```

网上找了一段代码示例。这看起来很复杂，出现很多新东西。这出现在「解谜计算机科学」里没有出现过的概念，`class`。这其实相当于我们说的温度控制器。里面则含有温度控制器的操作函数。也可以暂时理解为`模块`。它比`文件`小一些，又比`函数`大一些。接下来就是一个函数。`System.out`大概是一个依赖库。`String args[]`声明了一个字符串数组，名字叫`args`。



来，编译一下。

```shell
$javac hello.java

$ ls
Happy.class	hello.java	
```

编译后，发现啥也没有显示。列举文件之后，发现多了一个文件，叫`Happy.class`。



接下来，怎么办呢。该怎么运行呢。搜索资料简单看了下后，发现只要用`java`运行一下就行。

```shell
$ java Happy
Hello Java
```

这说明成功了。我们的 Java 程序跑起来了。



再来玩一下。

```java
class Happy{ 
  public static void main(String args[]){  
   System.out.println(2+3);  
  }  
}
```

```shell
$ javac hello.java

$ java Happy
5
```

嗯，很顺利。



### 练习

* 试着像本文一样，学生在自己电脑上试用Java编程。
* 作业提交形式为一百字以内的总结。也可以是对本文内容的补充知识。

