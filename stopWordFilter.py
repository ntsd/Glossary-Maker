from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import time

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print('%s function took %0.3f ms' % (f.__name__, (time2-time1)*1000.0))
        return ret
    return wrap

@timing
def stopWordFilter(words):
    """This method Faster but return filter"""
    stopWords = set(stopwords.words("english"))
    wordsNotStopWords = filter(lambda w: w not in stopWords, words)
    return wordsNotStopWords

@timing
def stopWordFilter2(words):
    """This slower but return list"""
    stopWords = set(stopwords.words("english"))
    return [w for w in words if w not in stopWords]

if __name__ == '__main__':
    exampleText = "This is example text for stop words."
    with open("SampleTexts/beggars.txt", "r") as f:
        content = f.read()
        words = word_tokenize(content)
        print(len(words))
        stopWordFilter(words)
        stopWordFilter2(words)
        stopWordFilter2(words)
        stopWordFilter(words)