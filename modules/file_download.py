# modules/file_download.py
import streamlit as st

def download_analysis(df):
    st.download_button("Unduh hasil analisis (.xls)", data=df.to_csv().encode('utf-8'), file_name="analysis_result.xls")
