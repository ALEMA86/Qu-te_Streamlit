######################################################################################
######################################################################################
###########################     LIBRAIRIES    ########################################
######################################################################################
######################################################################################

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import ipywidgets as widgets
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import plotly.graph_objects as go



######################################################################################
######################################################################################
###########################     CSS CODE   ###########################################
######################################################################################
######################################################################################

# CSS code to hide footer and header automatically installed on streamlit page
# I keep the main menu so people can switch from dark to light and vice versa
hide_menu= """
<style>
    #MainMenu {visibility:visible;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

</style>
"""

######################################################################################
######################################################################################
###########################     DONNEES    ###########################################
######################################################################################
######################################################################################


df = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv')


######################################################################################
######################################################################################
###########################     INTERFACE    #########################################
######################################################################################
######################################################################################


#set the page layout to automatically use full horoizontal size + get and icon and name inside the internet browser
st.set_page_config(page_title="ABC'S", page_icon=":heart:", layout='wide')


def main():
    # This is used to activate the CSS code at the top
    st.markdown(hide_menu, unsafe_allow_html=True)
    
    
    # Menu and Sidebar creation
    menu = ["Consignes Challenge", "Analyses"]
    choice = st.sidebar.selectbox("", menu)