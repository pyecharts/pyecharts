#!/usr/bin/env python
#coding=utf-8

from pyecharts.base import Base

class Parallel(Base):
    """
    <<< Parallel chart >>>
    Parallel Coordinates is a common way of visualizing high-dimensional geometry and analyzing multivariate data.
    """
    def __init__(self, title="", subtitle="", **kwargs):
        super(Parallel, self).__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def config(self, schema=None, c_schema=None):
        """

        :param schema:
            Dimension index of coordinate axis.
            a axis name list, like ['apple', 'orange', 'watermelon']
        :param c_schema:
            User customize coordinate axis for parallel coordinate.
            dim: Dimension index of coordinate axis.
            name: Name of axis.
            type: Type of axis
                value: Numerical axis, suitable for continuous data.
                category: Category axis, suitable for discrete category data.
                          Data should only be set via data for this type.
            min: The minimun value of axis.
            max: The maximum value of axis.
            inverse: Whether axis is inversed.
            nameLocation: Location of axis name. it can be 'start', 'middle', 'end'.
        :return:
        """
        if schema:
            _schema = [{"dim": i, "name": v} for i, v in enumerate(schema)]
            self._option.update(parallelAxis=_schema)
        if c_schema:
            self._option.update(parallelAxis=c_schema)

    def __add(self, name, data, **kwargs):
        """

        :param name:
            Series name used for displaying in tooltip and filtering with legend,
            or updaing data and configuration with setOption.
        :param data:
            data array of series, it is represented by a two-dimension array -> [[],[]]
        :param kwargs:
        :return:
        """
        self._option.update(parallel={"left": "5%", "right": "13%", "bottom": "10%", "top": "20%"})
        self._option.get('legend')[0].get('data').append(name)
        self._option.get('series').append({
            "type": "parallel",
            "coordinateSystem": "parallel",
            "name": name,
            "data": data,
        })
        self._legend_visualmap_colorlst(**kwargs)
