# 试用 C 编程



C语言是一门古老的编程语言。第一次发布是在1972年。然而它在计算机的发展中影响深远。也来学学如何用C来编程。



通常平台自带C语言的编译器。



让我们在网上找一段C语言的代码。



```c
#include <stdio.h>

int main()    
{
  printf("Hello, world!\n");
  return 0;
}
```



这表示什么意思呢。`#include <stdio.h>`表示引用一个头文件，头文件名字叫`stdio.h`。里面有很多的函数。stdio的意思是 `standard input output`， 即是标准输入输出。我们希望用这个依赖库所提供的函数来打印一些东西。实际上也许是不需要这个的。不妨改改代码。



```c
int main()    
{
  return 0;
}
```



这是C语言的函数定义方式。这定义了一个函数。int来表明返回值的类型。`return 0;`来把0作为值返回给这个函数。这个函数名叫 `main`。



```shell
$ gcc hello.c

$ ls
a.out	c.md	hello.c
```



输出了这个文件。就是说gcc编译器，将`hello.c`变成了`a.out`。`gcc`是C语言的编译器。还记得我们在「解谜计算机科学」上说的吗。这就是gcc将我们的程序转换成一系列更简单的操作，或转换成可被计算机执行的一系列命令。



试着把 `a.out`打印出来。



```shell
$ cat a.out
������ H__PAGEZERO�__TEXT@@__text__TEXT�?�?�__unwind_info__TEXT�?H�?H__LINKEDIT@@@�"�0@08@h@0
                                                                                             P
                                                                                               /usr/lib/dyld8A<P�8���m��2

                                                                                                                          a*(��?
                                                                                                                                8
                                                                                                                                 /usr/lib/libSystem.B.dylib&0)8@UH��1��E�]Ð�?44�?4
                        __mh_execute_header!main%���? __mh_execute_header_maindyld_stub_binder
```



这是什么东西。不知道。但它告诉我们一些东西。可见`/usr/lib/libSystem.B.dylib`是系统的一个文件。`__mh_execute_header_maindyld_stub_binder`或许是这个文件的一个函数。`__mh_execute_header!main`中，出现了`main`。说明什么。说明这个文件是在调用系统的文件来执行上面写的main函数。



能不能运行呢。

```shell
$ a.out
-bash: a.out: command not found
```

这不是运行程序。这是在命令行想执行`a.out`这个命令，而不是执行`a.out`这个文件。命令行发现系统并没有`a.out`这个命令。命令行可以执行`gcc`和`ls`等等，但没法执行`a.out`。命令行并不会在当前目录看看有没有`a.out`这个文件，然后去执行它。



接着，了解一下如何把当前目录下的一个文件，当做程序来执行。



```shell
$ ./a.out
```

什么也没有。但没有报错。说明什么，我们成功执行了这个文件。这个文件是一个可执行程序。也就是说我们编译成功。我们已经在用C编程了。



能不能显示一些东西呢。来改改代码。



```c
int main()    
{
  printf("hi");
  return 0;
}
```



接着继续用gcc来编译，然后执行`a.out`文件，看看输出什么。

```shell
$ gcc hello.c
hello.c:3:3: error: implicitly declaring library function 'printf' with type 'int (const char *, ...)' [-Werror,-Wimplicit-function-declaration]
  printf("hi");
  ^
hello.c:3:3: note: include the header <stdio.h> or explicitly provide a declaration for 'printf'
1 error generated.
```

出错了。这意思很详尽。说明我们的方式跟系统的`printf`函数冲突了。这样的代码隐含着来定义一个`printf`函数，而这样去定义的话，和系统的函数冲突了，名字重复了。我们可以来引入头文件`stdio.h`来明确地给printf一个声明。



这是什么意思呢。再来改改代码。



```c
int main()    
{
  print("hi");
  return 0;
}
```

```shell
$ gcc hello.c
hello.c:3:3: error: implicit declaration of function 'printfword' is invalid in C99 [-Werror,-Wimplicit-function-declaration]
  printfword("hi");
  ^
1 error generated.
```

看到出错信息了吗。两种情况下，出错信息是有差别的。一个是`implicitly declaring library function 'printf' with type`，一个是 `implicit declaration of function 'printfword' is invalid`。



也就是还没定义一个函数就使用它时，或把函数名字写错时，就会提示隐含地去声明该函数是不行的。而如果未把头文件引入进来，直接用系统函数，则是提示了隐含地使用系统函数是不行的。



这说明，系统函数要明确地声明来使用。来，接下来引入头文件试试看。

```c
#include<stdio.h>

int main()    
{
  printf("hi");
  return 0;
}
```

```shell
$ gcc hello.c
$./a.out
hi
```

终于正确了。上面出错的情况也很重要，几乎跟知道如何正确地编写代码同样重要。然而如果不是很明白上面出错的情况也可以，随着编程的深入，我们会明白的。以上这样就是编程的日常。不停试试看。从出错中学习是非常好的。



`a.out`这个文件名字有点丑陋。能不能好看一些。又如何改成其它呢。

```shell
$ gcc hello.c -o hello

$ ./hello
hi
```

好了。给gcc编译程序一个参数来表明输出的文件名。这个参数跟在`-o`后面。也可以写成这样`gcc -o hello hello.c` 。正是因为名字参数有`-o`在前，所以这两参数顺序不重要。这个命令是执行gcc程序。同时传递了两参数给它。一个参数表明源文件路径，一个参数表明编译后的文件路径。如果只是一个文件名，则指当前目录下的路径。



