# First-steps
### Make sure you have installed the latest version pyecharts
Now, you are ready to make your first chart!
```python
from pyecharts import Bar

bar = Bar("我的第一个图表", "这里是副标题")
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
bar.show_config()
bar.render()
```

![guide-0](https://user-images.githubusercontent.com/19553554/35103909-3ee41ba2-fca2-11e7-87be-1a3585b9e0fa.png)

**Tip：** You can click the download button on the right side to download the picture to your local disk.

* ```add()```
    main method，add the data and set up various options of the chart
* ```show_config()```
    print and output all options of the chart
* ```render()```
    creat a file named render.html in the root directory defaultly,which supports path parameter and set the location the file save in,for instance render(r"e:\my_first_chart.html")，open file with your browser.

**Note：** Click the image download button on the right hand side of the chart. If you need more buttons, please insert `is_more_utils=True` when calling add()

```python
from pyecharts import Bar

bar = Bar("我的第一个图表", "这里是副标题")
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90],
        is_more_utils=True)
bar.render()
```
![guide-1](https://user-images.githubusercontent.com/19553554/35104150-f31e1b7c-fca2-11e7-81cf-a12bf1629e02.png)


### Rendering as image using pyecharts-snapshot

If you would to get png, pdf, gif files instead of `render.html`, you can use [pyecharts-snapshot](https://github.com/chfw/pyecharts-snapshot)。However, node.js is required and can be downloaded from [https://nodejs.org/en/download/](https://nodejs.org/en/download/)

1. Install phantomjs  
    `npm install -g phantomjs-prebuilt`
2. install pyecharts-snapshot  
    `pip install pyecharts-snapshot`
3. In your program, import pyecharts-snapshot  
    `from pyecharts_snapshot.main import make_a_snapshot`
4. Programmatical usage
    `make_a_snapshot('render.html', 'snapshot.png')`  
    where the frist parameter is the output file(by default, render.html), and the second one is output file with file extension as png or pdf.

For more details, please refer to [pyecharts-snapshot](https://github.com/chfw/pyecharts-snapshot)  

```

### Chart rendering process

almost all the chart type drawed like this:
1. ```chart_name = Type()``` Initialise the concrete chart type.
2. ```add()``` Add data and options.
3. ```render()``` Creat .html file.

​```add()``` Data is two lists commonly(the same length),if your data is dictionary or dictionary with tuple,use ```cast()``` to convert.

​```python
@staticmethod
cast(seq)
​``` Convert the sequence with the dictionary and tuple type into k_lst, v_lst. ```
```
1. Tuple Lists
    [(A1, B1), (A2, B2), (A3, B3), (A4, B4)] --> k_lst[ A[i1, i2...] ], v_lst[ B[i1, i2...] ]
2. Dictionary Lists
    [{A1: B1}, {A2: B2}, {A3: B3}, {A4: B4}] --> k_lst[ A[i1, i2...] ], v_lst[ B[i1, i2...] ]
3. Dictionaries
    {A1: B1, A2: B2, A3: B3, A4: B4} -- > k_lst[ A[i1, i2...] ], v_lst[ B[i1, i2...] ]

### Render Charts Many Times

> Update on v0.4.0

You can call `chart.render`  many times to show some charts in a script.

```python
from pyecharts import Bar, Line

bar = Bar("我的第一个图表", "这里是副标题")
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
bar.render(path='bar.html')

line = Line("我的第一个图表", "这里是副标题")
line.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
line.render(path='line.html')
```

In v0.4.0+, pyecharts refactors the internal logic and make render faster.The following code is recommended.

```python
from pyecharts import Bar, Line
from pyecharts.engine import create_default_environment

bar = Bar("我的第一个图表", "这里是副标题")
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])

line = Line("我的第一个图表", "这里是副标题")
line.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])

env = create_default_environment()

env.render_chart_to_file(bar, path='bar.html')
env.render_chart_to_file(line, path='line.html')
```

This example use the only one engine object to render multiple charts.

### Pandas & Numpy examples

In the context of Numpy and/or Pandas, ```pdcast(pddata)``` and ``` npcast(npdata)``` methods, provided in 0.19.2 are no log required. Please see the advanced example in README.

![pandas-numpy](https://user-images.githubusercontent.com/19553554/35104252-3e36cee2-fca3-11e7-8e43-09bbe8dbbd1e.png)

If your DataFrame returns a transposed list(such as, [ [1], [2], [3] ]), you have to tranpose it by yourself (make it like [ 1, 2, 3 ] ). This transpose operation applies to Radar, Parallel, HeatMap.

Series type
```python
from pyecharts import Bar
import pandas as pd

pddata = pd.Series([1, 2, 3, 4], index=[1, 'b', 'c', 'd'])
vlst, ilst = Bar.pdcast(pddata)

print(vlst)
>>> [1.0, 2.0, 3.0, 4.0] 
print(ilst)
>>> ['1', 'b', 'c', 'd']
```

DataFrame type
```python
from pyecharts import Bar
import pandas as pd

pddt = pd.DataFrame([[1, 2, 3, 4], [2, 3, 4, 5], [4.1, 5.2, 6.3, 7.4]], index=["A", "B", "C"])
vlst, ilst = Bar.pdcast(pddata)

print(vlst)
>>> [[1.0, 2.0, 3.0, 4.0], [2.0, 3.0, 4.0, 5.0], [4.1, 5.2, 6.3, 7.4]]
print(ilst)
>>> ['A', 'B', 'C']
```

npcast()，It accepts numpy.array type.
```python
@staticmethod
npcast(npdata)
​``` handle the ndarray type in Numpy, return a list that ensures the correct type. Returns the nested list if there are multiple dimensions.```
```

Numpy.array type
```python
from pyecharts import Bar
import numpy ad np

npdata = np.array([[1, 2, 3, 4], [2, 4, 5.0, 6.3]])
print(npdata)
>>> [[1.0, 2.0, 3.0, 4.0], [2.0, 4.0, 5.0, 6.3]]
```

**Of course you can use the cooler way,use Jupyter Notebook to show the chart.But what matplotlib have，so do pyecharts**

like this

![notebook-0](https://user-images.githubusercontent.com/19553554/35104153-f6256212-fca2-11e7-854c-bacc61eabf6f.gif)

and this

![notebook-1](https://user-images.githubusercontent.com/19553554/35104157-fa39e170-fca2-11e7-9738-1547e22914a6.gif)

more Jupyter notebook examples, please refer to [notebook-use-cases](https://github.com/chenjiandongx/pyecharts/blob/master/document/notebook-use-cases.ipynb)。you could download and run it on your notebook.

**Tip：** The function was official added in 0.1.9.2 version,please update the newest version to use it.


### Offline installation instructions for pyecharts 0.3.2 +

Please download these three packages from pypi: pyecharts, pyecharts-jupyter-installer, 和 jupyter-echarts-pypkg. 

Then install them sequentially as:

```
pip install pyecharts-jupyter-installer.tar.gz
pip install jupyter-echarts-pypkg.tar.gz
pip install pyecharts.tar.gz
```
