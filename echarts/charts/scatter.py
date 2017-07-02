from PIL import Image
from echarts.base import Base
from echarts.option import get_all_options

class Scatter(Base):
    """
    <<< 散点图 >>>
    直角坐标系上的散点图可以用来展现数据的 x，y 之间的关系，如果数据项有多个维度，可以用颜色来表现，利用 geo 组件。
    """
    def __init__(self, title="", subtitle="", **kwargs):
        super().__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, x_value, y_value, *,
              symbol_size=10, **kwargs):
        """

        :param name:
            图例名称
        :param x_axis:
            x 坐标轴数据
        :param y_axis:
            y 坐标轴数据
        :param symbol_size:
            标记图形大小
        :param kwargs:
        """
        if isinstance(x_value, list) and isinstance(y_value, list):
            assert len(x_value) == len(y_value)
            kwargs.update(type="scatter")
            chart = get_all_options(**kwargs)
            xaxis, yaxis = chart['xy_axis']
            self._option.update(xAxis=xaxis, yAxis=yaxis)
            self._option.get('legend').get('data').append(name)
            self._option.get('series').append({
                "type": "scatter",
                "name": name,
                "symbol": chart['symbol'],
                "symbolSize": symbol_size,
                "data": [list(z) for z in zip(x_value, y_value)],
                "label": chart['label'],
            })
            self._legend_visualmap_colorlst(**kwargs)
        else:
            raise TypeError("x_axis and y_axis must be list")

    def draw(self, path, color=None):
        """ 将图片上的像素点转换为数组，如 color 为 （255,255,255）时只保留非白色像素点的坐标信息

        :param path:
            转换图片的地址
        :param color:
            所要排除的颜色
        :return:
        """
        color = color or (255, 255, 255)
        im = Image.open(path)
        width, height = im.size
        imarray = im.load()
        # 垂直翻转图片
        for x in range(width):
            for y in range(height):
                if y < int(height / 2):
                    imarray[x, y], imarray[x, height-y-1] = imarray[x, height-y-1], imarray[x, y]
        result = [(x, y) for x in range(width) for y in range(height) if imarray[x, y][:3] != color]
        return self.cast(result)
