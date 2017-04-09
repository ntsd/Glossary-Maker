from nltk.tokenize import word_tokenize

from nltk import FreqDist

import stopWordFilter

import collections

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
def getMostFrequency(words, limit=10):
    counter = collections.Counter(words)
    return counter.most_common(limit)


@timing
def getMostFrequency2(words, limit=10):
    fdist = FreqDist(words)
    return fdist.most_common(limit)


if __name__ == '__main__':
    with open("SampleTexts/beggars.txt", "r") as f:
        content = f.read()
        words = word_tokenize(content.lower())
        words = stopWordFilter.stopWordFilter(words)
        mostWords = getMostFrequency(words)
        print(mostWords)
