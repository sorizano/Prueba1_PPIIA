import streamlit as st
import pandas as pd

st.title("Lector de Datos Simple")

st.write("Sube un archivo CSV para visualizar los datos.")

uploaded_file = st.file_uploader("Elige un archivo CSV", type="csv")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.subheader("Vista Previa de Datos")
        st.dataframe(df)
        
        st.subheader("Estadísticas Descriptivas")
        st.write(df.describe())
    except Exception as e:
        st.error(f"Error al leer el archivo: {e}")
else:
    st.info("Esperando archivo...")
