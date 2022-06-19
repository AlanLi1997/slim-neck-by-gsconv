# Slim-neck by GSConv
paper: https://arxiv.org/ftp/arxiv/papers/2206/2206.02424.pdf

<p align="left"><img width="800" src="https://github.com/AlanLi1997/slim-neck-by-gsconv/blob/main/slim%20neck%20by%20gsconv.png"></p>
  Datasets:

  <br /> - PASCAL VOC 2007+12
  <br /> - WiderPerson
  <br /> - SODA10M (for autonomous vehicles)
  <br /> ...
  <br />(We only provide the train/val/test .txt file, and the images & labels can be found on the official websites of these datasets.) 
  

### 1. weights of standard detector for VOC 2007+12: 

  include:

    yolov3
    yolov4
    yolov5
    MobileNetsV3
    ShuffleNetV2
    GhostNet

### 2. weights of slim-neck detector for VOC 2007+12:
  include:
    
    slim-neck for 
    


#### To test the slim-neck detectors
( It will be updated soon, include:  yolov3/4/5 and yolo-MobileNetsV3/ShuffleNetV2/GhostNet )
    
    git clone 
    cd 
    pip install requirements.txt
    python 
    




 # References
  - https://github.com/ultralytics/yolov5
  - https://github.com/AlexeyAB/darknet/tree/yolov4
  - https://github.com/WongKinYiu/PyTorch_YOLOv4
  - https://github.com/huawei-noah/CV-backbones/tree/master/ghostnet_pytorch
  - https://github.com/d-li14/mobilenetv3.pytorch
  - https://github.com/megvii-model/ShuffleNet-Series
