import ffmpeg
import os

def merge_audio_video(sound1_path, sound2_path, video_path, output_path):
    input_video = ffmpeg.input(video_path, hwaccel='cuvid')
    input_audio1 = ffmpeg.input(sound1_path)
    input_audio2 = ffmpeg.input(sound2_path)

    # Merge two audio tracks and adjust their channels
    merged_audio = ffmpeg.filter([input_audio1, input_audio2], 'amerge', inputs=2)
    stereo_audio = ffmpeg.filter(merged_audio, 'pan', 'stereo|c0<c2|c1<c1')

    # Set the video and audio encoding options
    output = ffmpeg.output(
        input_video, stereo_audio, output_path,
        vcodec='h264_nvenc',  # NVIDIA NVENC H.264 encoder
        preset='medium',
        acodec='aac', audio_bitrate='192k'
    )

    # Run the process
    output.run()

# Directory paths
sound1_dir = 'E:/ffmpeg/Sound1'
sound2_dir = 'E:/ffmpeg/Sound2'
video_dir = 'E:/ffmpeg/Video'
export_dir = 'E:/Export_Music'

# Create export directory if it doesn't exist
if not os.path.exists(export_dir):
    os.makedirs(export_dir)

# Process all files in the directories
for filename in os.listdir(sound1_dir):
    sound1_path = os.path.join(sound1_dir, filename)
    sound2_path = os.path.join(sound2_dir, filename)
    video_path = os.path.join(video_dir, os.path.splitext(filename)[0] + '.mp4')
    output_path = os.path.join(export_dir, os.path.splitext(filename)[0] + '.mp4')

    # Check if all files exist
    if os.path.exists(sound1_path) and os.path.exists(sound2_path) and os.path.exists(video_path):
        merge_audio_video(sound1_path, sound2_path, video_path, output_path)

print("Processing complete!")
