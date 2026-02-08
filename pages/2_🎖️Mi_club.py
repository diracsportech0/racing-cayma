import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from mplsoccer import (VerticalPitch, Pitch, create_transparent_cmap,
                       FontManager, arrowhead_marker, Sbopen)

#from Home_page import name_club, id_club
from etl import df #df_tipo1, df_tipo2
from functions import barras_apiladas, tipo_tiros_goles, mostrar_tablas_zonas


colA, colB, colC = st.columns([5, 6, 2])
with colA:st.title('🎖️ MI CLUB')
with colB:pass
with colC:st.image('logo-piad.png', use_column_width=True)
#----------------------
#st.title(f'⚽ {name_club}')
#df = df[df['etapa'] != 'provincial'] #estamos obviando los partidos de la provincial


#------------ 1. MENU LATERAL
menu_miclub = ['Informe de partido','Informe acumulado']
choice2 = st.sidebar.radio("Submenú - Miclub", menu_miclub, 0)

if choice2 == 'Informe de partido':

    col1, col2 = st.columns(2)
    with col1:
        #st.subheader("Gráfico Ataque")
        fig1, ax1 = plt.subplots()
        ax1.plot([1, 2, 3], [10, 20, 10])
        barras_apiladas(df, 'Event', ['Ataque', 'Tran. Defensa - Ataque'],'output', "Resultado por fases")

    with col2:
        #st.subheader("Gráfico B")
        fig2, ax2 = plt.subplots()
        ax2.bar(['X', 'Y', 'Z'], [5, 15, 7])
        barras_apiladas(df, 'Event', ['Defensa', 'Tran. Ataque - Defensa'],'output', "Resultado por fases")

    mostrar_tablas_zonas(df)

    tipo_tiros_goles(df)


if choice2 == 'Informe acumulado':
    st.write("NO DISPONIBLE")