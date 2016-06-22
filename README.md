[![Build Status](https://travis-ci.org/eronde/py_word_suggest.svg?branch=master)](https://travis-ci.org/eronde/py_word_suggest)
Py_word_suggest
==============
Py_word_suggest is a  python library which returns suggested word of a given word. At this moment tThe suggested words are stored in a redis server.
# Example
````
 python3 examples/commandline.py lookup --lang=en --word=I

 'I' has the following suggested words:
['the', 'Alice', 'Bob']   
````


Licence
=======
[MIT](https://github.com/eronde/py_word_suggest/blob/master/LICENSE)
