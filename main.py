from io import BytesIO
import streamlit as st
import datetime
from pytubefix import YouTube

st.title("Youtube Downloder")
st.session_state['URL'] = ("")
dt_now = datetime.datetime.now()

url = st.text_input('input any youtube URL')

if url:
    buffer = BytesIO
    st.session_state.URL = (url)
    yt = YouTube(st.session_state.URL)
    video = yt.streams.get_highest_resolution()
    video.stream_to_buffer(buffer)

st.download_button(
    label="Download!!",
    data=buffer,
    file_name=str(dt_now),
    mine="video"
)
    

st.write(st.session_state.URL)
