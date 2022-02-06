import wave
import contextlib
import os
#import pandas
import matplotlib.pyplot as plt

directory = './../audible/'
min_dur = 10
max_dur = 0

#filename_list = []
#length_list = []

#ditionary = {}

file_dur_tuples = []

for filename in os.listdir(directory):
    if filename.endswith(".wav"):
        name = directory + filename
        with contextlib.closing(wave.open(name,'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = frames / float(rate)

            #filename_list.appen(filename)
            #length_list.append(duration)
            #dictionary[filename] = duration

            file_dur_tuples.append((filename, duration))
            
            #if duration < min_dur:
                #min_dur = duration
            #if duration > max_dur:
                #max_dur = duration
            if duration > 2.5:
                print(filename)

#s = pd.Series(dictionary)
#s.sort_values()
#print(s)

file_dur_tuples.sort(key=lambda x: x[1])
#print(file_dur_tuples)

#plt.hist(file_dur_tuples)

#print("audible")
#print("min: ", min_dur)
#print("max: ", max_dur)
