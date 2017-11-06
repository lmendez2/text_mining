from twython import Twython
import random 
import string

def process_data():
    # Replace the following strings with your own keys and secrets
    TOKEN = '926141030096875520-cPeB28AALjsDqXlrgZFfBP9UmmVJQsl'
    TOKEN_SECRET = 'v5d6uTaXnNYPHNjhgVJBeZ4A77NznKmHwl7qRh9zzvHmw'
    CONSUMER_KEY = '59CIo2eOMd7m8fjXVMHLBLjCY'
    CONSUMER_SECRET = '5tvo8vOrQqX4MYMOaMuiCbj5eBhVv06hIHKJtRMVK8iza77mCM'

    t = Twython(CONSUMER_KEY, CONSUMER_SECRET,
    TOKEN, TOKEN_SECRET)

    data = t.search(q="Dodgers", count=200)
    return data
    

def process_file(data):
    """Makes a histogram that contains the words from a file.
    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
    returns: map from each word to the number of times it appears.
    """
    hist = {}

    for status in data['statuses']:
        line = status['text'].replace("-", " ")
        strippables = string.punctuation + string.whitespace 
        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()
            hist[word] = hist.get(word, 0) + 1 
    return hist

def most_common(hist):
    """Makes a list of word-freq pairs in descending order of frequency.
    hist: map from word to frequency
    returns: list of (frequency, word) pairs
    """
    t = []
    for key, value in hist.items():
        t.append((value, key))

    t.sort()
    t.reverse()
    return t    


def print_most_common(hist, num=50):
    """Prints the most commons words in a histgram and their frequencies.
    hist: histogram (map from word to frequency)
    num: number of words to print
    """
 
    print('The most common words are:')
    for freq, word in t[:num]:
        print(word, '\t', freq)


def main():
    data = process_data()
    hist = process_file(data)
    print(hist)

    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[0:50]: ## getting fifty since most are insignificant to analysis
        print(word, '\t', freq)


if __name__ == '__main__':
    main()