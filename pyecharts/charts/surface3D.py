# coding=utf-8

from pyecharts.chart import Chart3D


class Surface3D(Chart3D):
    """
    <<< 3D 曲面图 >>>
    """

    def __init__(self, *args, **kwargs):
        super(Surface3D, self).__init__(*args, **kwargs)
        self._3d_chart_type = "surface"


if __name__ == '__main__':

    import numpy as np

    def fm(x, y):
        return np.sin(x) + 0.25 * x + np.sqrt(y) + 0.05 * y ** 2


    # 用np.meshgrid构建数据点网格
    x = np.linspace(0, 10, 20)
    y = np.linspace(0, 10, 20)
    X, Y = np.meshgrid(x, y)
    Z = fm(X, Y)

    x = X.flatten()
    y = Y.flatten()
    z = Z.flatten()

    data = np.vstack((x, y, z)).T

    surface3D = Surface3D('3D fm 图片')
    surface3D.add('', data)

    surface3D.render()