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



```shell
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



```shell
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



继续看官网文档：

```
Let’s write a small application with our new Rust development environment. To start, we’ll use Cargo to make a new project for us. In your terminal of choice run:

cargo new hello-rust

This will generate a new directory called hello-rust with the following files:

hello-rust
|- Cargo.toml
|- src
  |- main.rs
Cargo.toml is the manifest file for Rust. It’s where you keep metadata for your project, as well as dependencies.

src/main.rs is where we’ll write our application code.
```

这讲述了如何创建项目。接下来便创建。



```shell
cargo new hello-rust

Created binary (application) `hello-rust` package
```



我们用 VSCode来打开项目。



main.rs:

```rust
fn main() {
    println!("Hello, world!");
}
```



接下来，很自然想到要build以及run程序。



```shell
cargo build

error: could not find `Cargo.toml` in `/Users/lzw/ideas/curious-courses/program/run/rust` or any parent directory
```



出错了。为什么。这表明cargo只能在项目下的目录运行。接下来进入子目录，运行了`cd hello-rust`。



这时，想如果直接运行，会怎么样。



```shell
cargo run
   
   Compiling hello-rust v0.1.0 (/Users/lzw/ideas/curious-courses/program/run/rust/hello-rust)
    Finished dev [unoptimized + debuginfo] target(s) in 4.43s
     Running `target/debug/hello-rust`
Hello, world!
```



好了，成功了。输出了字符串，程序开始工作啦。



试着改动程序。



```rust
fn main() {
    println!(2+3);
}
```



`cargo run`之后，出现了：



```
   Compiling hello-rust v0.1.0 (/Users/lzw/ideas/curious-courses/program/run/rust/hello-rust)
error: format argument must be a string literal
 --> src/main.rs:2:14
  |
2 |     println!(2+3);
  |              ^^^
  |
help: you might be missing a string literal to format with
  |
2 |     println!("{}", 2+3);
  |              ^^^^^

error: aborting due to previous error

error: could not compile `hello-rust`

To learn more, run the command again with --verbose.
```



还没学习任何Rust语法。凭着我们的直觉来改动代码出错了。这个出错提示很好，已经告诉我们怎么改了。



```rust
fn main() {
    println!("{}", 2+3);
}
```



这次改对了，果然输出了5。



对了，build会怎么样。

```
cargo build
    Finished dev [unoptimized + debuginfo] target(s) in 0.00s
```



为什么要有build呢。因为有可能我们只是想生成可执行程序，而并不想执行。也许对于一些庞大的程序，执行是费时的。也许我们想本地生成，然后传输到远程服务器去执行。



我们已经把Rust程序跑起来了。后面便是熟悉更多的Rust语言语法，来在Rust中找到我们在「解谜计算机科学」上讲述的变量、函数、函数调用和表达式等概念所对应的符号表示。



