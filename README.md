# Slim-neck by GSConv
paper: https://arxiv.org/ftp/arxiv/papers/2206/2206.02424.pdf

<p align="left"><img width="800" src="https://github.com/AlanLi1997/slim-neck-by-gsconv/blob/main/slim%20neck%20by%20gsconv.png"></p>
  Datasets:

  <br /> - PASCAL VOC 2007+12
  <br /> - WiderPerson
  <br /> - SODA10M (for autonomous vehicles)
  <br /> ...
  <br />(We only provide the train/val/test .txt file, and the images & labels can be found on the official websites of these datasets.) 
  

## Training the custom datasets 
### 1. For GSConv-yolov5
    
    git clone https://github.com/AlanLi1997/slim-neck-by-gsconv.git
    cd slim-neck-by-gsconv/sngs-yolov5
    pip install requirements.txt
    python train.py --cfg models/gs-yolov5s.yaml
    
### 2. For GSConv-scaled_yolov4
( It will be updated soon )

    git clone 
    cd 
    pip install requirements.txt
    python 


## Testing the slim-neck detectors
### 1. For GSConv-yolov5
    
    python val.py --data yourdata.yaml --weights gsconv-yolov5s.pt
    




 # References
  - https://github.com/ultralytics/yolov5
  - https://github.com/AlexeyAB/darknet/tree/yolov4
  - https://github.com/WongKinYiu/PyTorch_YOLOv4
  - https://github.com/huawei-noah/CV-backbones/tree/master/ghostnet_pytorch
  - https://github.com/d-li14/mobilenetv3.pytorch
  - https://github.com/megvii-model/ShuffleNet-Series

# Citation
@article{li2022slim,<br />
  title={Slim-neck by GSConv: A better design paradigm of detector architectures for autonomous vehicles},<br />
  author={Li, Hulin and Li, Jun and Wei, Hanbing and Liu, Zheng and Zhan, Zhenfei and Ren, Qiliang},<br />
  journal={arXiv preprint arXiv:2206.02424},<br />
  year={2022}<br />
}
