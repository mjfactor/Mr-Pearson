import nltk
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
# nltk.download('punkt')


def tokenize(sentence):
    return nltk.word_tokenize(sentence)


def stem(words):
    return stemmer.stem(words.lower())


def bag_of_words(tokenized_sentence, all_words):
    pass



