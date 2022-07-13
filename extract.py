import snscrape.modules.twitter as twitterScraper
from datetime import datetime
import pandas as pd


def collectFromQuery(query, 
                     out_path, 
                     file_name = str(datetime.now().timestamp()).replace('.', ''), 
                     limit = 0):
    
    tweets = twitterScraper.TwitterSearchScraper(query)
    tweets_list_content = []
    
    for qnt, tweet in enumerate(tweets.get_items()):
        if qnt >= limit and limit != 0:
            break
        tweets_list_content.append([tweet.id, tweet.date, tweet.content, tweet.user.username])
        
    tweets_df = pd.DataFrame(tweets_list_content, columns = ['tweet_id', 'date', 'text', 'user'])
    tweets_df.to_csv(out_path + file_name + '.csv')
    
        
def collectFromUser(user, 
                    out_path, 
                    file_name = str(datetime.now().timestamp()).replace('.', ''),
                    limit = 0):
    
    tweets = twitterScraper.TwitterUserScraper(user)
    tweets_list_content = []
    
    for qnt, tweet in enumerate(tweets.get_items()):
        if qnt >= limit and limit != 0:
            break
        tweets_list_content.append([tweet.id, tweet.date, tweet.content, tweet.username])
        
    tweets_df = pd.DataFrame(tweets_list_content, columns = ['tweet_id', 'date', 'text', 'user'])
    
    tweets_df.to_csv(out_path + str(file_name) + '.csv')     
        
if __name__ == '__main__':
    #exemplo de query
    #https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query
    query = "python lang:pt since:2022-06-01 until:2022-06-02"
    out_path = 'datalake/'
    collectFromQuery(query, out_path, file_name='tweets_sobre_python', limit = 0)
    user = "CSGO"
    collectFromUser(user, out_path, file_name='tweets_csgo', limit = 0)
    
        