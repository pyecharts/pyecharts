import json
from pprint import pprint
from echarts.option import Option

class Base():

    def __init__(self, title,
                 subtitle,
                 background_color="#fff",
                 width=800,
                 height=400,
                 title_pos="auto",
                 title_color="#000",
                 subtitle_color="#aaa",
                 title_text_size=18,
                 subtitle_text_size=12):
        self.Option = Option()
        self._option = {}
        self._width, self._height = width, height
        self._colorlst = ['#c23531', '#2f4554', '#61a0a8', '#d48265', '#749f83',
                          '#ca8622', '#bda29a', '#6e7074', '#546570', '#c4ccd3']
        self._option.update(
            title={"text": title,
                   "subtext": subtitle,
                   "left": title_pos,
                   "textStyle": {"color": title_color, "fontSize": title_text_size},
                   "subtextStyle": {"color": subtitle_color, "fontSize": subtitle_text_size}
                  },
            tooltip={},
            series=[],
            legend={"data": []},
            backgroundColor=background_color
        )

    def add(self,
            label_show=None,            # for All
            label_pos=None,
            label_color=None,
            label_text_color=None,
            label_text_size=None,
            isemphasis=None,
            formatter=None,
            legend_show=None,
            legend_pos=None,
            legend_orient=None,
            visual_range=None,
            visual_range_text=None,
            visual_range_color=None,
            iscalculable=None,
            israndom=None,
            isstack=None,               # only for Bar
            layout=None,                # only for Graph
            edge_length=None,
            gravity=None,
            repulsion=None,
            issmooth=None,              # only for Line
            isroam=None,                # only for Map
            maptype=None,
            radius=None,                # only for Pie
            center=None,
            rosetype=None,
            line_width=None,            # only for Radar
            line_opacity=None,
            line_type=None,
            line_curve=None,
            split_line_show=None,
            axis_line_show=None,
            split_area_show=None,
            split_area_opacity=None,
            shape=None,                 # for Radar/WordCloud
            rader_text_color=None,
            area_opacity=None,
            xy_font_size=None,          # for Scatter/Bar/Line
            namegap=None,
            xaxis_name=None,
            xaxis_name_pos=None,
            interval=None,
            yaxis_name=None,
            yaxis_name_pos=None,
            isconvert=None,
            x_axis=None,
            mark_line=None,
            mark_point=None,
            word_gap=None,             # only for WordCloud
            word_size_range=None,
            rotate_step=None):
        pass

    def custom(self, series):
        for s in series:
            self._option.get('series').append(s)

    def get_series(self):
        return self._option.get('series')

    def show_config(self):
        pprint(self._option)

    def cast(self, seq):
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

    def render(self, path=r"..\render.html"):
        temple = r"..\temple\_temple.html"
        try:
            if self._option.get("series")[0].get("type", None) == "wordCloud":
                temple = r"..\temple\_temple_wordcloud.html"
            if self._option.get("series")[0].get("type", None) in ("scatter", "pie", "bar", "line"):
                temple = r"..\temple\temple.html"
        except KeyError:
            pass
        with open(temple, "r", encoding="utf-8") as f:
            my_option = json.dumps(self._option, indent=4, ensure_ascii=False)
            open(path, "w+", encoding="utf-8").write(
                f.read().replace("myOption", my_option)
                .replace("myWidth", str(self._width))
                .replace("myHeight", str(self._height)))
