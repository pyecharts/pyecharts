> 主题自定义篇：适用在 pyecharts v0.5.2 以后的版本。

自 0.5.2 起，pyecharts 支持更换主体色系。下面是跟换为 'dark' 的例子：

```python
from pyecharts import Bar

bar = Bar("我的第一个图表", "这里是副标题")
bar.use_theme('dark')
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
bar.render()
```
![guide-2](https://user-images.githubusercontent.com/4280312/39617664-79789878-4f78-11e8-9f0e-c3a2c371b6cb.png)

## 如何获得跟多主题

伴随 pyecharts 0.5.2, `echarts-themes-pypkg` 提供 vintage, macarons, infographic, shine 和 roma 主题。

### vintage:

![screen shot 2018-05-03 at 00 10 06](https://user-images.githubusercontent.com/4280312/39553641-8e54c766-4e66-11e8-9156-5b8fa13cb9f9.png)

### macarons:

![screen shot 2018-05-03 at 00 13 12](https://user-images.githubusercontent.com/4280312/39553690-cc3adffc-4e66-11e8-8423-eb39b5216329.png)

### infographic
![screen shot 2018-05-03 at 00 13 59](https://user-images.githubusercontent.com/4280312/39553714-eb2e7d74-4e66-11e8-9985-0bb3f5dd6f57.png)

### shine:

![screen shot 2018-05-03 at 00 14 59](https://user-images.githubusercontent.com/4280312/39553751-0f360778-4e67-11e8-8eea-0c2d6e3b91d9.png)


### roma:

![screen shot 2018-05-03 at 00 17 27](https://user-images.githubusercontent.com/4280312/39553828-656680fa-4e67-11e8-8c3c-ff4ec71fb4db.png)

你需要做的就是把 echarts-themes-pypkg 装上。

```
pip install echarts-themes-pypkg
```

然后在前面的例子里把 'dark' 换成你的新主题就可以了：

```python
bar.use_theme('vintage')
```
