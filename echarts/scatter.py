from PIL import Image
from echarts.base import Base

class Scatter(Base):

    def __init__(self, title="", subtitle="", *, width=800, height=440):
        super().__init__(title, subtitle, width=width, height=height)
        self._option.update(
            series={"type":"scatter"}
        )

    def add(self, x_value, y_value, *, xaxis_name="", xaxis_name_pos="middle",
            yaxis_name="", yaxis_name_pos="middle", interval="auto",
            label_show=False, label_pos="top", label_text_color="#000",
            label_text_size=12, label_color=None):

        if isinstance(x_value, list) and isinstance(y_value, list):
            assert len(x_value) == len(y_value)
            if label_pos not in ("top", "left", "right", "bottom", "inside"):
                label_pos = "top"
            if xaxis_name_pos not in("start", "middle", "end"):
                xaxis_name_pos = "middle"
            if yaxis_name_pos not in("start", "middle", "end"):
                yaxis_name_pos = "middle"
            self._option.update(
                xAxis={"name": xaxis_name, "nameLocation": xaxis_name_pos,
                       "nameGap":25, "nameTextStyle":{"fontSize":14},
                       "axisLabel":{"interval": interval}}
            )
            self._option.update(
                dimensions=[xaxis_name, yaxis_name],
                yAxis={"name": yaxis_name, "nameLocation": yaxis_name_pos, "nameGap":25,
                       "nameTextStyle": {"fontSize":14}}
            )
            self._option.get("series").update(
                data=[list(z) for z in zip(x_value, y_value)],
                label={"normal": {"show": label_show, "position": label_pos,
                                  "textStyle": {"color": label_text_color,
                                                "fontSize": label_text_size}}}
            )
            if label_color is not None:
                for color in reversed(list(label_color)):
                    self._colorlst.insert(0, color)
                self._option.update(
                    color=self._colorlst
                )
        else:
            raise ValueError

    @staticmethod
    def draw(path, color=None):
        if color is None:
            color = (255, 255, 255)
        im = Image.open(path)
        width, height = im.size
        imarray = im.load()
        # 垂直翻转图片
        for x in range(width):
            for y in range(height):
                if y < int(height / 2):
                    imarray[x, y], imarray[x, height - y - 1] = imarray[x, height - y - 1], imarray[x, y]
        # 默认只画出非白色区域，可自行配置颜色
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
    v1, v2 = scatter.draw(r"e:\cup.png")
    scatter.add(v1, v2)
    # scatter.show_config()
    scatter.render()