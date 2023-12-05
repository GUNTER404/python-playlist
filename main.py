import os
import zipfile
import requests
from pytube import Playlist

# Step 1: Download YouTube playlist videos using pytube
def download_yt_playlist(playlist_url):
    playlist = Playlist(playlist_url)
    playlist.populate_video_urls()
    for url in playlist.video_urls:
        video = YouTube(url)
        video.streams.get_highest_resolution().download()

# Step 2: Zip downloaded videos into a zip file
def zip_videos():
    with zipfile.ZipFile("playlist_videos.zip", "w") as zipf:
        for root, _, filenames in os.walk("."):
            for filename in filenames:
                if filename.endswith(".mp4"):
                    zipf.write(os.path.join(root, filename))

# Step 3: Upload the zip file to Anonfiles
def upload_to_anonfiles():
    url = 'https://anonymfile.com/api/v1/upload'
    files = {'file': open('playlist_videos.zip', 'rb')}
    response = requests.post(url, files=files)
    response_data = response.json()
    if response_data['status']:
        print("Upload successful!")
        print("File URL:", response_data['data']['file']['url']['full'])
    else:
        print("Upload failed.")

# Main function
if __name__ == "__main__":
    playlist_url = "https://www.youtube.com/playlist?list=PLMC9KNkIncKvYin_USF1qoJQnIyMAfRxl"
    
    # Step 1: Download YouTube playlist videos
    download_yt_playlist(playlist_url)
    
    # Step 2: Zip downloaded videos 
    zip_videos()
    
    # Step 3: Upload the zip file to Anonfiles
    upload_to_anonfiles()
