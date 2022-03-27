# ✨ Ted Talks Video Downloader 🎬 [![Project Status: Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active) [![](https://img.shields.io/badge/Prateek-Ralhan-brightgreen.svg?colorB=ff0000)](https://prateekralhan.github.io/)

A streamlit based webapp to download Ted Talks from their [official website](https://www.ted.com/).

### 🔴 THIS IS MEANT TO BE USED FOR EDUCATIONAL PURPOSES ONLY !! 🔴

## Installation:
* Simply run the command ***pip install -r requirements.txt*** to install the necessary dependencies.

## Usage:
1. Clone this repository and install the dependencies as mentioned above.
2. Make a directory within this cloned repository with the name `.streamlit` *(Don't forget the dot !!)*.
3. Create a file `config.toml` in this directory *(Be aware of the file extension !!)*.
4. Copy-Paste the following contents in this file and save :
```
[theme]
primaryColor="#5ff700"
backgroundColor="#000000"
secondaryBackgroundColor="#353737"
textColor="#40f593"
```

5. Navigate to the root directory of this repository and simply run the command: 
```
streamlit run app.py
```
Navigate to http://localhost:8501 in your web-browser.

![1](https://user-images.githubusercontent.com/29462447/160292672-12ca7d93-4fe6-4146-83ee-208a5789c238.png)
![2](https://user-images.githubusercontent.com/29462447/160292666-4972e646-1e86-4202-878d-e72cf15e3fd0.png)
![3](https://user-images.githubusercontent.com/29462447/160292670-e386d703-b27a-4775-ad9e-465992a70568.png)


### Running the Dockerized App
1. Ensure you have Docker Installed and Setup in your OS (Windows/Mac/Linux). For detailed Instructions, please refer [this.](https://docs.docker.com/engine/install/)
2. Navigate to the folder where you have cloned this repository ( where the ***Dockerfile*** is present ).
3. Build the Docker Image (don't forget the dot!! :smile: ): 
```
docker build -f Dockerfile -t app:latest .
```
4. Run the docker:
```
docker run -p 8501:8501 app:latest
```

This will launch the dockerized app. Navigate to ***http://localhost:8501/*** in your browser to have a look at your application. You can check the status of your all available running dockers by:
```
docker ps
```
