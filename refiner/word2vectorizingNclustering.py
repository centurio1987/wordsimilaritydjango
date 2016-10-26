
# coding: utf-8

import word2vec
import gensim

word2vec.word2phrase('./refined_text.txt', './wiki-phrase', verbose=True)
word2vec.word2vec('./wiki-phrase', './word2vec_model.bin', size=100, verbose=True)




word2vec.word2clusters('/Users/KYD/Documents/wiki_project/refined_text.txt', 'Users/KYD/Documents/wiki_project/refined_text_cluster.txt', 100, verbose=True)

