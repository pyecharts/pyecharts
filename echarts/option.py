import random

class Option():

    def label(self, type=None,
              is_emphasis=True,
              label_pos=None,
              is_label_show=False,
              label_text_color="#000",
              label_text_size=12,
              formatter=None,
              **kwargs):
        """

        :param type:
            图例类型
        :param is_emphasis:
            是否高亮显示标签
        :param label_pos:
            标签位置
        :param is_label_show:
            是否正常显示标签
        :param label_text_color:
            标签字体颜色
        :param label_text_size:
            标签字体大小
        :param formatter:
            标签内容格式器，有 series,name,value,percent 可选
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

    def color(self, colorlst,
              is_random=False,
              label_color=None,
              **kwargs):
        """

        :param colorlst:
            全局颜色列表
        :param is_random:
            是否随机排列颜色列表
        :param label_color:
            追加颜色项
        :param kwargs:
        :return:
        """
        if label_color:
            for color in reversed(list(label_color)):
                colorlst.insert(0, color)
        if is_random:
            random.shuffle(colorlst)
        return colorlst

    def line_style(self, line_width=1,
                   line_opacity=1,
                   line_curve=0,
                   line_type="solid",
                   **kwargs):
        """

        :param line_width:
            线的宽度
        :param line_opacity:
            线的透明度，0 为完全透明，1 为完全不透明
        :param line_curve:
            线的弯曲程度，0 为完全不弯曲，1 为最弯曲
        :param line_type:
            线的类型，有 solid，dashed，dotted
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

    def split_line(self, is_splitline_show=True, **kwargs):
        """

        :param is_splitline_show:
            是否显示分割线
        :param kwargs:
        :return:
        """
        _split_line = {
            "show": is_splitline_show,
            "lineStyle": self.line_style(**kwargs)
        }
        return _split_line

    def axis_line(self, is_axisline_show=True, **kwargs):
        """

        :param is_axisline_show:
            是否显示坐标轴线
        :param kwargs:
        :return:
        """
        _axis_line = {
            "show": is_axisline_show,
            "lineStyle": self.line_style(**kwargs)
        }
        return _axis_line

    def split_area(self, is_area_show=True, **kwargs):
        """

        :param is_area_show:
            是否显示填充区域
        :param kwargs:
        :return:
        """
        _split_area = {
            "show": is_area_show,
            "areaStyle": self.axis_line(**kwargs)
        }
        return _split_area

    def area_style(self, flag=False,
                   area_opacity=None,
                   area_color=None,
                   **kwargs):
        """

        :param flag:
            图例类型标记位
        :param area_opacity:
            填充区域透明度
        :param area_color:
            填充区域颜色
        :param kwargs:
        :return:
        """
        if area_opacity is None:
            area_opacity = 0 if flag else 1
        _area_style = {
            "opacity": area_opacity,
            "color": area_color
        }
        return _area_style

    def xy_axis(self, type=None,
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
            图例类型
        :param xy_font_size:
            x 轴和 y 轴字体大小
        :param namegap:
            坐标轴名称与轴线之间的距离
        :param xaxis_name:
            x 轴名称
        :param xaxis_name_pos:
            x 轴名称位置，有 start，middle，end 可选
        :param interval:
            坐标轴刻度标签的显示间隔，在类目轴中有效
            默认会采用标签不重叠的策略间隔显示标签
            可以设置成 0 强制显示所有标签
            如果设置为 1，表示『隔一个标签显示一个标签』，如果值为 2，表示隔两个标签显示一个标签，以此类推
        :param yaxis_name:
            y 轴名称
        :param yaxis_name_pos:
            y 轴名称位置，有 start，middle，end 可选
        :param is_convert:
            是否交换 x 轴与 y 轴
        :param x_axis:
            x 轴数据项
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
            标记数据项，有最小值，最大值，平均值可选
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

    def mark_point(self, mark_point=None, **kwargs):
        """

        :param mark_point:
            标记点，有最小值，最大值，平均值可选
        :param kwargs:
        :return:
        """
        return self._mark(mark_point)

    def mark_line(self, mark_line=None, **kwargs):
        """

        :param mark_line:
            标记线，有最小值，最大值，平均值可选
        :param kwargs:
        :return:
        """

        return self._mark(mark_line)

    def legend(self, is_legend_show=True,
               legend_orient="horizontal",
               legend_pos="center",
               **kwargs):
        """

        :param is_legend_show:
            是否显示顶端图例
        :param legend_orient:
            图例列表的布局朝向，有 horizontal，vertical 可选
        :param legend_pos:
            图例位置，有 left, center, right 可选
        :param kwargs:
        :return:
        """
        _legend = {
            "show": is_legend_show,
            "left": legend_pos,
            "orient": legend_orient
        }
        return _legend

    def visual_map(self, visual_range=None,
                   visual_text_color=None,
                   visual_range_text=None,
                   visual_range_color=None,
                   is_calculable=True,
                   **kwargs):
        """

        :param visual_range:
            指定组件的允许的最小值与最大值
        :param visual_text_color:
            两端文本颜色
        :param visual_range_text:
            两端文本
        :param visual_range_color:
            过渡的颜色，列表类型
        :param is_calculable:
            是否显示拖拽用的手柄（手柄能拖拽调整选中范围）
        :param kwargs:
        :return:
        """
        _min, _max = 0, 100
        if visual_range:
            if len(visual_range) == 2:
                _min, _max = visual_range

        _tlow, _thight = "low", "hight"
        if visual_range_text:
            if len(visual_range_text) == 2:
                _tlow, _thight = visual_range_text

        inrange= ['#50a3ba', '#eac763', '#d94e5d']
        if visual_range_color:
            if len(visual_range_color) >= 2:
                inrange = visual_range_color

        _visual_map = {
            "type": "continuous",
            "min": _min,
            "max": _max,
            "text": [_thight, _tlow],
            "textStyle": {"color": visual_text_color},
            "inRange": {"color": inrange},
            "calculable": is_calculable,
            "left": "left",
            "top": "bottom"
        }
        return _visual_map

    def gen_color(self):
        """

        :return:
        """
        return "rgb(%s,%s,%s)" % (random.randint(0, 160),
                                  random.randint(0, 160),
                                  random.randint(0, 160))

    def symbol(self, type=None, symbol="", **kwargs):
        """

        :param symbol:
            标记类型
        :param kwargs:
        :return:
        """
        if symbol is None:                      # Radar
            symbol = 'none'
        elif type == "line" and symbol == "":   # Line
            symbol = "emptyCircle"
        elif symbol not in ('rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow'):
            symbol = 'circle'
        return symbol
