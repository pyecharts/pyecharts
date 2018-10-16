# coding=utf8
"""Unit Test Cases
"""

from nose.tools import eq_

from pyecharts import Bar
from pyecharts.app import CURRENT_CONFIG, use_config, online, enable_nteract
from test.constants import CLOTHES
from test.utils import get_default_rendering_file_content

TITLE = "柱状图数据堆叠示例"


def test_use_config():
    c1 = CURRENT_CONFIG.jshost
    with use_config():
        online()
    c2 = CURRENT_CONFIG.jshost
    eq_(c1, c2)

    j1 = CURRENT_CONFIG.is_run_on_nteract
    with use_config():
        enable_nteract()
        eq_(True, CURRENT_CONFIG.is_run_on_nteract)

    j2 = CURRENT_CONFIG.is_run_on_nteract

    eq_(j1, j2)


def create_a_bar(title):
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    bar = Bar(title)
    bar.add("商家A", CLOTHES, v1, is_stack=True)
    bar.add("商家B", CLOTHES, v2, is_stack=True)
    return bar

def test_online_html():
    with use_config():
        online()
        bar = Bar()
        bar.add("", CLOTHES, [5, 20, 36, 10, 75, 90], is_stack=True)
        bar.render()
        html_content = get_default_rendering_file_content()
        assert (
            'src="https://pyecharts.github.io/assets/js/echarts.min.js'
            in html_content
        )
        # CURRENT_CONFIG.jshost = None
        # CURRENT_CONFIG.hosted_on_github = False


def test_online_feature():
    with use_config():
        online()
        bar = create_a_bar(TITLE)
        html = bar._repr_html_()
        # print(CURRENT_CONFIG.jshost)
        expected_jshost = "https://pyecharts.github.io/jupyter-echarts/echarts"
        assert expected_jshost in html
        # CURRENT_CONFIG.hosted_on_github = False


def test_online_with_custom_jshost():
    with use_config():
        online(host="https://my-site.com/js")
        assert CURRENT_CONFIG.jshost == 'https://my-site.com/js'
        bar = create_a_bar(TITLE)
        html = bar._repr_html_()
        expected_jshost = "https://my-site.com/js"
        assert expected_jshost in html
        # CURRENT_CONFIG.jshost = None


def test_nteract_feature():
    with use_config():
        enable_nteract()
        print(CURRENT_CONFIG.jupyter_presentation)
        print(CURRENT_CONFIG.is_run_on_nteract)
        bar = create_a_bar(TITLE)
        html = bar._repr_html_()
        assert "https://pyecharts.github.io/assets/js/echarts.min.js" in html
        assert "require" not in html
        # restore configuration
        # configure(output_image=constants.DEFAULT_HTML)
        # CURRENT_CONFIG.jshost = None
        # CURRENT_CONFIG.hosted_on_github = False
