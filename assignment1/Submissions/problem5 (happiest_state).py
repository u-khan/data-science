import sys
import json

def formatAfinnWords(afinn):
    '''Takes in AFINN-111.txt file and returns dictionary of words'''
    scores = {}
    for line in afinn:
        term, score = line.split("\t")
        scores[term] = int(score)
    return scores

def extractText(words):
    '''Extracts text from a tweet, and returns a list of the words'''
    text = words['text'].encode('utf-8')
    output = text.split()
    return output

def findSentiments(word, source):
    ''''Takes word. Returns sentiment of words in AFINN and list of new words.'''

    svalue = 0
    if word.lower() in source:
        return int(source[word.lower()])
    else:
        return svalue

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    #AFINN words are in scores dict. New words are in nscores(word, [count, sum of sent])
    scores = formatAfinnWords(sent_file)
    states = {}

    #Iterates through each tweet
    for line in tweet_file:
        total_sentiment = 0
        tweet = json.loads(line)

        #Checks if tweet as 'text' and 'place' keys
        if ("text" in tweet) and (tweet["place"] != None):

            #Checks if tweet's place's "country_code" is 'US'
            if tweet["place"]["country_code"] == "US":
                text = extractText(tweet)

                #Iterate through words of each tweet
                for word in text:
                    item_sent = findSentiments(word, scores)
                    total_sentiment = total_sentiment + (item_sent)

                if tweet["place"]["full_name"] in states:
                    states[tweet["place"]["full_name"]] += total_sentiment
                else:
                    states[tweet["place"]["full_name"]] = total_sentiment

    highest_value_key = max(states.iterkeys(), key=(lambda key: states[key]))
    print highest_value_key.split(", ")[-1]
    

if __name__ == '__main__':
    main()
