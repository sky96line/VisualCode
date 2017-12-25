from textblob import TextBlob

text = "What am i are you dooing here?"

blob = TextBlob(text)


ans = blob.tokenize()
print ans
'''
t = blob.correct()
print t

word = blob.words
print word

word = blob.word_counts
print word

for every in blob.sentiment_assessments:
  print every
'''

snt = blob.sentiment.polarity
print snt
