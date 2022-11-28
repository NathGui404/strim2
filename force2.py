# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 15:31:18 2022

@author: nguil
"""

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

st.sidebar.title('Ca parle de voitures')
st.sidebar.image('bugatti.jpg')
st.title('Toi tu aimes les voitures!')
# data !
link = 'https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv'
df_cars = pd.read_csv(link)

# Selection continent
st.sidebar.write('Choisis bien ton continent !')
continent_list = df_cars['continent'].unique()
countries = st.sidebar.multiselect(
	"Choix des continents", 
	continent_list, 
	continent_list[0]
	)

# Table 
df_cars_continent = df_cars[df_cars['continent'].isin(countries)]
st.write('Caractéristiques voitures')
df_cars_continent

st.write("Petite analyse des corrélations qui ne mange pas de pain...")
st.write("Tu vas voir ce que tu vas voir !")

viz_correlation = sns.heatmap(df_cars.corr(), center=0, cmap = sns.color_palette("vlag", as_cmap=True), annot=True)

st.pyplot(viz_correlation.figure)

# graph 2


fig = plt.figure(figsize=(12, 9))
fig = px.scatter(data_frame=df_cars,
                   y= "mpg", x="weightlbs",
                   color="continent",
                   )
fig.update_layout(title ="Distance parcourue en fonction du poids des véhicules",
                   title_x = 0.5,
                   dragmode='select',
                   width=1300,
                   height=700,
                   hovermode='closest',
                   template='plotly_dark')
st.plotly_chart(fig, use_container_width=True)
st.write("Plus la voiture est lourde, moins elle fait de miles!")
