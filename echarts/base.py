import json
from pprint import pprint

class Base():

    def __init__(self, title="", subtitle="", *, width, height):
        self._option = {}
        self._width, self._height = width, height
        self._colorlst = ['#c23531', '#2f4554', '#61a0a8', '#d48265', '#749f83',
                          '#ca8622', '#bda29a', '#6e7074', '#546570', '#c4ccd3']
        self._option.update(
            title={"text":title, "subtext":subtitle}
        )

    @staticmethod
    def cast(seq):
        k_lst, v_lst = [], []
        if isinstance(seq, list):
            for l in seq:
                try:
                    if isinstance(l, tuple):
                        k_lst.append(l[0])
                        v_lst.append(l[1])
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
        with open(r"..\temple.html", "r", encoding="utf-8") as f:
            my_option = json.dumps(self._option, indent=4, ensure_ascii=False)
            open(path, "w+", encoding="utf-8").write(f.read()
                                                     .replace("myOption", my_option)
                                                     .replace("myWidth", str(self._width))
                                                     .replace("myHeight", str(self._height)))


