
import spacy
import gensim
class PreProcess():
    def __init__(self, nlp):
        self.__nlp = nlp
        
    def __clean(self, doc):
        return " ".join(word for word in gensim.utils.simple_preprocess(doc, min_len = self.min_len))
        
    def __remove_stops(self, doc):
        
        if self.keep_digit:
            new_doc  = " ".join(token.text for token in self.__nlp(doc) if not token.is_stop and token.text not in self.stops )
        else:
            new_doc  = " ".join(token.text for token in self.__nlp(doc) if not token.is_stop and not token.is_digit and token.text not in self.stops  )          
        return new_doc
    
    def __lemmatization(self, doc):
        new_doc = " ".join(token.lemma_ for token in self.__nlp(doc))
        return new_doc
    
    def __process(self):
        new_docs = []
        for doc in self.__docs:
            new_docs.append(self.__lemmatization(self.__remove_stops(self.__clean(doc))))
        return new_docs

    def execute(self, docs: list, keep_digit = False, aditional_stops = [], min_len = 0):
        self.__docs = docs 
        self.min_len = min_len
        self.stops = aditional_stops
        self.keep_digit = keep_digit
        return self.__process()
        
    
    

    
    
