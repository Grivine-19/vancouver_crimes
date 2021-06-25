import streamlit as st
import pandas as pd
import plotly.graph_objects as go


@st.cache()
def get_data(filename):
    test_data = pd.read_csv(filename, parse_dates={'Date':['YEAR', 'MONTH']}, 
    keep_date_col=True)

    return test_data


def app():
    st.subheader('About')

    st.markdown('''
    ### Overview
    The dataset contains 530,652 records from 2003-01-01 to 2017-07-13.
    
    ### Source
    This dataset has been retrieved from [Kaggle](https://www.kaggle.com/wosaku/crime-in-vancouver)
    ''')

    test_data = get_data('data/crime.csv')

    #Use a subset of the dataset
    sample_data = test_data.sample(10000, random_state = 42)

    #Removing special characters from the neighbourhood column
    spec_chars = ["!", '"', "#", "%", "&", "'", "(", ")",
              "*", "+", ",", "-", ".", "/", ":", ";", "<",
              "=", ">", "?", "@", "[", "\\", "]", "^", "_",
              "`", "{", "|", "}", "~", "–", "/:"]
    for char in spec_chars:
        sample_data['NEIGHBOURHOOD'] = sample_data['NEIGHBOURHOOD'].str.replace(char, ' ')


    #Replace values in the Neighbourhood Column
    sample_data["NEIGHBOURHOOD"].fillna(method='ffill', inplace=True)

    #Drop invalid rows
    sample_data1 = sample_data[(sample_data.Latitude != 0) & (sample_data.Longitude != 0)]

    #Save the clean dataset in csv
    sample_data1.to_csv('data/crime1.csv')


    #Plot a fancy table to display the dataset
    fig = go.Figure(data=[go.Table(columnwidth=[2,2,2,2,2],header=dict(values=list(sample_data1[['TYPE', 'YEAR',
    'MONTH', 'NEIGHBOURHOOD', 'Latitude', 'Longitude']].columns),
    fill_color='#1f77b4',
    align=['left', 'center'], height=40, font=dict(color='white', size=15)),

    cells=dict(values=[sample_data1.TYPE, sample_data1.YEAR, sample_data1.MONTH, sample_data1.NEIGHBOURHOOD,
    sample_data1.Latitude, sample_data1.Longitude],
    fill_color='#8c564b',
    align='left'))
    ])

    fig.update_layout(margin=dict(l=5, r=5, b=10, t=10))
    st.write(fig)
