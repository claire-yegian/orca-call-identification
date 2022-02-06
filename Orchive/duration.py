import wave
import contextlib
import os

directory = './../audible/'
min_dur = 10
max_dur = 0
for filename in os.listdir(directory):
    if filename.endswith(".wav"):
        name = directory + filename
        with contextlib.closing(wave.open(name,'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = frames / float(rate)
            if duration < min_dur:
                min_dur = duration
            if duration > max_dur:
                max_dur = duration

print("audible")
print("min: ", min_dur)
print("max: ", max_dur)

directory = './../call-catalog/wav/'
min_dur = 10
max_dur = 0
for filename in os.listdir(directory):
    if filename.endswith(".wav"):
        name = directory + filename
        with contextlib.closing(wave.open(name,'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = frames / float(rate)
            if duration < min_dur:
                min_dur = duration
            if duration > max_dur:
                max_dur = duration

print()
print("call-catalog")
print("min: ", min_dur)
print("max: ", max_dur)

directory = 'extract'
min_dur = 10
max_dur = 0
for filename in os.listdir(directory):
    if filename.endswith(".wav"):
        name = 'extract/' + filename
        with contextlib.closing(wave.open(name,'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = frames / float(rate)
            if duration < min_dur:
                min_dur = duration
            if duration > max_dur:
                max_dur = duration

print()
print("extract")
print("min: ", min_dur)
print("max: ", max_dur)


directory = 'vocals'
min_dur = 10
max_dur = 0
for filename in os.listdir(directory):
    if filename.endswith(".wav"):
        name = 'vocals/' + filename
        with contextlib.closing(wave.open(name,'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = frames / float(rate)
            if duration < min_dur:
                min_dur = duration
            if duration > max_dur:
                max_dur = duration

print()
print("vocals")
print("min: ", min_dur)
print("max: ", max_dur)

        
