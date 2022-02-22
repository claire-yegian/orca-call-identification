#!usr/local/bin/python
# CREDIT: https://programmerblog.net/join-wav-audio-files-using-python/
# CREDIT: https://bbc.github.io/bbcat-orchestration-docs/installation-mac-manual/
# CREDIT: https://www.ffmpeg.org/download.html
import glob
import sys
import os

from pydub import AudioSegment

dirpathVocals = "Orchive/vocals/"
dirpathNoise = "Noise from Water/"
dirpathNewVocals = "Orchive/newVocals/"

addon = AudioSegment.from_wav(dirpathNoise + "water_noise.wav") # the water noise to pad each file with
filenames = glob.glob(dirpathVocals+'*.wav') # list of all files in the directory

for filename in filenames:
    file = os.path.split(filename)[1] # grab the filename without the path
    file = file[:-4] # remove the .wav extension because we'll add "-New.wav" when we export
    original = AudioSegment.from_wav(filename)
    filenames_combined = [original, addon]
    combined = AudioSegment.empty()
    for fname in filenames_combined:
        combined += fname
    combined_clipped = combined[:4000] # take first 4 seconds
    combined_clipped.export(dirpathNewVocals + file + "-New.wav", format="wav")
