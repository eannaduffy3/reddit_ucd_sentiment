# UCD Reddit Sentiment Analysis

A Python project that analyses the sentiment of discussions within
the r/UCD subreddit.

## Overview

The project retrieves posts from r/UCD and applies VADER sentiment
analysis to classify discussions as positive, neutral or negative.

Post information and sentiment results are structured using pandas
and exported to CSV for further analysis.

## Technologies

- Python
- pandas
- PRAW
- VADER Sentiment Analysis

## How It Works

1. Retrieves up to 100 hot posts from the r/UCD subreddit using PRAW.
2. Combines each post's title and text.
3. Applies VADER sentiment analysis to calculate negative, neutral,
   positive and compound sentiment scores.
4. Classifies each post as:
   - Positive: compound score >= 0.05
   - Negative: compound score <= -0.05
   - Neutral: compound score between -0.05 and 0.05
5. Stores post information, engagement metrics and sentiment scores
   in a pandas DataFrame.
6. Exports the results to a CSV file.

## Output

The resulting dataset includes:

- Post title and text
- Upvote score
- Number of comments
- Negative sentiment score
- Neutral sentiment score
- Positive sentiment score
- Compound sentiment score
- Sentiment classification

## Skills Demonstrated

- Python
- API data collection
- Data manipulation with pandas
- Natural language processing
- Sentiment analysis
- Data export and structuring
