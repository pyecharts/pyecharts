#coding=utf-8
from __future__ import unicode_literals

from nose.tools import eq_
from pyecharts.template import freeze_js
from pyecharts.template import write_utf8_html_file
import codecs


def test_freeze_js():
    html_content = """
        </style>
        <!-- build -->
        <script src="js/echarts.3.6.2.min.js"></script>
        <script src="js/echarts-wordcloud.min.js"></script>
        <!-- endbuild -->
    </head><body>"""

    html_content = freeze_js(html_content)
    assert 'exports.echarts' in html_content
    assert 'echarts-wordcloud' in html_content


def test_write_utf8_html_file():
    content = "柱状图数据堆叠示例"
    file_name = 'test.html'
    write_utf8_html_file(file_name, content)
    with codecs.open(file_name, 'r', 'utf-8') as f:
        actual_content = f.read()
        eq_(content, actual_content)
