from pyecharts.charts import WordCloud

wc = WordCloud()
wc.add("wc", [("a", 20), ("b", 30)])
wc.render()
