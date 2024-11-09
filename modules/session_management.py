# modules/session_management.py
import os
import streamlit as st

def clear_session(file_path):
    if 'exit' in st.session_state and st.session_state.exit:
        if os.path.exists(file_path):
            os.remove(file_path)
