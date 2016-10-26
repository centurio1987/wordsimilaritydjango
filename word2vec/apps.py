from django.apps import AppConfig
import word2vec_proxy
import word2vec_machine


class Word2VecConfig(AppConfig):
    name = 'word2vec'
    def ready(self):
        word2vec_proxy.Word2vecInstance
