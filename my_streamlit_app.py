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




######################################################################################
######################################################################################
######################     Consignes Challenge     ###################################
######################################################################################
######################################################################################
    if choice == "Consignes Challenge":
                # CSS code within markdown to center the title
        st.markdown("<h1 style='text-align: center;'>Consignes Challenge</h1>", unsafe_allow_html=True)
                # This create a nice grey line between the title and the multiselect menu
        st.write("---------------------------------------------------------")
        st.subheader('')
        st.subheader("Challenge")

        st.markdown(
        """
        A partir du [dataset des voitures](https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv), tu afficheras :

        - une analyse de corrélation et de distribution grâce à différents graphiques et des commentaires.
        - des boutons doivent être présents pour pouvoir filtrer les résultats par région (US / Europe / Japon).
        - l'application doit être disponible sur la plateforme de partage.

        Publie ensuite ici le lien de ton application. Le lien doit ressembler à https://share.streamlit.io/wilder/streamlit_app/my_streamlit_app.py.

        """
        )
        st.subheader('')
        st.subheader("Critères de validation")

        st.markdown(
        """
        - L'application est accessible en ligne
        - L'analyse est effectuée, avec des commentaires explicatifs
        - Des boutons sont présents pour filtrer par région
        
        """
        )