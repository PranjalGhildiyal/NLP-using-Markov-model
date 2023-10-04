import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('punkt')
import re

def clean(stories):
    cleaned_stories= []
    for line in stories:
        line= line.lower()
        line = re.sub(r"[,.\"\'!@#$%^&*(){}?/;`~:<>+=-\\]", "", line) # replacing any special characters in thr line
        tokens = word_tokenize(line)
        words = [word for word in tokens if word.isalpha()]
        cleaned_stories+=words
    return cleaned_stories