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

# carga de datos
data=pd.read_excel('datos/datosEstadoCargosADP.xlsx',sheet_name='datos')

#------------------------------------------------------------------------
# listas valores filtros
#------------------------------------------------------------------------
unique_sexo = data['Sexo'].unique()
Sexo = pd.DataFrame({'Sexo': unique_sexo})
nuevo_registro = pd.DataFrame({'Sexo': ['Todos']})
rango_etario = pd.concat([nuevo_registro, Sexo])
Sexo = Sexo.reset_index(drop=True)
Sexo = Sexo['Sexo'].tolist()

unique_region = data['Region'].unique()
region = pd.DataFrame({'Region': unique_region})
nuevo_registro = pd.DataFrame({'Region': ['Todas']})
region = pd.concat([nuevo_registro, region])
region = region.reset_index(drop=True)
region = region['Region'].tolist()

unique_ministerio = data['Ministerio'].unique()
Ministerio = pd.DataFrame({'Ministerio': unique_ministerio})
nuevo_registro = pd.DataFrame({'Ministerio': ['Todos']})
Ministerio = pd.concat([nuevo_registro, Ministerio])
Ministerio = Ministerio.reset_index(drop=True)
Ministerio = Ministerio['Ministerio'].tolist()

#------------------------------------------------------------------------
#------------------------------------------------------------------------
# Filtros
with st.container():
    col1,col2,col3=st.columns(3)
    with col1:
        option1=st.selectbox('Ministerio',Ministerio)
    with col2:
        option2=st.selectbox('Región',region)
    with col3:
        option3=st.selectbox('Sexo', Sexo)

with st.container():
    st.dataframe(data.head(10))