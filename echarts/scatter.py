from PIL import Image
from echarts.base import Base

class Scatter(Base):

    def __init__(self, title="", subtitle="", **kwargs):
        super().__init__(title, subtitle, **kwargs)
        self._option.update(series={"type": "scatter"})

    def add(self, x_value, y_value, **kwargs):
        if isinstance(x_value, list) and isinstance(y_value, list):
            assert len(x_value) == len(y_value)
            xaxis, yaxis = Base._xy_axis(**kwargs)
            self._option.update(
                xAxis=xaxis, yAxis=yaxis,
                # dimensions
            )
            self._option.get("series").update(
                data=[list(z) for z in zip(x_value, y_value)],
                label=Base._label(**kwargs)
            )
            self._option.update(color=Base._color(**kwargs))
        else:
            raise ValueError

    @staticmethod
    def draw(path, color=None):
        """
        :param path: 图片存放路径
        :param color: 默认只画出非白色区域，可自行配置颜色
        :return:
        """
        if color is None:
            color = (255, 255, 255)
        im = Image.open(path)
        width, height = im.size
        imarray = im.load()
        # 垂直翻转图片
        for x in range(width):
            for y in range(height):
                if y < int(height / 2):
                    imarray[x, y], imarray[x, height-y-1] = imarray[x, height-y-1], imarray[x, y]
        result = []
        for x in range(width):
            for y in range(height):
                if imarray[x, y] != color:
                    result.append((x, y))
        return Scatter.cast(result)

    def config(self):
        pass


v1 = [10, 20, 30, 40, 50, 60]
v2 = [10, 20, 30, 40, 50, 60]

if __name__ == "__main__":
    scatter = Scatter()
    scatter.add(v1, v2)
    scatter.show_config()
    scatter.render()