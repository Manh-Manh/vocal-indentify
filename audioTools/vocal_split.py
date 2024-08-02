# %%
import os
# py_exe = "C:\\Users\\MANHND\\AppData\\Local\\Programs\\Python\\Python39\\python.exe "
py_exe = "python3 "
base_cmd = "E:\\hoctap\\CH\\voiceIdentify\\audioTools\\split.py --input "
path_origin = "E:\\hoctap\\CH\\voiceIdentify\\audios\\origin"
path_csv = "./data2.csv"
path_vocal = "E:\\hoctap\\CH\\voiceIdentify\\audios\\vocal"
path_desniation = "E:\\hoctap\\CH\\voiceIdentify\\audios\\input"

exclude = []

vocal_dir = os.fsencode(path_vocal)
des_dir = os.fsencode(path_desniation)
for file in os.listdir(vocal_dir):
    if (exclude.count(os.fsdecode(file)) > 0):
        continue
    music_dir = os.path.join(vocal_dir, file)
    singer_name = file 
    desss = os.path.join(des_dir, file)
    print('process on ' + os.fsdecode(os.path.join(vocal_dir, file)))
    if (os.path.exists(desss) is False):
        os.makedirs(desss)
        print('make des dir ' + os.fsdecode(desss))
    
    for song in os.listdir(music_dir):
        song_file = os.path.join(music_dir, song)
        if os.path.isfile(song_file):
            cmd = py_exe + base_cmd + os.fsdecode(song_file) + " -r 5 -d " + os.fsdecode(desss) + " -c " + path_csv + " -z " + os.fsdecode(singer_name)
            print(cmd)
            ret = os.system(cmd)
            print(ret)
            if (ret == 0):
                print('Conver done ' + os.fsdecode(song_file))

print("all done")
# %%

name = 'Mytam'
print(exclude.count(name))
for i in range(1, 10):
    if (i > 6):
        continue
    print(i)
# %%
