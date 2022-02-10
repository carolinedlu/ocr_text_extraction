import os
os.system("pip install --upgrade pip")
os.system("pip install torch torchvision")
os.system("pip install numpy==1.21.0 mmcv-full openmim requests")
os.system("mim install mmdet")
os.system('git clone https://github.com/open-mmlab/mmocr.git')
os.system('pip install -r mmocr/requirements.txt')
os.system('pip install -v -e mmocr')
os.system('export PYTHONPATH=$(pwd)/mmocr:$PYTHONPATH')
os.system('pip freeze')
import sys
import requests
sys.path.append('./mmocr')
