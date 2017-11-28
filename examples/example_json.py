"""example_json.

Usage:
  example_json.py lookup --lang=<lang> --word=<preword> [-f <file>]
  example_json.py -h | --help

Options:
  -h --help             Show this screen.
  --lang=<lang>         Language of suggested word.
  --word=<preword>      Pre-word of suggested word.
  -f file               Json file
"""
from py_word_suggest.PWS_Selector_json import *
from py_word_suggest.utils import load_data_from_json
from docopt import docopt
def main():
    fn = None
    arguments = docopt(__doc__, version='commandline 0.0.1')
    if arguments['-f']:
       fn = arguments['-f']
        
    if fn is None:
        fn = './examples/example.json'
    
    try:
        bigrams = load_data_from_json(fn)
    except Exception as e:
        raise e
        exit(1)
    
    try:
        obj = PWS_selector_json(bigrams)
    except Exception as e:
        raise e
        exit(1)

    if arguments['lookup']:
       key = 'lang:{l}:0:{w}'.format(l=arguments['--lang'], w=arguments['--word'])
    try:
        obj.set_suggestedWords(key)
    except Exception as e:
        print("{e}".format(e=e))
        exit(1)

    print("'{w}' has the following suggested words:\n".format(w=arguments['--word']))
    print(list(obj._suggestWords))
    with open(fn, 'r') as f:
        obj._bigrams = f
    
if __name__ == "__main__":
    main()
