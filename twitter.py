import twython
import nltk
from nltk.twitter import Twitter
tw = Twitter()
tw.tweets(keywords='love, hate', limit=10) #sample from the public stream