import os
import subprocess

# กำหนดโฟลเดอร์ที่มีไฟล์เพลง
source_folder = 'E:/Sound'

# กำหนดโฟลเดอร์สำหรับเก็บไฟล์วิดีโอและเสียงที่แยกออกมา
video_folder = 'E:/ffmpeg/Video'
sound1_folder = 'E:/ffmpeg/Sound1'
sound2_folder = 'E:/ffmpeg/Sound2'

# สร้างโฟลเดอร์ที่จำเป็นถ้ายังไม่มี
os.makedirs(video_folder, exist_ok=True)
os.makedirs(sound1_folder, exist_ok=True)
os.makedirs(sound2_folder, exist_ok=True)

# วนลูปเพื่อแยกวิดีโอและเสียงจากแต่ละไฟล์
for file_name in os.listdir(source_folder):
    if file_name.endswith('.bin'):  # ตรวจสอบนามสกุลไฟล์
        full_path = os.path.join(source_folder, file_name)
        video_path = os.path.join(video_folder, os.path.splitext(file_name)[0] + '.mp4')
        sound1_path = os.path.join(sound1_folder, os.path.splitext(file_name)[0] + '.wav')
        sound2_path = os.path.join(sound2_folder, os.path.splitext(file_name)[0] + '.wav')

        # คำสั่ง FFmpeg สำหรับแยกวิดีโอ
        subprocess.run(f'ffmpeg -i "{full_path}" -an -vcodec copy "{video_path}"')

        # คำสั่ง FFmpeg สำหรับแยกเสียงแทร็กแรก
        subprocess.run(f'ffmpeg -i "{full_path}" -map 0:a:0 -vn -acodec pcm_s16le "{sound1_path}"')

        # คำสั่ง FFmpeg สำหรับแยกเสียงแทร็กที่สอง
        subprocess.run(f'ffmpeg -i "{full_path}" -map 0:a:1 -vn -acodec pcm_s16le "{sound2_path}"')

print("การแยกไฟล์เสร็จสิ้น")
