# Copyright (c) OpenMMLab. All rights reserved.
from .builder import DATASETS
from .custom_txt import CustomTxtDataset


@DATASETS.register_module()
class ZDYDataset(CustomTxtDataset):
    """ZiDingYi dataset.
    """
    CLASSES = ('background', 'target')

    PALETTE = [[0, 0, 0], [255, 255, 255]]

    def __init__(self, **kwargs):
        super(ZDYDataset, self).__init__(
            img_suffix='.JPG',
            seg_map_suffix='.png',
            reduce_zero_label=False,
            **kwargs)
