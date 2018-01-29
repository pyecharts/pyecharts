# Developer's Guide

## Pull request instructions

`dev` branch is for the development of each new releases. `master` branch is reserved for released code only. What it means for contributors is:
please checkout `dev` branch right after you have a clone of pyecharts. Then start your engineering effort. When you are ready, please submit a PR
against `dev` branch too.

If your PR has code changes, please include unit tests. If possible, please attach a screenshot on your contribution. It helps everyone to see your contribution.

## Generate uml diagram

It uses plantuml and please get it from [its website](http://plantuml.com).

```
jar -jar plantuml.jar class-relationship-diagram.uml.
```

## How to add more javascript libraries to pyecharts

All javascript libraries are now managed in a [submodule](https://git-scm.com/docs/git-submodule) [jupyter-echarts](https://github.com/chfw/jupyter-echarts). It means
new javascript library shall go through `jupyter-echarts`.

jupyter-echarts is a front-end project. If you are new to front-end engineering, please find the crash course for you in the end.

### Step 1: add the library to jupyter-echarts

Checkout the repository:

```
git clone https://github.com/chfw/jupyter-echarts.git
```

And then do

```
npm install --save your_javascript_library
```

Edit gulp.js

```
...
FILES = [
    './node_modules/echarts/dist/echarts.min.js',
    './node_modules/echarts/map/js/china.js',
    './node_modules/your_library/dist/min_version.js' <---
...
FILE_MAP = [
...
    'nick_name': 'min_version' // note, please do not put .js suffix
...
]
PROVINCE_PINYIN_MAP = [
...
    'chinese location name': 'nick_name', // note nick_name is the same as previous one
...
]
```

Then run

```
$ gulp
```

The most important thing is to do git commit. You will need to commit it
to jupyter-echarts. If you do not have write access, please submit a PR.

If your contribution become large, please reference: echarts-countries-js or
echarts-china-cities-js.

### Step 2: update pyecharts

Once your previous commit is accepted in jupyter-notebooks, you could then
checkout pyecharts::

```
$ git clone --recursive https://github.com/chenjiandongx/pyecharts.git
$ cd pyecharts/pyecharts/templates/js
$ git pull
remote: Counting objects: 7, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 7 (delta 4), reused 7 (delta 4), pack-reused 0
Unpacking objects: 100% (7/7), done.
From https://github.com/chfw/jupyter-echarts
   af7184b..bb87949  master     -> origin/master
Updating af7184b..bb87949
Fast-forward
 echarts/main.js | 2 +-
 gulpfile.js     | 2 +-
 src/main.ts     | 2 +-
 3 files changed, 3 insertions(+), 3 deletions(-)
$ cd ../../../
$ git commit -am "pull latest changes from jupyter-echarts
```

And then push your changes to pyecharts.


## Front end engineering for Pythonistas

In front end engineering field, no one manually downloads a javascript/css file
and type the script tag into html file. To an extreme, no one writes html, css
nor javascript though they are writing web pages. All of those work are either
automated and transcompiled.

[npm](https://docs.npmjs.com/getting-started/what-is-npm) is a node.js package manager and helps front end engineers to automate
the delivery of all javascript and css modules. In this category, there are
other similiar tools: [bower](https://bower.io), [jspm](https://jspm.io) etc. [gulp](https://gulpjs.com) is the `make` command in node.js 
world and gulpfile.js is the `Makefile` for gulp. You will write all commands 
in javascript. These tools helps the developer automate the delivery of 
javascript and css files as you would use pip for python packages.

So what do they write if no html, css nor javascript are written? They write
[pug file](https://pugjs.org/api/getting-started.html)/[HAML file](http://haml.info), [sass file](http://sass-lang.com) and [coffeescript](http://coffeescript.org)/[typescript](http://www.typescriptlang.org) files. Those files
are then trans-compiled into what you see as html, css and javascript. Nowadays,
writing a few webpage has become a software engineering acitvity. Object
oriented programming, code reuse, css attribute inheritance are the things
in front end engineer's head on daily basis.

Above is a quick introduction to front end engineering. There are many excellent
projects, tools and developers in node.js universe, waiting for you to find and
meet.
