import sqlite3
import subprocess
import os
import re

def get_media_duration(file_path):
    cmd = ['ffmpeg', '-i', file_path]
    process = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    stdout, stderr = process.communicate()

    matches = re.search(r"Duration: (\d{2}):(\d{2}):(\d{2})\.\d{2}", stderr.decode('utf-8'))
    if matches:
        hours, minutes, seconds = map(int, matches.groups())
        return hours * 3600 + minutes * 60 + seconds
    return None

def extract_audio(video_path, audio_output_path):
    try:
        cmd = ['ffmpeg', '-i', video_path, '-vn', '-acodec', 'pcm_s16le', '-ar', '44100', '-ac', '2', audio_output_path]
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError:
        return False
    return True

db_path = 'Music_Database.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("SELECT filepath FROM tbfiles WHERE vdo_length IS NULL OR sound_length IS NULL")
rows = cursor.fetchall()

for row in rows:
    video_path = row[0]
    audio_path = "temp_audio.wav"

    video_duration = get_media_duration(video_path)

    if extract_audio(video_path, audio_path):
        audio_duration = get_media_duration(audio_path)
        os.remove(audio_path)  # Only remove if extraction was successful
    else:
        audio_duration = None  # Set to None if extraction failed

    cursor.execute("UPDATE tbfiles SET vdo_length = ?, sound_length = ? WHERE filepath = ?", (video_duration, audio_duration, video_path))
    conn.commit()

conn.close()