import json
from pprint import pprint

class Base():

    def __init__(self, title, subtitle, **kwargs):
        self._option = {}
        self._width = kwargs.get('width', 800)
        self._height = kwargs.get('height', 440)
        self._option.update(
            title={"text":title, "subtext":subtitle,
                   "left":kwargs.get('title_pos', 'auto'),
                   "textStyle":{"color":kwargs.get('title_color', '#000')}
                   },
            backgroundColor=kwargs.get('background', '#fff')
        )

    @staticmethod
    def _label(type=None, **kwargs):
        # Pie -> label_pos ("center", "outside", "inside"):
        # Line/Scatter/Bar -> label_pos ("top", left", "right", "bottom", "inside"):
        label_pos = "top"
        if type == "pie":
            label_pos = "outside"
        label={"normal": {"show":kwargs.get('label_show', False),
                          "position":label_pos, "formatter":kwargs.get('formatter', None),
                          "textStyle":{"color":kwargs.get('label_text_color', '#000'),
                                       "fontSize":kwargs.get('label_text_size', 12)}}
               }
        return label

    @staticmethod
    def _color(**kwargs):
        lc = kwargs.get('label_color', None)
        colorlst = ['#c23531', '#2f4554', '#61a0a8', '#d48265', '#749f83',
                    '#ca8622', '#bda29a', '#6e7074', '#546570', '#c4ccd3']
        if lc is not None:
            for color in reversed(list(lc)):
                colorlst.insert(0, color)
        return colorlst

    @staticmethod
    def _xy_axis(**kwargs):
        # xaxis_name_pos ("start", "middle", "end")
        fontsize = kwargs.get('xy_font_size', 14)
        namegap = kwargs.get('nameGap', 25)
        xAxis = {"data":kwargs.get('x_axis'), "name":kwargs.get('xaxis_name', ""),
                 "nameLocation":kwargs.get('xaxis_name_pos', "middle"),
                 "nameGap":namegap, "nameTextStyle":{"fontSize":fontsize},
                 "axisLabel": {"interval": kwargs.get('interval', "auto")}
                 }
        yAxis = {"name":kwargs.get('yaxis_name', ""),
                 "nameLocation":kwargs.get('yaxis_name_pos', "middle"),
                 "nameGap":namegap, "nameTextStyle":{"fontSize":fontsize}
                 }
        return xAxis, yAxis

    @staticmethod
    def cast(seq):
        k_lst, v_lst = [], []
        if isinstance(seq, list):
            for s in seq:
                try:
                    if isinstance(s, tuple):
                        k_lst.append(s[0])
                        v_lst.append(s[1])
                except:
                    raise ValueError
        elif isinstance(seq, dict):
            for k, v in seq.items():
                k_lst.append(k)
                v_lst.append(v)
        return k_lst, v_lst

    def show_config(self):
        pprint(self._option)

    def render(self, path=r"..\render.html"):
        temple = r"..\temple.html"
        try:
            if self._option.get("series")[0].get("type") == "radar":
                temple = r"..\radartemple.html"
        except:
            pass
        with open(temple, "r", encoding="utf-8") as f:
            my_option = json.dumps(self._option, indent=4, ensure_ascii=False)
            open(path, "w+", encoding="utf-8").write(f.read()
                                                     .replace("myOption", my_option)
                                                     .replace("myWidth", str(self._width))
                                                     .replace("myHeight", str(self._height)))


