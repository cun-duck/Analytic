# modules/visualization.py
import plotly.express as px
import streamlit as st

def plot_visualization(df, chart_type):
    if df.empty:
        st.warning("DataFrame kosong. Silakan unggah data terlebih dahulu.")
        return
    
    # Tampilkan opsi untuk memilih kolom x dan y
    x_axis = st.selectbox("Pilih kolom untuk sumbu X:", df.columns)
    y_axis = st.selectbox("Pilih kolom untuk sumbu Y:", df.columns)
    
    if chart_type == "Line Chart":
        try:
            fig = px.line(df, x=x_axis, y=y_axis)
            st.plotly_chart(fig, use_container_width=True)
        except ValueError:
            st.error("Data tidak cocok untuk Line Chart.")
    elif chart_type == "Bar Chart":
        try:
            fig = px.bar(df, x=x_axis, y=y_axis)
            st.plotly_chart(fig, use_container_width=True)
        except ValueError:
            st.error("Data tidak cocok untuk Bar Chart.")
    elif chart_type == "Scatter Plot":
        try:
            fig = px.scatter(df, x=x_axis, y=y_axis)
            st.plotly_chart(fig, use_container_width=True)
        except ValueError:
            st.error("Data tidak cocok untuk Scatter Plot.")
    else:
        st.warning("Tipe chart tidak dikenali.")
