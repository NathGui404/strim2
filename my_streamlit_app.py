# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import seaborn as sns

st.title('On va voir des voitures')
st.write("j'adore les voitures")
st.image(img, width=200))
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)

viz_correlation = sns.heatmap(df_cars.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

st.pyplot(viz_correlation.figure)
