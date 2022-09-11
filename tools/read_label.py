import cv2
import numpy as np
from PIL import Image
import os
import mmcv
import imageio


p = '/home/jicredt_data/dsj/paper_whub/whub01_test/val/label'
# files = os.listdir(p)
# for item in files:
#     # img = cv2.imread(os.path.join(p, item), 0)
#     # img = np.asarray(Image.open(os.path.join(p, item)).convert('L'))
#     img = mmcv.imread(os.path.join(p, item))
#     # print(img)
#     print(set(img.flatten()))



img = imageio.imread(os.path.join(p, 'val_135.tif'))

print(img)


