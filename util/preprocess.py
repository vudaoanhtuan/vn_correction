import re
import string

def preprocess(sent):
    sent = sent.lower().strip()
    sent = sent.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation)))
    sent = re.sub(r'[0-9]+', '', sent)
    sent = re.sub(r'\s+', ' ', sent)
    return sent