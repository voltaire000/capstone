#imports
import tensorflow as tf
import pandas as import pd
import io
import os

from PIL import Image
from object_detection.utils import dataset_util
from collections import namedtuple, OrderedDict


# TO-DO replace this with label map
def class_text_to_int(row_label):
    if row_label == 'A-label':
        return 1
    elif row_label == 'B-Label':
        return 2
    elif row_label == 'C-label':
        return 3
    elif row_label == 'C-label':
        return 4
    elif row_label == 'D-label':
        return 5
    elif row_label == 'Ref-label':
        return 6
    elif row_label == 'Barcode-Label-1':
        return 7
    elif row_label == 'Barcode-Label-2':
        return 8
    elif row_label == 'Ref-Label':
        return 9
    else:
        return None
