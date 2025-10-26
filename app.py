import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="Análisis de Vehículos", layout="wide")

# Título principal
st.title("Análisis de Vehículos Usados")

# Cargar los datos
@st.cache_data
def load_data():
    df = pd.read_csv('vehicles_us.csv')
    return df

# Cargar datos
df = load_data()

# Mostrar información básica
st.header("Información del Dataset")
st.write(f"Total de vehículos: {len(df)}")

# Crear checkbox para mostrar datos
if st.checkbox("Mostrar datos"):
    st.dataframe(df.head())

# Histograma
st.header("Histograma de Precios")
fig_hist = px.histogram(df, x='price', title='Distribución de Precios')
st.plotly_chart(fig_hist)

# Gráfico de dispersión
st.header("Gráfico de Dispersión")
fig_scatter = px.scatter(df, x='odometer', y='price', title='Precio vs Kilometraje')
st.plotly_chart(fig_scatter)