> Frequently asked questions and its solutions

**jupyter-notebook export problem**

Since 0.1.9.7, pyecharts has gone into offline mode, drawing without internet connection. Now, the charts in exported note book cannot be display as they have been put outside
jupyter environment.

So the solution is to add the following statement:

```python
...
from pyecharts import online

online()
...
```
Above code will take javascripts from github.
you cannot connect to github, you could clone https://github.com/pyecharts/assets. Then, you put `js` folder onto your own server. Here is a simple command to achieve it:

```
$ git clone https://github.com/pyecharts/assets
$ cd js
$ python -m http.server # for python 2, use python -m SimpleHTTPServer
Serving HTTP on 0.0.0.0 port 8000 ...
```

Then, add localhost into previous python code:

```python
...
from pyecharts import online

online(host="http://localhost:8000)
...
```

**Python2 Coding Problem**

default code type is UTF-8, there's no problem in Python3, because Python3 have a good support in chinese. But in Python2, please use the following sentence to ensure avoiding wrong coding problem:
```
#!/usr/bin/python
#coding=utf-8
from __future__ import unicode_literals
```
The first two sentences are telling your editor that it should use UTF-8 ([PEP-0263](https://www.python.org/dev/peps/pep-0263/)). And the last sentence is telling Python all the characters are UTF-8 ([unicode literals](http://python-future.org/unicode_literals.html))
