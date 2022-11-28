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

st.sidebar.image('bugatti.jpg', caption='Bugatti')
st.title('Toi tu aimes les voitures!')
# data !
link = 'https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv'
df_auto = pd.read_csv(link)

# Selection continent
continent_list = df_auto['continent'].unique()
countries = st.sidebar.multiselect(
	"Choix des continents", 
	continent_list, 
	continent_list[0]
	)

# Table 
df_auto_continent = df_auto[df_auto['continent'].isin(countries)]
st.write('Caractéristiques voitures')
df_auto_continent





st.write("Tu vas voir ce que tu vas voir !")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"


st.write("Petite analyse des corrélations qui ne mange pas de pain")

viz_correlation = sns.heatmap(df_cars.corr(), center=0, cmap = sns.color_palette("vlag", as_cmap=True), annot=True)

st.pyplot(viz_correlation.figure)

# graph 2
# distance parcourue par gallon consommée - Plus la voiture est lourde, moins elle fait de miles

fig = plt.figure(figsize=(12, 9))
fig = px.scatter(data_frame=df_cars,
                   y= "Miles per gallon_(mpg)", x="Weight_Lbs",
                   color="Continent",
                   )
fig.update_layout(title ="bDistance parcourue en fonction du poids des véhiculesb",
                   title_x = 0.5,
                   dragmode='select',
                   width=1300,
                   height=700,
                   hovermode='closest',
                   template='plotly_dark')
st.plotly_chart(fig, config=config, use_container_width=True)
