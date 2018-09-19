> 技术文档篇：介绍 pyecharts 开发过程中所使用的工具、实践规范。

## 开发工具

- [Travis CI](https://travis-ci.org) ：在线构建工具
- [AppVeyor CI](https://www.appveyor.com/) ：Windows 构建工具
- [Codecov](https://codecov.io)：代码覆盖率
- [nose](http://nose.readthedocs.io/en/latest/index.html) ：单元测试工具
- [flake8](http://flake8.pycqa.org/en/latest/index.html) ：静态代码检查
- [black(18.6b4)](https://github.com/ambv/black) ：代码格式化
- [McCabe](https://pypi.org/project/mccabe/) ：复杂度检测工具

## 开发约定

- 每行不超过 79 个字符。
- 函数复杂度不超过 14 。
- 代码覆盖率不低于 90% 。

## 文档构建工具

主网站 [pyechart.org](http://pyecharts.org) 由 [docsify](https://docsify.js.org/) 构建。
