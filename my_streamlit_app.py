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
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import ipywidgets as widgets


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
st.set_page_config(page_title="Quête Streamlit", page_icon=":chart_with_upwards_trend:")
def _max_width_():
    max_width_str = "max-width: 1500px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )

_max_width_()

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
        st.markdown("<h1 style='text-align: center;'>Analyses</h1>", unsafe_allow_html=True)
                # This create a nice grey line between the title and the multiselect menu
        st.write("---------------------------------------------------------")
        st.write("")
        st.write("")



        st.subheader("Présentation du dataset") # add a subtitle
        st.dataframe(df)
        st.write("")
        st.write("")
        st.write("")



        st.write("La colonne 'mpg' représente le nombre de miles parcourus par gallon de carburant (mesure impériale que l'on peut mettre en parallèle à notre km/litre)" )
        st.write("La colonne 'cylinders' correspond au nombre de cylindres de la voiture" )
        st.write("La colonne 'cubicinches' correspond à la cylindrée en cubic inches, sachant que 122 cubic inches correspond à 2 litres" )
        st.write("La colonne 'hp' se rapporte à la puissance en chevaux du véhicule" )
        st.write("La colonne 'weightlbs ' correspond au poids du véhicule en livres, sachant que 1 livre équivaut à 0.454 kg)" )
        st.write("La colonne 'time-to-60' se rapporte au temps en seconde pour passer du 0 à 60 miles/h, soit l'équivalent du 0 à 100 km/h" )
        st.write("La colonne 'year ' correspond à l'année de commercialisation du véhicule" )
        st.write("La colonne 'continent' correspond à la région dont le véhicule est originaire ; nous en avons ici 3 : les USA, l'Europe et le Japon" )
        st.write("")
        st.write("")
        st.write("")



        st.subheader("Heatmap de corrélation") # add a subtitle


        # Paramétrage des données pour faire la heatmap de corrélation :
        corr = df.corr()

        heatmap = px.imshow(corr, text_auto=True, color_continuous_scale='RdBu_r', origin='upper', aspect = "auto")
        heatmap.update_layout(title='Heatmap de corrélation', xaxis_nticks=36)
        st.plotly_chart(heatmap)
        st.write("")
        st.write("")
        st.write("")


        st.markdown(
                """
                D'après la heatmap obtenue, si nous ne filtrons pas sur la colonne 'continent', nous remarquons que :
                - le champ 'mpg' est fortement corrélée avec les champs suivants :
                    -   cylinders
                    -   cubinches
                    -   hp
                    -   weightlbs
                - il y a corrélation entre la colonne 'time_to_60' et la colonne 'hp'
                """
            )
        st.write("")
        st.write("")
        st.write("")

        st.subheader("Production de voitures par région") # add a subtitle


        st.write("")
        st.write("")
        st.write("")


        st.subheader("Profil des différentes données, par continent") # add a subtitle
        st.write("")
        st.write("")


        # Variables to insert df inside the multiselect menu
        continent3 = df['continent'].unique()
        continent_multiselect2 = st.multiselect('Filtre sur la région', continent3)
        df_boxplot = df.query('continent in @continent_multiselect2')
        
        col1, col2, col3 = st.columns([7,1,7])
        with col1:
            box_mpg = px.box(df_boxplot, x = 'year', y="mpg", color = 'continent', 
            title = 'Distribution des données de la colonne "mpg", par continent',
            labels = {'year': 'Période', 'mpg' : 'Consommation en litres'},width=700, height=500)
            box_mpg.update_layout(showlegend=True, title_x=0.5, yaxis={'visible': True}, template='plotly_dark')
            st.plotly_chart(box_mpg)
            st.write("")
            st.write("La voiture qui consomme le plus est Américaine. On peut parcourir 10 miles par gallon consommé. Elle a été commercialisée en 1971.")
            st.write("On remarque que les voitures Américaines sont celles qui consomment le plus en moyenne.")
            st.write("Celle qui consomme le moins est Japonnaise. Elle a été commercialisée en 1981. On peut parcourir 46.6 miles pour 1 gallon consommé")
            st.write("La consommation des voitures Européennes et Japonnaises sont plutôt comparables dans le temps.")

        with col3:
            box_cylinders = px.box(df_boxplot, x = 'year', y="cylinders", color = 'continent', 
            title = 'Distribution des données de la colonne "cylinders", par continent',
            labels = {'year': 'Période', 'cylinders' : 'Nb de cylindres'},width=700, height=500)
            box_cylinders.update_layout(showlegend=True, title_x=0.5, yaxis={'visible': True}, template='plotly_dark')
            st.plotly_chart(box_cylinders)
            st.write("")
            st.write("Les voitures Américaines sont celles qui comportent le plus de cylindres en comparaison avec les autres voitures.")    
            st.write("Celles qui ont le moins de cylindres sont Japonnaises.")        
        st.write("")
        st.write("")


        col1, col2, col3 = st.columns([7,1,7])
        with col1:
            box_cubicinches = px.box(df_boxplot, x = 'year', y='cubicinches', color = 'continent', 
            title = 'Distribution des données de la colonne "cubicinches", par continent',
            labels = {'year': 'Période', 'cubicinches' : 'Cylindrée en cubic inches'},width=700, height=500)
            box_cubicinches.update_layout(showlegend=True, title_x=0.5, yaxis={'visible': True}, template='plotly_dark')
            st.plotly_chart(box_cubicinches)
            st.write("")
            st.write("Les plus grosses cylindrées ont été produites au USA.")    
            st.write("La plus petite cylindrée est Européenne (68 cubic inches). Elle a été produite en 1974.")   
            st.write("Les plus petites cylindrées sont généralement Japonnaises.") 


        with col3:
            box_hp = px.box(df_boxplot, x = 'year', y="hp", color = 'continent', 
            title = 'Distribution des données de la colonne "hp", par continent',
            labels = {'year': 'Période', 'hp' : 'Puissance (en chevaux)'},width=700, height=500)
            box_hp.update_layout(showlegend=True, title_x=0.5, yaxis={'visible': True}, template='plotly_dark')
            st.plotly_chart(box_hp)
        st.write("")
        st.write("")

        col1, col2, col3 = st.columns([7,1,7])
        with col1:
            box_weightlbs  = px.box(df_boxplot, x = 'year', y="weightlbs", color = 'continent', 
            title = 'Distribution des données de la colonne "weightlbs ", par continent',
            labels = {'year': 'Période', 'weightlbs ' : 'Poids (en livres)'},width=700, height=500)
            box_weightlbs.update_layout(showlegend=True, title_x=0.5, yaxis={'visible': True}, template='plotly_dark')
            st.plotly_chart(box_weightlbs)

        with col3:
            box_chrono = px.box(df_boxplot, x = 'year', y="time-to-60", color = 'continent', 
            title = 'Distribution des données de la colonne "time-to-60", par continent',
            labels = {'year': 'Période', 'time-to-60' : 'Temps (en secondes) pour passer du 0 à 60 miles/h'},width=700, height=500)
            box_chrono.update_layout(showlegend=True, title_x=0.5, yaxis={'visible': True}, template='plotly_dark')
            st.plotly_chart(box_chrono)

        st.write("")
        st.write("")
        st.write("")




        st.subheader("Evolution des cylindrées dans le temps, par continent") # add a subtitle
        col1, col2 = st.columns([1, 2])
        with col1:
            # Variables to insert df inside the multiselect menu
            continent = df['continent'].unique()
            continent_multiselect2 = st.multiselect('Filtre sur la région ', continent)
            st.write(" Analyse ")

        with col2:
            cylinders_per_yr = pd.DataFrame()
            cylinders_per_yr['year'] = df['year']
            cylinders_per_yr['cylinders'] = df['cylinders']
            cylinders_per_yr['continent'] = df['continent']
            cylinders_per_yr = cylinders_per_yr.query('continent in @continent_multiselect2')
            

            fig_cyl = px.bar(cylinders_per_yr, x = 'year', y="cylinders", color = 'continent', title = 'Evolution des cylindrées dans le temps, par continent',
            labels = {'year': 'Période', 'cylinders' : 'Nb de cylindres'},width=700, height=600)
            fig_cyl.update_layout(showlegend=True, title_x=0.5, yaxis={'visible': True}, template='plotly_dark')

            st.plotly_chart(fig_cyl)





main()