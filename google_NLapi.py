# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import os

# Setting the Google API Credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "..."

# Instantiates a client
client = language.LanguageServiceClient()

def analyze_sentiment(t):
    text = t
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    sentis = [sentiment.score, sentiment.magnitude]
    return sentis