# Converts the videos to mp3 
import os 
import subprocess
files = os.listdir("2pointer_Sliding") 
for file in files: 
    if not file.endswith(".mp4"):
        continue
 # Expected format: "01 - Title ｜ Suffix.mp4"
    parts = file.split(" - ")
    if len(parts) > 1:
        tutorial_number = parts[0]
        # Extract title, removing suffix if present
        remainder = parts[1]
        file_name = remainder.split(" ｜ ")[0].replace(".mp4", "")
        print(tutorial_number, file_name)
        subprocess.run(["ffmpeg", "-y", "-i", f"2pointer_Sliding/{file}", f"audios/{tutorial_number} {file_name}.mp3"])
    else:
        print(f"Skipping file with unexpected format: {file}")