import sys
import json

def main():
  tweetsfile = open(sys.argv[1])
  hashtags={}
  for line in tweetsfile:
    tj = json.loads(line)
    if 'entities' in tj and 'hashtags' in tj['entities']:
      tags = tj['entities']['hashtags']
      for tag in tags :
        name=tag['text']
        if name in hashtags :
          hashtags[name] += 1
        else :
          hashtags[name] = 1
  topten=[]
  for ht in hashtags:
    if len(topten) < 10 :
      topten.append((hashtags[ht], ht))
      continue
    small=min(topten)
    if small[0] < hashtags[ht] :
      topten.remove(small)
      topten.append((hashtags[ht], ht))
  for tt in reversed(sorted(topten)):
    print tt[1], float(tt[0])

if __name__ == '__main__':
    main()