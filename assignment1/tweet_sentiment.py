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
                thisscore += dict_of_sent[word]
        scores.append(thisscore)
    return scores

def main():
    # sent_file = open(sys.argv[1])
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]
    # hw()
    # lines(sent_file)
    # lines(tweet_file)
    dict_of_sent = sent_dict(sent_file)
    list_of_tweet_text = get_tweet_text(tweet_file)
    scores = sum_sent_score(dict_of_sent, list_of_tweet_text)
    for thisscore in scores:
        print thisscore

if __name__ == '__main__':
    main()

