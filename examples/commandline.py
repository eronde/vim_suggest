"""commandline.

Usage:
  commandline.py lookup --lang=<lang> --word=<preword> [--ip=<redis-ip>] [--port=<redis-port>]
  commandline.py -h | --help

Options:
  -h --help             Show this screen.
  --lang=<lang>         Language of suggested word.
  --word=<preword>      Pre-word of suggested word.
  --ip=<rediis-ip>      Ip of redis server (Default: 172.17.0.3)
  --port=<rediis-port>  Port of redis server (Default: 6379)

"""
import redis
import py_word_suggest
# from config import REDIS_IP
from docopt import docopt


def main():
    arguments = docopt(__doc__, version='commandline 0.0.1')
    if arguments['--port']:
        rp = arguments['--port']
    else:
        rp = 6379
    if arguments['--ip']:
        rs = arguments['--ip']
    else:
        rs = '172.17.0.3'
    r = redis.StrictRedis(host=rs, port=rp, db=0)
    try:
        obj = py_word_suggest.Selector_redis(r)
    except Exception as e:
        print("{e} Fail to connect to: {ip}:{port}".format(e=e, ip=rs, port=rp))
        exit(1)

    if arguments['lookup']:
       key = 'lang:{l}:gram:2:{w}'.format(l=arguments['--lang'], w=arguments['--word'])
    try:
       fetch = obj.gen_fetchWords(key)
    except Exception as e:
        print("{e}".format(e=e))
        exit(1)

    print("'{w}' has the following suggested words:\n".format(w=arguments['--word']))
    print(list(obj.gen_suggestWord(*fetch)))

if __name__ == "__main__":
    main()
