#  运行 Rust 程序



Rust 是这几年比较火的编程语言。2006年时，Mozilla的一个员工开始做一个个人项目，后来得到了公司的支持，于2010年发布这个项目。这个项目就叫Rust。



接下来，运行起来Rust的第一个程序吧。打开官网，来看看如何把程序跑起来。



官网提供了一个脚本：

```shell
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```



在 Mac 上也可以用 Mac系统的包管理工具Homebrew来安装。可运行命令：

```shell
brew install rust
```



这些脚本只需要复制粘贴到终端，即可执行。为什么有时要用Homebrew来安装。因为官网的脚本通常只通过了安装功能，而没有卸载功能。升级可能也没有Homebrew那么方便。Homebrew也能把这类程序都统一管理起来。通常折腾计算机，需要安装很多的程序，各种各样的程序，时常也用到多种编程语言。如果每种语言都安装到不同的地方，那我们很难记得它们在哪里，也就不方便管理它们。然而刚开始接触编程的话，用官网的脚本是很方便的。



我这里用Homebrew来安装rust。安装的时刻，让我们继续看官网。



接着我们看官网出现了Cargo这个东西，Rust的构建工具和包管理工具。Cargo可以理解为编译器的一环。通过「解谜计算机科学」一文，我们已经很明白了。Cargo具有构建功能。构建功能这里便是在做编译器的工作。真实的程序通常是包含很多功能的。比如写个画图的程序。可能需要图形的依赖库。写个数学的程序，可能需要数学的依赖库。依赖库是什么意思。是有很多的函数。比如数学的依赖库，可能有方便的求和、求平均、求n次方等函数。图形的依赖库，则可能有画圆圈、画矩形的函数。于是传递参数给那些函数，便得到了想要的结果。也就是说当引用了某一个依赖库，可以在当前想写的这个Rust程序里，就能很方便地使用这个依赖库所提供的便捷函数。依赖库，也就是所谓的「包」。Cargo工具则是用来编译Rust程序和管理众多Rust依赖库的。



官方网站上说，



- build your project with `cargo build`
- run your project with `cargo run`
- test your project with `cargo test`



告诉我们如何构建、运行和测试Cargo程序。



运行：



```
brew install rust
```



输出：



```shell
==> Downloading https://homebrew.bintray.com/bottles/rust-1.49.0_1.big_sur.bottle.tar.gz
==> Downloading from https://d29vzk4ow07wi7.cloudfront.net/5a238d58c3fa775fed4e12ad74109deff54a82a06cb6a3a4f51b5d37587fb319?response-content-disposition=a
######################################################################## 100.0%
==> Pouring rust-1.49.0_1.big_sur.bottle.tar.gz
==> Caveats
Bash completion has been installed to:
  /usr/local/etc/bash_completion.d
==> Summary
🍺  /usr/local/Cellar/rust/1.49.0_1: 15,736 files, 606.2MB
```



这便安装成功了。



当在终端运行`cargo`时，输出如下：



```
Rust's package manager

USAGE:
    cargo [OPTIONS] [SUBCOMMAND]

OPTIONS:
    -V, --version           Print version info and exit
        --list              List installed commands
        --explain <CODE>    Run `rustc --explain CODE`
    -v, --verbose           Use verbose output (-vv very verbose/build.rs output)
    -q, --quiet             No output printed to stdout
        --color <WHEN>      Coloring: auto, always, never
        --frozen            Require Cargo.lock and cache are up to date
        --locked            Require Cargo.lock is up to date
        --offline           Run without accessing the network
    -Z <FLAG>...            Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for details
    -h, --help              Prints help information

Some common cargo commands are (see all commands with --list):
    build, b    Compile the current package
    check, c    Analyze the current package and report errors, but don't build object files
    clean       Remove the target directory
    doc         Build this package's and its dependencies' documentation
    new         Create a new cargo package
    init        Create a new cargo package in an existing directory
    run, r      Run a binary or example of the local package
    test, t     Run the tests
    bench       Run the benchmarks
    update      Update dependencies listed in Cargo.lock
    search      Search registry for crates
    publish     Package and upload this package to the registry
    install     Install a Rust binary. Default location is $HOME/.cargo/bin
    uninstall   Uninstall a Rust binary

See 'cargo help <command>' for more information on a specific command.
```



无需弄懂所有的命令。只需要知道常用的命令即可。build 和 run 命令很重要。



