import json
from pprint import pprint
from echarts.api import Api

class Base():

    def __init__(self, title, subtitle, **kwargs):
        self.Parms = Api()
        self._option = {}
        self._width = kwargs.get('width', 800)
        self._height = kwargs.get('height', 440)
        self._colorlst = ['#c23531', '#2f4554', '#61a0a8', '#d48265', '#749f83',
                          '#ca8622', '#bda29a', '#6e7074', '#546570', '#c4ccd3']
        self._option.update(
            title={"text": title,
                   "subtext": subtitle,
                   "left": kwargs.get('title_pos', 'auto'),
                   "textStyle": {"color": kwargs.get('title_color', '#000')}
                  },
            tooltip={},
            series=[],
            legend={"data": []},
            backgroundColor=kwargs.get('background', '#fff')
        )

    def show_config(self):
        pprint(self._option)

    def render(self, path=r"..\render.html"):
        temple = r"..\temple.html"
        try:
            if self._option.get("series")[0].get("type", None) in ("radar", "graph") \
                    or self._option.get("series")[0].get('type', None) == "gauge":
                temple = r"..\_temple.html"
        except:
            pass
        with open(temple, "r", encoding="utf-8") as f:
            my_option = json.dumps(self._option, indent=4, ensure_ascii=False)
            open(path, "w+", encoding="utf-8").write(
                f.read().replace("myOption", my_option)
                .replace("myWidth", str(self._width))
                .replace("myHeight", str(self._height))
            )


