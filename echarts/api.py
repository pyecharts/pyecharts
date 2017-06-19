from echarts.option import Option

class Api():

    def __init__(self):
        self.config = Option()

    def label(self, type=None, **kwargs):
        """

        :param type: 图表类型
        :param kwargs:
        :return:
        """
        return self.config.label(type, **kwargs)

    def color(self, colorlst, **kwargs):
        """

        :param colorlst: 颜色列表
        :param kwargs:
        :return:
        """
        return self.config.color(colorlst, **kwargs)

    def line_style(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        return self.config.line_style(**kwargs)

    def split_line(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        return self.config.split_line(**kwargs)

    def axis_line(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        return self.config.axis_line(**kwargs)

    def split_area(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        return self.config.split_area(**kwargs)

    def xy_axis(self, type=None, **kwargs):
        """

        :param type: 图表类型
        :param kwargs:
        :return:
        """
        return self.config.xy_axis(type, **kwargs)

    def _mark(self, data):
        """

        :param data: 标记数据
        :return:
        """
        return self.config._mark(data)

    def mark_point(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        return self.config.mark_point(**kwargs)

    def mark_line(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        return self.config.mark_line(**kwargs)

    def legend(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        return self.config.legend(**kwargs)

    def cast(self, seq):
        """

        :param seq: 转换序列
        :return:
        """
        return self.config.cast(seq)