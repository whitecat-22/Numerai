#!/bin/bash

cd `dirname $0`

SHELL=/bin/bash
# �p�X��ʂ�
source /home/ubuntu/.bashrc
# �D����Python����ݒ�
source activate tensorflow2_latest_serving

sudo shutdown +45

cd /home/ubuntu/numerai
/ubuntu/numerai/python3 predict.py