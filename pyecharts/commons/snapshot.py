# coding=utf-8

import base64
import os

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common import exceptions


def snapshot(
    html_path: str, image_name: str, pixel_ratio: int = 2, is_remove_html: bool = False
):
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    capabilities = DesiredCapabilities.CHROME
    capabilities["loggingPrefs"] = {"browser": "ALL"}
    driver = webdriver.Chrome(options=option, desired_capabilities=capabilities)
    driver.set_script_timeout(4)

    if not html_path.startswith("http"):
        html_path = os.path.abspath(html_path)
    driver.get(html_path)

    ext = image_name.split(".")[1]

    try:
        driver.execute_async_script(__gen_js_code(ext, pixel_ratio))
    except exceptions.TimeoutException:
        pass

    try:
        output = driver.get_log("browser")[0]["message"]
        output = output.split(" ")[2].replace('"', "").split(",")[1]
        driver.close()
    except:
        raise

    with open(image_name, "wb") as f:
        f.write(base64.b64decode(output))

    if is_remove_html:
        os.remove(html_path)


def __gen_js_code(file_type: str, pixel_ratio: int) -> str:
    script = """
    fn = function(){
        var ele = document.querySelector('div[_echarts_instance_]');
        var mychart = echarts.getInstanceByDom(ele);
        return mychart.getDataURL(
            {type:'--file-type--', pixelRatio: --pixel-ratio--, excludeComponents: ['toolbox']});
    };
    window.setTimeout(function() {var content = fn(); console.log(content);}, 3000)
    """.replace(
        "--file-type--", file_type
    ).replace(
        "--pixel-ratio--", str(pixel_ratio)
    )
    return script
