import re
import pytest
from py_word_suggest.Selector import *

@pytest.fixture()
def bigrams():
    b = {'I':[['am',1],['want', 10], ['like', 5]]}
    bigrams = Selector(b)
    return bigrams

@pytest.mark.skip
def test_getsuggestedwords(bigrams):
    """Selector: Get all suggested words of words 'I'
    :returns: TODO
    """
    match = ('want', 'like', 'am')
    # assertListEqual(list(bigram.gen_suggestWord(*x)), match, "Should be ['want', 'like','am']")
    result = set(bigrams.get_suggestWord('I',True))
#    assert obj.p() == "t"
    assert match == result

#@pytest.mark.skip
def test_genSuggestedWords(bigrams):
    """Selector: Generate suggested words object"""
    #Test set
    assert bigrams._suggestWords == None
    smatch = {'want', 'like', 'am'}
    bigrams.set_suggestedWords('I')
   #test empty after list
    assert set(bigrams._suggestWords) == smatch
    assert bigrams._suggestWords == None
    usmatch = {'am','like','want'}
    bigrams.set_suggestedWords('I',sort=False)
    assert set(bigrams._suggestWords) == usmatch
    assert bigrams._suggestWords == None
    #Test list
    lmatch = ['want', 'like', 'am']
    bigrams.set_suggestedWords('I',sort=True)
    assert list(bigrams._suggestWords) == lmatch
    assert bigrams._suggestWords == None
    ulmatch = ['am','like','want']
    bigrams.set_suggestedWords('I',sort=False)
    assert list(bigrams._suggestWords) == ulmatch
    assert bigrams._suggestWords == None

@pytest.mark.skip
def test_getSuggestedWords(bigrams):
    """Selector: Generate suggested words object"""
    assert bigrams.selectedSuggestWords == None
    match = {'want', 'like', 'am'}
    bigrams.set_suggestedWords('I')
    assert bigrams._suggestWords == match

@pytest.mark.parametrize("testInput,sortTypeOutput",
            [
            (None,['am','want','like']),
            (True,['want','like','am']),
            (False,['am','like','want'])
            ]
        )
def test_setSuggestedWords(bigrams, testInput, sortTypeOutput):
    """Selector: Set list of suggested word to object"""
    bigrams.set_suggestedWords('I',sort=testInput)
    assert list(bigrams._suggestWords) == sortTypeOutput
    assert bigrams._suggestWords == None

def test_setSelectedBigram(bigrams):
    """Selector: Set Suggested bigram (values of basekey) to object"""
    assert bigrams._selectedBigram == None
    bigramValues = [['am',1],['want', 10], ['like', 5]]   
    bigrams.set_bigram('I')
    assert bigrams._selectedBigram == bigramValues
    with pytest.raises(SelectorNoBaseKeyFoundError) as e:
        bigrams.set_bigram('NoBaseKey==')
    assert str(e.value) == "Error: key, \'NoBaseKey==\' does not exists." 

def test_setSelectedBaseKey(bigrams):
    """Selector: Set Suggested basekey (key) to object"""
    assert bigrams._selectedBaseKey == None
    basekey='I'
    bigrams.set_baseKey(basekey)
    assert bigrams._selectedBaseKey == basekey

    with pytest.raises(SelectorNoBaseKeyFoundError) as e:
        bigrams.set_baseKey('NoBaseKey==')
    assert str(e.value) == "Error: key, \'NoBaseKey==\' does not exists." 

@pytest.mark.skip
def test_addNewsuggestedWord(bigrams):
    """Selector: Add new suggested word to 'I' key to selected_bigram
    :returns: TODO

    """
    bigrams.set_bigram('I')
    with pytest.raises(SelectorError) as e:
        bigrams.add_newSuggestedWord('am')
    assert str(e.value) == "Error: word: 'am' already in bigram object." 
     
    # bigramValues = [['am',1],['want', 10], ['like', 5],['test',1 ]]
    # bigrams.add_newSuggestedWord('test')
    # assert bigrams._selectedBigram == bigramValues

