# pyecharts 文档-FAQ 篇

### 克隆项目到本地后 template/js 文件夹为空，没有 js 文件？
请按照 README.md 中介绍的，使用 `git clone --recursive https://github.com/chenjiandongx/pyecharts.git`。因为 template/js 实际上是一个 git submodule，不递归克隆的话会遗漏该模块的内容。
    