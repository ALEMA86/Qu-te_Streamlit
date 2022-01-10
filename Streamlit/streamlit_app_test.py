######################################################################################
######################################################################################
###########################     LIBRAIRIES    ########################################
######################################################################################
######################################################################################

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import ipywidgets as widgets
from plotly.subplots import make_subplots
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
st.set_page_config(page_title="Quête Streamlit", page_icon=":chart_with_upwards_trend:", layout='wide')


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

######################################################################################
######################################################################################
###########################     Challenge     ########################################
######################################################################################
######################################################################################   


    elif choice == "Analyses":

        st.subheader("Heatmap de corrélation") # add a subtitle


        # Paramétrage des données pour faire la heatmap de corrélation :
        corr = df.corr()

        heatmap = px.imshow(corr, text_auto=True, color_continuous_scale='RdBu_r', origin='upper', aspect = "auto")
        heatmap.update_layout(title='Heatmap de corrélation', xaxis_nticks=36)
        st.plotly_chart(heatmap)

        st.markdown(
                """
                Analyse heatmap

                """
            )

        st.subheader("Evolution des cylindrées dans le temps, par continent") # add a subtitle
        col1, col2 = st.columns([1, 2])
        with col1:
            # Variables to insert df_input inside the multiselect menu
            continent = df['continent'].unique()
            continent_select = st.multiselect(' ', continent)

            # Mask to filter dataframe
            mask_movies = df['continent'].isin(continent_select)
            data = df[mask_movies]

        with col2:
            fig1 = px.bar(df, x = 'year', y="cylinders", color = 'continent', title = 'Evolution des cylindrées dans le temps, par continent',
            labels = {'year': 'Période', 'continent': 'Continent', 'cylinders' : 'Nb de cylindres'},width=800, height=600)
            fig1.update_layout(showlegend=False, title_x=0.5, yaxis={'visible': True}, template='plotly_dark')
            st.plotly_chart(fig1)





main()
