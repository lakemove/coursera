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
        scores[term] = float(score)
    #print scores.items()
    newterm = {}
    tweetsfile = open(sys.argv[2])
    for line2 in tweetsfile:
        tj = json.loads(line2)
        if 'text' in tj: #is a tweet or not
            tokens = re.split('\W+', tj['text'])
            total_score = 0.0
            for token in tokens:
                if token in scores:
                    total_score = total_score + scores[token]
            #got tweet sentiment score, now calc new term score
            for token in tokens:
            	if token not in scores:
            		if token not in newterm:
            			if len(token) > 0:
            				newterm[token] = [total_score, 1];#[score, freq]
            		else:
            			ti = newterm[token];
            			freq = ti[1] + 1;
            			sc = (ti[0] * ti[1] + total_score)/(ti[1] + 1.0)
    for i in newterm:
    	print i, newterm[i][0]

if __name__ == '__main__':
    main()
