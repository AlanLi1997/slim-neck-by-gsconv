from ultralytics import YOLO

if __name__ == '__main__':
    # initial model
    model = YOLO("gsconv-yolov8_9_10_11/ultralytics/cfg/models/v8/yolov8-gsconv.yaml") #
    # gsconv-yolov8_9_10_11/ultralytics/cfg/models/v8/yolov8n.yaml
    # gsconv-yolov8_9_10_11/ultralytics/cfg/models/v8/yolov8-gsconve.yaml
    # gsconv-yolov8_9_10_11/ultralytics/cfg/models/v8/yolov8-sn.yaml
    results = model.train(
        data="gsconv-yolov8_9_10_11/ultralytics/cfg/datasets/coco8.yaml",
        device='0',
        epochs=200,
        imgsz=640,
        batch=16,
        workers=16,
        rect=False,
        amp=False,
        optimizer='SGD',
        cache=True,
        name='exp-gsconv',
        resume=False,
        half=False,
        deterministic=False,
        vid_stride=1,
        v5loader=False,
        augment=False,
        # save_hybrid=True,

    )