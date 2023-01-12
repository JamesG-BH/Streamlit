import streamlit as st
import pandas as pd
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.markdown("# A Random Table 🎉")
st.sidebar.markdown("# Main page 🎈")

df
