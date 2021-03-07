#!/bin/bash

cd `dirname $0`

SHELL=/bin/bash
# パスを通す
source /home/ubuntu/.bashrc
# 好きなPython環境を設定
source activate tensorflow2_latest_serving

sudo shutdown +45

cd /home/ubuntu/numerai
/ubuntu/numerai/python3 predict.py