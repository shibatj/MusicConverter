import subprocess

# ตั้งชื่อไฟล์วิดีโอที่คุณต้องการแยกเสียงและวิดีโอ
video_file = "800002.bin"

# ตั้งชื่อไฟล์สำหรับแต่ละ track เสียงที่จะถูกแยกออกมา
audio_track1 = "audio_track1.wav"
audio_track2 = "audio_track2.wav"

# ตั้งชื่อไฟล์สำหรับวิดีโอที่ไม่มีเสียง
video_only = "video_only.mp4"

# คำสั่ง FFmpeg สำหรับแยก track เสียงแรกเป็น WAV
command1 = f"ffmpeg -i {video_file} -map 0:a:0 -c:a pcm_s16le -vn {audio_track1}"

# คำสั่ง FFmpeg สำหรับแยก track เสียงที่สองเป็น WAV
command2 = f"ffmpeg -i {video_file} -map 0:a:1 -c:a pcm_s16le -vn {audio_track2}"
# คำสั่ง FFmpeg สำหรับแยกวิดีโอโดยไม่มีเสียง
# command3 = f"ffmpeg -i {video_file} -c:v copy -an {video_only}"
command3 = f"ffmpeg -i {video_file} -c:v libx264 -crf 23 -preset medium -an {video_only}"

# รันคำสั่ง
subprocess.call(command1, shell=True)
subprocess.call(command2, shell=True)
subprocess.call(command3, shell=True)