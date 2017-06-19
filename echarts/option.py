
class Option():

    def label(self,
              type=None,
              label_pos="top",
              label_show=False,
              label_text_color="#000",
              label_text_size=12,
              formatter=None,
              **kwargs):
        """

        :param type:
        :param label_pos:
        :param label_show:
        :param label_text_color:
        :param label_text_size:
        :param formatter:
        :param kwargs:
        :return:
        """
        if type == "pie":
            label_pos = "outside"
        elif type == "graph":
            label_pos = "inside"
        _label = {"normal": {"show": label_show,
                             "position": label_pos,
                             "textStyle": {"color": label_text_color,
                                           "fontSize": label_text_size}}}
        if type != "graph":
            _label.get("normal").update(formatter=formatter)
        return _label

    def color(self,
              colorlst,
              label_color=None,
              **kwargs):
        """

        :param colorlst:
        :param label_color:
        :param kwargs:
        :return:
        """
        if label_color is not None:
            for color in reversed(list(label_color)):
                colorlst.insert(0, color)
        return colorlst

    def line_style(self,
                   line_width=1,
                   line_opacity=1,
                   line_type="solid",
                   **kwargs):
        """

        :param line_width:
        :param line_opacity:
        :param line_type:
        :param kwargs:
        :return:
        """
        _line_style = {"normal": {"width": line_width,
                                  "opacity": line_opacity,
                                  "type": line_type}}
        return _line_style

    def split_line(self,
                   split_line_show=True,
                   **kwargs):
        """

        :param split_line_show:
        :param kwargs:
        :return:
        """
        _split_line = {"show": split_line_show,
                       "lineStyle": self.line_style(**kwargs)}
        return _split_line

    def axis_line(self,
                  axis_line_show=True,
                  **kwargs):
        """

        :param axis_line_show:
        :param kwargs:
        :return:
        """
        _axis_line = {"show": axis_line_show,
                      "lineStyle": self.line_style(**kwargs)}
        return _axis_line

    def split_area(self,
                   split_area_show=False,
                   split_area_opacity=1,
                   **kwargs):
        """

        :param split_area_show:
        :param split_area_opacity:
        :param kwargs:
        :return:
        """
        _split_area = {"show": split_area_show,
                       "areaStyle": {"opacity": split_area_opacity}}
        return _split_area

    def xy_axis(self, type=None,
                xy_font_size=14,
                nameGap=25,
                xaxis_name="",
                xaxis_name_pos="middle",
                interval="auto",
                yaxis_name="",
                yaxis_name_pos="middle",
                exchange=False,
                x_axis=None,
                **kwargs):
        """

        :param type:
        :param xy_font_size:
        :param nameGap:
        :param xaxis_name:
        :param xaxis_name_pos:
        :param interval:
        :param yaxis_name:
        :param yaxis_name_pos:
        :param exchange:
        :param x_axis:
        :param kwargs:
        :return:
        """
        _xAxis = {"name": xaxis_name,
                  "nameLocation": xaxis_name_pos,
                  "nameGap": nameGap,
                  "nameTextStyle": {"fontSize": xy_font_size},
                  "axisLabel": {"interval": interval}
                 }
        _yAxis = {"name": yaxis_name,
                  "nameLocation": yaxis_name_pos,
                  "nameGap": nameGap,
                  "nameTextStyle": {"fontSize": xy_font_size}
                 }
        if exchange:
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
        if data is not None:
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
               legend_show=True,
               legend_orient="horizontal",
               legend_pos="auto",
               **kwargs):
        """

        :param legend_show:
        :param legend_orient:
        :param legend_pos:
        :param kwargs:
        :return:
        """
        legend = {"show": legend_show, "left": legend_pos, "orient": legend_orient}
        return legend

    def cast(self, seq):
        """

        :param seq:
        :return:
        """
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