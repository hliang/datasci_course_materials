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

# from tweet_sentiment import *
"""
from tweet_sentiment import sent_dict
from tweet_sentiment import get_tweet_text
from tweet_sentiment import sum_sent_score
"""

def sent_dict(infile):
    """ read a file containing a list of sentiment scores
    return a dict like {word : score}
    """
    dict_of_sent = {}
    sent_file = open(infile)
    for thisline in sent_file.readlines(): 
        # thisline = thisline.strip() # remove newline '\n'
        # dict_of_sent[thisline.split('\t')[0]]= int(thisline.split('\t')[1])
        term, score  = thisline.split("\t")
        dict_of_sent[term] = int(score)
    return dict_of_sent

def get_tweet_text(infile):
    """ read a file containing tweets
    return a list of tweet text contents
    """
    texts = []
    f = open(infile)
    # i = 0
    for thisline in f.readlines():
        # print i, thisline
        thistweet = json.loads(thisline)
        if "text" in thistweet.keys(): #if the tweet has text, and not deleted
            this_text = thistweet["text"]
            # print "tweet", i, "::::", this_text
            # i += 1
            texts.append(this_text)
    return texts

def sum_sent_score(dict_of_sent, list_of_tweet):
    scores = []
    for t in list_of_tweet:
        # print t.encode('utf-8')
        thisscore = 0.0
        for word in t.split():
            if word.encode('utf-8').lower() in dict_of_sent.keys():
                # print word
                thisscore += dict_of_sent[word.lower()]
        scores.append(thisscore)
    return scores

def estimate_term_score(dict_of_sent, list_of_tweet_text):
    tweet_scores = sum_sent_score(dict_of_sent, list_of_tweet_text)
    new_term_scores = {}
    for i in range(len(list_of_tweet_text)):
        text = list_of_tweet_text[i]
        text_score = tweet_scores[i]
        # print text.encode('utf-8')
        # text = text.lower() # lower case
        text = re.sub(r'[^\w@#]', ' ', text) # remove non-english characters
        # print text.encode('utf-8')
        for term in text.split():
            if term not in dict_of_sent:
                try:
                    new_term_scores[term] += text_score
                except KeyError:
                    new_term_scores[term] = text_score
    return new_term_scores

def main():
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]
    dict_of_sent = sent_dict(sent_file)
    list_of_tweet_text = get_tweet_text(tweet_file)
    scores = sum_sent_score(dict_of_sent, list_of_tweet_text)

    new_term_scores = estimate_term_score(dict_of_sent, list_of_tweet_text)

    for term in new_term_scores.keys():
        print term.encode('utf-8'), new_term_scores[term]

if __name__ == '__main__':
    main()

