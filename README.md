# Slim-neck by GSConv

<p align="left"><img width="800" src="https://github.com/AlanLi1997/slim-neck-by-gsconv/blob/main/slim%20neck%20by%20gsconv.png"></p>
  trained datasets:
  <br /> - PASCAL VOC 2007+12
  <br /> - WiderPerson
  <br /> - SODA10M (for autonomous vehicles)
  <br /> more...

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
    git clone https://github.com/ultralytics/yolov5
    cd yolov5/
    pip install requirements.txt
    python val.py --data data/VOC.yaml --weights your_select.pt --task test
    




 # References
  - https://github.com/ultralytics/yolov5
  - https://github.com/AlexeyAB/darknet/tree/yolov4
  - https://github.com/WongKinYiu/PyTorch_YOLOv4
  - https://github.com/huawei-noah/CV-backbones/tree/master/ghostnet_pytorch