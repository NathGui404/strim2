# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import PIL
from PIL import Image


# radio button
# first argument is the title of the radio button
# second argument is the options for the ratio button
status = st.radio("Quel est ton formateur préféré?",('Autre','Pierre'))
# conditional statement to print
# show the result using the success function

if (status == 'Pierre'):    
	st.success("C'était évident !")
	image = Image.open('pierre_mur.jpg')
	st.image(image, width=200)
else:
	st.warning("Est tu sûr de ton choix?")

