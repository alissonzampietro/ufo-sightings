import streamlit as st
from services.data_service import load_data
df = load_data()

st.set_page_config(
    page_title="Report by Country",
    layout="wide"
)

st.title("Report by Country")

country_labels = {
    'us': 'United States',
    'gb': 'United Kingdom',
    'ca': 'Canada',
    'au': 'Australia',
    'de': 'Germany'
}

countries = [item for item in df['country'].unique().tolist() if type(item) is str]

selected_country = st.selectbox("Select a country", countries, format_func=lambda x: country_labels[x])


df = df[df['country'] == selected_country].groupby("year").size().reset_index(name="count")
 
st.line_chart(df, x="year", y="count", x_label="Date", y_label="Total Ocurrences", use_container_width=True)