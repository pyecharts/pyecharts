import os
import json
from pprint import pprint
from echarts.option import Option

class Base():

    def __init__(self, title, subtitle,
                 width=800,
                 height=400,
                 title_pos="auto",
                 title_color="#000",
                 subtitle_color="#aaa",
                 title_text_size=18,
                 subtitle_text_size=12,
                 background_color="#fff"):
        """

        :param title:
        :param subtitle:
        :param background_color:
        :param width:
        :param height:
        :param title_pos:
        :param title_color:
        :param subtitle_color:
        :param title_text_size:
        :param subtitle_text_size:
        """
        self.Option = Option()
        self._option = {}
        self._width, self._height = width, height
        self._colorlst = ['#c23531', '#2f4554', '#61a0a8', '#d48265', '#749f83',
                          '#ca8622', '#bda29a', '#6e7074', '#546570', '#c4ccd3']
        self._option.update(
            title={
                "text": title,
                "subtext": subtitle,
                "left": title_pos,
                "textStyle": {"color": title_color, "fontSize": title_text_size},
                "subtextStyle": {"color": subtitle_color, "fontSize": subtitle_text_size}
            },
            toolbox={
                "show": True,
                "orient": "vertical",
                "left": "right",
                "top": "center",
                "feature": {"saveAsImage": {"show": True}}
            },
            tooltip={},
            series=[],
            legend={"data": []},
            backgroundColor=background_color
        )

    def add(self,
            is_label_show=None,            # for All
            label_pos=None,
            label_color=None,
            label_text_color=None,
            label_text_size=None,
            is_emphasis=None,
            formatter=None,
            is_legend_show=None,
            legend_pos=None,
            legend_orient=None,
            visual_range=None,
            visual_range_text=None,
            visual_range_color=None,
            is_calculable=None,
            is_random=None,
            is_symbol_show=None,
            symbol_size=None,
            is_stack=None,                # for Bar/Line
            scale_range=None,             # only for Gauge
            angle_range=None,
            layout=None,                  # only for Graph
            is_focusnode=None,
            is_rotatelabel=None,
            edge_length=None,
            gravity=None,
            repulsion=None,
            is_smooth=None,               # only for Line
            is_fill=None,
            is_step=None,
            is_roam=None,                 # only for Map
            maptype=None,
            radius=None,                  # only for Pie
            center=None,
            rosetype=None,
            line_width=None,              # only for Radar
            item_color=None,
            symbol=None,
            line_opacity=None,
            line_type=None,
            line_curve=None,
            is_splitline_show=None,
            is_axisline_show=None,
            is_area_show=None,
            area_opacity=None,
            area_color=None,
            shape=None,                  # for Radar/WordCloud
            rader_text_color=None,
            xy_font_size=None,           # for Scatter/Bar/Line
            namegap=None,
            xaxis_name=None,
            xaxis_name_pos=None,
            interval=None,
            yaxis_name=None,
            yaxis_name_pos=None,
            is_convert=None,
            x_axis=None,
            mark_line=None,
            mark_point=None,
            word_gap=None,              # only for WordCloud
            word_size_range=None,
            rotate_step=None,
            effect_brushtype=None,
            effect_scale=None,
            effect_period=None):
        pass

    def custom(self, series):
        _name, _series = series
        for n in _name:
            self._option.get('legend').get('data').append(n)
        for s in _series:
            self._option.get('series').append(s)

    def get_series(self):
        return self._option.get('legend').get('data'), self._option.get('series')

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

    def render(self, path=r"E:\Python\pyecharts\render.html"):
        temple = r"E:\Python\pyecharts\temple\_temple.html"
        series = self._option.get("series")
        for s in series:
            if s.get('type') == "wordCloud":
                temple = r"E:\Python\pyecharts\temple\_temple_wordcloud.html"
                break
            if s.get('type') in ("scatter", "pie", "bar", "line"):
                temple = r"E:\Python\pyecharts\temple\temple.html"
                break
        with open(temple, "r", encoding="utf-8") as f:
            my_option = json.dumps(self._option, indent=4, ensure_ascii=False)
            open(path, "w+", encoding="utf-8").write(
                f.read().replace("myOption", my_option)
                .replace("myWidth", str(self._width))
                .replace("myHeight", str(self._height)))
