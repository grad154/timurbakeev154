from moviepy.editor import *
import os

directory = "F:/NewwPy-11.22"
files = os.listdir(directory)
img = list(filter(lambda x: x.endswith(".png"), files))
clips = [ImageClip(m).set_duration(2) for m in img]

final_clip = concatenate_videoclips(clips, method="compose")
final_clip.write_videofile("возможностиНейронки154.mp4", fps = 24)