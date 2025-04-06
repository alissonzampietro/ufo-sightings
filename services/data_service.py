import streamlit as st
import pandas as pd

@st.cache_data()
def load_data():
    df = pd.read_csv("data/ufo.csv", on_bad_lines='skip', low_memory=False)
    df['year'] = pd.to_datetime(df['datetime'], errors='coerce').dt.year
    return df