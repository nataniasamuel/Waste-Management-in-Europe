import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import sidebar
import seaborn as sns
import importlib
import visuals
import metrics

importlib.reload(visuals)
importlib.reload(metrics)
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
    
    kpi_data = metrics.kpi_metrics(data_filtered)

    col1,col2 = st.columns(2)

    col1.metric("Total Waste Generated", 
                f"{kpi_data['Total Waste Generated']:.0f} Kg per capita",
                delta = f"{kpi_data['Waste Trend (%)']:.1f}%",)
    
    col2.metric("Recycling Rate",
                f"{kpi_data['Recycling Rate (%)']:.1f}%",
                delta = "Good" if kpi_data['is_good'] else "Needs Improvement",
                delta_color="normal" if kpi_data['is_good'] else "inverse")
    
    

    col4, = st.columns(1)
    with col4:
        visuals.plot_map(data)
    
    col5,col6 = st.columns(2)
    with col5:
        visuals.plot_waste_generated_time(data_filtered)
    with col6:
        visuals.plot_donut(data_filtered)

    col7,col8 = st.columns(2)
    with col7:
        visuals.waste_treatment_time(data_filtered)
    with col8:
        visuals.recycle_rate(data_filtered,data)

if __name__ == "__main__":
    main()
