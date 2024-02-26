import subprocess
import re

def get_video_duration(video_path):
    # คำสั่ง FFmpeg เพื่อตรวจสอบรายละเอียดของวิดีโอ
    cmd = ['ffmpeg', '-i', video_path]

    # รันคำสั่ง FFmpeg และจับผลลัพธ์
    process = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    stdout, stderr = process.communicate()

    # ใช้ Regular Expression เพื่อค้นหาระยะเวลาของวิดีโอ
    matches = re.search(r"Duration: (\d{2}):(\d{2}):(\d{2})\.\d{2}", stderr.decode('utf-8'))
    if matches:
        hours, minutes, seconds = map(int, matches.groups())
        total_seconds = hours * 3600 + minutes * 60 + seconds
        return total_seconds
    else:
        return "Duration not found"

# ตัวอย่างการใช้งาน
video_path = 'video_only.mp4'  # แทนที่ด้วยที่อยู่ของไฟล์วิดีโอ
duration = get_video_duration(video_path)
print(f"Duration of the video is: {duration} seconds")
