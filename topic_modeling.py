from bertopic import BERTopic
import pandas as pd
import numpy as np

topic_model = BERTopic()
tweets = pd.read_csv("datalake/pre_proc/tweets_sobre_python.csv")
docs = tweets.preproc.to_text()

#TRAINING
topics, probabilities = topic_model.fit_transform(docs, language='portuguese')
