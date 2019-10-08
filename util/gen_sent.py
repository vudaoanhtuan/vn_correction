import argparse
import pandas as pd

from tqdm import tqdm
import numpy as np

from preprocess import preprocess
from word_transform import gen_wrong_word

parser = argparse.ArgumentParser()
parser.add_argument('corpus')
parser.add_argument('word_list')
parser.add_argument('--percent', type=float, default=0.5)
parser.add_argument('--max_len', type=int, default=30)
parser.add_argument('-o', '--output', default='bisent.tsv')

def generate_bisent(sent, word_list, max_len=30, percent=0.5):
    sent = preprocess(sent)
    sent = sent.split()
    if len(sent) > max_len:
        sent = sent[:max_len]
    w_sent = []
    for w in sent:
        change_word = np.random.choice([True, False], p=[percent, 1-percent])
        if w in word_list and change_word:
            w = gen_wrong_word(w)
        w_sent.append(w)
    w_sent = ' '.join(w_sent)
    sent = ' '.join(sent)
    return sent, w_sent

if __name__=='__main__':
    args = parser.parse_args()

    with open(args.word_list) as f:
        word_list = f.read().split('\n')[:-1]

    with open(args.corpus) as f:
        corpus = f.read().split('\n')[:-1]

    with open(args.output, 'w') as f:
        for sent in tqdm(corpus):
            s,w = generate_bisent(sent, word_list, max_len=args.max_len, percent=args.percent)
            f.write(w+'\t'+s+'\n')