import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

# Set Page Header
st.header("Estado Cargos Sistema Alta Dirección Pública")
# Set custom CSS for hr element
st.markdown(
    """
        <style>
            hr {
                margin-top: 0.0rem;
                margin-bottom: 0.5rem;
                height: 3px;
                background-color: #333;
                border: none;
            }
        </style>
    """,
    unsafe_allow_html=True,
)

# Add horizontal line
st.markdown("<hr>", unsafe_allow_html=True)
