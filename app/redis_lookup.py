import redis
from util.Profile import profileThis
import redis_config

r = redis.StrictRedis(host=redis_config.REDIS_IP, port=6379, db=0)
def _connected(func):
    """TODO: Docstring for pre.

    :func:
    :returns: Boolean

    """
    def wrapper(*args,**opts):
        if is_redis_available():
            return func(*args, **opts)
    return wrapper
def redis_connect():
    """TODO: Docstring for redis_connect.
    :returns: TODO

    """
    # r = redis.StrictRedis(host='redis-dev-bigram-suggest', port=6379, db=0)
    r = redis.StrictRedis(host=redis_config.REDIS_IP, port=6379, db=0)
    result = r.zrevrange('gram:2:Ik',0,-1)
    for i in result :
        print(i.decode())
    # redis_server.get('x')

@profileThis
@_connected
def showKeys():
    res = r.keys('*')
    for i in res[0:9] :
       print(i.decode())

def populate():
    """TODO: Docstring for populate.
    :returns: TODO

    """
    # r = redis.StrictRedis(host=redis_config.REDIS_IP, port=6379, db=0)
    r = redis.StrictRedis(host='redis-dev-bigram-suggest', port=6379, db=0)
    kv={"top":55,"lll":77,"tddg":5}
    r.zadd("tesset",**kv)

def is_redis_available():
    try:
        r.ping()
    except (redis.exceptions.ConnectionError, redis.exceptions.BusyLoadingError):
        print("Can not connect to the redis server. Please start a redis service.")
        return False
    return True


if __name__ == '__main__':
    # populate()
    # redis_connect()
    # print(is_redis_available())
    showKeys()
