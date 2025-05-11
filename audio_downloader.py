import yt_dlp
import os

def download_audio(url, output_folder="downloads", limit=None):
    """Downloads audio from a supported URL and converts it to MP3."""

    os.makedirs(output_folder, exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'noplaylist': False,
        'quiet': False,
        'ignoreerrors': True,
        'keepvideo': False,
    }

    if limit:
        ydl_opts['playlist_items'] = f"1-{limit}"

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    print("🎵 Audio Downloader (for royalty-free or personal sources)")
    link = input("🔗 Enter audio or playlist URL: ").strip()
    folder = input("📁 Target folder (leave empty for 'downloads'): ").strip()
    max_songs = input("🔢 Number of items to download (leave empty for all): ").strip()

    if not folder:
        folder = "downloads"

    limit = int(max_songs) if max_songs.isdigit() else None

    download_audio(link, folder, limit)
    print("✅ Download complete. Files saved in:", os.path.abspath(folder))
