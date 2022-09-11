#!/bin/bash
# nohup bash run.sh > 0911.log 2>&1 &
bash tools/dist_train.sh configs/ocrnet/ocrnet_hr48_512x512_160k_zdy.py 2 --work-dir work_dirs/ocrnet_hr48_512x512_160k_zdy/ --deterministic