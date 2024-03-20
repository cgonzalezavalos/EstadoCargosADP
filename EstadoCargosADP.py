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
#------------------------------------------------------------------------
data=pd.read_excel('datos/datosEstadoCargosADP.xlsx',sheet_name='datos')
#------------------------------------------------------------------------
# orden de los estados
Estados_Orden=['Planificación','Convocatoria','En Evaluación','Nómina','Nombrado','Titular No ADP']

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
# valores
total_nombrados=data.query("Estado=='Nombrado'").count()

#------------------------------------------------------------------------
# Filtros
with st.container():
    col1,col2=st.columns(2)
    with col1:
        option1=st.selectbox('Ministerio',Ministerio)
    with col2:
        option2=st.selectbox('Región',region)




# gráfico 1 estado de cargos I y II nivel adscrito

df_total=data.groupby('Estado').agg({'id_cargo':'count'}).reset_index()
df_total=df_total.rename(columns={'id_cargo':'cargos'})

graf_1 = px.bar(df_total, x='Estado', y='cargos', category_orders={'Estado': Estados_Orden})
graf_1.update_xaxes(title_text=None,tickmode='linear', dtick=1,tickangle=-90)
graf_1.update_traces(texttemplate='%{text}', textposition='outside')


with st.container():
    col3, col4=st.columns(spec=[0.2,0.8])
    with col3:
        total_nombrados_I_II = f"{total_nombrados:,}"
        st.markdown(f"<h1 style='text-align: center; color: grey;'>{total_nombrados_I_II}</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: grey;'>Total Nombrados/as en cargos de I y II nivel jerárquico</h3>", unsafe_allow_html=True)
#    st.dataframe(df_total)
    st.plotly_chart(graf_1,use_container_width=True)

    