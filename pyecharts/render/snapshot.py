# coding=utf-8
import base64
import time
import sys
import os

from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def make_snapshot(
    html_path: str,
    image_name: str,
    pixel_ratio: int = 2,
    delay: int = 2,
    is_remove_html: bool = True,
    browser='Chrome'
):
    if delay < 0:
        raise Exception('Time travel is not possible')
    if browser == 'Chrome':
        driver = get_chrome()
    elif browser == 'Safari':
        driver = get_safari()
    else:
        raise Exception('Unknown browser!')
    driver.set_script_timeout(delay + 1)

    if not html_path.startswith("http"):
        html_path = 'file://' + os.path.abspath(html_path)
    driver.get(html_path)
    time.sleep(delay)

    ext = image_name.split(".")[1]

    try:
        output = driver.execute_script(__gen_js_code(ext, pixel_ratio, delay))
    except exceptions.TimeoutException:
        pass

    try:
        output = output.split(",")[1]
    except:
        raise

    with open(image_name, "wb") as f:
        f.write(base64.b64decode(output))

    if is_remove_html and not html_path.startswith("http"):
        os.remove(html_path[7:])
    driver.close()
    print("render {}".format(image_name))


def __gen_js_code(file_type: str, pixel_ratio: int, delay: int) -> str:
    script = (
        """
        var ele = document.querySelector('div[_echarts_instance_]');
        var mychart = echarts.getInstanceByDom(ele);
        return mychart.getDataURL(
            {type:'--file-type--', pixelRatio: --pixel-ratio--, excludeComponents: ['toolbox']});
    """.replace(
            "--file-type--", file_type
        )
        .replace("--pixel-ratio--", str(pixel_ratio))
    )
    return script


def get_chrome():
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    if sys.platform == 'darwin':
        option.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    capabilities = DesiredCapabilities.CHROME
    capabilities["loggingPrefs"] = {"browser": "ALL"}
    return webdriver.Chrome(
        options=option,
        desired_capabilities=capabilities)


def get_safari():
    return webdriver.Safari(executable_path='/usr/bin/safaridriver')
