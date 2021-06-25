from altair.vegalite.v4.schema.channels import Longitude
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from apps.data import get_data


#Read the clean datset
sample_data1 = pd.read_csv('data/crime1.csv')


def app():
    #create two columns for the dropdown menu to change map display
    col1, col2 = st.beta_columns([1,1])
    with col1:
        #Create a list for the hover options
        hover_options = ['HUNDRED_BLOCK', 'NEIGHBOURHOOD']

        #Create a dropdown to choose from
        choice = st.selectbox('Set hover information', hover_options)

    with col2:
        #Create a list for the animation_frame options
        time_options = ['YEAR', 'MONTH', 'DAY']

        #Create a dropdown to choose from
        choice1 = st.selectbox('Set hover information', time_options)

    zoom = st.slider('Set zoom level', 0,10)

    #Define a function for the scatter map
    def animate_map(time_col):
        fig = px.scatter_mapbox(sample_data1,
                lat="Latitude" ,
                lon="Longitude",
                hover_name=choice,
                color="TYPE",
                animation_frame=time_col,
                mapbox_style='carto-positron',
                category_orders={
                time_col:list(np.sort(sample_data1[time_col].unique()))
                    },                  
                zoom=zoom)
        st.write(fig)
    animate_map(time_col=choice1)
