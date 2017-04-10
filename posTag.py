from nltk.tag import pos_tag

from nltk.tokenize import word_tokenize


def posTag(words):
    tagged_sent = pos_tag(words)
    return tagged_sent

if __name__ == '__main__':
    exampleText = "This is example text for stop words."
    words = word_tokenize(exampleText)
    print(posTag(words))