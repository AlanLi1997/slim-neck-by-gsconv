---
comments: true
description: Learn to deploy Ultralytics YOLOv8 on NVIDIA Jetson devices with our detailed guide. Explore performance benchmarks and maximize AI capabilities.
keywords: Ultralytics, YOLOv8, NVIDIA Jetson, JetPack, AI deployment, performance benchmarks, embedded systems, deep learning, TensorRT, computer vision
---

# Quick Start Guide: NVIDIA Jetson with Ultralytics YOLOv8

This comprehensive guide provides a detailed walkthrough for deploying Ultralytics YOLOv8 on [NVIDIA Jetson](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/) devices. Additionally, it showcases performance benchmarks to demonstrate the capabilities of YOLOv8 on these small and powerful devices.

<p align="center">
  <br>
  <iframe loading="lazy" width="720" height="405" src="https://www.youtube.com/embed/mUybgOlSxxA"
    title="YouTube video player" frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen>
  </iframe>
  <br>
  <strong>Watch:</strong> How to Setup NVIDIA Jetson with Ultralytics YOLOv8
</p>

<img width="1024" src="https://github.com/ultralytics/docs/releases/download/0/nvidia-jetson-ecosystem.avif" alt="NVIDIA Jetson Ecosystem">

!!! note

    This guide has been tested with both [Seeed Studio reComputer J4012](https://www.seeedstudio.com/reComputer-J4012-p-5586.html) which is based on NVIDIA Jetson Orin NX 16GB running the latest stable JetPack release of [JP6.0](https://developer.nvidia.com/embedded/jetpack-sdk-60), JetPack release of [JP5.1.3](https://developer.nvidia.com/embedded/jetpack-sdk-513) and [Seeed Studio reComputer J1020 v2](https://www.seeedstudio.com/reComputer-J1020-v2-p-5498.html) which is based on NVIDIA Jetson Nano 4GB running JetPack release of [JP4.6.1](https://developer.nvidia.com/embedded/jetpack-sdk-461). It is expected to work across all the NVIDIA Jetson hardware lineup including latest and legacy.

## What is NVIDIA Jetson?

NVIDIA Jetson is a series of embedded computing boards designed to bring accelerated AI (artificial intelligence) computing to edge devices. These compact and powerful devices are built around NVIDIA's GPU architecture and are capable of running complex AI algorithms and [deep learning](https://www.ultralytics.com/glossary/deep-learning-dl) models directly on the device, without needing to rely on [cloud computing](https://www.ultralytics.com/glossary/cloud-computing) resources. Jetson boards are often used in robotics, autonomous vehicles, industrial automation, and other applications where AI inference needs to be performed locally with low latency and high efficiency. Additionally, these boards are based on the ARM64 architecture and runs on lower power compared to traditional GPU computing devices.

## NVIDIA Jetson Series Comparison

[Jetson Orin](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/) is the latest iteration of the NVIDIA Jetson family based on NVIDIA Ampere architecture which brings drastically improved AI performance when compared to the previous generations. Below table compared few of the Jetson devices in the ecosystem.

|                   | Jetson AGX Orin 64GB                                              | Jetson Orin NX 16GB                                              | Jetson Orin Nano 8GB                                          | Jetson AGX Xavier                                           | Jetson Xavier NX                                              | Jetson Nano                                   |
| ----------------- | ----------------------------------------------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------- | --------------------------------------------- |
| AI Performance    | 275 TOPS                                                          | 100 TOPS                                                         | 40 TOPs                                                       | 32 TOPS                                                     | 21 TOPS                                                       | 472 GFLOPS                                    |
| GPU               | 2048-core NVIDIA Ampere architecture GPU with 64 Tensor Cores     | 1024-core NVIDIA Ampere architecture GPU with 32 Tensor Cores    | 1024-core NVIDIA Ampere architecture GPU with 32 Tensor Cores | 512-core NVIDIA Volta architecture GPU with 64 Tensor Cores | 384-core NVIDIA Volta™ architecture GPU with 48 Tensor Cores | 128-core NVIDIA Maxwell™ architecture GPU    |
| GPU Max Frequency | 1.3 GHz                                                           | 918 MHz                                                          | 625 MHz                                                       | 1377 MHz                                                    | 1100 MHz                                                      | 921MHz                                        |
| CPU               | 12-core NVIDIA Arm® Cortex A78AE v8.2 64-bit CPU 3MB L2 + 6MB L3 | 8-core NVIDIA Arm® Cortex A78AE v8.2 64-bit CPU 2MB L2 + 4MB L3 | 6-core Arm® Cortex®-A78AE v8.2 64-bit CPU 1.5MB L2 + 4MB L3 | 8-core NVIDIA Carmel Arm®v8.2 64-bit CPU 8MB L2 + 4MB L3   | 6-core NVIDIA Carmel Arm®v8.2 64-bit CPU 6MB L2 + 4MB L3     | Quad-Core Arm® Cortex®-A57 MPCore processor |
| CPU Max Frequency | 2.2 GHz                                                           | 2.0 GHz                                                          | 1.5 GHz                                                       | 2.2 GHz                                                     | 1.9 GHz                                                       | 1.43GHz                                       |
| Memory            | 64GB 256-bit LPDDR5 204.8GB/s                                     | 16GB 128-bit LPDDR5 102.4GB/s                                    | 8GB 128-bit LPDDR5 68 GB/s                                    | 32GB 256-bit LPDDR4x 136.5GB/s                              | 8GB 128-bit LPDDR4x 59.7GB/s                                  | 4GB 64-bit LPDDR4 25.6GB/s"                   |

For a more detailed comparison table, please visit the **Technical Specifications** section of [official NVIDIA Jetson page](https://developer.nvidia.com/embedded/jetson-modules).

## What is NVIDIA JetPack?

[NVIDIA JetPack SDK](https://developer.nvidia.com/embedded/jetpack) powering the Jetson modules is the most comprehensive solution and provides full development environment for building end-to-end accelerated AI applications and shortens time to market. JetPack includes Jetson Linux with bootloader, Linux kernel, Ubuntu desktop environment, and a complete set of libraries for acceleration of GPU computing, multimedia, graphics, and [computer vision](https://www.ultralytics.com/glossary/computer-vision-cv). It also includes samples, documentation, and developer tools for both host computer and developer kit, and supports higher level SDKs such as DeepStream for streaming video analytics, Isaac for robotics, and Riva for conversational AI.

## Flash JetPack to NVIDIA Jetson

The first step after getting your hands on an NVIDIA Jetson device is to flash NVIDIA JetPack to the device. There are several different way of flashing NVIDIA Jetson devices.

1. If you own an official NVIDIA Development Kit such as the Jetson Orin Nano Developer Kit, you can [download an image and prepare an SD card with JetPack for booting the device](https://developer.nvidia.com/embedded/learn/get-started-jetson-orin-nano-devkit).
2. If you own any other NVIDIA Development Kit, you can [flash JetPack to the device using SDK Manager](https://docs.nvidia.com/sdk-manager/install-with-sdkm-jetson/index.html).
3. If you own a Seeed Studio reComputer J4012 device, you can [flash JetPack to the included SSD](https://wiki.seeedstudio.com/reComputer_J4012_Flash_Jetpack/) and if you own a Seeed Studio reComputer J1020 v2 device, you can [flash JetPack to the eMMC/ SSD](https://wiki.seeedstudio.com/reComputer_J2021_J202_Flash_Jetpack/).
4. If you own any other third party device powered by the NVIDIA Jetson module, it is recommended to follow [command-line flashing](https://docs.nvidia.com/jetson/archives/r35.5.0/DeveloperGuide/IN/QuickStart.html).

!!! note

    For methods 3 and 4 above, after flashing the system and booting the device, please enter "sudo apt update && sudo apt install nvidia-jetpack -y" on the device terminal to install all the remaining JetPack components needed.

## JetPack Support Based on Jetson Device

The below table highlights NVIDIA JetPack versions supported by different NVIDIA Jetson devices.

|                   | JetPack 4 | JetPack 5 | JetPack 6 |
| ----------------- | --------- | --------- | --------- |
| Jetson Nano       | ✅        | ❌        | ❌        |
| Jetson TX2        | ✅        | ❌        | ❌        |
| Jetson Xavier NX  | ✅        | ✅        | ❌        |
| Jetson AGX Xavier | ✅        | ✅        | ❌        |
| Jetson AGX Orin   | ❌        | ✅        | ✅        |
| Jetson Orin NX    | ❌        | ✅        | ✅        |
| Jetson Orin Nano  | ❌        | ✅        | ✅        |

## Quick Start with Docker

The fastest way to get started with Ultralytics YOLOv8 on NVIDIA Jetson is to run with pre-built docker images for Jetson. Refer to the table above and choose the JetPack version according to the Jetson device you own.

=== "JetPack 4"

    ```bash
    t=ultralytics/ultralytics:latest-jetson-jetpack4
    sudo docker pull $t && sudo docker run -it --ipc=host --runtime=nvidia $t
    ```

=== "JetPack 5"

    ```bash
    t=ultralytics/ultralytics:latest-jetson-jetpack5
    sudo docker pull $t && sudo docker run -it --ipc=host --runtime=nvidia $t
    ```

=== "JetPack 6"

    ```bash
    t=ultralytics/ultralytics:latest-jetson-jetpack6
    sudo docker pull $t && sudo docker run -it --ipc=host --runtime=nvidia $t
    ```

After this is done, skip to [Use TensorRT on NVIDIA Jetson section](#use-tensorrt-on-nvidia-jetson).

## Start with Native Installation

For a native installation without Docker, please refer to the steps below.

### Run on JetPack 6.x

#### Install Ultralytics Package

Here we will install Ultralytics package on the Jetson with optional dependencies so that we can export the [PyTorch](https://www.ultralytics.com/glossary/pytorch) models to other different formats. We will mainly focus on [NVIDIA TensorRT exports](../integrations/tensorrt.md) because TensorRT will make sure we can get the maximum performance out of the Jetson devices.

1. Update packages list, install pip and upgrade to latest

    ```bash
    sudo apt update
    sudo apt install python3-pip -y
    pip install -U pip
    ```

2. Install `ultralytics` pip package with optional dependencies

    ```bash
    pip install ultralytics[export]
    ```

3. Reboot the device

    ```bash
    sudo reboot
    ```

#### Install PyTorch and Torchvision

The above ultralytics installation will install Torch and Torchvision. However, these 2 packages installed via pip are not compatible to run on Jetson platform which is based on ARM64 architecture. Therefore, we need to manually install pre-built PyTorch pip wheel and compile/ install Torchvision from source.

Install `torch 2.3.0` and `torchvision 0.18` according to JP6.0

```bash
sudo apt-get install libopenmpi-dev libopenblas-base libomp-dev -y
pip install https://github.com/ultralytics/assets/releases/download/v0.0.0/torch-2.3.0-cp310-cp310-linux_aarch64.whl
pip install https://github.com/ultralytics/assets/releases/download/v0.0.0/torchvision-0.18.0a0+6043bc2-cp310-cp310-linux_aarch64.whl
```

Visit the [PyTorch for Jetson page](https://forums.developer.nvidia.com/t/pytorch-for-jetson/72048) to access all different versions of PyTorch for different JetPack versions. For a more detailed list on the PyTorch, Torchvision compatibility, visit the [PyTorch and Torchvision compatibility page](https://github.com/pytorch/vision).

#### Install `onnxruntime-gpu`

The [onnxruntime-gpu](https://pypi.org/project/onnxruntime-gpu/) package hosted in PyPI does not have `aarch64` binaries for the Jetson. So we need to manually install this package. This package is needed for some of the exports.

All different `onnxruntime-gpu` packages corresponding to different JetPack and Python versions are listed [here](https://elinux.org/Jetson_Zoo#ONNX_Runtime). However, here we will download and install `onnxruntime-gpu 1.18.0` with `Python3.10` support.

```bash
wget https://nvidia.box.com/shared/static/48dtuob7meiw6ebgfsfqakc9vse62sg4.whl -O onnxruntime_gpu-1.18.0-cp310-cp310-linux_aarch64.whl
pip install onnxruntime_gpu-1.18.0-cp310-cp310-linux_aarch64.whl
```

!!! note

    `onnxruntime-gpu` will automatically revert back the numpy version to latest. So we need to reinstall numpy to `1.23.5` to fix an issue by executing:

    `pip install numpy==1.23.5`

### Run on JetPack 5.x

#### Install Ultralytics Package

Here we will install Ultralytics package on the Jetson with optional dependencies so that we can export the PyTorch models to other different formats. We will mainly focus on [NVIDIA TensorRT exports](../integrations/tensorrt.md) because TensorRT will make sure we can get the maximum performance out of the Jetson devices.

1. Update packages list, install pip and upgrade to latest

    ```bash
    sudo apt update
    sudo apt install python3-pip -y
    pip install -U pip
    ```

2. Install `ultralytics` pip package with optional dependencies

    ```bash
    pip install ultralytics[export]
    ```

3. Reboot the device

    ```bash
    sudo reboot
    ```

#### Install PyTorch and Torchvision

The above ultralytics installation will install Torch and Torchvision. However, these 2 packages installed via pip are not compatible to run on Jetson platform which is based on ARM64 architecture. Therefore, we need to manually install pre-built PyTorch pip wheel and compile/ install Torchvision from source.

1. Uninstall currently installed PyTorch and Torchvision

    ```bash
    pip uninstall torch torchvision
    ```

2. Install PyTorch 2.1.0 according to JP5.1.3

    ```bash
    sudo apt-get install -y libopenblas-base libopenmpi-dev
    wget https://developer.download.nvidia.com/compute/redist/jp/v512/pytorch/torch-2.1.0a0+41361538.nv23.06-cp38-cp38-linux_aarch64.whl -O torch-2.1.0a0+41361538.nv23.06-cp38-cp38-linux_aarch64.whl
    pip install torch-2.1.0a0+41361538.nv23.06-cp38-cp38-linux_aarch64.whl
    ```

3. Install Torchvision v0.16.2 according to PyTorch v2.1.0

    ```bash
    sudo apt install -y libjpeg-dev zlib1g-dev
    git clone https://github.com/pytorch/vision torchvision
    cd torchvision
    git checkout v0.16.2
    python3 setup.py install --user
    ```

Visit the [PyTorch for Jetson page](https://forums.developer.nvidia.com/t/pytorch-for-jetson/72048) to access all different versions of PyTorch for different JetPack versions. For a more detailed list on the PyTorch, Torchvision compatibility, visit the [PyTorch and Torchvision compatibility page](https://github.com/pytorch/vision).

#### Install `onnxruntime-gpu`

The [onnxruntime-gpu](https://pypi.org/project/onnxruntime-gpu/) package hosted in PyPI does not have `aarch64` binaries for the Jetson. So we need to manually install this package. This package is needed for some of the exports.

All different `onnxruntime-gpu` packages corresponding to different JetPack and Python versions are listed [here](https://elinux.org/Jetson_Zoo#ONNX_Runtime). However, here we will download and install `onnxruntime-gpu 1.17.0` with `Python3.8` support.

```bash
wget https://nvidia.box.com/shared/static/zostg6agm00fb6t5uisw51qi6kpcuwzd.whl -O onnxruntime_gpu-1.17.0-cp38-cp38-linux_aarch64.whl
pip install onnxruntime_gpu-1.17.0-cp38-cp38-linux_aarch64.whl
```

!!! note

    `onnxruntime-gpu` will automatically revert back the numpy version to latest. So we need to reinstall numpy to `1.23.5` to fix an issue by executing:

    `pip install numpy==1.23.5`

## Use TensorRT on NVIDIA Jetson

Out of all the model export formats supported by Ultralytics, TensorRT delivers the best inference performance when working with NVIDIA Jetson devices and our recommendation is to use TensorRT with Jetson. We also have a detailed document on TensorRT [here](../integrations/tensorrt.md).

## Convert Model to TensorRT and Run Inference

The YOLOv8n model in PyTorch format is converted to TensorRT to run inference with the exported model.

!!! example

    === "Python"

        ```python
        from ultralytics import YOLO

        # Load a YOLOv8n PyTorch model
        model = YOLO("yolov8n.pt")

        # Export the model
        model.export(format="engine")  # creates 'yolov8n.engine'

        # Load the exported TensorRT model
        trt_model = YOLO("yolov8n.engine")

        # Run inference
        results = trt_model("https://ultralytics.com/images/bus.jpg")
        ```

    === "CLI"

        ```bash
        # Export a YOLOv8n PyTorch model to TensorRT format
        yolo export model=yolov8n.pt format=engine  # creates 'yolov8n.engine'

        # Run inference with the exported model
        yolo predict model=yolov8n.engine source='https://ultralytics.com/images/bus.jpg'
        ```

!!! note

    Visit the [Export page](../modes/export.md#arguments) to access additional arguments when exporting models to different model formats

## NVIDIA Jetson Orin YOLOv8 Benchmarks

YOLOv8 benchmarks were run by the Ultralytics team on 10 different model formats measuring speed and [accuracy](https://www.ultralytics.com/glossary/accuracy): PyTorch, TorchScript, ONNX, OpenVINO, TensorRT, TF SavedModel, TF GraphDef, TF Lite, PaddlePaddle, NCNN. Benchmarks were run on Seeed Studio reComputer J4012 powered by Jetson Orin NX 16GB device at FP32 [precision](https://www.ultralytics.com/glossary/precision) with default input image size of 640.

### Comparison Chart

Even though all model exports are working with NVIDIA Jetson, we have only included **PyTorch, TorchScript, TensorRT** for the comparison chart below because, they make use of the GPU on the Jetson and are guaranteed to produce the best results. All the other exports only utilize the CPU and the performance is not as good as the above three. You can find benchmarks for all exports in the section after this chart.

<div style="text-align: center;">
    <img width="800" src="https://github.com/ultralytics/docs/releases/download/0/nvidia-jetson-ecosystem-2.avif" alt="NVIDIA Jetson Ecosystem">
</div>

### Detailed Comparison Table

The below table represents the benchmark results for five different models (YOLOv8n, YOLOv8s, YOLOv8m, YOLOv8l, YOLOv8x) across ten different formats (PyTorch, TorchScript, ONNX, OpenVINO, TensorRT, TF SavedModel, TF GraphDef, TF Lite, PaddlePaddle, NCNN), giving us the status, size, mAP50-95(B) metric, and inference time for each combination.

!!! performance

    === "YOLOv8n"

        | Format          | Status | Size on disk (MB) | mAP50-95(B) | Inference time (ms/im) |
        |-----------------|--------|-------------------|-------------|------------------------|
        | PyTorch         | ✅      | 6.2               | 0.6381      | 14.3                   |
        | TorchScript     | ✅      | 12.4              | 0.6117      | 13.3                   |
        | ONNX            | ✅      | 12.2              | 0.6092      | 70.6                   |
        | OpenVINO        | ✅      | 12.3              | 0.6092      | 104.2                  |
        | TensorRT (FP32) | ✅      | 16.1              | 0.6091      | 8.01                   |
        | TensorRT (FP16) | ✅      | 9.2               | 0.6093      | 4.55                   |
        | TensorRT (INT8) | ✅      | 5.9               | 0.2759      | 4.09                   |
        | TF SavedModel   | ✅      | 30.6              | 0.6092      | 141.74                 |
        | TF GraphDef     | ✅      | 12.3              | 0.6092      | 199.93                 |
        | TF Lite         | ✅      | 12.3              | 0.6092      | 349.18                 |
        | PaddlePaddle    | ✅      | 24.4              | 0.6030      | 555                    |
        | NCNN            | ✅      | 12.2              | 0.6092      | 32                     |

    === "YOLOv8s"

        | Format          | Status | Size on disk (MB) | mAP50-95(B) | Inference time (ms/im) |
        |-----------------|--------|-------------------|-------------|------------------------|
        | PyTorch         | ✅      | 21.5              | 0.6967      | 18                     |
        | TorchScript     | ✅      | 43.0              | 0.7136      | 23.81                  |
        | ONNX            | ✅      | 42.8              | 0.7136      | 185.55                 |
        | OpenVINO        | ✅      | 42.9              | 0.7136      | 243.97                 |
        | TensorRT (FP32) | ✅      | 46.4              | 0.7136      | 14.01                  |
        | TensorRT (FP16) | ✅      | 24.2              | 0.722       | 7.16                   |
        | TensorRT (INT8) | ✅      | 13.7              | 0.4233      | 5.49                   |
        | TF SavedModel   | ✅      | 107               | 0.7136      | 260.03                 |
        | TF GraphDef     | ✅      | 42.8              | 0.7136      | 423.4                  |
        | TF Lite         | ✅      | 42.8              | 0.7136      | 1046.64                |
        | PaddlePaddle    | ✅      | 85.5              | 0.7140      | 1464                   |
        | NCNN            | ✅      | 42.7              | 0.7200      | 63                     |

    === "YOLOv8m"

        | Format          | Status | Size on disk (MB) | mAP50-95(B) | Inference time (ms/im) |
        |-----------------|--------|-------------------|-------------|------------------------|
        | PyTorch         | ✅      | 49.7              | 0.7370      | 36.4                   |
        | TorchScript     | ✅      | 99.2              | 0.7285      | 53.58                  |
        | ONNX            | ✅      | 99                | 0.7280      | 452.09                 |
        | OpenVINO        | ✅      | 99.1              | 0.7280      | 544.36                 |
        | TensorRT (FP32) | ✅      | 102.4             | 0.7285      | 31.51                  |
        | TensorRT (FP16) | ✅      | 52.6              | 0.7324      | 14.88                  |
        | TensorRT (INT8) | ✅      | 28.6              | 0.3283      | 10.89                  |
        | TF SavedModel   | ✅      | 247.5             | 0.7280      | 543.65                 |
        | TF GraphDef     | ✅      | 99                | 0.7280      | 906.63                 |
        | TF Lite         | ✅      | 99                | 0.7280      | 2758.08                |
        | PaddlePaddle    | ✅      | 197.9             | 0.7280      | 3678                   |
        | NCNN            | ✅      | 98.9              | 0.7260      | 135                    |

    === "YOLOv8l"

        | Format          | Status | Size on disk (MB) | mAP50-95(B) | Inference time (ms/im) |
        |-----------------|--------|-------------------|-------------|------------------------|
        | PyTorch         | ✅      | 83.7              | 0.7768      | 61.3                   |
        | TorchScript     | ✅      | 167.2             | 0.7554      | 87.9                   |
        | ONNX            | ✅      | 166.8             | 0.7551      | 852.29                 |
        | OpenVINO        | ✅      | 167               | 0.7551      | 1012.6                 |
        | TensorRT (FP32) | ✅      | 170.5             | 0.7554      | 49.79                  |
        | TensorRT (FP16) | ✅      | 86.1              | 0.7535      | 22.89                  |
        | TensorRT (INT8) | ✅      | 46.4              | 0.4048      | 14.61                  |
        | TF SavedModel   | ✅      | 417.2             | 0.7551      | 990.45                 |
        | TF GraphDef     | ✅      | 166.9             | 0.7551      | 1649.86                |
        | TF Lite         | ✅      | 166.9             | 0.7551      | 5652.37                |
        | PaddlePaddle    | ✅      | 333.6             | 0.7551      | 7114.67                |
        | NCNN            | ✅      | 166.8             | 0.7685      | 231.9                  |

    === "YOLOv8x"

        | Format          | Status | Size on disk (MB) | mAP50-95(B) | Inference time (ms/im) |
        |-----------------|--------|-------------------|-------------|------------------------|
        | PyTorch         | ✅      | 130.5             | 0.7759      | 93                     |
        | TorchScript     | ✅      | 260.7             | 0.7472      | 135.1                  |
        | ONNX            | ✅      | 260.4             | 0.7479      | 1296.13                |
        | OpenVINO        | ✅      | 260.6             | 0.7479      | 1502.15                |
        | TensorRT (FP32) | ✅      | 264.0             | 0.7469      | 80.01                  |
        | TensorRT (FP16) | ✅      | 133.3             | 0.7513      | 40.76                  |
        | TensorRT (INT8) | ✅      | 70.2              | 0.4277      | 22.08                  |
        | TF SavedModel   | ✅      | 651.1             | 0.7479      | 1451.76                |
        | TF GraphDef     | ✅      | 260.5             | 0.7479      | 4029.36                |
        | TF Lite         | ✅      | 260.4             | 0.7479      | 8772.86                |
        | PaddlePaddle    | ✅      | 520.8             | 0.7479      | 10619.53               |
        | NCNN            | ✅      | 260.4             | 0.7646      | 376.38                 |

[Explore more benchmarking efforts by Seeed Studio](https://www.seeedstudio.com/blog/2023/03/30/yolov8-performance-benchmarks-on-nvidia-jetson-devices) running on different versions of NVIDIA Jetson hardware.

## Reproduce Our Results

To reproduce the above Ultralytics benchmarks on all export [formats](../modes/export.md) run this code:

!!! example

    === "Python"

        ```python
        from ultralytics import YOLO

        # Load a YOLOv8n PyTorch model
        model = YOLO("yolov8n.pt")

        # Benchmark YOLOv8n speed and accuracy on the COCO8 dataset for all all export formats
        results = model.benchmarks(data="coco8.yaml", imgsz=640)
        ```

    === "CLI"

        ```bash
        # Benchmark YOLOv8n speed and accuracy on the COCO8 dataset for all all export formats
        yolo benchmark model=yolov8n.pt data=coco8.yaml imgsz=640
        ```

    Note that benchmarking results might vary based on the exact hardware and software configuration of a system, as well as the current workload of the system at the time the benchmarks are run. For the most reliable results use a dataset with a large number of images, i.e. `data='coco8.yaml' (4 val images), or `data='coco.yaml'` (5000 val images).

## Best Practices when using NVIDIA Jetson

When using NVIDIA Jetson, there are a couple of best practices to follow in order to enable maximum performance on the NVIDIA Jetson running YOLOv8.

1. Enable MAX Power Mode

    Enabling MAX Power Mode on the Jetson will make sure all CPU, GPU cores are turned on.

    ```bash
    sudo nvpmodel -m 0
    ```

2. Enable Jetson Clocks

    Enabling Jetson Clocks will make sure all CPU, GPU cores are clocked at their maximum frequency.

    ```bash
    sudo jetson_clocks
    ```

3. Install Jetson Stats Application

    We can use jetson stats application to monitor the temperatures of the system components and check other system details such as view CPU, GPU, RAM utilization, change power modes, set to max clocks, check JetPack information

    ```bash
    sudo apt update
    sudo pip install jetson-stats
    sudo reboot
    jtop
    ```

<img width="1024" src="https://github.com/ultralytics/docs/releases/download/0/jetson-stats-application.avif" alt="Jetson Stats">

## Next Steps

Congratulations on successfully setting up YOLOv8 on your NVIDIA Jetson! For further learning and support, visit more guide at [Ultralytics YOLOv8 Docs](../index.md)!

## FAQ

### How do I deploy Ultralytics YOLOv8 on NVIDIA Jetson devices?

Deploying Ultralytics YOLOv8 on NVIDIA Jetson devices is a straightforward process. First, flash your Jetson device with the NVIDIA JetPack SDK. Then, either use a pre-built Docker image for quick setup or manually install the required packages. Detailed steps for each approach can be found in sections [Quick Start with Docker](#quick-start-with-docker) and [Start with Native Installation](#start-with-native-installation).

### What performance benchmarks can I expect from YOLOv8 models on NVIDIA Jetson devices?

YOLOv8 models have been benchmarked on various NVIDIA Jetson devices showing significant performance improvements. For example, the TensorRT format delivers the best inference performance. The table in the [Detailed Comparison Table](#detailed-comparison-table) section provides a comprehensive view of performance metrics like mAP50-95 and inference time across different model formats.

### Why should I use TensorRT for deploying YOLOv8 on NVIDIA Jetson?

TensorRT is highly recommended for deploying YOLOv8 models on NVIDIA Jetson due to its optimal performance. It accelerates inference by leveraging the Jetson's GPU capabilities, ensuring maximum efficiency and speed. Learn more about how to convert to TensorRT and run inference in the [Use TensorRT on NVIDIA Jetson](#use-tensorrt-on-nvidia-jetson) section.

### How can I install PyTorch and Torchvision on NVIDIA Jetson?

To install PyTorch and Torchvision on NVIDIA Jetson, first uninstall any existing versions that may have been installed via pip. Then, manually install the compatible PyTorch and Torchvision versions for the Jetson's ARM64 architecture. Detailed instructions for this process are provided in the [Install PyTorch and Torchvision](#install-pytorch-and-torchvision) section.

### What are the best practices for maximizing performance on NVIDIA Jetson when using YOLOv8?

To maximize performance on NVIDIA Jetson with YOLOv8, follow these best practices:

1. Enable MAX Power Mode to utilize all CPU and GPU cores.
2. Enable Jetson Clocks to run all cores at their maximum frequency.
3. Install the Jetson Stats application for monitoring system metrics.

For commands and additional details, refer to the [Best Practices when using NVIDIA Jetson](#best-practices-when-using-nvidia-jetson) section.
