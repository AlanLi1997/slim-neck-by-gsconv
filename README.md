# Slim-neck by GSConv: A better design paradigm of detector architectures for autonomous vehicle
paper: https://arxiv.org/ftp/arxiv/papers/2206/2206.02424.pdf

<p align="left"><img width="800" src="https://github.com/AlanLi1997/slim-neck-by-gsconv/blob/main/slim%20neck%20by%20gsconv.png"></p>
  Datasets:

  <br /> - PASCAL VOC 2007+12
  <br /> - WiderPerson
  <br /> - SODA10M (for autonomous vehicles)
  <br /> ...
  <br />(We only provide the train/val/test.txt file we used so that you can reproduce our results. The images & labels can be found on the official websites of these datasets.) 


## Training the custom datasets 
### 1. For GSConv-yolov5
(Updated July 14th)
    
    git clone https://github.com/AlanLi1997/slim-neck-by-gsconv.git
    cd slim-neck-by-gsconv/gsconv-yolov5-6.1
    pip install requirements.txt
    python train.py --cfg models/GSConv-yolov5s.yaml
    
### 2. For GSConv-scaled_yolov4
( It will be updated soon )

    git clone 
    cd 
    pip install requirements.txt
    python 


## Testing the slim-neck detectors
### 1. For GSConv-yolov5
    
    python val.py --data yourdata.yaml --weights GSConv-yolov5s.pt
    




 ## References
  - https://github.com/ultralytics/yolov5
  - https://github.com/AlexeyAB/darknet/tree/yolov4
  - https://github.com/WongKinYiu/PyTorch_YOLOv4
  - https://github.com/huawei-noah/CV-backbones/tree/master/ghostnet_pytorch
  - https://github.com/d-li14/mobilenetv3.pytorch
  - https://github.com/megvii-model/ShuffleNet-Series

## Citation
@article{li2022slim,<br />
  title={Slim-neck by GSConv: A better design paradigm of detector architectures for autonomous vehicles},<br />
  author={Li, Hulin and Li, Jun and Wei, Hanbing and Liu, Zheng and Zhan, Zhenfei and Ren, Qiliang},<br />
  journal={arXiv preprint arXiv:2206.02424},<br />
  year={2022}<br />
}

# 基于GSConv的轻量融合层：一个更好的轻量化检测器结构设计范式
论文地址: https://arxiv.org/ftp/arxiv/papers/2206/2206.02424.pdf

<p align="left"><img width="800" src="https://github.com/AlanLi1997/slim-neck-by-gsconv/blob/main/slim%20neck%20by%20gsconv.png"></p>
  实验数据集:

  <br /> - PASCAL VOC 2007+12 (通用检测器)
  <br /> - WiderPerson (用于行人检测)
  <br /> - SODA10M (用于自动驾驶)
  <br /> ...
  <br />(我们只提供我们所使用的训练、验证和测试的文本文档,以便于您复现我们的结果。 被标注的图像和它们的标注文件请您访问相应的数据集官方网站获取。) 
  

## 训练自定义数据集
### 1. 使用GSConv改进yolov5
(7月14日更新)
    
    git clone https://github.com/AlanLi1997/slim-neck-by-gsconv.git
    cd slim-neck-by-gsconv/gsconv-yolov5-6.1
    pip install requirements.txt
    python train.py --cfg models/GSConv-yolov5s.yaml
    
### 2. 使用GSConv改进scaled_yolov4
(即将到来)

    git clone 
    cd 
    pip install requirements.txt
    python 


## 验证和测试改进后的检测器的性能
### 1. 测试被GSConv改进的yolov5
    
    python val.py --data yourdata.yaml --weights GSConv-yolov5s.pt
    




 ## 参考
  - https://github.com/ultralytics/yolov5
  - https://github.com/AlexeyAB/darknet/tree/yolov4
  - https://github.com/WongKinYiu/PyTorch_YOLOv4
  - https://github.com/huawei-noah/CV-backbones/tree/master/ghostnet_pytorch
  - https://github.com/d-li14/mobilenetv3.pytorch
  - https://github.com/megvii-model/ShuffleNet-Series

## 引用此工作
@article{li2022slim,<br />
  title={Slim-neck by GSConv: A better design paradigm of detector architectures for autonomous vehicles},<br />
  author={Li, Hulin and Li, Jun and Wei, Hanbing and Liu, Zheng and Zhan, Zhenfei and Ren, Qiliang},<br />
  journal={arXiv preprint arXiv:2206.02424},<br />
  year={2022}<br />
}
