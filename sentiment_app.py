%pip install streamlit
%pip install vaderSentiment

import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load the VADER sentiment analysis model
analyzer = SentimentIntensityAnalyzer()

# Define the app interface
st.title('VADER Sentiment Analysis App')
st.write('Enter the text to analyze sentiment')

# Text input for the model
input_text = st.text_area('Enter text here')

# Button to perform sentiment analysis
if st.button('Analyze'):
    # Use the loaded VADER model to analyze sentiment
    sentiment_score = analyzer.polarity_scores(input_text)
    st.write(f'The sentiment scores are: {sentiment_score}')
