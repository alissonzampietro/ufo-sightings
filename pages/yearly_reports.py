import streamlit as st
import pandas as pd

st.title("Yearly Appearances Reports")

@st.cache_data
def load_data():
    return pd.read_csv("data/ufo.csv", on_bad_lines='skip')

df = load_data()
original_df = df
df["year"] = pd.to_datetime(df["datetime"], errors='coerce').dt.year
max_year = df["year"].max()
min_year = df["year"].min()

df = df.groupby("year").size().reset_index(name="count")



st.line_chart(df, x="year", y="count", x_label="Years", y_label="Total Ocurrences")
st.write(f"""
    From :green[{min_year:g}] to :green[{max_year:g}] a total of {len(original_df)} reports were registered.
""")
st.dataframe(original_df)
