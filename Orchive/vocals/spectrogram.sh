#!/bin/bash
mkdir -p spectrograms
for file in *.wav;do
    outfile="${file%.*}.png"
    sox "$file" -n spectrogram -o "$outfile"
    mv "$outfile" spectrograms/
done
mogrify -strip -quality 80% -sampling-factor 4:4:4 -format jpg spectrograms/*.png
rm /spectrograms/*.png