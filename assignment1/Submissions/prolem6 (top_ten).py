import sys
import json


def extractText(words):
    '''Extracts text from a tweet, and returns a list of the words'''
    text = words['text'].encode('utf-8')
    output = text.split()
    return output

def main():

    tweet_file = open(sys.argv[1])
    hash_tags = {}



    #Iterates through each tweet
    for line in tweet_file:
        tweet = json.loads(line)

        #Checks if tweet as 'text' and 'place' keys
        if "text" in tweet:
            tags = tweet["entities"]["hashtags"]

            #Checks if word starts with "#" and adds to hash_tags dict
            for tag in tags:
                if tag["text"] in hash_tags:
                    hash_tags[tag["text"]] += 1
                else:
                    hash_tags[tag["text"]] = 1

    my_list = sorted(hash_tags, key=hash_tags.get, reverse=True)[:10]
    for item in my_list:
        print str(item) + "\t" + str(hash_tags[item])
                    

if __name__ == '__main__':
    main()
