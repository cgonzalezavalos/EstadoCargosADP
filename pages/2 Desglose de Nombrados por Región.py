import streamlit as st
import pandas as pd
import plotly.express as px


# carga de datos
#------------------------------------------------------------------------
data=pd.read_excel('datos/datosEstadoCargosADP.xlsx',sheet_name='datos')
#------------------------------------------------------------------------
# Fecha Actualizacion
fecha_actualizacion=data['FechaActualizacion'].max()
#------------------------------------------------------------------------

st.set_page_config(layout='wide',
                   initial_sidebar_state="expanded")    

# Set Page Header
st.header("Desglosadose por región de nombrados/as en ADP")
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
st.caption(f'Fecha de actualización: _{fecha_actualizacion}_')
# Add horizontal line
st.markdown("<hr>", unsafe_allow_html=True)