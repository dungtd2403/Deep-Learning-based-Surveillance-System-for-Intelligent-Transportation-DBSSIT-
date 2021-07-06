**Deep Learning based Surveillance System for Intelligent Transportation**

In this repository, a deep learning based approach for surveillance camera is presented.
Our system composes of 3 tasks:
* Object Detection: Automatically localizing and classifying different types of vehicles on the street. This is done using YOLOv4-tiny [[1]](#1).
* Object Tracking: Assign ID to each detected object. The object tracker is applied using Deep Sort [[2]](#2).
* Lane detection: Classifying each pixel if it belongs to a lane line or not. This is done using a U-net based segmentation neural network. [[3]](#3).

How to run:
1. Train YOLOv4-tiny using Darknet repository
2. Run save_model.py
3. Train U-net using \ref{} this repo
4. Run DBSSIT.py with saved YOLO and U-net models. 


## References
<a id="1">[1]</a> Wang, C.-Y., Bochkovskiy, A., and Liao, H.-Y. M., “Scaled-YOLOv4: Scaling Cross Stage Partial Network”, <i>arXiv e-prints</i>, 2020.
<a id="2">[2]</a> N. Wojke, A. Bewley and D. Paulus, "Simple online and realtime tracking with a deep association metric," 2017 IEEE International Conference on Image Processing (ICIP), 2017, pp. 3645-3649, doi: 10.1109/ICIP.2017.8296962.
<a id="3">[3]</a> Ronneberger, O., Fischer, P., and Brox, T., “U-Net: Convolutional Networks for Biomedical Image Segmentation”, <i>arXiv e-prints</i>, 2015.