# @pytest.mark.skip
def test_addChangesToBigrams(bigrams):
    """Selector: Add changes to bigram object
    :returns: TODO
    """
    with pytest.raises(SelectorError) as e:
    # with pytest.raises(SelectorNoBaseKeyFoundError, SelectorError):
         bigrams.set_bigram('NoKey')
    assert str(e.value) == "Error: key, \'NoKey\' does not exists." 
    #assert str(e.value) == "Error: _selectedBigram is None"
    #assert str(SelectorNoBaseKeyFoundError.value) == "Error: key, \'NoKey\' does not exists." 
    # bigrams.set_bigram('I')
    # with pytest.raises(SelectorError) as e:
    #     bigrams.add_newSuggestedWord('am')
    # assert str(e.value) == "Error: word: 'am' already in bigram object." 
    # bigramValues = [['am',1],['want', 10], ['like', 5],['test',1 ]]
    # bigrams.add_newSuggestedWord('test')
    # assert bigrams._selectedBigram == bigramValues

def test_checkKeyExist(bigrams):
    """Selector: Check if base 'word' key exists or not exists
    :returns: TODO

        """
    exist = bigrams.existBaseKey('I')
    assert exist == True
    notexist = bigrams.existBaseKey('How')
    assert notexist == False

def test_setBigramToObject(bigrams):
    """Selector: Set bigram values to bigram object
    :returns: TODO
    """
    assert bigrams._selectedBigram == None
    bigrams.set_bigram('I')
    bigramValues = [['am',1],['want', 10], ['like', 5]]
    assert bigrams._selectedBigram == bigramValues
    
    with pytest.raises(SelectorNoBaseKeyFoundError) as e:
        bigrams.set_bigram('NoKey')
    assert str(e.value) == "Error: key, \'NoKey\' does not exists." 
    assert bigrams._selectedBigram == None









# @pytest.fixture
# def bigram():
#         data = {'I':[['am',1],['want', 10], ['like', 5]]}
#         bigrams = Selector(data)
#         return bigrams

    # self.redis.zadd("Hello",  "Alice", 1)
    # self.redis.zadd("Hello", "Bob", 10)

#     """Selector: Fetch all suggested words of words 'I' with scores
#     :returns: TODO
#     """
#     obj = Selector_redis(self.redis)
#     x = obj.gen_fetchWords('I', withscore=True)
#     match = [('want'.encode(), 10), ('am'.encode(), 1)]
#     self.assertListEqual(list(x), match, "Should be [(b'want', 10),(b'am', 1)]")

# def test_fetchSuggestedWordsWithoutScores(self):
#     """Selector: Fetch all suggested words of words 'I' without scores
#     :returns: TODO
#     """
#     obj = Selector_redis(self.redis)
#     x = obj.gen_fetchWords('I')
#     match = ['want'.encode(), 'am'.encode()]
#     self.assertListEqual(list(x), match, "Should be ['want','am']")

# def test_gensuggestedwords(bigrams):
#     """Selector: Generateor of all suggested words
#     :returns: TODO
#     """
#     match = ['want', 'like', 'am']
#     # assertListEqual(list(bigram.gen_suggestWord(*x)), match, "Should be ['want', 'like','am']")
#     result = list(bigrams.gen_suggestWord())
# #    assert obj.p() == "t"
#     assert match == result
#     assert match == result

# def test_getInvalidKey(self):
#     """Selector: Fetch invalid base key[A]
#     :returns: TODO
#     """
#     obj = Selector_redis(self.redis)
#     with self.assertRaises(SelectorRedisNoBaseKeyFoundError) as e:
#         obj.gen_fetchWords('NoBaseKey')
#     error = str(e.exception)
#     self.assertTrue("Error: key \', \'NoBaseKey\', \' does not exists." in error)

# def test_removeSuggestedWord(self):
#     """Selector: Remove suggested word from 'I' key
#     :returns: TODO

#     """
#     obj = Selector_redis(self.redis)
#     match = ['want']
#     obj.removeSuggestWord('I', 'am')
#     x = self.redis.zrevrange('I', 0, -1)
#     self.assertListEqual(list(obj.gen_suggestWord(*x)), match, "Should be ['am']")


