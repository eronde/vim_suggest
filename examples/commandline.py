"""commandline.

Usage:
  commandline.py lookup --lang=<lang> --word=<preword>
  commandline.py -h | --help

Options:
  -h --help     Show this screen.
  --lang=<lang> Language of suggested word.
  --word=<preword>    Pre-word of suggested word.

"""
import redis
import py_word_suggest
# from config import REDIS_IP
from docopt import docopt
# r = redis.StrictRedis(host='py-word-suggest-redis', port=6379, db=0)
# r = redis.StrictRedis(host=REDIS_IP, port=6379, db=0)
rs = '172.17.0.3'
r = redis.StrictRedis(host=rs, port=6379, db=0)
def main():
    try:
        obj = py_word_suggest.Selector_redis(r)    
    except Exception as e:
        print("{e} Fail to connect to: {ip}".format(e=e,ip=rs))
        exit(1)

    arguments = docopt(__doc__, version='commandline 0.0.1')
    if arguments['lookup']:
       key = 'lang:{l}:gram:2:{w}'.format(l=arguments['--lang'],w=arguments['--word'])
    try:
       fetch = obj.gen_fetchWords(key)    
    except Exception as e:
        print("{e}".format(e=e))
        exit(1)

    print("'{w}' has the following suggested words:\n".format(w=arguments['--word']))
    print(list(obj.gen_suggestWord(*fetch)))

if __name__ == "__main__":
    main()
