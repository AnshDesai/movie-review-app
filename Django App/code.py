from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy as nltk_accuracy


def extract_features(words):
    return dict([(word, True) for word in words])

import nltk
nltk.download('movie_reviews')

def SentimentAnalyzer(text):

    fileids_pos = movie_reviews.fileids('pos')
    fileids_neg = movie_reviews.fileids('neg')

    features_pos = [(extract_features(movie_reviews.words(fileids=[f])),'Positive') for f in fileids_pos]
    features_neg = [(extract_features(movie_reviews.words(fileids=[f])),'Negative') for f in fileids_neg]

    threshold = 0.8
    num_pos = int(threshold*len(features_pos))
    num_neg = int(threshold*len(features_neg))
    features_train = features_pos[:num_pos] + features_neg[:num_neg]
    features_test = features_pos[num_pos:] + features_neg[num_neg:]
    classifier = NaiveBayesClassifier.train(features_train)
    
    probabilities = classifier.prob_classify(extract_features(text.split()))
    predicted_sentiment = probabilities.max()
    
    return predicted_sentiment  
