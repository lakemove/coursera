import sys
import json
import re

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    afinnfile = open(sys.argv[1])
    scores = {}
    for line in afinnfile:
        term, score = line.split("\t")
        scores[term] = int(score)
    #print scores.items()
    tweetsfile = open(sys.argv[2])
    for line2 in tweetsfile:
        tj = json.loads(line2)
        if 'text' in tj: #is a tweet or not
            tokens = re.split('\W+', tj['text'])
            total_score = 0
            for token in tokens:
                if token in scores:
                    total_score = total_score + scores[token]
            print total_score

if __name__ == '__main__':
    main()
