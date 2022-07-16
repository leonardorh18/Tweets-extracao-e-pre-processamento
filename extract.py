import os
import pandas as pd
from datetime import datetime

class TwitterExtraction():
    def __init__(self, twitterScraper):
        self.twitterScraper = twitterScraper
        
    def __check_path(self, out_path):
        os.makedirs(out_path, exist_ok = True)
        
    def collectFromQuery(self,
                        query, 
                        out_path, 
                        file_name = str(datetime.now().timestamp()).replace('.', ''), 
                        limit = 0):
        
        self.__check_path(out_path)
        tweets = self.twitterScraper.TwitterSearchScraper(query)
        tweets_list_content = []
        
        for qnt, tweet in enumerate(tweets.get_items()):
            if qnt >= limit and limit != 0:
                break
            tweets_list_content.append([tweet.id, tweet.date, tweet.content, tweet.user.username])
            
        tweets_df = pd.DataFrame(tweets_list_content, columns = ['tweet_id', 'date', 'text', 'user'])
        tweets_df.to_csv(out_path + "/" + file_name + '.csv')
        
            
    def collectFromUser(self,
                        user, 
                        out_path, 
                        limit = 0):
        file_name = f'tweets_{user}'
        self.__check_path(out_path)
        tweets = self.twitterScraper.TwitterUserScraper(user)
        tweets_list_content = []
        
        for qnt, tweet in enumerate(tweets.get_items()):
            if qnt >= limit and limit != 0:
                break
            tweets_list_content.append([tweet.id, tweet.date, tweet.content, tweet.user.username])
            
        tweets_df = pd.DataFrame(tweets_list_content, columns = ['tweet_id', 'date', 'text', 'user'])
        
        tweets_df.to_csv(out_path + "/" + file_name + '.csv')   

    
        