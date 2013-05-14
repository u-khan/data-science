import sys
import json


def extractText(words):
    '''Extracts text from a tweet, and returns a list of the words'''
    text = words['text'].encode('utf-8')
    output = text.split()
    return output

def formatAfinnWords(afinn):
    '''Takes in AFINN-111.txt file and returns dictionary of words'''
    scores = {}
    for line in afinn:
        term, score = line.split("\t")
        scores[term] = int(score)
    return scores

def findSentiments(word, source):
    ''''Takes word. Returns sentiment of words in AFINN and list of new words.'''

    svalue = 0
    new_words = []
    if word.lower() in source:
        return int(source[word.lower()]), new_words
    else:
        new_words.append(word)
        return svalue, new_words

def update_newwords(nwords, sentiment, new_scores):
    '''Takes in list of new words and updates nscores dict for count, and sentiment sum depending on sentiment (positive or negative)'''

    for item in nwords:
        #If word is in nwords dictionary update values
        if item in new_scores:
            new_scores[item][0] += 1
            new_scores[item][1] = new_scores[item][1] + (sentiment)
        #If word not in nwords then add it and update values
        else:
            new_scores[item] = [1,sentiment]
    return new_scores

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    #AFINN words are in scores dict. New words are in nscores(word, [count, sum of sent])
    afinn = formatAfinnWords(sent_file)
    nscores = {}

    
    #Iterates through each tweet
    for line in tweet_file:
        totalSentiment = 0
        tweet = json.loads(line)
        if "text" in tweet:
            text = extractText(tweet)
            list_of_nwords = []
            #Iterate through words of each tweet
            for item in text:
                word_sent, new_sent = findSentiments(item, afinn)
                totalSentiment = totalSentiment + (word_sent)
                list_of_nwords = list_of_nwords + new_sent
   

            #Update nscores dict
            nscores = update_newwords(list_of_nwords, totalSentiment, nscores)


    #Print out key and score pairs for each pairs
    for key in nscores:
        print str(key) + "\t" + str(float(nscores[key][1])/float(nscores[key][0]))


if __name__ == '__main__':
    main()
