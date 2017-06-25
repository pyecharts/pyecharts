from echarts import EffectScatter

def test_effectscatter():
    v1 = [25, 20, 15, 10, 5]
    v2 = [25, 20, 15, 10, 5]

    effectscatter = EffectScatter()
    effectscatter.add("a", v1, v2, symbol_size=20, effect_scale=6, effect_period=10, symbol="pin")
    effectscatter.add("b", v1[::-1], v2, symbol_size=20, effect_scale=6, effect_period=5, symbol="pin")
    effectscatter.show_config()
    effectscatter.render()