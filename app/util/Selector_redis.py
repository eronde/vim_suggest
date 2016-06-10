from app.util.decorators import empty_arguments
class SelectorRedisError(Exception): pass

class SelectorRedisNoBaseKeyFoundError(SelectorRedisError): pass

class SelectorRedisNoSuggestWordFoundError(SelectorRedisError): pass

class SelectorRedisEmptyValue(SelectorRedisError): pass

class Selector_redis(object):
    """ Selector_redis. Class for fetching bigram data from redis db
    :Datastructure:
            sorte dset: key:value(listOfTuples), 'lang:{language}:gram:2:{word}':[({word},{freq score})]
    """

    def __init__(self, redis_connection=None):
        """TODO: check redis_connection """
        self.r = redis_connection
        try:
            self.r.ping()
        except Exception:
            raise Exception("Error: Redis server is not connected. {x} must be a redis object.".format(x=redis_connection))
        else:
            self.redis_running = True
        finally:
            self.redis_running = False

    def _connected(func):
        """_connected: Decoration to check if redis server is connected
        :func:
        :returns: Boolean

        """
        def wrapper(self, *args, **opts):
            if self.is_redis_available():
                return func(self, *args,  **opts)
        return wrapper

    def is_redis_available(self):
        """is_redis_available: Check of redis conntion is available
        :TODO: can not yet test this function, StrictRedis doesn't allow to disconnect
        a redis connection and coverage  problem
        :return: Bool
        """
        self.redis_running = False
        try:
            self.r.ping()
        except AttributeError:
            raise Exception('l')
        # except self.r.exceptions.ConnectionError:
        #     self.redis_running = False
        # except self.r.exceptions.BusyLoadingError:
        #     self.redis_running = False
        # except AttributeError:
        #     self.redis_running = False
        else:
            return True

    @_connected
    @empty_arguments(SelectorRedisEmptyValue)
    def gen_suggestWord(self, *data):
        """gen_suggestWord: Generate decoded suggested word of a data set
        :data: list 
        :return: string
        """
        return (x.decode() for x in data)

    @_connected
    @empty_arguments(SelectorRedisEmptyValue)
    def gen_fetchWords(self, key:str,  withscore=False):
        """gen_fetchWords: Fetch all suggested word of giving key from redis
            Sorted by hightest frequency and alphabetic order
        :key: string 'lang:{language}:gram:2:{word}'
        :Todo: Look at exception
        :return: coded string
        """
        if not self.r.exists(key):
            raise SelectorRedisNoBaseKeyFoundError("Error: key ", key, " does not exists. ")
        if not withscore:
            return (x for x in self.r.zrevrange(key, 0, -1))
        else:
            return (x for x in self.r.zrevrange(key, 0, -1, 'WITHSCORES'))

    @_connected
    @empty_arguments(SelectorRedisEmptyValue)
    def addNewSuggestWord(self, key, word, freq=1):
        """addNewSuggestWord: Adding new suggested word to key
        :key: string
        :word: string
        :freq: int, score 
        :returns: void
        :TODO: Validate  if word only contains Alpha str.isalpha()
        """
        self.r.zadd(key, word, freq)

    @_connected
    @empty_arguments(SelectorRedisEmptyValue)
    def removeSuggestWord(self, key, word):
        """removeSuggestWord: Remove suggested word from key
        :key: string
        :word: string 
        :returns: void
        :TODO: validation
        """
        self.r.zrem(key, word)

    @_connected
    @empty_arguments(SelectorRedisEmptyValue)
    def existBaseKey(self, key):
        """existBaseKey: Check if key exists
        :key: string
        :returns: bool

        """
        return self.r.exists(key)

    @_connected
    @empty_arguments(SelectorRedisEmptyValue)
    def increaseScoreSuggestedWord(self, key, suggestedWord, score=1):
        """increaseScoreSuggestedWord: Increase score of suggested word of giving key
        :key: String
        :suggestedWord: String
        :score: int
        :returns: void

        """
        # Check if key or suggestedWord are empty
        # Test key exists
        if not self.r.exists(key):
            raise SelectorRedisNoBaseKeyFoundError( "Error: key '{x}' does not exists.".format(x=key))
        # Test suggested word
        fetch_collection = self.gen_fetchWords(key)
        suggestedWords = set(self.gen_suggestWord(*fetch_collection))
        if not self.containing(suggestedWords, suggestedWord):
            raise SelectorRedisNoSuggestWordFoundError("Error: suggested word: '{x}' does not exists with basekey '{y}'.".format(x=suggestedWord, y=key))
        if type(score) != int:
            raise TypeError("Error: Score '{x}' needs to be an int or a float.".format(x=score))
        # Update
        self.r.zincrby(key, suggestedWord, score)

    @empty_arguments(SelectorRedisEmptyValue)
    def containing(self, collection, targetItem):
        """containing: Checks if a item is or is not in a collection of items
        :items: collection of items
        :targetItem: 
        :returns: bool
        """
        return targetItem in collection
