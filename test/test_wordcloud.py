from echarts import WordCloud

def test_wordcloud():
    name = ['Sam S Club', 'Macys', 'Amy Schumer', 'Jurassic World', 'Charter Communications',
            'Chick Fil A', 'Planet Fitness', 'Pitch Perfect', 'Express', 'Home', 'Johnny Depp',
            'Lena Dunham', 'Lewis Hamilton', 'KXAN', 'Mary Ellen Mark', 'Farrah Abraham',
            'Rita Ora', 'Serena Williams', 'NCAA baseball tournament', 'Point Break']
    value = [10000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112, 965, 847, 582, 555,
             550, 462, 366, 360, 282, 273, 265]

    wordcloud = WordCloud(width=1200, height=600)
    wordcloud.add("", name, value, word_size_range=[20, 100])
    wordcloud.show_config()
    wordcloud.render()
