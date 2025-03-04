from io import BytesIO
import streamlit as st
import datetime
from pytubefix import YouTube

st.title("Youtubeダウンローダー")
dt_now = datetime.datetime.now()

@st.cache_data(show_spinner=False)
def download_audio_to_buffer(url):
    buffer = BytesIO()
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    video.stream_to_buffer(buffer)
    return buffer

def main():
    url = st.text_input("YoutubeのURLを入力してください:")
    if url:
        with st.expander("ダウンロードオプション"):
            form = st.selectbox(
                'ダウンロード形式を選択',
                ['mp3','mp4'],
                index = 1
            )
        with st.spinner("準備中..."):
            buffer = download_audio_to_buffer(url)
        st.download_button(
            label="ダウンロード！！",
            data=buffer,
            file_name=str(dt_now) + "." +form,
            mime="video/" + "form")

if __name__ == "__main__":
    main()
