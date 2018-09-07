# coding=utf-8
from pyecharts.base import Base
from pyecharts.constants import PAGE_TITLE
from pyecharts.echarts.option import grid
from pyecharts.utils import merge_js_dependencies


class Grid(Base):
    """
    <<< 并行显示多张图 >>>

    用户可以自定义结合 Line/Bar/Kline/Scatter/EffectScatter/Pie/HeatMap
    /Boxplot 图表，将不同类型图表画在多张图上。第一个图需为 有 x/y 轴的图，
    即不能为 Pie，其他位置顺序任意。
    """

    def __init__(self, page_title=PAGE_TITLE, width=800, height=400, **kwargs):
        super(Grid, self).__init__(width=width, height=height, **kwargs)
        self._page_title = page_title

    def add(
        self,
        chart,
        grid_width=None,
        grid_height=None,
        grid_top=None,
        grid_bottom=None,
        grid_left=None,
        grid_right=None,
    ):
        """

        :param chart:
            图形实例
        :param grid_width:
            grid 组件的宽度。默认自适应。
        :param grid_height:
            grid 组件的高度。默认自适应。
        :param grid_top:
            grid 组件离容器顶部的距离。默认为 None, 有'top', 'center',
            'middle'可选，也可以为百分数或者整数
        :param grid_bottom:
            grid 组件离容器底部的距离。默认为 None, 有'top', 'center',
            'middle'可选，也可以为百分数或者整数
        :param grid_left:
            grid 组件离容器左侧的距离。默认为 None, 有'left', 'center',
            'right'可选，也可以为百分数或者整数
        :param grid_right:
            grid 组件离容器右侧的距离。默认为 None, 有'left', 'center',
            'right'可选，也可以为百分数或者整数
        """
        if not self._option:
            self._option = chart.get_options(remove_none=False)
            self._option.update(grid=[])
            self._js_dependencies = chart.js_dependencies

            _grid = grid(
                grid_width,
                grid_height,
                grid_top,
                grid_bottom,
                grid_left,
                grid_right,
            )
            if _grid:
                for _ in range(len(self._option.get("series"))):
                    self._option.get("grid").append(_grid)
        else:
            chart_options = chart.get_options(remove_none=False)
            _series = (
                chart_options.get("series"),
                chart_options.get("xAxis", None),
                chart_options.get("yAxis", None),
                chart_options.get("legend")[0],
                chart_options.get("title")[0],
            )
            (
                _index,
                _index_once,
                _xaxis,
                _yaxis,
                _legend,
                _title,
            ) = self.__custom(_series)
            self._option.get("legend").append(_legend)
            self._option.get("title").append(_title)

            if _xaxis and _yaxis is not None:
                for _x in _xaxis:
                    _x["gridIndex"] = _index - 1
                    self._option.get("xAxis").append(_x)
                for _y in _yaxis:
                    _y["gridIndex"] = _index - 1
                    self._option.get("yAxis").append(_y)

                # series id 是每个图实例的唯一标识
                _flag = self._option.get("series")[0].get("seriesId")
                _series_index = 0
                for s in self._option.get("series"):
                    if _flag == s.get("seriesId"):
                        s.update(
                            xAxisIndex=_series_index, yAxisIndex=_series_index
                        )
                    else:
                        _series_index += 1
                        s.update(
                            xAxisIndex=_series_index, yAxisIndex=_series_index
                        )
                    _flag = s.get("seriesId")

            _grid = grid(
                grid_width,
                grid_height,
                grid_top,
                grid_bottom,
                grid_left,
                grid_right,
            )
            for _ in range(_index_once):
                self._option.get("grid").append(_grid)
            self._js_dependencies = merge_js_dependencies(
                self._js_dependencies, chart.js_dependencies
            )
        return self

    def __custom(self, series):
        """

        :param series: series data
        """
        _series, _xaxis, _yaxis, _legend, _title = series
        for s in _series:
            self._option.get("series").append(s)
        return (
            len(self._option.get("series")),
            len(_series),
            _xaxis,
            _yaxis,
            _legend,
            _title,
        )