# def test_increaseScoreOfSuggestedWord(self):
#     """Selector: Increase score of suggested word
#     :returns: TODO

#     """
#     obj = Selector_redis(self.redis)
#     obj.increaseScoreSuggestedWord('I', 'am')
#     scores = obj.gen_fetchWords('I', withscore=True)
#     match = [('want'.encode(), 10),  ('am'.encode(), 2)]
#     self.assertListEqual(list(scores), match, "Should be [(b'want', 10),(b'am', 2)]")
#     # Increase by 4
#     obj.increaseScoreSuggestedWord('I', 'am', 4)
#     scores = obj.gen_fetchWords('I', withscore=True)
#     match = [('want'.encode(), 10),  ('am'.encode(), 6)]
#     self.assertListEqual(list(scores), match, "Should be [(b'want', 10),(b'am', 6)]")
#     # Increase by -7
#     obj.increaseScoreSuggestedWord('I', 'am', -7)
#     scores = obj.gen_fetchWords('I', withscore=True)
#     match = [('want'.encode(), 10),  ('am'.encode(), -1)]
#     self.assertListEqual(list(scores), match, "Should be [(b'want', 10),(b'am', -1)]")
#     # Increase by string
#     with self.assertRaises(TypeError) as e:
#         obj.increaseScoreSuggestedWord('I', 'am', 'l')
#     # Increase non existing key
#     with self.assertRaises(SelectorRedisNoBaseKeyFoundError) as e:
#         obj.increaseScoreSuggestedWord('Hel', 'am', 4)
#     error = str(e.exception)
#     pat = "Error: key 'Hel' does not exists."
#     self.assertTrue(pat in error, "'{e} ' should be 'Error: key 'Hel' does not exists.'".format(e=pat))
#     # Increase non existing suggested word
#     with self.assertRaises(SelectorRedisNoSuggestWordFoundError) as e:
#         obj.increaseScoreSuggestedWord('I', 'bobby',  4)
#     error = str(e.exception)
#     pat = "Error: suggested word: 'bobby' does not exists with basekey 'I'." 
#     self.assertTrue(pat in error, "'{e} ' should be: 'Error: suggested word: 'bobbypat' does not exists with basekey 'I.'".format(e=pat))
#     # Increase non existing suggested word
#     with self.assertRaises(SelectorRedisEmptyValue) as e:
#         obj.increaseScoreSuggestedWord('I', '', 4)
#     error = str(e.exception)
#     pat = "^Error in 'increaseScoreSuggestedWord': One of the given arguments .*\, 'I', '', 4\)' are empty\.$"
#     regex = re.search(pat, error)
#     assert regex is not None, "'{e} ' should contain:Error in 'increaseScoreSuggestedWord': One of the given arguments , 'I', '', 4\)' are empty .format(e=pat)"
#     # Increase suggested word invalid score
#     with self.assertRaises(TypeError) as e:
#         obj.increaseScoreSuggestedWord('I', 'want', 'nonvalid')
#     error = str(e.exception)
#     pat = "^Error: Score 'nonvalid' needs to be an int or a float.$"
#     regex = re.search(pat, error)
#     assert regex is not None,"'{e}' should contain: Error: Score 'nonvalid' needs to be an int or a float.".format(e=pat)

# def test_checkSuggestedWordExists(self):
#     """Selector: Check if suggested word exists or not exists
#     :returns: TODO

#     """
#     obj = Selector_redis(self.redis)
#     # list
#     data = ['test', 'bla']
#     self.assertTrue(obj.containing(data, 'test'))
#     # sets$
#     self.assertTrue(obj.containing(data, 'test'))
#     # Not containing
#     self.assertFalse(obj.containing(data, 'hello'))
#     # generator
#     fetchdata = obj.gen_fetchWords('I')
#     data = set(obj.gen_suggestWord(*fetchdata))
#     self.assertTrue(obj.containing(data, 'want'))
#     self.assertFalse(obj.containing(data, 'wantby'))

