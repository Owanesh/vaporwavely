<p align="center">
    <img src="https://raw.githubusercontent.com/Owanesh/vaporwavely/master/logo.png" alt="Vaporwavely Logo" />
    <br>
    <a href="https://codecov.io/gh/Owanesh/vaporwavely">
      <img src="https://codecov.io/gh/Owanesh/vaporwavely/branch/master/graph/badge.svg" />
    </a>
    <a href="https://github.com/Owanesh/vaporwavely/blob/master/LICENSE">
      <img src="https://img.shields.io/badge/License-MIT-blue.svg" />
    </a>
    <a class="badge-align" href="https://www.codacy.com/app/Owanesh/vaporwavely?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Owanesh/vaporwavely&amp;utm_campaign=Badge_Grade">
        <img src="https://api.codacy.com/project/badge/Grade/54e13d686273408a9e44bb54bb438fdd"/>
    </a>
    <a href="https://travis-ci.org/Owanesh/vaporwavely">
      <img src="https://travis-ci.org/Owanesh/vaporwavely.svg?branch=master" />
    </a>
    <a href="https://badge.fury.io/py/vaporwavely">
        <img src="https://badge.fury.io/py/vaporwavely.svg" alt="PyPI version" height="18">
    </a>
    <br>
    <a href="http://forthebadge.com">
      <img src="http://forthebadge.com/images/badges/made-with-python.svg" />
    </a>
</p>

Convert your text in an aesthetical text, or generate nostalgic 1999 paragraphs with vaporipsum


## How to use 👾

### Installation
```sh
pip install vaporwavely
```
### Usage
- `vaporipsum` : Generate a random text, like [Lorem Ipsum](https://www.lipsum.com/), but more nostalgic and aesthetic

    ```py
    from vaporwavely import vaporipsum

    vaporipsum(4) # it generates 4 paragraphs of random text
    ```


- `vaporize` : Convert your text from this **Hello World** to this **Ｈｅｌｌｏ Ｗｏｒｌｄ**

    ```py
    from vaporwavely import vaporize

    mystring = "Hi Owanesh"
    vaporize(mystring) # Ｈｉ Ｏｗａｎｅｓｈ
    ```

### Use combo for an ａｅｓｔｈｅｔｉｃ results 🦄

- **Vaporize your vaporipsum**

    ```py
    from vaporwavely import vaporize, vaporipsum

    vaporize(vaporipsum(4))
    ```
- **Do it upper**
    ```py
    from vaporwavely import vaporize

    vaporize('get me upper and vaporized').upper()
    ```
    ＧＥＴ ＭＥ ＵＰＰＥＲ ＡＮＤ ＶＡＰＯＲＩＺＥＤ

### Contribute 🎖
*Ｒｅａｌｌｙ ｍａｎ?*

First of all thanks if you want help me. Below there are requirements and steps for testing

    pip install -r requirements-dev.txt
    py.test --cov=vaporwavely tests


---
#### Credits 🙏
Thanks to [TristanAG](https://github.com/TristanAG/vaporipsum) for Vaporipsum idea

