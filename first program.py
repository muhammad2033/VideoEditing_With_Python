from moviepy.editor import *

# Load the video file
video = VideoFileClip("input_video.mp4")

# Extract audio from the video
audio = video.audio

# Cut the video clip from 0s to 10s
clip = video.subclip(0, 10)

# Add a text title to the clip
txt_clip = TextClip("My Awesome Video", fontsize=50, color='white')
txt_clip = txt_clip.set_pos('center').set_duration(3)
final_clip = CompositeVideoClip([clip, txt_clip])

# Save the final video
final_clip.write_videofile("output_video.mp4", fps=30, codec='mpeg4', audio_codec='aac')
