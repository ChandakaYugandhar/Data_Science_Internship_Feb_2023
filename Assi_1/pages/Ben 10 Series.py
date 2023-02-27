import streamlit as st
from matplotlib import image
import pandas as pd
import os

st.title("Dashboard - Ben 10 Versions")

FILE_DIR = os.path.dirname(os.path.abspath(__file__))

PARENT_DIR = os.path.join(FILE_DIR, os.pardir)

dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "ben10.jpg")

img = image.imread(IMAGE_PATH)
st.image(img)

st.header("Select the Series:")
power = st.selectbox("To See Poster",{"Ben10_Classic","Ben10_Alien_Force","Ben10_Ultimate","Ben10_Omniverse","Ben10_Reboot"})
    
if power == 'Ben10_Classic':
    IMAGE_PATH1 = os.path.join(dir_of_interest, "images", "Ben-10-Classic.jpg")
    imgg = image.imread(IMAGE_PATH1)
    st.image(imgg)
if power == 'Ben10_Alien_Force':
    IMAGE_PATH1 = os.path.join(dir_of_interest, "images", "alien force.jpg")
    imgg = image.imread(IMAGE_PATH1)
    st.image(imgg)
if power == 'Ben10_Ultimate':
    IMAGE_PATH1 = os.path.join(dir_of_interest, "images", "ultimate.jpg")
    imgg = image.imread(IMAGE_PATH1)
    st.image(imgg)
if power == 'Ben10_Omniverse':
    IMAGE_PATH1 = os.path.join(dir_of_interest, "images", "omniverse.jpg")
    imgg = image.imread(IMAGE_PATH1)
    st.image(imgg)
if power == 'Ben10_Reboot':
    IMAGE_PATH1 = os.path.join(dir_of_interest, "images", "reboot.jpg")
    imgg = image.imread(IMAGE_PATH1)
    st.image(imgg)








