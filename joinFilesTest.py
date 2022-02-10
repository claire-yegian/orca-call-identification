#!usr/local/bin/python
# CREDIT: https://programmerblog.net/join-wav-audio-files-using-python/
# CREDIT: https://bbc.github.io/bbcat-orchestration-docs/installation-mac-manual/
# CREDIT: https://www.ffmpeg.org/download.html
import glob
import sys
import os

from pydub import AudioSegment

dirpathVocals = "Orchive/vocals/"
#headingsNewsDir = dirpath+"2019-03-01/"
dirpathNoise = "Noise from Water/"
generatedFile = "newCall.wav"

#filenames = glob.glob(dirpathVocals+'*.wav')
original = AudioSegment.from_wav(
    dirpathVocals + "A05-N04-082108-D120-11350.wav")
addon = AudioSegment.from_wav(dirpathNoise + "water_noise.wav")

filenamesCombined = [original, addon]
combined = AudioSegment.empty()
# for filename in filenames:
#audiofilename = AudioSegment.from_wav(filename)
#filenamesCombined.extend([audiofilename, beep])
# filenamesCombined.extend([thankyou]

for fname in filenamesCombined:
    combined += fname

combined.export(generatedFile, format="wav")
