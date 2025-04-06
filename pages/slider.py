import streamlit as st
import pandas as pd

age = st.slider("Select your age", 0, 100, 25)

data = [i*age for i in range(100)]
df = pd.DataFrame(data, columns=["age"])
st.line_chart(df)

st.write("This is a line chart of the age of the people in the dataset.")