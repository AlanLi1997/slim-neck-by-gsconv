---
comments: true
description: Optimize your fitness routine with real-time workouts monitoring using Ultralytics YOLOv8. Track and improve your exercise form and performance.
keywords: workouts monitoring, Ultralytics YOLOv8, pose estimation, fitness tracking, exercise assessment, real-time feedback, exercise form, performance metrics
---

# Workouts Monitoring using Ultralytics YOLOv8

Monitoring workouts through pose estimation with [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics/) enhances exercise assessment by accurately tracking key body landmarks and joints in real-time. This technology provides instant feedback on exercise form, tracks workout routines, and measures performance metrics, optimizing training sessions for users and trainers alike.

<p align="center">
  <br>
  <iframe loading="lazy" width="720" height="405" src="https://www.youtube.com/embed/LGGxqLZtvuw"
    title="YouTube video player" frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen>
  </iframe>
  <br>
  <strong>Watch:</strong> Workouts Monitoring using Ultralytics YOLOv8 | Pushups, Pullups, Ab Workouts
</p>

## Advantages of Workouts Monitoring?

- **Optimized Performance:** Tailoring workouts based on monitoring data for better results.
- **Goal Achievement:** Track and adjust fitness goals for measurable progress.
- **Personalization:** Customized workout plans based on individual data for effectiveness.
- **Health Awareness:** Early detection of patterns indicating health issues or over-training.
- **Informed Decisions:** Data-driven decisions for adjusting routines and setting realistic goals.

## Real World Applications

