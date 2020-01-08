import nltk 
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import json
import pickle

import numpy as np 
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
import random

words = []
classes = []
ignore_words = ['?', '!']
data_file = open('intents.json').read()
intents = json.loads(data_file)


for intent in intents['intents']:
    for pattern in intent['patterns']:
        w = nltk.word_tokenize(pattern) # tokenize each word
        documents.append((w, intent['tag'])) # add documents in the corpus

        if intent['tag'] not in classes: # add to our classes list
            classes.append(intent['tag'])

# lemmatize, lower each word and remove duplicates
words = [
    lemmatizer.lemmatize(w.lower()) 
    for w in words if w not in ignore_words
    ]
words = sorted(list(set(words)))

#sort classes
classes = sorted(list(set(classes)))
# documents = combination between patterns and intents
print(len(documents), "documents")
# classes = intents
print (len(classes), "classes", classes)
# words = all words, vocabulary
print(len(words), "unique lemmatized words", words)

pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))



