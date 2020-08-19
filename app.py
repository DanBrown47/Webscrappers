
import streamlit as st
import pandas as pd
import numpy as np

st.title('News Level')
DATA_FILE  = "/home/rook/PycharmProjects/news/View_log.csv"
DATE_TIME = 'Time'

@st.cache
def load_data():
    data = pd.read_csv(DATA_FILE )
    # data[DATE_TIME] = pd.to_datetime(data[DATE_TIME])
    data = data.rename(columns={'Time':'index'}).set_index('index')
    return data

data = load_data()


st.subheader("Raw Data")
st.write(data)

st.line_chart(data)