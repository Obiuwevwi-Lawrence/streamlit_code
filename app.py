import streamlit as st
import assemblyai

# Set up AssemblyAI API key
assemblyai.settings.api_key = "4342dd3e0a584dc1a279b412ac509b98"

def main():
    st.title("Audio Transcription and Speaker Diarization")

    # Upload audio file
    uploaded_file = st.file_uploader("Upload an audio file", type=['mp3', 'wav'])

    if uploaded_file:
        # Transcribe audio file
        transcript = assemblyai.transcribe_file(uploaded_file, speaker_labels=True)

        # Display transcription
        st.subheader("Transcription:")
        st.write(transcript['text'])

        # Display speaker diarization
        st.subheader("Speaker Diarization:")
        for speaker_label in transcript['speaker_labels']:
            st.write(f"Speaker {speaker_label['speaker']} - {speaker_label['text']}")

if __name__ == '__main__':
    main()
