import os
import random


class _Faker:
    clothes = ["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"]
    drinks = ["可乐", "雪碧", "橙汁", "绿茶", "奶茶", "百威", "青岛"]
    phones = ["小米", "三星", "华为", "苹果", "魅族", "VIVO", "OPPO"]
    fruits = ["草莓", "芒果", "葡萄", "雪梨", "西瓜", "柠檬", "车厘子"]
    animal = ["河马", "蟒蛇", "老虎", "大象", "兔子", "熊猫", "狮子"]
    cars = ["宝马", "法拉利", "奔驰", "奥迪", "大众", "丰田", "特斯拉"]
    dogs = ["哈士奇", "萨摩耶", "泰迪", "金毛", "牧羊犬", "吉娃娃", "柯基"]
    week = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    week_en = "Saturday Friday Thursday Wednesday Tuesday Monday Sunday".split()
    clock = (
        "12a 1a 2a 3a 4a 5a 6a 7a 8a 9a 10a 11a 12p "
        "1p 2p 3p 4p 5p 6p 7p 8p 9p 10p 11p".split()
    )
    visual_color = [
        "#313695",
        "#4575b4",
        "#74add1",
        "#abd9e9",
        "#e0f3f8",
        "#ffffbf",
        "#fee090",
        "#fdae61",
        "#f46d43",
        "#d73027",
        "#a50026",
    ]
    months = ["{}月".format(i) for i in range(1, 13)]
    provinces = ["广东省", "北京市", "上海市", "江西省", "湖南省", "浙江省", "江苏省"]
    guangdong_city = ["汕头市", "汕尾市", "揭阳市", "阳江市", "肇庆市", "广州市", "惠州市"]
    country = [
        "China",
        "Canada",
        "Brazil",
        "Russia",
        "United States",
        "Africa",
        "Germany",
    ]
    days_attrs = ["{}天".format(i) for i in range(30)]
    days_values = [random.randint(1, 30) for _ in range(30)]

    def choose(self) -> list:
        return random.choice(
            [
                self.clothes,
                self.drinks,
                self.phones,
                self.fruits,
                self.animal,
                self.dogs,
                self.week,
            ]
        )

    @staticmethod
    def values(start: int = 20, end: int = 150) -> list:
        return [random.randint(start, end) for _ in range(7)]

    @staticmethod
    def rand_color() -> str:
        return random.choice(
            [
                "#c23531",
                "#2f4554",
                "#61a0a8",
                "#d48265",
                "#749f83",
                "#ca8622",
                "#bda29a",
                "#6e7074",
                "#546570",
                "#c4ccd3",
                "#f05b72",
                "#444693",
                "#726930",
                "#b2d235",
                "#6d8346",
                "#ac6767",
                "#1d953f",
                "#6950a1",
            ]
        )

    @staticmethod
    def img_path(path: str, prefix: str = "images") -> str:
        return os.path.join(prefix, path)


Faker = _Faker()


class Collector:
    charts = []

    @staticmethod
    def funcs(fn):
        Collector.charts.append((fn, fn.__name__))
