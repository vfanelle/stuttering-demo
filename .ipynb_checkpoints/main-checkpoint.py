import streamlit as st
import pandas as pd
import soundfile as sf
import numpy as np
import io

st.set_page_config(layout="wide")

# Function to load audio file
def load_audio(file):
    try:
        data, samplerate = sf.read(file)
        return data, samplerate
    except Exception as e:
        st.error(f"Error loading audio file: {e}")
        return None, None

# Demo data (you can replace these with your actual data)
audio_file = '/nobackup-fast/jirayu/wow/5678-43303-0036.flac'
groundtruth_transcript = "I'm back all is well now listen can you hear yes the best has happened it is all over in the East felsenburgh has done it now listen I cannot come home tonight it will be announced in Paul's house in 2 hours from now"
wav2vec_transcript = "I AM BACK ALL AS WELL NOW LISTEN I WELL NOW LISTEN WELL NOW LISTEN CAN YOU HEAR YES YES THE BEST HAS HAPPENED IT IS IIS ALL OVER IN THE EAST FELSENBURGH HAS DONE IT NOW LISTEN I CANNOT COME HOME TO NIGHT IT WILL WILL WILL BE ANNOUNCED IN PAUL'S HOUSE IN TWO HOURS FROM NOW"
whisper_transcript = "I'm back all as well. Now listen. Well, now listen. Well, now listen. Can you hear? Yes, yes. The best has happened. It is I'm is all over in the east. Thelsonburg has done it. Now listen, I cannot come home tonight. It will will be announced in Paul's house in two hours from now."
whispering_llama_transcript = "I'm back all as well. Now listen. Well, now listen. Well, now listen. Can you hear? Yes, yes. The best has happened. It is I'm is all over in the east. Thelsonburg has done it. Now listen, I cannot come home tonight. It will will be announced in Paul's house in two hours from now."
ours_transcript = "I'm back all is well now listen can you hear yes the best has happened it is all over in the East felsenburgh has done it now listen I cannot come home tonight it will be announced in Paul's house in 2 hours from now"

# Streamlit app
st.title("Stuttered Speech Recognition Demo")

# Audio Playback
st.header("Audio Playback")
audio_data, audio_samplerate = load_audio(audio_file)
if audio_data is not None:
    st.audio(audio_file, format='audio/wav')

# Transcriptions
st.header("Transcriptions")
transcriptions = {
    "Groundtruth": groundtruth_transcript,
    "Wav2Vec": wav2vec_transcript,
    "Whisper": whisper_transcript,
    "Whispering Llama": whispering_llama_transcript,
    "Ours": ours_transcript,
}

for name, transcript in transcriptions.items():
    st.info(f"**{name}**\n\n{transcript}")
