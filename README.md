[![Build Status](https://travis-ci.org/eronde/py_word_suggest.svg?branch=master)](https://travis-ci.org/eronde/py_word_suggest)
Py_word_suggest
==============
Py_word_suggest is a python library which returns suggested words of a given word. Data-structure stored in redis or json
# Installation
- Load data in redis server.
- Install package 
````
python3 -m  pip install -r dockerfile/requirements.txt
python3 setup.py install
````

# Example
Redis:
````
python3 examples/commandline.py lookup --lang=en --word=I --ip=localhost

 'I' has the following suggested words:

['am', 'will', 'want', 'eat'] 

python3 examples/commandline.py lookup --lang=en --word=am --ip=localhost

 'am' has the following suggested words:
['the', 'Alice', 'Bob']   
````
Json:
````
python3 examples/example_json.py lookup --lang=nl --word=Ik -f examples/example.json
'Ik' has the following suggested words:

['heb', 'ben', 'denk', 'wil', 'weet', 'kan', 'hoop', 'was', 'geef', 'doe', 'vind', 'had', 'zal', 'zoek', 'voel', 'verwacht', 'moet', 'zou', 'zie', 'wilde', 'werk', 'probeerde', 'moest', 'kreeg', 'kon', 'ken', 'ga', 'zit', 'zeg', 'zat', 'wou', 'wist', 'vraag', 'scoorde', 'neem', 'leg', 'kom', 'hou', 'hoor', 'geloof', 'dacht', 'blijf', 'word', 'won', 'werd', 'wees', 'vroeg', 'vreesde', 'vrees', 'verzamel', 'vervul', 'trek', 'stel', 'stap', 'sta', 'spreek', 'sliep', 'schrok', 'rij', 'probeer', 'praat', 'pas', 'overdrijf', 'na', 'mik', 'meen', 'mag', 'maakte', 'maak', 'luister', 'loop', 'lijk', 'leef', 'kwam', 'keerde', 'juich', 'hing', 'herinner', 'grapte', 'ging', 'erken', 'communiceer', 'beleef', 'begrijp', 'bang', 'acht']

````

Licence
=======
[MIT](https://github.com/eronde/py_word_suggest/blob/master/LICENSE)
