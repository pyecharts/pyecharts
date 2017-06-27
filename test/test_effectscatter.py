from echarts import EffectScatter

def test_effectscatter():
    v1 = [10, 20, 30, 40, 50, 60]
    v2 = [10, 20, 30, 40, 50, 60]
    v3 = [25, 20, 15, 10, 5]
    v4 = [25, 20, 15, 10, 5]

    effectscatter = EffectScatter()
    effectscatter.add("a", v3, v4, symbol_size=20, effect_scale=6, effect_period=10, symbol="pin")
    # effectscatter.add("a", v1, v2, symbol_size=20)
    # effectscatter.add("b", v1[::-1], v2, symbol_size=20)
    effectscatter.add("b", v3[::-1], v4, symbol_size=20, effect_scale=6, effect_period=5, symbol="pin")
    effectscatter.show_config()
    effectscatter.render()