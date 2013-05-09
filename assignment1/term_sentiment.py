"""
term_sentiment.py, which can be executed using the following command:
 
          $ python term_sentiment.py <sentiment_file> <tweet_file>
 
Your script should print to stdout each term-sentiment pair, one pair per line, in the following format:        
         
          <term:string> <sentiment:float>
 
For example, if you have the pair ("foo", 103.256) it should appear in the output as:
 
          foo 103.256
 
The order of your output does not matter.
"""

import sys
import json
import re

from tweet_sentiment import *
"""
from tweet_sentiment import sent_dict
from tweet_sentiment import get_tweet_text
from tweet_sentiment import sum_sent_score
"""

def estimate_term_score(dict_of_sent, list_of_tweet_text):
    tweet_scores = sum_sent_score(dict_of_sent, list_of_tweet_text)
    new_terms = {}
    for text in list_of_tweet_text:
        # print text.encode('utf-8')
        text = text.lower()
        # text = re.sub(r'[^\w]', ' ', text)
        # print text.encode('utf-8')
        for term in text.split():
            print "::", term.encode('utf-8'), "::", 

def main():
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]
    dict_of_sent = sent_dict(sent_file)
    list_of_tweet_text = get_tweet_text(tweet_file)
    scores = sum_sent_score(dict_of_sent, list_of_tweet_text)
    for thisscore in scores:
        print thisscore

    estimate_term_score(dict_of_sent, list_of_tweet_text)

if __name__ == '__main__':
    main()

