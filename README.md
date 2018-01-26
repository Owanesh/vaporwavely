![Vaporwavely](https://raw.githubusercontent.com/Owanesh/vaporwavely/master/vaporwavely/logo.png)
---
[![forthebadge](http://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)


Convert your text in an aesthetical text, or generate nostalgic 1999 paragraphs with vaporipsum


## How to use 👾


- `vaporipsum` : Generate a random text, like [Lorem Ipsum](https://www.lipsum.com/), but more nostalgic and aesthetic

    ```
    from vaporwavely import vaporipsum

    mytext = vaporipsum(4) # it generates 4 paragraphs of random text
    print(mytext)
    ```


- `vaporize` : Convert your text from this **Hello World** to this **Ｈｅｌｌｏ Ｗｏｒｌｄ**

    ```
    from vaporwavely import vaporize

    mystring = "Hi Owanesh"
    mytext = vaporize(mystring)
    print(mytext) # Ｈｉ Ｏｗａｎｅｓｈ
    ```
### Use combo for an ａｅｓｔｈｅｔｉｃ results 🦄

- **Vaporize your vaporipsum**

    ```
    from vaporwavely import vaporize, vaporipsum

    print(vaporize(vaporipsum(4)))
    ```
- **Do it upper**
    ```
    from vaporwavely import vaporize

    print(vaporize('get me upper and vaporized').upper())
    ```
    ＧＥＴ ＭＥ ＵＰＰＥＲ ＡＮＤ ＶＡＰＯＲＩＺＥＤ

### Contribute 🎖
*Ｒｅａｌｌｙ ｍａｎ?*

First of all thanks if you want help me. Below there are requirements and steps for testing

    pip install tests/requirements.txt
    nosetests --with-coverage --cover-package=vaporwavely


---
#### Credits 🙏
Thanks to [TristanAG](https://github.com/TristanAG/vaporipsum) for Vaporipsum idea

