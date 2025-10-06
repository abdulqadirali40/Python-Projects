from pytube import YouTube

def download_youtube_video(url, save_path='.'):
    try:
        yt = YouTube(url)
        print(f"Title: {yt.title}")
        print("Downloading...")
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=save_path)
        print(f"Download completed! Saved to {save_path}")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_path = input("Enter the download path (default is current folder): ") or '.'
    download_youtube_video(video_url, download_path)
