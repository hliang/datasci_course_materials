"""
happiest_state.py should take a file of tweets as an input and be usable in the following way:
 
          $ python happiest_state.py <sentiment_file> <tweet_file>
 
The file AFINN-111.txt contains a list of pre-computed sentiment score.
 
Assume the tweet file contains data formatted the same way as the livestream data.
 
We recommend that you build on your solution to Problem 2.
 
There are three different objects within the tweet that you can use to determine it's origin.
1      The coordinates object
2      The place object
3      The user object
 
You are free to develop your own strategy for determining the state that each tweet originates from.
 
Limit the tweets you analyze to those in the United States.
"""

import sys
import json

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

def get_state_happiness(dict_of_sent, tweet_file):
    """ read a file containing tweets
    return a list of tweet text contents
    """
    state_happiness = {}
    f = open(tweet_file)
    for thisline in f.readlines():
        # print i, thisline
        thistweet = json.loads(thisline)
        # print thistweet.keys()
        #if "text" in thistweet.keys() and thistweet["entities"]["lang"] == "en": #if the tweet has english text, and not deleted
        if "text" in thistweet.keys() and thistweet['place'] != None : #if the tweet has text, and not deleted, and has "place" info
            if thistweet['place']['country_code'] == 'US' and thistweet['place']['place_type'] == 'city': 
                this_text = thistweet["text"].lower()
                # print this_text.encode('utf-8')
                state = thistweet['place']["full_name"].split()[-1]
                try:
                    state_happiness[state] += sum_sent_score(dict_of_sent, this_text)
                except KeyError:
                    state_happiness[state] = sum_sent_score(dict_of_sent, this_text)
    return state_happiness

def sum_sent_score(dict_of_sent, tweet):
    """
    sum score of sentiment for ONE tweet
    """
    score = 0
    # print t.encode('utf-8')
    thisscore = 0.0
    for word in tweet.split():
        if word.encode('utf-8').lower() in dict_of_sent.keys():
            # print word
            score += dict_of_sent[word.lower()]
    return score

def main():
    # sent_file = open(sys.argv[1])
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]
    # hw()
    # lines(sent_file)
    # lines(tweet_file)
    dict_of_sent = sent_dict(sent_file)
    state_happiness = get_state_happiness(dict_of_sent, tweet_file)

    # print out the state with the highest sentiment score
    the_happiest_state = None
    the_happiest_score = None
    for state in state_happiness:
        if state_happiness[state] > the_happiest_score:
            the_happiest_state, the_happiest_score = state, state_happiness[state]
    print the_happiest_state

if __name__ == '__main__':
    main()

