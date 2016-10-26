from gensim.models import word2vec

class Word2vecMachine:
    def __init__(self):
        self.model = word2vec.Word2Vec.load_word2vec_format('word2vec/word2vec_model.bin', binary=True, unicode_errors='ignore')

    def getSimilarity(self, positive=[], negative=[]):
        if positive == None:
            return [('', '')]
        return self.model.most_similar(positive=positive, negative=negative)
