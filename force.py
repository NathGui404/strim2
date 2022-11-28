# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 15:31:18 2022

@author: nguil
"""

import streamlit as st
import pandas as pd
import seaborn as sns

st.title('Toi tu aimes les voitures!')

st.write("Tu vas voir ce que tu vas voir !")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)
df_cars['continent']=df_cars['continent'].str.strip('123.!? \n\t')



if st.button('US'):
    st.write(df_cars[df_cars['continent']=='US'])
elif st.button('Europe'):
    st.write(df_cars[df_cars['continent']=='Europe'])
else:
    st.button('Japan')
    st.write(df_cars[df_cars['continent']=='Japan'])



viz_correlation = sns.heatmap(df_cars.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True),
                                annot=True
								)

st.pyplot(viz_correlation.figure)