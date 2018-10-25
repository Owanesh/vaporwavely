.. image:: https://raw.githubusercontent.com/Owanesh/vaporwavely/master/logo.png
.. image:: https://travis-ci.org/Owanesh/vaporwavely.svg?branch=master
    :target: https://travis-ci.org/Owanesh/vaporwavely  
.. image:: https://codecov.io/gh/Owanesh/vaporwavely/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/Owanesh/vaporwavely
.. image:: https://badge.fury.io/py/vaporwavely.svg
    :target: https://badge.fury.io/py/vaporwavely

Convert your text in an aesthetical text, or generate nostalgic 1999
paragraphs with vaporipsum

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
How to use 👾
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


-  ``vaporipsum`` : Generate a random text, like `Lorem
   Ipsum <https://www.lipsum.com/>`__, but more nostalgic and aesthetic

   .. code:: py

       from vaporwavely import vaporipsum

       vaporipsum(4) # it generates 4 paragraphs of random text

-  ``vaporize`` : Convert your text from this **Hello World** to this
   **Ｈｅｌｌｏ Ｗｏｒｌｄ**

   .. code:: py

       from vaporwavely import vaporize

       mystring = "Hi Owanesh"
       vaporize(mystring) # Ｈｉ Ｏｗａｎｅｓｈ


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Use combo for an ａｅｓｔｈｅｔｉｃ results 🦄
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **Vaporize your vaporipsum**

   .. code:: py

       from vaporwavely import vaporize, vaporipsum

       vaporize(vaporipsum(4))

-  **Do it upper** \`\`\`py from vaporwavely import vaporize

   vaporize('get me upper and vaporized').upper() \`\`\` ＧＥＴ ＭＥ
   ＵＰＰＥＲ ＡＮＤ ＶＡＰＯＲＩＺＥＤ

~~~~~~~~~~~~~~~~~~~~~~~~
Contribute 🎖
~~~~~~~~~~~~~~~~~~~~~~~~

*Ｒｅａｌｌｙ ｍａｎ?*

First of all thanks if you want help me. Below there are requirements
and steps for testing

::

    pip install -r requirements-dev.txt
    py.test --cov=vaporwavely tests

--------------

^^^^^^^^^^^^^^^^^^
Credits 🙏
^^^^^^^^^^^^^^^^^^

Thanks to `TristanAG <https://github.com/TristanAG/vaporipsum>`__ for
Vaporipsum idea
