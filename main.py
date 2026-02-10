from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()
text = "VADER is smart, handsome, and funny."
score = analyser.polarity_scores(text)
print(score)
print("Compound", score['compound'])
if score['compound'] >= 0.05:
    label = ("Positive")
elif score['compound'] <= -0.05:
    label = ("Negative")
else:
    label = ("Neutral")

print("Final label: ", label)