|                                        Workouts Monitoring                                         |                                        Workouts Monitoring                                         |
| :------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------: |
| ![PushUps Counting](https://github.com/ultralytics/docs/releases/download/0/pushups-counting.avif) | ![PullUps Counting](https://github.com/ultralytics/docs/releases/download/0/pullups-counting.avif) |
|                                          PushUps Counting                                          |                                          PullUps Counting                                          |

!!! example "Workouts Monitoring Example"

    === "Workouts Monitoring"

        ```python
        import cv2

        from ultralytics import YOLO, solutions

        model = YOLO("yolov8n-pose.pt")
        cap = cv2.VideoCapture("path/to/video/file.mp4")
        assert cap.isOpened(), "Error reading video file"
        w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

        gym_object = solutions.AIGym(
            line_thickness=2,
            view_img=True,
            pose_type="pushup",
            kpts_to_check=[6, 8, 10],
        )

        while cap.isOpened():
            success, im0 = cap.read()
            if not success:
                print("Video frame is empty or video processing has been successfully completed.")
                break
            results = model.track(im0, verbose=False)  # Tracking recommended
            # results = model.predict(im0)  # Prediction also supported
            im0 = gym_object.start_counting(im0, results)

        cv2.destroyAllWindows()
        ```

    === "Workouts Monitoring with Save Output"

        ```python
        import cv2

        from ultralytics import YOLO, solutions

        model = YOLO("yolov8n-pose.pt")
        cap = cv2.VideoCapture("path/to/video/file.mp4")
        assert cap.isOpened(), "Error reading video file"
        w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

        video_writer = cv2.VideoWriter("workouts.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

        gym_object = solutions.AIGym(
            line_thickness=2,
            view_img=True,
            pose_type="pushup",
            kpts_to_check=[6, 8, 10],
        )

        while cap.isOpened():
            success, im0 = cap.read()
            if not success:
                print("Video frame is empty or video processing has been successfully completed.")
                break
            results = model.track(im0, verbose=False)  # Tracking recommended
            # results = model.predict(im0)  # Prediction also supported
            im0 = gym_object.start_counting(im0, results)
            video_writer.write(im0)

        cv2.destroyAllWindows()
        video_writer.release()
        ```

???+ tip "Support"

    "pushup", "pullup" and "abworkout" supported

### KeyPoints Map

![keyPoints Order Ultralytics YOLOv8 Pose](https://github.com/ultralytics/docs/releases/download/0/keypoints-order-ultralytics-yolov8-pose.avif)

### Arguments `AIGym`

| Name              | Type    | Default  | Description                                                                            |
| ----------------- | ------- | -------- | -------------------------------------------------------------------------------------- |
| `kpts_to_check`   | `list`  | `None`   | List of three keypoints index, for counting specific workout, followed by keypoint Map |
| `line_thickness`  | `int`   | `2`      | Thickness of the lines drawn.                                                          |
| `view_img`        | `bool`  | `False`  | Flag to display the image.                                                             |
| `pose_up_angle`   | `float` | `145.0`  | Angle threshold for the 'up' pose.                                                     |
| `pose_down_angle` | `float` | `90.0`   | Angle threshold for the 'down' pose.                                                   |
| `pose_type`       | `str`   | `pullup` | Type of pose to detect (`'pullup`', `pushup`, `abworkout`, `squat`).                   |

### Arguments `model.predict`

{% include "macros/predict-args.md" %}

### Arguments `model.track`

{% include "macros/track-args.md" %}

## FAQ

### How do I monitor my workouts using Ultralytics YOLOv8?

To monitor your workouts using Ultralytics YOLOv8, you can utilize the pose estimation capabilities to track and analyze key body landmarks and joints in real-time. This allows you to receive instant feedback on your exercise form, count repetitions, and measure performance metrics. You can start by using the provided example code for pushups, pullups, or ab workouts as shown:

```python
import cv2

from ultralytics import YOLO, solutions

model = YOLO("yolov8n-pose.pt")
cap = cv2.VideoCapture("path/to/video/file.mp4")
assert cap.isOpened(), "Error reading video file"
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

gym_object = solutions.AIGym(
    line_thickness=2,
    view_img=True,
    pose_type="pushup",
    kpts_to_check=[6, 8, 10],
)

while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        print("Video frame is empty or video processing has been successfully completed.")
        break
    results = model.track(im0, verbose=False)
    im0 = gym_object.start_counting(im0, results)

cv2.destroyAllWindows()
```

For further customization and settings, you can refer to the [AIGym](#arguments-aigym) section in the documentation.

### What are the benefits of using Ultralytics YOLOv8 for workout monitoring?

Using Ultralytics YOLOv8 for workout monitoring provides several key benefits:

- **Optimized Performance:** By tailoring workouts based on monitoring data, you can achieve better results.
- **Goal Achievement:** Easily track and adjust fitness goals for measurable progress.
- **Personalization:** Get customized workout plans based on your individual data for optimal effectiveness.
- **Health Awareness:** Early detection of patterns that indicate potential health issues or over-training.
- **Informed Decisions:** Make data-driven decisions to adjust routines and set realistic goals.

You can watch a [YouTube video demonstration](https://www.youtube.com/watch?v=LGGxqLZtvuw) to see these benefits in action.

### How accurate is Ultralytics YOLOv8 in detecting and tracking exercises?

Ultralytics YOLOv8 is highly accurate in detecting and tracking exercises due to its state-of-the-art pose estimation capabilities. It can accurately track key body landmarks and joints, providing real-time feedback on exercise form and performance metrics. The model's pretrained weights and robust architecture ensure high [precision](https://www.ultralytics.com/glossary/precision) and reliability. For real-world examples, check out the [real-world applications](#real-world-applications) section in the documentation, which showcases pushups and pullups counting.

### Can I use Ultralytics YOLOv8 for custom workout routines?

Yes, Ultralytics YOLOv8 can be adapted for custom workout routines. The `AIGym` class supports different pose types such as "pushup", "pullup", and "abworkout." You can specify keypoints and angles to detect specific exercises. Here is an example setup:

```python
from ultralytics import solutions

gym_object = solutions.AIGym(
    line_thickness=2,
    view_img=True,
    pose_type="squat",
    kpts_to_check=[6, 8, 10],
)
```

For more details on setting arguments, refer to the [Arguments `AIGym`](#arguments-aigym) section. This flexibility allows you to monitor various exercises and customize routines based on your needs.

### How can I save the workout monitoring output using Ultralytics YOLOv8?

To save the workout monitoring output, you can modify the code to include a video writer that saves the processed frames. Here's an example:

```python
import cv2

from ultralytics import YOLO, solutions

model = YOLO("yolov8n-pose.pt")
cap = cv2.VideoCapture("path/to/video/file.mp4")
assert cap.isOpened(), "Error reading video file"
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

video_writer = cv2.VideoWriter("workouts.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

gym_object = solutions.AIGym(
    line_thickness=2,
    view_img=True,
    pose_type="pushup",
    kpts_to_check=[6, 8, 10],
)

while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        print("Video frame is empty or video processing has been successfully completed.")
        break
    results = model.track(im0, verbose=False)
    im0 = gym_object.start_counting(im0, results)
    video_writer.write(im0)

cv2.destroyAllWindows()
video_writer.release()
```

This setup writes the monitored video to an output file. For more details, refer to the [Workouts Monitoring with Save Output](#workouts-monitoring-using-ultralytics-yolov8) section.
