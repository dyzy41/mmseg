import os
import random
import sys

src_path = '/home/jicredt_data/dsj/paper_whub/whub01_test'
state = 'test'

image_path = os.path.join(src_path, '{}/image'.format(state))
label_path = os.path.join(src_path, '{}/label'.format(state))

images = os.listdir(image_path)
random.shuffle(images)

with open('../data/{}_list.txt'.format(state), 'w') as ff:
    for name in images:
        if os.path.exists(os.path.join(image_path, name)) and os.path.exists(os.path.join(label_path, name)):
            cur_info = '{}  {}\n'.format(os.path.join(image_path, name), os.path.join(label_path, name))
            ff.writelines(cur_info)

