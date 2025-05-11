# Audio Tools (MP3 Downloader + MP3 Filter Copy Script)

This project includes two Python scripts for working with audio files:

1. 🎧 **audio_downloader.py**  
   Downloads audio files from supported platforms (e.g., Archive.org, personal uploads) and converts them to MP3.

2. 💾 **copy_files.py**  
   Copies MP3 files from a source folder to a target folder (e.g., SD card), **only if they are shorter than a specified duration** (e.g., less than 7 minutes). Files are renamed and shuffled.

---

## 🛠️ Requirements

- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [mutagen](https://mutagen.readthedocs.io/)
- `ffmpeg` must be installed and available in the system PATH

Install required packages (recommended in a virtual environment):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## ▶️ Usage

### 1. Download MP3s

```bash
python audio_downloader.py
```

- Enter a URL to the audio source or playlist
- Choose a download folder
- Optionally limit the number of items to download

⚠️ **For royalty-free or legally allowed content only.**

---

### 2. Filter and Copy MP3s

```bash
python copy_files.py
```

- Enter the folder containing your MP3 files
- Choose a target folder (e.g., your SD card)
- Set the maximum duration in minutes for allowed MP3 files

The script will:
- read the duration of each MP3 file
- skip files that are too long
- rename files to `000_filename.mp3` format
- copy them in random order

---

## ⚖️ Legal Notice

This tool is intended **only for use with free, legal content**.  
It **does not bypass copy protection** and must **not be used for copyright infringement**.

---

Created to simplify audio handling and personal backups. Enjoy!
