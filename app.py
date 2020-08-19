import streamlit as st
import pandas as pd


st.title('News Level')
DATA_FILE  = "/home/rook/PycharmProjects/news/View_log.csv"


@st.cache
def load_data():
    data = pd.read_csv(DATA_FILE )
    data = data.rename(columns={'Time':'index'}).set_index('index')
    return data

data = load_data()

if st.checkbox('View Data'):
    st.subheader("Raw Data")
    st.write(data)

st.subheader("Chart")
st.line_chart(data)
