import os
import pathlib
import numpy as np
import scipy as sp
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import models

def STFT(x):
    X = np.fft.rfft(np.reshape(x,(64,254)),axis=1)
    Xc = np.real(X)
    Xs = np.imag(X)
    X = np.reshape(np.hstack((Xc,Xs)),(128,128))
    return X

def ISTFT(X):
    Xc = X[0::2,:]
    Xs = X[1::2,:]
    X = Xc + 1j*Xs
    return np.reshape(np.fft.irfft(X,axis=1),-1)

def play_audio(x):
    return display.Audio(np.reshape(x,-1), rate=16000)

def load_mini_speech_commands():
    DATASET_PATH = 'data/mini_speech_commands'

    data_dir = pathlib.Path(DATASET_PATH)
    if not data_dir.exists():
      tf.keras.utils.get_file(
          'mini_speech_commands.zip',
          origin="http://storage.googleapis.com/download.tensorflow.org/data/mini_speech_commands.zip",
          extract=True,
          cache_dir='.', cache_subdir='data')

    train_ds, val_ds = tf.keras.utils.audio_dataset_from_directory(
        directory=data_dir,
        batch_size=None,
        validation_split=0.2,
        seed=0,
        output_sequence_length=16256,
        subset='both')
    
    X = []
    y = []
    Xv = []
    yv = []
    for xi,yi in train_ds:
        X.append(np.expand_dims(STFT(xi),0))
        y.append(yi)
    for xi,yi in val_ds:
        Xv.append(np.expand_dims(STFT(xi),0))
        yv.append(yi)
    X = np.vstack(X)
    y = np.vstack(y)
    Xv = np.vstack(Xv)
    yv = np.vstack(yv)
    
    # X = np.vstack([np.expand_dims(STFT(x),0) for x,_ in train_ds])
    # y = np.vstack([y for _,y in train_ds])
    # Xv = np.vstack([np.expand_dims(STFT(x),0) for x,_ in val_ds])
    # yv = np.vstack([y for _,y in val_ds])
    
    return X, y, Xv, yv