        
import snscrape.modules.twitter as twitterScraper
from datetime import datetime
import pandas as pd
import spacy
import os
from extract import TwitterExtraction
from preprocess import PreProcess
import glob
import time

####################################################
# EXECUTE THIS LINE IF YOU DONT HAVE THE package
####################################################
#spacy.cli.download("en_core_web_lg")
#spacy.cli.download('pt_core_news_lg')

#nlp = spacy.load('pt_core_news_lg') # Package to preprocess in portuguese if you want
nlp = spacy.load('en_core_web_lg')


def extracting_tweets():
    twitterExtractor = TwitterExtraction(twitterScraper)
    #exemplo de query
    #https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query
    #query = "python lang:pt since:2022-06-01 until:2022-06-02"
    #query = "eleições lang:pt since:2018-12-01 until:2018-12-30"
    query = "china lang:en"
    out_path = 'datalake/raw_tweets'
    
    twitterExtractor.collectFromQuery(query, out_path, file_name='tweets_sobre_china', limit = 20000, verbose=True)
    #user = "uffsonline"
    #twitterExtractor.collectFromUser(user, out_path, limit = 0) 
    
def pre_process():
    preProc = PreProcess(nlp)
    path = 'datalake/raw_tweets/'
    csv_files = glob.glob(os.path.join(path, "*.csv"))
    for file in csv_files:
        df = pd.read_csv(file)
        texts = df.text.to_list()
        texts = preProc.execute(texts, min_len= 3, remove_link=True)
        df['preproc'] = texts 
        file_name = file.split('\\')[-1]
        df.to_csv(f'datalake/pre_proc/{file_name}')

if __name__ == '__main__':
    print("Extraindo tweets")
    #extracting_tweets()
    time.sleep(10)
    print("Pre processando tweets")
    pre_process()
    
    
    