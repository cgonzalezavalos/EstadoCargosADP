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
st.caption(f'Fecha de actualización: _{fecha_actualizacion}_')
# Add horizontal line
st.markdown("<hr>", unsafe_allow_html=True)


# colores y orden de los estados
Estados_Orden=['Planificación','Convocatoria','En Evaluación','Nómina','Nombrado','Titular No ADP']
Estado_Color = {'Planificación': 'orange', 'Convocatoria': 'blue','En Evaluación':'grey','Nómina':'yellow','Nombrado':'#00f118','Titular No ADP':'red'}  # Mapeo de colores por sexo

#------------------------------------------------------------------------
# listas valores filtros
#------------------------------------------------------------------------
unique_nivel = data['Nivel'].unique()
nivel = pd.DataFrame({'Sexo': unique_nivel})
nuevo_registro = pd.DataFrame({'Nivel': ['Todos']})
nivel = pd.concat([nuevo_registro, nivel])
nivel = nivel.reset_index(drop=True)
nivel = nivel['Nivel'].tolist()

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
total_nombrados=data.query("Estado=='Nombrado'")['id_cargo'].count()
total_nombrados_hombres=data.query("Estado=='Nombrado' & Sexo=='Hombre'")['id_cargo'].count()
total_nombrados_mujeres=data.query("Estado=='Nombrado' & Sexo=='Mujer'")['id_cargo'].count()

#------------------------------------------------------------------------
# Filtros
with st.container():
    col1,col2,col3=st.columns(3)
    with col1:
        option1=st.selectbox('Ministerio',Ministerio)
    with col2:
        option2=st.selectbox('Región',region)
    with col3:
        option3=st.selectbox('Nivel Jerárquico',nivel)


df_total=data.groupby('Estado').agg({'id_cargo':'count'}).reset_index()
df_total=df_total.rename(columns={'id_cargo':'cargos'})

# gráfico 1 estado de cargos I y II nivel adscrito
graf_1 = px.bar(df_total, x='Estado', y='cargos', 
                category_orders={'Estado': Estados_Orden},
                color='Estado',
                color_discrete_map=Estado_Color,
                title='Cantidad de Cargos Adscritos por Estado')
graf_1.update_xaxes(title_text=None,tickmode='linear', dtick=1,tickangle=-90)


# grafico 2 porcentaje estado de cargos

graf_2=px.pie(df_total, values='cargos', 
                names='Estado', 
                title='Estado de cargos en porcentaje',
                category_orders={'Estado': Estados_Orden},
                color='Estado',
                color_discrete_map=Estado_Color,
                hole=0.4,
                title='Distribución de Cargos Adscritos por Estado')
#graf_2.update_layout(showlegend=False)


with st.container():
    col3, col4, col5=st.columns(spec=[0.3,0.35,0.35])
    with col3:
        total_nombrados_I_II = f"{total_nombrados}"
        st.markdown(f"<h1 style='text-align: center; color: grey;'>{total_nombrados_I_II}</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: grey;'>Total nombrados/as actualmente en cargos de I y II nivel jerárquico</h3>", unsafe_allow_html=True)
    with col4:
        total_nombrados_I_II_hombre = f"{total_nombrados_hombres}"
        st.markdown(f"<h1 style='text-align: center; color: grey;'>{total_nombrados_hombres}</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: grey;'>Total hombres nombrados actualmente en cargos de I y II nivel jerárquico</h3>", unsafe_allow_html=True)
    with col5:
        total_nombrados_I_II_mujer = f"{total_nombrados_mujeres}"
        st.markdown(f"<h1 style='text-align: center; color: grey;'>{total_nombrados_mujeres}</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: grey;'>Total mujeres nombradas actualmente en cargos de I y II nivel jerárquico</h3>", unsafe_allow_html=True)
#    st.dataframe(df_total)
with st.container():
    col6,col7=st.columns(spec=[0.3,0.7])
    with col6:
        st.plotly_chart(graf_2,use_container_width=True)
    with col7:
        st.plotly_chart(graf_1,use_container_width=True)

    

texto_foot_1="""Dirección Nacional del Servicio Civil, Morandé 115, P.9, Santiago, Chile."""
texto_foot_2 = """Consultas a: <a href='mailto:cgonzalez@serviciocivil.cl'>cgonzalez@serviciocivil.cl</a>"""
st.caption(texto_foot_1, unsafe_allow_html=False, help=None)    
st.caption(texto_foot_2, unsafe_allow_html=True, help=None)