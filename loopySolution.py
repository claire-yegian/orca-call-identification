#!usr/local/bin/python
# CREDIT: https://programmerblog.net/join-wav-audio-files-using-python/
# CREDIT: https://bbc.github.io/bbcat-orchestration-docs/installation-mac-manual/
# CREDIT: https://www.ffmpeg.org/download.html

# Useful AudioSegment APIs
# https://github.com/jiaaro/pydub
# https://github.com/jiaaro/pydub/blob/master/API.markdown

import glob
import sys
import os

from pydub import AudioSegment

dirpathVocals = "Orchive/vocals/"
dirpathNoise = "Noise from Water/"
dirpathNewVocals = "Orchive/newVocalsLooped/"

# addon = AudioSegment.from_wav(dirpathNoise + "water_noise.wav") # the water noise to pad each file with
# list of all files in the directory
filenames = glob.glob(dirpathVocals+'*.wav')

# for filename in filenames:
#     file = os.path.split(filename)[1]  # grab the filename without the path
#     # remove the .wav extension because we'll add "-NewLooped.wav" when we export
#     file = file[:-4]
#     original = AudioSegment.from_wav(filename)
#     addon = original[9:]
#     filenames_combined = [original, addon]
#     combined = AudioSegment.empty()
#     combined += original
#     for i in range(33):
#         combined += addon
#     combined_clipped = combined[:4000]  # take first 4 seconds
#     combined_clipped.export(dirpathNewVocals + file +
#                             "-NewLooped.wav", format="wav")

original = AudioSegment.from_wav(dirpathVocals+"A08-N17-082010-D072-14804.wav")
print(len(original))
addon = original[-200:][:150]
addon2 = addon.reverse()
combined = AudioSegment.empty()
combined = original + addon2 + addon
combined.export(dirpathNewVocals+"loopedExample.wav", format="wav")

awesome = combined.fade_out(400)
awesome.export(dirpathNewVocals+"fadedLoopedEx.wav", format="wav")
