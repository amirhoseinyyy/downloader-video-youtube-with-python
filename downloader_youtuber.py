import yt_dlp
def download_video(url):
    ydl_opts = {
    'format': 'bestvideo',  
    'noplaylist':True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl :
        ydl.download([url])
if __name__ == "__main__":
    video_url = input("enter your video url : ")
    download_video(video_url)