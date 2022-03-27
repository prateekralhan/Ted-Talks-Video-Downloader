import streamlit as st
from PIL import Image
from app_funcs import *

st.set_page_config(
    page_title="TED Talks Video Downloader",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="auto",
)

main_image = Image.open('static/main_banner.png')

download_path = "downloads/"

st.image(main_image,use_column_width='auto')
st.title("✨ Ted Talks Video Downloader 🎬")
st.error(" 🔴 THIS IS MEANT TO BE USED FOR EDUCATIONAL PURPOSES ONLY!! 🔴")
st.info('⚠ Fetching the Ted Talk video may take several minutes depending on the time duration and size.')

url = st.text_input("Enter your URL: 🔗")
if url and st.button("Fetch Video 🎥"):
    with st.spinner(f"Working... 💫"):
        file_name = fetch_request(url)

    final_video = open(os.path.abspath(os.path.join(download_path,file_name)), 'rb')
    video_bytes = final_video.read()
    print("Opening ",final_video)
    st.markdown("---")
    with open(os.path.abspath(os.path.join(download_path,file_name)), "rb") as file:
        if file_name.endswith('.avi') or file_name.endswith('.AVI'):
            st.success('✅ Your results are ready !! 😲')
            if st.download_button(
                                    label="Download Ted Talk Video 📽",
                                    data=file,
                                    file_name=file_name,
                                    mime='video/x-msvideo'
                                 ):
                download_success()

        if file_name.endswith('.mp4') or file_name.endswith('.MP4'):
            st.success('✅ Your results are ready !! 😲')
            if st.download_button(
                                    label="Download Ted Talk Video 📽",
                                    data=file,
                                    file_name=file_name,
                                    mime='video/mp4'
                                 ):
                download_success()

        if file_name.endswith('.mov') or file_name.endswith('.MOV'):
            st.success('✅ Your results are ready !! 😲')
            if st.download_button(
                                    label="Download Ted Talk Video 📽",
                                    data=file,
                                    file_name=file_name,
                                    mime='video/quicktime'
                                 ):
                download_success()

        if file_name.endswith('.mkv') or file_name.endswith('.MKV'):
            st.success('✅ Your results are ready !! 😲')
            if st.download_button(
                                    label="Download Ted Talk Video 📽",
                                    data=file,
                                    file_name=file_name,
                                    mime='video/x-matroska'
                                 ):
                download_success()
else:
    st.warning('⚠ Please enter the URL! 😯')


st.markdown("<br><hr><center>Made with ❤️ by <a href='mailto:ralhanprateek@gmail.com?subject=Ted Talks Video Downloader WebApp!&body=Please specify the issue you are facing with the app.'><strong>Prateek Ralhan</strong></a></center><hr>", unsafe_allow_html=True)


