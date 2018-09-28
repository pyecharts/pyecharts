> Shortcuts 篇：工具方法

pyecharts 提供了一系列工具方法。

## 方法

**dumps_json**

将图表的 options 转化为 json 字符串。例如在 Django 视图中返回 options 的 json 数据：

```python
from django.http.response import HttpResponse
from pyecharts import Bar
from pyecharts.shortcuts import dumps_json

def get_bar_data(request):
    bar = Bar("我的第一个图表", "这里是副标题")
    bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
    return HttpResponse(dumps_json(bar.options), content_type="application/json")
```

pyecharts 使用了自己的序列化类，定义在 `pyecharts.javascripthon.api.MyJSONEncoder` 。


