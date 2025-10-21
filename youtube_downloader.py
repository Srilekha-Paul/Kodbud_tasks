from pytube import YouTube
import os

def download_video():
    try:
        # Ask for video URL
        url = input("Enter YouTube video URL: ").strip()

        # Fix short URL format if needed
        if "youtu.be/" in url:
            video_id = url.split("/")[-1].split("?")[0]
            url = f"https://www.youtube.com/watch?v={video_id}"

        yt = YouTube(url)

        # Ask for destination folder
        path = input("Enter the destination folder (leave blank for current directory): ").strip()
        if not path:
            path = os.getcwd()
        elif not os.path.exists(path):
            print("⚠️ Folder not found. Saving in current directory instead.")
            path = os.getcwd()

        print(f"\n🎬 Downloading: {yt.title}")
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=path)

        print(f"✅ Download completed! Saved at: {path}")

    except Exception as e:
        print("❌ Error: Invalid link or download failed.")
        print("Details:", e)

# Run program
download_video()
