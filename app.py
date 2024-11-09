# app.py
import streamlit as st
from modules import file_upload, data_preprocessing, visualization, ai_training, file_download, telegram_logging, session_management

st.title("Aplikasi Analisis dan Visualisasi Dokumen")

uploaded_file = file_upload.upload_file()
if uploaded_file:
    df = data_preprocessing.load_data(uploaded_file)
    if df is not None:
        df = file_upload.select_columns(df)
        df = data_preprocessing.clean_data(df)
        
        common_columns = data_preprocessing.detect_common_columns(df)
        st.write("Kolom Umum yang Terdeteksi:")
        st.write(common_columns)
        
        st.write("Data yang diunggah:")
        st.write(df)
        
        chart_type = st.selectbox("Pilih jenis visualisasi", ["Bar Chart", "Pie Chart", "Line Chart", "Scatter Plot"])
        visualization.plot_visualization(df, chart_type)
        
        file_download.download_analysis(df)
        
        ai_training.enhance_training_with_common_columns(df, common_columns)
        doc_text = " ".join(df.columns)
        doc_type = ai_training.classify_document(doc_text)
        st.write(f"Jenis dokumen terdeteksi: {doc_type}")
        
        user_ip = st.experimental_get_query_params().get("user_ip", ["N/A"])[0]
        user_agent = st.experimental_get_query_params().get("user_agent", ["N/A"])[0]
        telegram_logging.send_log(uploaded_file.name, user_ip, user_agent, doc_type)
        
        session_management.clear_session(uploaded_file.name)
    else:
        st.error("File tidak dapat dibaca.")
