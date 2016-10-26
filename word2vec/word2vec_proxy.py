from . import word2vec_machine
from . import singletone_decorator

singletone = singletone_decorator.SingletoneDecorator(word2vec_machine.Word2vecMachine)
Word2vecInstance = singletone()
