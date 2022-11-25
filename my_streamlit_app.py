# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import seaborn as sns


# radio button
# first argument is the title of the radio button
# second argument is the options for the ratio button
status = st.radio("Quel est ton formateur préféré: ", ('Pierre', 'Autre'))
 
st.image(pierre_mur.jpg, width=200)
# conditional statement to print
# Male if male is selected else print female
# show the result using the success function
if (status == 'Pierre'):    
	st.success("Pierre Evidemment")
	
else:
    st.success("Est tu sûr de ton choix?")

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
