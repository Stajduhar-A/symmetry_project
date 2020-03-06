import os
import shutil
import random

#a = '183a'
#b = '250'
#c = '260'

src = "/Volumes/Andreja's_Mac_Drive/symmetry_experiment/new_blobs_2/asymmetric"
dest = 'dest/2D/sym_per_b/2'

folders = os.listdir("/Volumes/Andreja's_Mac_Drive/symmetry_experiment/new_blobs_2/asymmetric")

random.shuffle(folders)

if not os.path.exists(dest):
    os.mkdir(dest)


for image in folders:
    if image[-4:] == '.png' and 'per' in image and 'sym' and len(os.listdir(dest)) < 8 and 'b_' in image and '2D' in image:
        image_src = os.path.join(src, image)
        shutil.copy(image_src, dest)



print(folders)

'''
You only need to change three things:
1. The source (src).
2. The destination (dest).
3. The image ID (property and number) you want to search for.
'''
