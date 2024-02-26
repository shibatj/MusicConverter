import subprocess
import re

def get_audio_duration(file_path):
    # คำสั่ง FFmpeg เพื่อตรวจสอบรายละเอียดของเสียงหรือวิดีโอ
    cmd = ['ffmpeg', '-i', file_path]

    # รันคำสั่ง FFmpeg และจับผลลัพธ์
    process = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    stdout, stderr = process.communicate()

    # ใช้ Regular Expression เพื่อค้นหาระยะเวลาของไฟล์
    matches = re.search(r"Duration: (\d{2}):(\d{2}):(\d{2})\.\d{2}", stderr.decode('utf-8'))
    if matches:
        hours, minutes, seconds = map(int, matches.groups())
        total_seconds = hours * 3600 + minutes * 60 + seconds
        return total_seconds
    else:
        return "Duration not found"

# ตัวอย่างการใช้งาน
file_path = 'audio_track1.mp3'  # แทนที่ด้วยที่อยู่ของไฟล์เสียงหรือวิดีโอ
duration = get_audio_duration(file_path)
print(f"Duration of the audio is: {duration} seconds")
