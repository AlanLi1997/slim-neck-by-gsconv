# [Slim-neck by GSConv: A better design paradigm of detector architectures for autonomous vehicles](https://link.springer.com/article/10.1007/s11554-024-01436-6)

[English](README.md) | [简体中文](README.zh-CN.md)
<br>


<p align="center">
  <img src="gsconvdet.png" alt="" width="800" />
</p>
  
Datasets:
  <br /> - PASCAL VOC 2007+12
  <br /> - WiderPerson
  <br /> - SODA10M (for autonomous vehicles)
  <br /> - DOTA1.0
  <br />(We only provide the train/val/test.txt file we used so that you can reproduce our results. The images & labels can be found on the official websites of these datasets.) 
---
### An example of comparison on remote sensing images

scaled-yolov4
<p align="center">
  <img src="remote-scaledv4.jpg" alt="" width="800" />
</p>

slim neck scaled-yolov4
<p align="center">
  <img src="sm-remote-scaledv4.jpg" alt="" width="800" />
</p>

---

## Training the custom datasets 
### 1. For GSConv-yolov5
(Updated July 14th)
    
    git clone https://github.com/AlanLi1997/slim-neck-by-gsconv.git
    cd slim-neck-by-gsconv/gsconv-yolov5
    pip install requirements.txt
    python train.py --cfg models/sm-yolov5s.yaml
    
### 2. For GSConv-scaled_yolov4
(Updated Aug 17th)

    git clone https://github.com/AlanLi1997/slim-neck-by-gsconv.git
    cd slim-neck-by-gsconv
    pip install requirements.txt
    cd gsconv-scaled-yolov4
    python train.py --cfg models/sm-yolov4-p5.yaml

### Pretrained Checkpoints 
MS COCO

|Model |size<br><sup>(pixels) |mAP<sup>val<br>0.5:0.95 |mAP<sup>val<br>0.5 |FPS<br><sup>T4 b1<br> |FPS<br><sup>T4 b32<br> |params<br><sup>(M) |FLOPs<br><sup>@640 (G)
|---                 |---  |---    |---            |---    |---    |---    |---
|[yolov5n(ultralytics)](https://objects.githubusercontent.com/github-production-release-asset-2e65be/264818686/3444cd1f-277c-414f-bdc9-3ac8ed6062df?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20221024%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221024T112402Z&X-Amz-Expires=300&X-Amz-Signature=93c777453bc3699dc5da551f5d6ea052bc34d4d0c67dd7400629780ddb2d8054&X-Amz-SignedHeaders=host&actor_id=80144976&key_id=0&repo_id=264818686&response-content-disposition=attachment%3B%20filename%3Dyolov5n.pt&response-content-type=application%2Foctet-stream)         |640  |28.0   |45.7           | -- |--|1.9|4.5
|[GSyolov5n]()      |640  |**28.4**(+0.4) |**47.0**(+1.3) |**147** |**207**|**1.8**|**4.0**
|**Model** |**size<br><sup>(pixels)** |**mAP<sup>val<br>0.5:0.95** |**mAP<sup>val<br>0.5** |**FPS<br><sup>A40 b1<br>** |**FPS<br><sup>A40 b32<br>** |**params<br><sup>(M)** |**FLOPs<br><sup>@640 (G)**
|[yolov5s](https://raw.githubusercontent.com/AlanLi1997/slim-neck-by-gsconv/master/pre_trained_weights/yolov5s.pt)      |640  |35.7 |**54.3** |**109** |297|7.2|16.4
|[GSyolov5s](https://raw.githubusercontent.com/AlanLi1997/slim-neck-by-gsconv/master/pre_trained_weights/GSyolov5s.pt)    |640  |**36.0**(+0.3) |54.2 |95 |**312**(+15)|**7.0**|**14.5**


## Testing the slim-neck detectors
### 1. For GSConv-yolov5
    
    cd gsconv-yolov5
    python val.py --data yourdata.yaml --weights sm-yolov5s.pt --task test

### 2. For GSConv-scaled-yolov4
    
    cd gsconv-scaled-yolov4
    python val.py --data yourdata.yaml --weights sm-yolov4-p5.pt --task test

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
