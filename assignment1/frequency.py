"""
The frequency of a term can be calculate with the following formula:
[# of occurrences of the term in all tweets]/[# of occurrences of all terms in all tweets]
frequency.py should take a file of tweets as an input and be usable in the following way:
 
          $ python frequency.py <tweet_file>
 
Assume the tweet file contains data formatted the same way as the livestream data.
 
Your script should print to stdout each term-frequency pair, one pair per line, in the following format:
         
          <term:string> <frequency:float>
 
For example, if you have the pair (bar, 0.1245) it should appear in the output as:
 
          bar 0.1245
"""

import sys
import json
import re

# from tweet_sentiment import *

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

def calc_freq(list_of_tweet_text):
    term_freq = {}
    num_all_terms = 0
    for text in list_of_tweet_text:
        # print text.encode('utf-8')
        text = re.sub(r'[^\w@#]', ' ', text) # remove non-english characters
        # print text.encode('utf-8')
        for term in text.split():
            try:
                term_freq[term] += 1
            except KeyError:
                term_freq[term] = 1
            num_all_terms += 1.
    for term in term_freq:
        term_freq[term] = term_freq[term]/num_all_terms
    return term_freq

def main():
    tweet_file = sys.argv[1]
    list_of_tweet_text = get_tweet_text(tweet_file)

    term_freq = calc_freq(list_of_tweet_text)
    for term in term_freq.keys():
        print term.encode('utf-8'), term_freq[term]

if __name__ == '__main__':
    main()

