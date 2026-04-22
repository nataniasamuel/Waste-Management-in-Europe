import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import sidebar
import seaborn as sns
import importlib
import visuals

importlib.reload(visuals)
# page configurations
st.set_page_config(page_title="Waste Management Analysis", layout="wide")

#loading the dataset
@st.cache_data
def load_data():
    data = pd.read_csv("cleaned_data.csv")
    return data
    
#app
def main():
    st.title("Waste Management Analysis Dashboard")
    data = load_data()

    country, years = sidebar.sidebar(data)
    data_filtered = data[
        (data['Region'] == country) & 
        (data['Year'] >= years[0]) & 
        (data['Year'] <= years[1])]

    col1,col2,col3 = st.columns(3)
    with col1:
        visuals.plot_map(data)
    with col2:
        visuals.plot_waste_generated_time(data_filtered)
    with col3:
        visuals.plot_donut(data_filtered)

    col4,col5 = st.columns(2)
    with col4:
        visuals.waste_treatment_time(data_filtered)
    with col5:
        visuals.recycle_rate(data_filtered,data)

if __name__ == "__main__":
    main()
