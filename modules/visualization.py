# modules/visualization.py
import streamlit as st
import plotly.express as px

def plot_visualization(df, chart_type):
    if chart_type == "Bar Chart":
        fig = px.bar(df)
    elif chart_type == "Pie Chart":
        fig = px.pie(df)
    elif chart_type == "Line Chart":
        fig = px.line(df)
    elif chart_type == "Scatter Plot":
        fig = px.scatter(df)
    st.plotly_chart(fig, use_container_width=True)
