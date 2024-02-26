import subprocess

# ตั้งชื่อไฟล์วิดีโอที่คุณต้องการแยกเสียง
video_file = "800002.mpg"

# ตั้งชื่อไฟล์สำหรับแต่ละ track เสียงที่จะถูกแยกออกมา
audio_track1 = "audio_track1.mp3"
audio_track2 = "audio_track2.mp3"

# คำสั่ง FFmpeg สำหรับแยก track เสียงแรก
command1 = f"ffmpeg -i {video_file} -map 0:a:0  -c copy {audio_track1}"

# คำสั่ง FFmpeg สำหรับแยก track เสียงที่สอง
command2 = f"ffmpeg -i {video_file} -map 0:a:1 -c copy {audio_track2}"

# รันคำสั่ง
subprocess.call(command1, shell=True)
subprocess.call(command2, shell=True)