import sys
import json
import re

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    freq = {}
    total = 0;
    tweetsfile = open(sys.argv[1])
    for line in tweetsfile:
        tj = json.loads(line)
        if 'text' in tj: #is a tweet or not
            tokens = re.split('\W+', tj['text'])
            #iterate token and update freq dict
            for token in tokens:
                if token not in freq:
                    if len(token) > 0:
                        freq[token] = 1
                        total += 1
                else:
                    freq[token] += 1
                    total += 1
    for i in freq:
    	print i, float(freq[i])/total

if __name__ == '__main__':
    main()
