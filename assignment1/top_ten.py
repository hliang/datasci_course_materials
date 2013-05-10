"""
Write a Python script, top_ten.py, that computes the ten most frequently occurring hash tags from the data you gathered in Problem 1.
 
top_ten.py should take a file of tweets as an input and be usable in the following way:
 
          $ python top_ten.py <tweet_file>
 
Assume the tweet file contains data formatted the same way as the livestream data.
In the tweet file, each line is a Tweet object, as described in the twitter documentation.
You should not be parsing the "text" field.
 
Your script should print to stdout each hashtag-count pair, one per line, in the following format:
         
          <hashtag:string> <count:float>
 
For example, if you have the pair (baz, 30) it should appear in the output as:
 
          baz 30.0
 
Remember your output must contain floats, not ints.
"""

import sys
import json
import re

def get_hashtag_counts(infile):
    """ read a file containing tweet stream,
    return a dict of {hashtag:count}
    """
    hashtag_counts = {}
    f = open(infile)
    # i = 0
    for thisline in f.readlines():
        # print i, thisline
        thistweet = json.loads(thisline)
        if 'entities' in thistweet.keys():
            for ht in thistweet['entities']['hashtags']: # hashtags is a list
                # print ht['text'].encode('utf-8')
                try:
                    hashtag_counts[ht['text']] += 1.0
                except KeyError:
                    hashtag_counts[ht['text']] = 1.0
    return hashtag_counts

def sort_by_value(in_dict):
    """
    input dict of {word:count}
    get list of the words in order of frequency.
    the sort function iterates over the dictionary keys, using as sort-key the number of word occurrences.
    return a list of tuple pairs [(word, count), (word, count), ...  ]
    """
    result = []
    for word in sorted(in_dict, key=in_dict.get, reverse=True):
        result.append((word, in_dict[word]))
    return result

def main():
    tweet_file = sys.argv[1]
    hashtag_counts = get_hashtag_counts(tweet_file)
    # return top 10 most frequent hashtags
    for ht, count in sort_by_value(hashtag_counts)[0:10]:
        print ht.encode('utf-8'), count

if __name__ == '__main__':
    main()

