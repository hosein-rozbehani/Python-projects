import os
from moviepy.editor import *

os.system(command="cls")

filename = "khandeh.mp4"

movie = VideoFileClip(filename=filename)

audio = movie.audio
audio.write_audiofile(filename="khandeh.mp3")

audio.close()
movie.close()