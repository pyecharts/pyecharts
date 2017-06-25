import random

class Option():

    def label(self,
              type=None,
              is_emphasis=True,
              label_pos=None,
              is_label_show=False,
              label_text_color="#000",
              label_text_size=12,
              formatter=None,
              **kwargs):
        """

        :param type:
        :param is_emphasis:
        :param label_pos:
        :param is_label_show:
        :param label_text_color:
        :param label_text_size:
        :param formatter:
        :param kwargs:
        :return:
        """
        if label_pos is None:
            label_pos = "outside" if type in ["pie", "graph"] else "top"
        _label = {
            "normal": {"show": is_label_show,
                       "position": label_pos,
                       "textStyle": {"color": label_text_color,
                                     "fontSize": label_text_size}},
            "emphasis": {"show": is_emphasis}
        }
        fmat = {
            "series": "{a} ",
            "name": "{b} ",
            "value": "{c} ",
            "percent": "{d}% "
        }
        if formatter is None:
            _formatter = "{b} {d}%" if type == "pie" else None
        else:
            _formatter = "".join([fmat.get(f) for f in formatter if fmat.get(f, None)])
        if type != "graph":
            _label.get("normal").update(formatter=_formatter)
        return _label

    def color(self,
              colorlst,
              is_random=False,
              label_color=None,
              **kwargs):
        """

        :param colorlst:
        :param is_random:
        :param label_color:
        :param kwargs:
        :return:
        """
        if label_color:
            for color in reversed(list(label_color)):
                colorlst.insert(0, color)
        if is_random:
            random.shuffle(colorlst)
        return colorlst

    def line_style(self,
                   line_width=1,
                   line_opacity=1,
                   line_curve=0,
                   line_type="solid",
                   **kwargs):
        """

        :param line_width:
        :param line_opacity:
        :param line_curve:
        :param line_type:
        :param kwargs:
        :return:
        """
        _line_style = {
            "normal": {"width": line_width,
                       "opacity": line_opacity,
                       "curveness": line_curve,
                       "type": line_type}
        }
        return _line_style

    def split_line(self,
                   is_splitline_show=True,
                   **kwargs):
        """

        :param is_splitline_show:
        :param kwargs:
        :return:
        """
        _split_line = {
            "show": is_splitline_show,
            "lineStyle": self.line_style(**kwargs)
        }
        return _split_line

    def axis_line(self,
                  is_axisline_show=True,
                  **kwargs):
        """

        :param is_axisline_show:
        :param kwargs:
        :return:
        """
        _axis_line = {
            "show": is_axisline_show,
            "lineStyle": self.line_style(**kwargs)
        }
        return _axis_line

    def split_area(self,
                   is_area_show=True,
                   **kwargs):
        """

        :param is_area_show:
        :param kwargs:
        :return:
        """
        _split_area = {
            "show": is_area_show,
            "areaStyle": self.axis_line(**kwargs)
        }
        return _split_area

    def area_style(self,
                   flag=False,
                   area_opacity=None,
                   area_color=None,
                   **kwargs):
        if area_opacity is None:
            area_opacity = 0 if flag else 1
        _area_style = {
            "opacity": area_opacity,
            "color": area_color
        }
        return _area_style

    def xy_axis(self,
                type=None,
                xy_font_size=14,
                namegap=25,
                xaxis_name="",
                xaxis_name_pos="middle",
                interval="auto",
                yaxis_name="",
                yaxis_name_pos="middle",
                is_convert=False,
                x_axis=None,
                **kwargs):
        """

        :param type:
        :param xy_font_size:
        :param namegap:
        :param xaxis_name:
        :param xaxis_name_pos:
        :param interval:
        :param yaxis_name:
        :param yaxis_name_pos:
        :param is_convert:
        :param x_axis:
        :param kwargs:
        :return:
        """
        _xAxis = {
            "name": xaxis_name,
            "nameLocation": xaxis_name_pos,
            "nameGap": namegap,
            "nameTextStyle": {"fontSize": xy_font_size},
            "axisLabel": {"interval": interval}
            }
        _yAxis = {
            "name": yaxis_name,
            "nameLocation": yaxis_name_pos,
            "nameGap": namegap,
            "nameTextStyle": {"fontSize": xy_font_size}
            }
        if is_convert:
            _yAxis.update(data=x_axis, type="category")
            _xAxis.update(type="value")
        else:
            _xAxis.update(data=x_axis, type="category")
            _yAxis.update(type="value")
        if type == "scatter":
            _xAxis.update(data=x_axis, type="value")
            _yAxis.update(type="value")
        return _xAxis, _yAxis

    def _mark(self, data):
        """

        :param data:
        :return:
        """
        mark = {"data": []}
        if data:
            for d in list(data):
                if "max" in d:
                    mark.get("data").append({"type": "max", "name": "最大值"})
                elif "min" in d:
                    mark.get("data").append({"type": "min", "name": "最小值"})
                elif "average" in d:
                    mark.get("data").append({"type": "average", "name": "平均值"})
        return mark

    def mark_point(self,
                   mark_point=None,
                   **kwargs):
        """

        :param mark_point:
        :param kwargs:
        :return:
        """
        return self._mark(mark_point)

    def mark_line(self,
                  mark_line=None,
                  **kwargs):
        """

        :param mark_line:
        :param kwargs:
        :return:
        """

        return self._mark(mark_line)

    def legend(self,
               is_legend_show=True,
               legend_orient="horizontal",
               legend_pos="center",
               **kwargs):
        """

        :param is_legend_show:
        :param legend_orient:
        :param legend_pos:
        :param kwargs:
        :return:
        """
        _legend = {
            "show": is_legend_show,
            "left": legend_pos,
            "orient": legend_orient
        }
        return _legend

    def visual_map(self,
                   visual_range=None,
                   visual_range_text=None,
                   visual_range_color=None,
                   is_calculable=True,
                   **kwargs):

        _min, _max = 0, 100
        if visual_range:
            if len(visual_range) == 2:
                _min, _max = visual_range

        _tlow, _thight = "low", "hight"
        if visual_range_text:
            if len(visual_range_text) == 2:
                _tlow, _thight = visual_range_text

        _clow, _chight = '#e0ffff', '#006edd'
        if visual_range_color:
            if len(visual_range_color) == 2:
                _clow, _chight = visual_range_color

        _visual_map = {
            "min": _min,
            "max": _max,
            "text": [_tlow, _thight],
            "inRange": {"color": [_clow, _chight]},
            "calculable": is_calculable,
            "left": "left",
            "top": "bottom"
        }
        return _visual_map

    def gen_color(self):
        return "rgb({},{},{})".format(random.randint(0, 160),
                                      random.randint(0, 160),
                                      random.randint(0, 160))

    def symbol(self,
               symbol="",
               **kwargs):
        """

        :param symbol:
        :param kwargs:
        :return:
        """
        if symbol is None:
            symbol = 'none'
        elif symbol not in ('rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow'):
            symbol = 'circle'
        return symbol