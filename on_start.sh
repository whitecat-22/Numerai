#!/bin/bash

cd `dirname $0`

SHELL=/bin/bash
# ƒpƒX‚ğ’Ê‚·
source /home/ubuntu/.bashrc
# D‚«‚ÈPythonŠÂ‹«‚ğİ’è
source activate tensorflow2_latest_serving

sudo shutdown +45

cd /home/ubuntu/numerai
/ubuntu/numerai/python3 predict.py