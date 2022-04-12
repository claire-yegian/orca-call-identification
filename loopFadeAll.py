import glob
import sys
import os

from pydub import AudioSegment

dirpathVocals = "Orchive/vocals/"
dirpathNewVocals = "Orchive/newVocalsLooped/"
# list of all files in the directory
filenames = glob.glob(dirpathVocals+'*.wav')

for filename in filenames:
    file = os.path.split(filename)[1]  # grab the filename without the path
    # remove the .wav extension because we'll add "-New.wav" when we export
    file = file[:-4]
    original = AudioSegment.from_wav(filename)
    # take the first 150 of the last 200 miliseconds
    addon = original[-200:][:150]
    addon2 = addon.reverse()  # make a reversed version of that
    combined = AudioSegment.empty()  # create the new audio segment
    combined = original  # start with the original sound
    while (len(combined) < 4000):  # while it's not four seconds long
        # alternate reversed and regular clips of the last part of the file
        combined = combined + addon2 + addon
    combined_clipped = combined[:4000]  # take first 4 seconds
    combined_clipped = combined.fade_out(400)  # fade out the end of the file
    combined_clipped.export(dirpathNewVocals + file +
                            "-Looped.wav", format="wav")  # export the new file
