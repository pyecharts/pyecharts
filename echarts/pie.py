from echarts.base import Base

class Pie(Base):

    def __init__(self, title="", subtitle="", *, background="#fff", width=800, height=440):
        super().__init__(title, subtitle, background=background, width=width, height=height)
        self._option.update(
            series={"type":"pie"}
        )

    def add(self, name, value, *, rad=None, rose_type=False,
            formatter=("data_name", "percent"), label_show=False, label_pos="outside",
            label_text_color="#000", label_text_size=12,  label_color=None):

        if isinstance(name, list) and isinstance(value, list):
            assert len(name) == len(value)
            if label_pos not in ("center", "outside", "inside"):
                label_pos = "outside"
            data = [{"name":z[0], "value":z[1]} for z in zip(name, value)]
            if rad is None:
                rad = ["0%", "75%"]
            else:
                rad = ["{}%".format(rad[0]), "{}%".format(rad[1])]
            if rose_type is True: rose_type = "radius"
            fmat_result = ""
            fmat = {"series_name": "{a} ", "data_name": "{b} ", "data_value": "{c} ", "percent": "{d}% "}
            for f in formatter:
                fmat_result += fmat.get(f)
            self._option.get("series").update(
                data=data,
                radius=rad,
                roseType=rose_type,
                label={"normal":{"show":label_show, "position":label_pos, "formatter":fmat_result,
                                 "textStyle":{"color":label_text_color,
                                              "fontSize":label_text_size}}}
            )
            if label_color is not None:
                for color in reversed(list(label_color)):
                    self._colorlst.insert(0, color)
                self._option.update(
                    color=self._colorlst,
                )
        else:
            raise ValueError

    def config(self):
        pass


attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
value = [11, 12, 13, 10, 10, 10]

if __name__ == "__main__":
    pie = Pie("异地招聘-工资范围分布", "[x, y] 包含边界值 x 和 y")
    pie.add(attr, value, label_show=True, rose_type=True)
    pie.show_config()
    pie.render()