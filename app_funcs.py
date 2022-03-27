import requests
from bs4 import BeautifulSoup
import re
import os
import json
import streamlit as st

download_path = "downloads/"

@st.cache(persist=True,allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def download_video(mp4_response, url_content):
    if mp4_response.status_code == 200:
        print("Video fetched 200 OK")
        file_name = url_content.split('/')[-1]
        with open(os.path.abspath(os.path.join(download_path,file_name)),'wb') as f:
            f.write(mp4_response.content)
            print("Video downloaded successfully!")
            return file_name
    else:
        st.error("Oops!😵 Video couldn't be fetched. Please try after sometime.😫")


@st.cache(persist=True,allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def fetch_request(url):
    r = requests.get(url)
    if r.status_code == 200:
        print("API response 200 OK")
        soup = BeautifulSoup(r.content, "html.parser")
        next_data_script = soup.find(id="__NEXT_DATA__")
        player_data = json.loads(next_data_script.string)['props']['pageProps']['videoData']['playerData']
        url_content = json.loads(player_data)['resources']['h264'][0]['file']
        mp4_response = requests.get(url_content)
        file_name = download_video(mp4_response, url_content)
        return file_name
    else:
        st.error("Oops!🤕 Connection couldn't be established. Please try after sometime.🤔")


@st.cache(persist=True,allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def download_success():
    st.balloons()
