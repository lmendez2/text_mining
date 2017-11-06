from nltk.sentiment.vader import SentimentIntensityAnalyzer
"""
here imported the most common for the astros
"""

astros_MC_words = "amp amp amp amp amp amp amp amp amp amp amp amp amp amp amp amp amp amp amp amp amp amp amp amp amp amp amp amp amp amp amp amp amp amp amp amp amp team team team team team team team team team team team team team team team team team team team team team team team team team team team team team team team team team team team team thing thing thing thing thing thing thing thing thing thing thing thing thing thing thing thing thing thing thing thing thing thing thing thing thing thing thing thing thing thing thing thing thing thing thing meet meet meet meet meet meet meet meet meet meet meet meet meet meet meet meet meet meet meet meet meet meet meet meet meet meet meet meet meet meet meet meet meet meet meet fans fans fans fans fans fans fans fans fans fans fans together together together together together together together together together hat hat hat hat hat hat hat hat hat great great great great great great great great great dropped dropped dropped dropped dropped dropped dropped dropped worked worked worked worked worked worked worked"

score = SentimentIntensityAnalyzer().polarity_scores(astros_MC_words)
print(score)