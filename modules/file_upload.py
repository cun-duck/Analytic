# modules/file_upload.py
import streamlit as st
import os

def upload_file():
    uploaded_file = st.file_uploader("Unggah file (.csv atau .xls)", type=["csv", "xls"])
    if uploaded_file and uploaded_file.size <= 10 * 1024 * 1024:
        return uploaded_file
    elif uploaded_file:
        st.error("Ukuran file terlalu besar. Maksimal 10MB.")
    return None

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

def select_columns(df):
    selected_columns = st.multiselect("Pilih kolom untuk dianalisis", options=df.columns)
    return df[selected_columns] if selected_columns else df
