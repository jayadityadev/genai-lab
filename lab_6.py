from transformers import pipeline

sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    """Analyze sentiment of the input test using HuggingFace pipeline."""
    result = sentiment_analyzer(text)
    label = result[0]['label']
    score = result[0]['score']
    return f"Sentiment: {label}, Confidence Score: {score:.2f}"


while True:
    user_input = input("Enter a sentence to analyze (or 'exit' to quit): ").strip()
    if user_input.lower() == 'exit':
        break
    sentiment_result = analyze_sentiment(user_input)
    print(sentiment_result)