[![Build Status](https://travis-ci.org/eronde/py_word_suggest.svg?branch=master)](https://travis-ci.org/eronde/py_word_suggest)
Py_word_suggest
==============
Py_word_suggest is a python library which returns suggested words of a given word. At this moment the suggested words are stored in a redis server.
# Installation
- Load data in redis server.
- Install package 
````
python3 -m  pip install -r dockerfile/requirements.txt
python3 setup.py install
````

# Example
````
python3 examples/commandline.py lookup --lang=en --word=I --ip=localhost

 'I' has the following suggested words:

['am', 'will', 'want', 'eat'] 

python3 examples/commandline.py lookup --lang=en --word=am --ip=localhost

 'am' has the following suggested words:
['the', 'Alice', 'Bob']   
````


Licence
=======
[MIT](https://github.com/eronde/py_word_suggest/blob/master/LICENSE)
