import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

FILE_DIR = os.path.dirname(os.path.abspath(__file__))

PARENT_DIR = os.path.join(FILE_DIR, os.pardir)

dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "logo.png")
DATA_PATH = os.path.join(dir_of_interest, "data", "Ben_10_Data_Set.csv")

st.title("Dashboard - BEN 10 Powers")

img = image.imread(IMAGE_PATH)
st.image(img)

st.header("Characters Data")

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

st.header("Select the Series:")

Series_ = st.selectbox(" ", df['Ben_10_Series'].unique())

col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['Ben_10_Series'] == Series_], x="Type")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['Ben_10_Series'] == Series_], y="Power_Level")
col2.plotly_chart(fig_2, use_container_width=True)