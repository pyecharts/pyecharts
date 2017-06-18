from echarts.option import Option

class Api():

    def __init__(self):
        self.config = Option()

    def label(self, type=None, **kwargs):
        """

        :param type:
        :param kwargs:
            :param formatter:
            :param label_pos:
            :param label_show:
            :param label_text_color:
            :param label_text_size:
        :return:
        """
        return self.config.label(type, **kwargs)

    def color(self, colorlst, **kwargs):
        """

        :param colorlst:
        :param kwargs:
            :param label_color
        :return:
        """
        return self.config.color(colorlst, **kwargs)

    def line_style(self, **kwargs):
        """

        :param kwargs:
            :param line_width
            :param line_opacity
            :param line_type
        :return:
        """
        return self.config.line_style(**kwargs)

    def split_line(self, **kwargs):
        """

        :param kwargs:
            :param split_line_show
        :return:
        """
        return self.config.split_line(**kwargs)

    def axis_line(self, **kwargs):
        """

        :param kwargs:
            :param axis_line_show
        :return:
        """
        return self.config.axis_line(**kwargs)

    def split_area(self, **kwargs):
        """

        :param kwargs:
            :param split_area_show
            :param split_area_opacity
        :return:
        """
        return self.config.split_area(**kwargs)

    def xy_axis(self, type=None, **kwargs):
        """

        :param type:
        :param kwargs:
            :param xy_font_size
            :param nameGap
            :param xaxis_name
            :param xaxis_name_pos
            :param fontSize
            :param interval
            :param yaxis_name
            :param yaxis_name_pos
            :param exchange
            :param x_axis
        :return:
        """
        return self.config.xy_axis(type, **kwargs)

    def _mark(self, data):
        """

        :param data:
        :return:
        """
        return self.config._mark(data)

    def mark_point(self, **kwargs):
        """

        :param kwargs:
            :param mark_point
        :return:
        """
        return self.config.mark_point(**kwargs)

    def mark_line(self, **kwargs):
        """

        :param kwargs:
            :param mark_line
        :return:
        """
        return self.config.mark_line(**kwargs)

    def cast(self, seq):
        """

        :param seq:
        :return:
        """
        return self.config.cast(seq)