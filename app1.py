import streamlit as st
from gtts import gTTS
import os # file handling
import base64

def text_to_speech(text, lang='en'):
    tts = gTTS(text, lang=lang)
    tts.save("output.mp3")
    return "output.mp3"

def get_audio_download_link(file_path):
    with open(file_path,"rb") as f:
        data=f.read()
        b64 = base64.b64encode(data).decode()
        href = f'<a href="data:audio/mp3;base64,{b64}" download="speech.mp3">🔊 Download Audio</a>'
        return href
    
# creating a streamlit ui 
st.set_page_config(page_title="Text to Speech App", page_icon="🗣️")
st.title("🗣️ Text-to-Speech Web App")
st.markdown("Convert your text into speech using Google TTS (gTTS)")

text_input = st.text_area("Enter text here", placeholder="Type something...")

if st.button("🔊 Convert to Speech"):
    if text_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        audio_file = text_to_speech(text_input)
        audio_bytes = open(audio_file, 'rb').read()
        st.audio(audio_bytes, format='audio/mp3')
        st.markdown(get_audio_download_link(audio_file), unsafe_allow_html=True)
