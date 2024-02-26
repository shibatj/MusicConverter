import subprocess

# ตั้งชื่อไฟล์สำหรับแต่ละส่วน
video_only = "video_only.mp4"
audio_track1 = "audio_track1.mp3"  # เสียงลำโพงด้านขวา
audio_track2 = "audio_track2.mp3"  # เสียงลำโพงด้านซ้าย
output_file = "test.mp4"

# คำสั่ง FFmpeg สำหรับรวมเสียงและวิดีโอ เสียง track1 อยู่ด้านขวา และ track2 อยู่ด้านซ้าย
# และ compress วิดีโอ
command = (
    f"ffmpeg -i {video_only} "
    f"-i {audio_track1} -i {audio_track2} "
    f"-filter_complex \"[1:a][2:a]amerge=inputs=2,pan=stereo|c0<c2|c1<c1[a]\" "
    f"-map 0:v -map \"[a]\" "
    f"-c:v libx264 -crf 23 -preset medium "
    f"-c:a aac -b:a 192k "
    f"{output_file}"
)

# รันคำสั่ง
subprocess.call(command, shell=True)
