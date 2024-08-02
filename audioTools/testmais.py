# %%
import os

dir = 'C:\\Users\\MANHND\\Desktop\\1'
base_cmd = 'ffmpeg -i '
ext = '.awb'
des_ext = '.mp3'
for f in os.listdir(dir):
    
    file_name = os.path.basename(f)
    file = os.path.splitext(file_name)
    if (file[1] == ext):
        cmd = base_cmd + '"' + dir + "\\" + os.fsdecode(f) + '" "' + dir + "\\" + file[0] + des_ext + '"'
        print(cmd)
        ret = os.system(cmd)
        print(ret)
        if (ret == 0):
            print('Conver done ' + os.fsdecode(f))
# %%
dir = 'C:\\Users\\MANHND\\Desktop\\1'
base_cmd = 'ffmpeg -i '
ext = '.awb'
des_ext = '.mp3'
for f in os.listdir(dir):
    print(dir + "\\" + os.fsdecode(f))
    file_name = os.path.basename(f)
    file = os.path.splitext(file_name)
    print(file)
# %%
