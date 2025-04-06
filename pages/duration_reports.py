import streamlit as st
import pandas as pd
from services.data_service import load_data

st.set_page_config(
    page_title="Duration Appearances Reports",
    layout="wide"
)

st.title("Duration Appearances Reports")

total_items_to_show = 10

st.write("This report shows the total duration of all UFO sightings grouped by year.")

df = load_data()
original_df = df
df["year"] = pd.to_datetime(df["datetime"], errors='coerce').dt.year
max_year = df["year"].max()
min_year = df["year"].min()

df["duration (seconds)"] = pd.to_numeric(df["duration (seconds)"], errors='coerce')
df = df.groupby("year")["duration (seconds)"].sum().reset_index(name="total_duration")

st.line_chart(df, x="year", y="total_duration", x_label="Years", y_label="Total Duration (seconds)")
st.write(f"""
    From :red[{min_year:g}] to :red[{max_year:g}] a total of :green[{len(original_df)}] reports were registered.
""")

st.dataframe(original_df.sample(total_items_to_show))
