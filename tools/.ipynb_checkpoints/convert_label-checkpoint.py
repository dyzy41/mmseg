import os
import cv2
import numpy as np
import tqdm


p = '/root/mmseg/dataset/labels'
files = os.listdir(p)
for item in tqdm.tqdm(files):
    img = cv2.imread(os.path.join(p, item), 0)
    img_ = np.where(img>0, 1, 0)
    cv2.imwrite(os.path.join(p, item), img_)