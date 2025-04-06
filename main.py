import streamlit as st


st.set_page_config(
    page_title="UFO Sightings Dashboard",
    page_icon="🛸",
    layout="wide"
)

# This will automatically discover all pages in the pages directory
# and create navigation for them

st.title('UFO Sightings Dashboard')
st.write("Welcome to the UFO Sightings analysis dashboard!")