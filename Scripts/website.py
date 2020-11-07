import streamlit as st
import cv2
import os
import numpy as np
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import zipfile

from collections import defaultdict
from io import StringIO, BytesIO
from matplotlib import pyplot as plt
from PIL import Image

sys.path.append("..")
from object_detection.utils import ops as utils_ops

from utils import label_map_util

from utils import visualization_utils as vis_util

from correct import corrections, run_inference_for_single_image, load_image_into_numpy_array


st.write("""
# Malaria Detection Personal Project
Detecting *Plasmodium falciparum* with Machine Learning

***WARNING: Please do not use this for medical purposes.***


	""")
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

cwd = os.getcwd()
currentpath = cwd.replace("object_detection", "")

collectionImage = cv2.imread(currentpath + '/usingTripod.jpg')
st.image(collectionImage, caption='Data being collected in Rwanda.')

uploaded_file = st.file_uploader("Upload Image", type=['png', 'jpg'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image.save('beforeAnnotations.jpg')
    st.image(image, caption='Uploaded Image.', use_column_width=True)

#st.image(filename)

if st.button('Detect parasites'):
    corrections('beforeAnnotations.jpg')

    annotationsImage = cv2.imread('annotations.jpg')
    st.image(annotationsImage, caption='Parasites detected.')



st.write("""
 












©️ Leo Strijbos 2020
    """)