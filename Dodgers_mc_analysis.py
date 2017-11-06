from nltk.sentiment.vader import SentimentIntensityAnalyzer
"""
here imported the most common for the dodgers
"""

dodgers_MC_words = "military military military military military military military military military military military military military military military military military military military military military military military military military military military military military military military military military military draft draft draft draft draft draft draft draft draft draft draft draft draft draft draft draft draft draft draft trump trump trump trump trump trump trump trump trump trump trump trump trump trump trump trump trump today today today today today today today today today today today today today today today today today personnel personnel personnel personnel personnel personnel personnel personnel personnel personnel personnel personnel personnel personnel personnel personnel personnel discovered discovered discovered discovered discovered discovered discovered discovered discovered discovered discovered discovered discovered discovered discovered discovered discovered decided decided decided decided decided decided decided decided decided decided decided decided decided decided decided decided decided lost lost lost lost lost lost lost lost lost lost lost lost lost lost lost lost hitting hitting hitting hitting hitting hitting hitting hitting hitting hitting hitting hitting"

score = SentimentIntensityAnalyzer().polarity_scores(dodgers_MC_words)
print(score)