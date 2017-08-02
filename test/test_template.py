from pyecharts.template import freeze_js


def test_freeze_js():
    html_content = """
        </style>
        <!-- build -->
        <script src="js/echarts.min.js"></script>
        <script src="js/echarts-wordcloud.min.js"></script>
        <!-- endbuild -->
    </head><body>"""

    html_content = freeze_js(html_content)
    assert 'exports.echarts' in html_content
    assert 'echarts-wordcloud' in html_content
