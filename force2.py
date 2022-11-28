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

continent_liste=np.append(df_cars['continent'].unique(),'All') 

continent=st.radio(
    "select a continent",
    continent_liste,
    key=1


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

  # graph 2
   # distance parcourue par gallon consommée - Plus la voiture est lourde, moins elle fait de miles
fig = plt.figure(figsize=(12, 9))
fig = px.scatter(data_frame = df_cars,
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
st.plotly_chart(fig, config = config, use_container_width = True)
