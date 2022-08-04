
import spacy
import gensim
class PreProcess():
    def __init__(self, nlp):
        self.__nlp = nlp
        
    def __clean(self, doc):
        if self.remove_link:
            doc = " ".join(word for word in doc.split() if "http" not in word and "www" not in word)
                
        return " ".join(word for word in gensim.utils.simple_preprocess(doc, min_len = self.min_len))
        
    def __remove_stops(self, doc):
       
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

    def execute(self, docs: list, aditional_stops = [], min_len = 0, remove_link = True):
        self.__docs = docs 
        self.remove_link = remove_link
        self.min_len = min_len
        self.stops = aditional_stops
        return self.__process()
        
    
    

    
    
