import spacy
import gensim

spacy.cli.download("pt_core_news_lg")
nlp = spacy.load('pt_core_news_lg')

class PreProcess():
    def __init__(self, nlp):
        self.__nlp = nlp
        self.__docs = []
        
    def __clean(self, doc):
      return " ".join(word for word in gensim.utils.simple_preprocess(doc))
        
    def __remove_stops(self, doc):
      
        pass 
    
    def __lemmatization(self):
        pass
    
    def __process(self):
      new_docs = []
      for doc in self.__docs:
        __remove_stops(__clean(self, doc))

    def execute(self, docs: list):
        self.__docs = docs 
        __process()
        
    
    

    
    
