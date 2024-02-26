import subprocess
import re
import sqlite3

def get_media_duration(file_path):
    cmd = ['ffmpeg', '-i', file_path]
    process = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    stdout, stderr = process.communicate()

    matches = re.search(r"Duration: (\d{2}):(\d{2}):(\d{2})\.\d{2}", stderr.decode('utf-8'))
    if matches:
        hours, minutes, seconds = map(int, matches.groups())
        total_seconds = hours * 3600 + minutes * 60 + seconds
        return total_seconds
    else:
        return None

def insert_into_database(id_music, use_status):
    conn = sqlite3.connect('Music_Database.db')
    cursor = conn.cursor()

    # Ensure the table exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usageData (
            ID_Music INTEGER PRIMARY KEY,
            Use INTEGER,
            NotUse INTEGER,
            status TEXT CHECK( status IN ('Use','NotUse') )
        )
    ''')

    status = 'Use' if use_status else 'NotUse'
    cursor.execute('''
        INSERT INTO usageData (ID_Music, Use, NotUse, status)
        VALUES (?, ?, ?, ?)
    ''', (id_music, int(use_status), int(not use_status), status))

    conn.commit()
    conn.close()

video_path = 'VDO/video_only.mp4'  # ที่อยู่ของไฟล์วิดีโอ
audio_paths = ['Sounds/audio_track1_1.wav']  # รายการของไฟล์เสียง

video_duration = get_media_duration(video_path)

for idx, audio_path in enumerate(audio_paths, start=1):
    audio_duration = get_media_duration(audio_path)

    if video_duration is None or audio_duration is None:
        print(f"NoFile for {audio_path}")
    else:
        use_status = video_duration == audio_duration
        insert_into_database(idx, use_status)
        if use_status:
            print(f"Use: {audio_path} - {audio_duration} Sec")
        else:
            print(f"NotUse: {audio_path} - Video: {video_duration} Sec, Audio: {audio_duration} Sec")