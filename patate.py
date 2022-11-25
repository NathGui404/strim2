import streamlit as st
import pandas as pd
import numpy as np

st.title('Hello Wilders, welcome to my application!')

name = st.text_input("Please give me your name :")
name_length = len(name)
st.write("Your name has ",name_length,"characters")
st.title('Même si aucun rapport avec le début, on va étudier des correlations avec des voitures')
st.write("j'adore les voitures")
st.write("jamais une heatmap n'aura été si belle")
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)

viz_correlation = sns.heatmap(df_cars.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

st.pyplot(viz_correlation.figure)
