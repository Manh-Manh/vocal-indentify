# %%
import os
py_exe = "C:\\Users\\MANHND\\AppData\\Local\\Programs\\Python\\Python39\\python.exe "
base_cmd = "E:\\hoctap\\CH\\voiceremover\\vocal-remover\\inference.py -P E:\\hoctap\\CH\\voiceremover\\vocal-remover\\models\\baseline.pth --input "
path_origin = "E:\\hoctap\\CH\\voiceIdentify\\audios\\origin"
path_vocal = "E:\\hoctap\\CH\\voiceIdentify\\audios\\vocal"
exclude = []
origin_dir = os.fsencode(path_origin)
vocal_dir = os.fsencode(path_vocal)
for file in os.listdir(origin_dir):
    if (exclude.count(os.fsdecode(file)) > 0):
        continue
    music_dir = os.path.join(origin_dir, file)
    vocl_dir = os.path.join(vocal_dir, file)
    print('process on ' + os.fsdecode(os.path.join(origin_dir, file)))
    if (os.path.exists(vocl_dir) is False):
        os.makedirs(vocl_dir)
        print('make vocal dir ' + os.fsdecode(vocl_dir))
    singer_name = file 
    for song in os.listdir(music_dir):
        song_file = os.path.join(music_dir, song)
        if os.path.isfile(song_file):
            cmd = py_exe + base_cmd + os.fsdecode(song_file) + " -o " + os.fsdecode(vocl_dir)
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
