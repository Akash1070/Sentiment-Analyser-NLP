#install libraries: nltk, flask

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


text = "today is a very lucky day"
nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()
score = ((sid.polarity_scores(str(text))))['compound'] #The normalized compound score which calculates the sum of all lexicon ratings and takes values from -1 to 1

if(score > 0):
    label = 'The sentiment in the sentence is positive'
elif(score == 0):
    label = 'The sentiment in the sentence is neutral'
else:
    label = 'The sentiment in the sentence is negative'

print(label)