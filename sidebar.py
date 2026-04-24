import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

#side bar function with europe as the default
def sidebar(data):
    st.sidebar.title("♻️Dashboard Settings")
    countries = sorted(data['Region'].unique().tolist())
    default_idx = countries.index('European Union - 27 countries (from 2020)') if 'European Union - 27 countries (from 2020)' in countries else 0
    country = st.sidebar.selectbox("Select a Country", options=countries, index = default_idx)

#year slider
    min_year = int(data['Year'].min())
    max_year = int(data['Year'].max())
    years = st.sidebar.slider("Drag to select a year range", min_year, max_year, (min_year, max_year))
    return country, years
