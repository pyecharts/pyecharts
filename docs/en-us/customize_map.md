> Map extensions

## How to get map extensions

Since 0.3.2, the map extensions become independent and optional python packages. No longer pyecharts carries any javascript libraries. Developer should cherry-pick the map extension of their need.

1. [Maps of All countries](https://echarts-maps.github.io/echarts-countries-js/): [echarts-countries-pypkg](https://github.com/pyecharts/echarts-countries-pypkg) (1.9MB): Map of world, 213 countries including China.
2. [Maps of Chinese provinces](https://echarts-maps.github.io/echarts-china-provinces-js/): [echarts-china-provinces-pypkg](https://github.com/pyecharts/echarts-china-provinces-pypkg) (730KB)：23 provinces, 5 autonomous regions
3. [Maps of Chinese cities](https://echarts-maps.github.io/echarts-china-cities-js/): [echarts-china-cities-pypkg](https://github.com/pyecharts/echarts-china-cities-pypkg) (3.8MB)：370 Chinese cities

The following pip commands will install the maps for you:

```
pip install echarts-countries-pypkg
pip install echarts-china-provinces-pypkg
pip install echarts-china-cities-pypkg
```

Please note China map exists in echarts-countries-pypkg.

## How to make a map extension

You will need to create two github projects: one is a npm project，providing javascript libraries；the other is a python project，package previous project as a python package.

### npm project

It must be a npm project on github, and has gh-pages enabled to host all javascript librraries. 
With gh-pages, your jupyter user cannot see the maps when they export ipynb as html.

Now, first, you need to get the following utilities:

```
pip install yehua
git clone https://github.com/echarts-maps/echarts-js-mobans.git
export YEHUA_FILE=/ABSOLUTE/PATH/TO/echarts-js-mobans/yehua.yml
```

Then you can create your own work folder and change into it. Take echarts-united-kingdom-js as an example:

```
$ yh
Yehua will walk you through creating a echarts-maps js package.
Press ^C to quit at any time.

project name: echarts-united-kingdom-js
description: UK maps for echarts
license: MIT
author: C.W.
All done!! project echarts-united-kingdom-js is created
```

All is done. Let's see what was the output:

```
pyecharts-host:tmp chfw$ cd echarts-united-kingdom-js/
pyecharts-host:echarts-united-kingdom-js chfw$ ls
echarts-united-kingdom-js	package.json			registry.json
```

Now, let's talk about the folder structure of an echarts js project:


```
+ echarts-united-kingdom-js
  + registry.json
  + package.json
  + echarts-united-kingdom-js
     + london.js
     + manchester.js
     + index.js
  + other files
```

In registry.json ，the following dictionary should be filled by yourself, in order to work with pyecharts in all situations:
```
{
    "JUPYTER_URL": "/nbextensions/echarts-united-kingdom-js",
    "GITHUB_URL": "https://your.github.io/echarts-united-kingdom-js/echarts-united-kingdoms-js",
    "JUPYTER_ENTRY": "echarts-united-kingdom-js/index",
    "JS_FOLDER": "echarts-united-kingdoms-js",
    "PINYIN_MAP": {
        "伦敦": "lundun",
        "曼彻斯特": "manqiesite"
    },
    "FILE_MAP": {
        "lundun": "london",
        "manqiesite": "manchester"
    }
}
```

index.js is made for jupyter notebook only:
```
define(["require", "exports"], function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var version = '1.0.0';
    function load_ipython_extension() {
        console.log("echarts-united-kingdom-js " + version + " has been loaded");
    }
    exports.load_ipython_extension = load_ipython_extension;
});

Now, you need to put javascript libraries under the sub-folder `echarts-united-kingdom-js` and please remember to update `PINYI_MAP` and `FILE_MAP`.

```

### python repository

Again, you will need the following utilities:

```
pip install yehua
git clone https://github.com/pyecharts/pypkg-mobans.git
export YEHUA_FILE=/ABSOLUTE/PATH/TO/pypkg-mobans/yehua.yml
```

Then create your work folder and change to it please. Take echarts-united-kingdom-pykg as an example:

```
$ yh
Yehua will walk you through creating a pyecharts pypkg package.
Press ^C to quit at any time.

project name: echarts-united-kingdom-pypkg
npm project name: echarts-united-kingdom-js
description: pyecharts map extension - united kingdom maps - python package
license: MIT
author: C.W.
contact email: wangc_2011@hotmail.com
github profile/organisation: chfw
copyright owner: C.W.
Cloning into 'mobans'...
remote: Counting objects: 214, done.
remote: Compressing objects: 100% (11/11), done.
remote: Total 214 (delta 8), reused 12 (delta 5), pack-reused 198
Receiving objects: 100% (214/214), 30.31 KiB | 17.00 KiB/s, done.
Resolving deltas: 100% (126/126), done.
Templating CUSTOM_README.rst.jj2 to README.rst
Templating custom_setup.py.jj2 to setup.py
Templating requirements.txt.jj2 to requirements.txt
Templating tests/custom_requirements.txt.jj2 to tests/requirements.txt
Templating docs/source/conf.py.jj2 to docs/source/conf.py
Templating test.script.jj2 to test.sh
Templating _version.py.jj2 to echarts_united_kingdom_pypkg/_version.py
Templating gitignore.jj2 to .gitignore
Templating travis.yml.jj2 to .travis.yml
Templated 9 files.
Initialized empty Git repository in /private/tmp/echarts-united-kingdom-pypkg/.git/
Please review changes before commit!
```

Now all files have been generated. Let's add previous project as a submodule:


```
pyecharts-host:tmp chfw$ cd echarts-united-kingdom-pypkg/
git submodule add https://github.com/your/npm/project your_project_name_pypkg/resources
git submodule init
```

Please add all files and then do:

```
git commit
```

Now it is ready for github.
