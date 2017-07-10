from pyecharts import Polar

def test_polar():
    import math
    data = []
    for i in range(101):
        theta = i / 100 * 360
        r = 5 * (1 + math.sin(theta / 180 * math.pi))
        data.append([r, theta])
    hour = [i for i in range(1, 25)]
    polar = Polar(width=1200, height=600)
    polar.add("For my honey", data, angle_data=hour, boundary_gap=False)
    polar.show_config()
    polar.render()
