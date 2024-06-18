from typing import List
import re
import nltk


def preprocess_text(data: str):
    lemmatize = nltk.WordNetLemmatizer()
    processed_text = []
    for i in [data]:
        text = re.sub("[^a-zA-Z]", " ", i)
        text = nltk.word_tokenize(text, language="english")
        text = [lemmatize.lemmatize(word) for word in text]
        text = " ".join(text)
        processed_text.append(text)
    
    return processed_text