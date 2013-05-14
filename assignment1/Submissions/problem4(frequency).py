import sys
import json

def extractText(words):
    '''Extracts text from a tweet, and returns a list of the words'''
    text = words['text'].encode('utf-8')
    output = text.split()
    return output

def main():
    tweet_file = open(sys.argv[1])

    total_num_words = 0
    word_frequency = {}

    #Iterates through each tweet
    for line in tweet_file:
        tweet = json.loads(line)

        #Check if tweet has 'text' key
        if "text" in tweet:
            text = extractText(tweet)
            total_num_words += len(text)

            for word in text:
                if word in word_frequency:
                    word_frequency[word] += 1
                else:
                    word_frequency[word] = 1
    #Print each (key, frequency) pair
    for key in word_frequency:
        key_frequency = float(word_frequency[key]) / float(total_num_words)
        print str(key) + "\t" + str(key_frequency)


if __name__ == '__main__':
    main()
