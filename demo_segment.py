import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'true'

import cv2
import numpy as np
import tensorflow as tf 
#import segmentation_models as sm
import importlib
import glob
from tensorflow.keras.metrics import TrueNegatives, TruePositives, FalseNegatives, FalsePositives
from tensorflow.keras.callbacks import Callback, ModelCheckpoint, ReduceLROnPlateau, CSVLogger, EarlyStopping, LearningRateScheduler, TensorBoard
#from tensorflow.graph_util import convert_variables_to_constants, remove_training_nodes
#from segmentation_models import Unet
#from segmentation_models.metrics import IOUScore, FScore, Precision, Recall

#from model.datasets import Dataset, Dataloader, get_training_augmentation, get_validation_augmentation, visualize

CONFIG_NAME = "config01"
MODEL_PATH = "./saved_models/config01/model_.008-0.512481.h5"
IMAGE_FOLDER = "./testing/image-1"
OUTPUT_FOLDER = "test_results-h"

from model.list_config import config01 as cfg
tf.keras.backend.set_learning_phase(False)
model = tf.keras.models.load_model(MODEL_PATH, compile=False)
print('success')

# Create output folder
import pathlib
pathlib.Path(OUTPUT_FOLDER).mkdir(parents=True, exist_ok=True)

img_paths = os.listdir(IMAGE_FOLDER)
for img_path in img_paths:

    if not (img_path.endswith("jpg") or img_path.endswith("png")):
        continue

    print(img_path)

    input_path = os.path.join(IMAGE_FOLDER, img_path)
    output_path = os.path.join(OUTPUT_FOLDER, img_path)
    img = cv2.imread(input_path, cv2.IMREAD_COLOR)
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (cfg.image_size, cfg.image_size), interpolation=cv2.INTER_NEAREST)

    net_input = np.expand_dims(img, axis=0)
    pr_mask = model.predict(net_input)[0]
    pr_mask *= 255
    pr_mask = pr_mask.astype(np.uint8)
    pr_mask = cv2.cvtColor(pr_mask, cv2.COLOR_GRAY2BGR)

    result = np.concatenate((img, pr_mask), axis=1)
    cv2.imwrite(output_path, result)

