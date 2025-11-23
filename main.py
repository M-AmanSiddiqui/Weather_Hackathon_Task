import streamlit as st
import sys
import os
import plotly.express as px

# Path fix
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from etl.weather_etl import weather_etl

API_KEY = "f84eee37c2c4ff4a3a3d83e0d5b3e972"

# Page config
st.set_page_config(page_title="Weather Dashboard", layout="wide", page_icon="🌤️")

# Title
st.markdown("""
    <h1 style='text-align: center; color: #4B8BBE;'>🌤️ Weather ETL & Dashboard</h1>
    <p style='text-align: center; color: #306998;'>Check real-time weather metrics with unit conversion</p>
""", unsafe_allow_html=True)

# Sidebar for inputs
st.sidebar.header("🔍 Weather Settings")
city = st.sidebar.text_input("Enter city name:", "Karachi")
temp_unit = st.sidebar.radio("Temperature Unit:", ("Celsius", "Fahrenheit"))
wind_unit = st.sidebar.radio("Wind Speed Unit:", ("m/s", "km/h"))
pressure_unit = st.sidebar.radio("Pressure Unit:", ("hPa", "atm"))

if st.sidebar.button("Fetch Weather"):
    try:
        df = weather_etl(
            city, API_KEY,
            temp_unit="F" if temp_unit=="Fahrenheit" else "C",
            wind_unit=wind_unit,
            pressure_unit=pressure_unit
        )

        # Metrics cards
        st.markdown(f"### Current Weather in {city}")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric(df["Parameter"][0], f"{df['Value'][0]:.2f}")
        col2.metric(df["Parameter"][1], f"{df['Value'][1]:.0f}")
        col3.metric(df["Parameter"][2], f"{df['Value'][2]:.2f}")
        col4.metric(df["Parameter"][3], f"{df['Value'][3]:.2f}")

        # Table
        with st.expander("Show Data Table"):
            st.table(df)

        # Chart
        fig = px.bar(
            df, x="Parameter", y="Value", text="Value", color="Value",
            color_continuous_scale="Viridis",
            title=f"Weather Metrics for {city}"
        )
        fig.update_layout(title_x=0.5, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"Error: {e}")
