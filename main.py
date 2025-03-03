from io import BytesIO
import streamlit as st
import datetime
from pytubefix import YouTube

st.title("Youtube Downloder")
st.session_state['URL'] = ("")
dt_now = datetime.datetime.now()

@st.cache_data(show_spinner=False)
def download_audio_to_buffer(url):
    buffer = BytesIO()
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    video.stream_to_buffer(buffer)
    return buffer

def main():
    url = st.text_input("Insert Youtube URL:")
    if url:
        with st.spinner("Downloading Audio Stream from Youtube..."):
            buffer = download_audio_to_buffer(url)
        st.subheader("Download!!")
        st.download_button(
            label="Download mp3",
            data=buffer,
            file_name=str(dt_now) + ".mp3",
            mime="video/mp3")

if __name__ == "__main__":
    main()
