
### Q:克隆项目到本地后 template/js 文件夹为空，没有 js 文件？

A: 请按照 README.md 中介绍的，使用 `git clone --recursive https://github.com/chenjiandongx/pyecharts.git`。因为 template/js 实际上是一个 git submodule，不递归克隆的话会遗漏该模块的内容。

### Q:pyecharts 是否支持  jupyterlab?

A: 暂不支持。 jupyterlab应该是下一代 jupyter notebook 的雏形。欢迎大家提交相关 PR。

### Q:怎么设置 echarts 主题？

A: 主题功能暂时不支持。

### Q:如何设置 tooltip 的 formatter 选项为回调函数？

A: 目前暂时无法支持。因为暂无法将 python 函数通过 json 转换对应的 js 函数。

### Q:为什么安装后还是无法 import Bar,Line 等图形

A:请检查是否将测试文件命名为 pyecharts.py，如若是请重命名该文件。