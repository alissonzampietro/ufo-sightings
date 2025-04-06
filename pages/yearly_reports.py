import streamlit as st
import pandas as pd
from services.data_service import load_data

st.set_page_config(
    page_title="Yearly Appearances Reports",
    layout="wide"
)

st.title("Yearly Appearances Reports")

total_items_to_show = 10

df = load_data()
original_df = df
df["year"] = pd.to_datetime(df["datetime"], errors='coerce').dt.year
max_year = df["year"].max()
min_year = df["year"].min()

df = df.groupby("year").size().reset_index(name="count")



st.line_chart(df, x="year", y="count", x_label="Years", y_label="Total Ocurrences")
st.write(f"""
    From :red[{min_year:g}] to :red[{max_year:g}] a total of :green[{len(original_df)}] reports were registered.
""")

st.dataframe(original_df.filter(items=["datetime", "year", "country"]).sample(total_items_to_show))
