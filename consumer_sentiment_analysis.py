from textblob import TextBlob
import json

def perform_sentiment_analysis(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0:
        return "Positive"
    elif sentiment_score < 0:
        return "Negative"
    else:
        return "Neutral"

def analyze_sentiment_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                data = json.loads(line)
                if 'category' in data:
                    text_data = ' '.join(data['category'])  
                    print("Text Data:", text_data)
                    sentiment = perform_sentiment_analysis(text_data)
                    print("Sentiment:", sentiment)
            except json.JSONDecodeError as e:
                print("Error decoding JSON:", e)

if __name__ == '__main__':
    file_path = 'Category_Only.json'
    analyze_sentiment_from_file(file_path)
