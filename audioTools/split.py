# %%
import os
import argparse
import librosa
import numpy as np
from pathlib import Path
from pydub import AudioSegment
import csv
def doWork(input, des, deltaTime, fcsv, clazz):
    AUDIO_FILE = input
    samples, sample_rate = librosa.load(AUDIO_FILE, sr=None)
    originAudio = AudioSegment.from_wav(AUDIO_FILE)
    # librosa.display.waveshow(samples, sr=sample_rate)
    filename = Path(AUDIO_FILE).stem
    suffix = Path(AUDIO_FILE).suffix
    db = librosa.amplitude_to_db(samples, ref=np.min)
    # %%
    # caculator
    second = int(len(samples)/sample_rate)
    milis = 1
    mapsec = []
    for i in range(1, second, milis):
        start = (i-1) * 1000
        end = milis*1000 + start
        if ((sum(db[sample_rate*(i-1): sample_rate*i])/sample_rate) >50):

            mapsec.append(i)
    # %%
    csvfilename = fcsv
    csv_data = []
    count = 0
    outshape = AudioSegment.empty()

    pre = filename

    for i in mapsec:
        start = (i-1) * 1000
        print("Start: " + str(start))
        if len(outshape) == 0:
            outshape = originAudio[start: start + 1000]
        else:
            print("append")
            outshape = outshape + originAudio[start: start + 1000]
        count = count + 1
        pre = pre + "_" + str(i)
        print ("Count: " + str(count) + ", len: " + str(len(outshape)))
        if count == deltaTime:
            print("Save " + str(len(outshape)))
            newName = des + "/" +  pre + ".wav"
            pathNew = newName
            outshape.export(pathNew, format="wav")
            csv_data.append({'file_name': newName, 'class': clazz, 'relative_path': pathNew})
            count = 0
            outshape = AudioSegment.empty()
            pre = filename
    fields = ['file_name', 'class', 'relative_path']
    # writing to csv file
    if (os.path.exists(os.fsencode(csvfilename))):
        with open(csvfilename, 'a') as csvfile:     
            # creating a csv dict writer object
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            # writing headers (field names)
            # writing data rows
            writer.writerows(csv_data)      
            csvfile.close() 
    else:
        with open(csvfilename, 'w') as csvfile:     
            # creating a csv dict writer object
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            # writing headers (field names)
            writer.writeheader()
            # writing data rows
            writer.writerows(csv_data)      
            csvfile.close() 

# %%
def main():
    p = argparse.ArgumentParser()
    p.add_argument('--input', '-i', type=str, default='tesst_Vocals.wav')
    p.add_argument('--destination', '-d', type=str, default='./')
    p.add_argument('--range', '-r', type=int, default=5)
    p.add_argument('--csv', '-c', type=str, default='data.csv')
    p.add_argument('--clazz', '-z', type=str, default='none')
    args = p.parse_args()
    doWork(args.input, args.destination, args.range, args.csv, args.clazz)

# %%
if __name__== "__main__":
    main()
# %%

 