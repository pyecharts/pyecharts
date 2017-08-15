# 用户自定义地图

考虑到项目更好的通用性，以及更好可扩展性，所以决定对地图部分提供自定义模式。

## 下载地图

这里是 Echarts 官方地图下载地址 [download-map](http://echarts.baidu.com/download-map.html)

![customize-map-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/customize-map-0.png)

除了官方提供的主要省份的地图，还可根据自己的需求自定义。

![customize-map-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/customize-map-1.png)

所有地图均要下载成 JS 格式。


## 如何添加
下面就以广东地图为例，说明如何自行添加地图。

### 保存地图文件
我已经下载了广东地图的 JS 文件，文件名为 guangdong.js。将 guangdong.js 保存在项目安装目录下的 templates/js 文件夹中。Windows 下一般为 Lib/site-packages/pyecharts/templates/js/echarts

### 修改代码
打开 templates 文件夹下的 base.html 文件，新增一行 ```<script type="text/javascript " src="js/guangdong.js "></script>```

![customize-map-2](https://github.com/chenjiandongx/pyecharts/blob/master/images/customize-map-2.png)

在 Map 类的 add() 中，设置 mapType='广东' 即可。如下
```python
from pyecharts import Map

value = [20, 190, 253, 77, 65]
attr = ['汕头市', '汕尾市', '揭阳市', '阳江市', '肇庆市']
map = Map("广东地图示例", width=1200, height=600)
map.add("", attr, value, maptype='广东', is_visualmap=True, visual_text_color='#000')
map.show_config()
map.render()
```

如果只是使用 render() 生成 .html 文件的话到这里就可以了。还想要在 jupyter notebook 上展示地图的话，还需要下面一个步骤。  
打开项目根目录下的 template.py，找到 _mapindex 变量，新增 ```"广东": "guangdong"```，格式为 ```省份中文: "省份英文"。

```python
_mapindex = {
    "广东": "guangdong",
}
```

然后查看jupyter-notebook的所有路径。下面是mac os的例子：

```
$ jupyter --paths
config:
    /Users/jaska/.jupyter
    /Users/jaska/github/data-analysis-env/bin/../etc/jupyter
    /usr/local/etc/jupyter
    /etc/jupyter
data:
    /Users/jaska/Library/Jupyter  <--- user directory
    /Users/jaska/github/data-analysis-env/bin/../share/jupyter
    /usr/local/share/jupyter
    /usr/share/jupyter
runtime:
    /Users/jaska/Library/Jupyter/runtime
```

你需要做的就是把guangdong.js拷贝到/Users/jaska/Library/Jupyter/nbextensions/echarts/.

现在也能在 jupyter notebook 上展示你所属要的地图了。