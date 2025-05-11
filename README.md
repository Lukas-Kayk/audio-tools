# Audio Tools – MP3 Downloader & MP3 Filter Copy Script

This project provides two Python scripts designed to simplify the handling of audio files.  
It focuses on **downloading audio from supported sources**, converting them to MP3, and  
**filtering/copying MP3s** to a target directory under defined conditions (e.g., maximum length).

---

## About the Project

The tools were created to streamline the process of downloading audio files  
and preparing curated playlists (e.g., for portable devices or SD cards).  
All scripts are lightweight, command-line based, and rely on widely used Python packages.

---

## Project Goals

- **Audio Downloader**  
  - Download audio files from supported platforms (e.g., Archive.org, personal uploads)  
  - Convert to MP3 format automatically  
  - Ensure compatibility across players  

- **Filter & Copy Tool**  
  - Copy only files shorter than a defined maximum duration (e.g., < 7 minutes)  
  - Shuffle files and rename them to a standardized format (`000_filename.mp3`)  
  - Prepare ready-to-use playlists for external storage (e.g., SD card)  

---

## Repository Structure

```plaintext
audio-tools/
├── audio_downloader.py    # Download & convert audio to MP3
├── copy_files.py          # Filter and copy MP3 files
├── requirements.txt       # Required Python packages
└── README.md              # Project documentation
```

---

## Requirements

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) – for downloading and converting  
- [mutagen](https://mutagen.readthedocs.io/) – for reading audio metadata  
- [`ffmpeg`](https://ffmpeg.org/) – must be installed and available in the system PATH  

Install all required packages (recommended in a virtual environment):

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## Usage

### 1. Download MP3s

```bash
python audio_downloader.py
```

- Enter a URL to the audio source or playlist  
- Choose a download folder  
- Optionally limit the number of items to download  

---

### 2. Filter and Copy MP3s

```bash
python copy_files.py
```

- Enter the folder containing your MP3 files  
- Choose a target folder (e.g., SD card)  
- Set the maximum duration in minutes  

The script will:  
- Read the duration of each MP3 file  
- Skip files that are too long  
- Rename files to `000_filename.mp3` format  
- Copy them in random order  

---

## Results

- Automated audio downloads and format conversion  
- Playlist curation with consistent duration constraints  
- Simplified transfer to external storage  

---

## Documentation

- [`audio_downloader.py`](audio_downloader.py) – Script for downloading and converting audio  
- [`copy_files.py`](copy_files.py) – Script for filtering and copying MP3s  
- [`requirements.txt`](requirements.txt) – Dependencies list  

---

## Portfolio Value

This project demonstrates skills in:  
- Python scripting for file handling  
- Metadata processing with external libraries  
- Integration of command-line tools (`yt-dlp`, `ffmpeg`)  
- Automating workflows for media preparation  

---

## License

This project is released without any restrictions.  
You are free to use, modify, and share the code for any purpose.  
No attribution is required.
