from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import pandas as pd
import string 

data=pd.read_csv(r"C:\Users\rctuh\Desktop\sentimentAIET\dataset\train-processed.csv")


STOPWORDS = stopwords.words('english')
STOPWORDS += list(string.punctuation)

STOPWORDS = set(STOPWORDS)


#Create a list of all the tweet texts.
positive_tweets = []
for tweet in data['tweet']: # add a condition here or it inputs all the reviews
    positive_tweets.append(tweet)
#print(positive_tweets)
#Create bag of words for positive tweets. Instead of a list of tweets now we'll have a list of words.
positive_tweets_bag = ''.join([str(tweet) for tweet in data['tweet']])
#print(positive_tweets_bag)

wordcloud = WordCloud(stopwords = STOPWORDS, background_color = "white", max_words = 1000).generate(positive_tweets_bag)
plt.figure(figsize = (10, 6))
plt.imshow(wordcloud)
plt.axis("off")
plt.title("Most frequent words in positive tweets")