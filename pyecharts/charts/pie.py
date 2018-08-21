# coding=utf-8

from pyecharts.chart import Chart


class Pie(Chart):
    """
    <<< 饼图 >>>

    饼图主要用于表现不同类目的数据在总和中的占比。每个的弧度表示数据数量的比例。
    """

    def __init__(self, title="", subtitle="", **kwargs):
        super(Pie, self).__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)
        return self

    def __add(
        self,
        name,
        attr,
        value,
        radius=None,
        center=None,
        rosetype=None,
        **kwargs
    ):
        """

        :param name:
            系列名称，用于 tooltip 的显示，legend 的图例筛选。
        :param attr:
            属性名称。
        :param value:
            属性所对应的值。
        :param radius:
            饼图的半径，数组的第一项是内半径，第二项是外半径，默认为 [0, 75]
            默认设置成百分比，相对于容器高宽中较小的一项的一半。
        :param center:
            饼图的中心（圆心）坐标，数组的第一项是横坐标，第二项是纵坐标，默认为 [50, 50]
            默认设置成百分比，设置成百分比时第一项是相对于容器宽度，第二项是相对于容器高度。
        :param rosetype:
           是否展示成南丁格尔图，通过半径区分数据大小，有'radius'和'area'两种模式。
           默认为'radius'
                radius：扇区圆心角展现数据的百分比，半径展现数据的大小。
                area：所有扇区圆心角相同，仅通过半径展现数据大小。
        :param kwargs:
        """
        kwargs.update(type="pie")
        chart = self._get_all_options(**kwargs)
        assert len(attr) == len(value)
        _data = []
        for data in zip(attr, value):
            _name, _value = data
            _data.append({"name": _name, "value": _value})

        _rmin, _rmax = "0%", "75%"
        if radius:
            if len(radius) == 2:
                _rmin, _rmax = ["{}%".format(r) for r in radius]

        _cmin, _cmax = "50%", "50%"
        if center:
            if len(center) == 2:
                _cmin, _cmax = ["{}%".format(c) for c in center]

        if rosetype:
            if rosetype not in ("radius", "area"):
                rosetype = "radius"

        for a in attr:
            self._option.get("legend")[0].get("data").append(a)

        _dlst = self._option.get("legend")[0].get("data")
        _dset = list(set(_dlst))
        _dset.sort(key=_dlst.index)
        self._option.get("legend")[0].update(data=list(_dset))

        self._option.get("series").append(
            {
                "type": "pie",
                "name": name,
                "data": _data,
                "radius": [_rmin, _rmax],
                "center": [_cmin, _cmax],
                "roseType": rosetype,
                "label": chart["label"],
                "seriesId": self._option.get("series_id"),
            }
        )
        self._config_components(**kwargs)
