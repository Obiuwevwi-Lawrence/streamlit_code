import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import assemblyai

# Set up AssemblyAI API key
assemblyai.settings.api_key = "4342dd3e0a584dc1a279b412ac509b98"

def main():
    st.title("Audio Transcription and Word Cloud Generation")

    # Upload audio file
    uploaded_file = st.file_uploader("Upload an audio file", type=['mp3', 'wav'])

    if uploaded_file:
        # Transcribe audio file
        transcript = assemblyai.transcribe_file(uploaded_file)

        # Extract text from the transcript
        transcription_text = transcript['text']

        # Generate word cloud
        st.subheader("Transcription Word Cloud")
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(transcription_text)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        st.pyplot()

if __name__ == '__main__':
    main()


