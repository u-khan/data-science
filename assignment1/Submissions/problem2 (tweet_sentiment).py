import sys
import json


def extract_text(words):
    '''Extracts text from a tweet, lowercases it, and returns a list of the words'''
    text = words['text'].encode('utf-8')
    ltext = text.lower()
    output = ltext.split()
    return output

def find_sentiment(word, source):
    ''''Takes a word and returns matching sentiment value from source file as int'''
    svalue = 0
    source.seek(0)
    for line in source:
        sword = line.split()
        if word == sword[0]:
            return int(sword[1])
    return int(svalue)

def main():
    sent_file = open(sys.argv[1], 'r')
    tweet_file = open(sys.argv[2], 'r')
    
    #Iterate through each tweet
    for line in tweet_file:
        total_sentiment = 0
        tweet = json.loads(line)
        text = extract_text(tweet)
        
        #Iterate through words of each tweet
        for item in text:
            item_sentiment = find_sentiment(item, sent_file)
            total_sentiment = total_sentiment + (item_sentiment)

        #Print Tweet sentiment value
        print total_sentiment



if __name__ == '__main__':
    main()
