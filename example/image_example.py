from pyecharts.components import Image
from pyecharts.options import ComponentTitleOpts


def image_base() -> Image:
    image = Image()

    img_src = (
        "https://user-images.githubusercontent.com/19553554/396123"
        "58-499eb2ae-4f91-11e8-8f56-179c4f0bf2df.png"
    )
    image.add(
        src=img_src,
        style_opts={"width": "200px", "height": "200px", "style": "margin-top: 20px"},
    ).set_global_opts(
        title_opts=ComponentTitleOpts(title="Image-基本示例", subtitle="我是副标题支持换行哦")
    )
    return image
