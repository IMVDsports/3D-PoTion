import os, sys
import numpy as np
import scipy.io as sio
from collections import Counter
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import cv2
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
import matplotlib.image as mpimg
import imageio
import h5py
import random
from PIL import Image
import json
from astropy.modeling.models import Gaussian2D
from numpy.random import randint
import random

from keras.utils import to_categorical
from tensorflow.keras.utils import Sequence
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Flatten,Dropout,Activation,Average,Concatenate
#from tensorflow.keras import Sequential
#from tensorflow.keras.layers import Conv2D, Flatten, Dense
from tensorflow.keras.layers import Conv2D,GlobalAveragePooling2D
# from tensorflow.keras.layers.normalization import BatchNormalization
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras import backend as K # see the image_data_format information
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam,SGD
# from tensorflow.keras.models import Model, load_model
from tensorflow.keras.models import load_model
from tensorflow.keras import Model
from tensorflow.keras.callbacks import TensorBoard,EarlyStopping,ModelCheckpoint,LearningRateScheduler,ReduceLROnPlateau
from sklearn.metrics import classification_report

from numpy.random import seed    # fix random seed
seed(1)
import tensorflow
tensorflow.random.set_seed(2)

config={}
####################
# training settings
####################
config['data_format']=K.image_data_format()
config['num_classes']=15
config['n_filters']=[64,128,256]
config['strides']=[2,1,2,1,2,1,]
config['kernel_size']=3
config['kernel_initializer']='glorot_uniform'
config['dropout_rate']=0.25
config['activation']='relu'
config['optimizer']='adam'
config['loss']='categorical_crossentropy'
config['epoch']=100
config['batch_size']=32
config['lr']=1e-4


#####################
# IO settings
#####################
config['model_name']='gt-labels2-normtest-32'
config['dir_potion']=os.path.join('/usr/local/data01/julienbe/PoTion',config['model_name'])
config['n_channels']=105
config['frame_size']=32
config['output']='/usr/local/data01/julienbe/3D-PoTion/src/output'