import os
import shutil
import random
from mutagen.mp3 import MP3

print("🎵 MP3 Selection and Copy Script")

# Prompt user for source and target folders
source_folder = input("📂 Source folder containing MP3 files: ").strip()
target_folder = input("💾 Target folder (e.g., your SD card): ").strip()

# Prompt for maximum duration in minutes (e.g., 7)
max_duration_minutes = input("⏱️ Maximum duration in minutes (e.g., 7): ").strip()
try:
    max_duration = int(max_duration_minutes) * 60
except:
    print("⚠️ Invalid time input. Using default = 7 minutes.")
    max_duration = 7 * 60

# Validate folders
if not os.path.exists(source_folder):
    print(f"❌ Source folder not found: {source_folder}")
    exit()

os.makedirs(target_folder, exist_ok=True)

# Collect and filter MP3 files
all_files = [f for f in os.listdir(source_folder) if f.lower().endswith(".mp3")]
unique_files = list(dict.fromkeys(all_files))

valid_files = []
for f in unique_files:
    try:
        audio = MP3(os.path.join(source_folder, f))
        duration = audio.info.length
        if duration <= max_duration:
            valid_files.append(f)
        else:
            print(f"⏩ Skipped (too long): {f} ({duration/60:.1f} minutes)")
    except Exception as e:
        print(f"⚠️ Error reading file {f}: {e}")

random.shuffle(valid_files)

# Copy files
for i, filename in enumerate(valid_files):
    src_path = os.path.join(source_folder, filename)
    new_filename = f"{i:03d}_{filename}"
    dest_path = os.path.join(target_folder, new_filename)
    shutil.copy2(src_path, dest_path)
    print(f"✅ Copied: {new_filename}")

print(f"🎉 Done! {len(valid_files)} MP3 files were copied.")
