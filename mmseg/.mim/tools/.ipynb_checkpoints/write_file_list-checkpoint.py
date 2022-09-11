import os
import random
import sys

src_path = '/root/mmseg/dataset'

image_path = os.path.join(src_path, 'images')
label_path = os.path.join(src_path, 'labels')

images = os.listdir(image_path)
random.shuffle(images)

with open('../data/{}_list.txt'.format('train'), 'w') as ff:
    for name in images:
        if os.path.exists(os.path.join(image_path, name)) and os.path.exists(os.path.join(label_path, name.replace('.JPG', '.png'))):
            cur_info = '{}  {}\n'.format(os.path.join(image_path, name), os.path.join(label_path, name.replace('.JPG', '.png')))
            ff.writelines(cur_info)

