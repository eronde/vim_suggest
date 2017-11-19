# py_word_suggest/PSW_Selector_json.py
class SelectorError(Exception): pass

class SelectorNoBaseKeyFoundError(SelectorError): pass

class SelectorNoSuggestWordFoundError(SelectorError): pass

class SelectorEmptyValue(SelectorError): pass
from .decorators import empty_arguments
from . import export
from .utils import containing

@export
class PWS_selector_json(object):
    """ PWS_selector_json. Class to retreive bigram from json     
    :Datastructure:
            dictionary: key:value(listOflist, 'lang:<language>:gram:2:<word>':[[<word>,<freq score>]]
    """

    def __init__(self, bigrams):
        self.bigrams = bigrams
        self._suggestWords = None
        self._selectedBaseKey = None #B bigram (key) that user selected, -1=current selected
        self._selectedBigram = None#Bigram (Base (value) that user selected
        self._lookups = () #tuple, bigrams that user has selected
        
    def gen_suggestWord(self,key:str,sort=None):
        """gen_suggestWord: Generate suggested word, sorted by hightest frequency
        :key: string 'lang:{language}:gram:2:{word}'
        :sort: sort by frequency, True=descending, False=ascending, None=No sorting
        :return: generator
        """
        if type(sort) is bool:
            sortList = sorted(self.bigrams[key], key=lambda w: w[1],reverse=sort)
        else:
           sortList = self.bigrams[key]
        for x in sortList:
            yield x[0]
        self._suggestWords = None

    @empty_arguments(SelectorEmptyValue)
    def set_suggestedWords(self, key:str,**kwargs):
        """set_suggestedWords: Set all suggested word of giving key 
            Sorted by hightest frequency 
        :key: string 'lang:{language}:gram:2:{word}'
        :return: void generator type 
        """
        if not containing(self.bigrams, key):
           raise SelectorNoBaseKeyFoundError("Error: key, '{k}' does not exists.".format(k=key))
            
        self._suggestWords = self.gen_suggestWord(key, **kwargs)

    @empty_arguments(SelectorEmptyValue)
    def set_baseKey(self, baseKey:str):
        """set_bigram: Set baseKey (key) to object 
        :baseKey: string 'lang:{language}:gram:2:{word}'
        :return: void 
        """
        if not containing(self.bigrams, baseKey):
            raise SelectorNoBaseKeyFoundError("Error: key, '{k}' does not exists.".format(k=baseKey))
            
        self._selectedBaseKey = baseKey
        
    @empty_arguments(SelectorEmptyValue)
    def set_bigram(self, baseKey:str):
        """set_bigram: Set bigram (values) of giving baseKey 
        :baseKey: string 'lang:{language}:gram:2:{word}'
        :return: void 
        """
        if not containing(self.bigrams, baseKey):
            self._selectedBigram = None
            raise SelectorNoBaseKeyFoundError("Error: key, '{k}' does not exists.".format(k=baseKey))
        self._selectedBigram = self.bigrams.get(baseKey, None)

    def addBigramLookup(self, lookupEntree:str):
        """addBigramLookup: Add new entree of what user has lookup
        :lookupEntree string,
        :return: void, add to tuple 
        """

        if isinstance(lookupEntree,str) and not ' ' in lookupEntree:
            self._lookups = self._lookups + (lookupEntree, )
        else:
            raise SelectorNoBaseKeyFoundError("Error: lookupEntree, '{k}' needs to be a string.".format(k=lookupEntree))

    def getLookup(self):
        """getLookup: Get entree of what user has lookup
        :return:  tuple 
        """
        return self._lookups

