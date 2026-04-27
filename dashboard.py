import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import sidebar
import seaborn as sns
import importlib
import visuals
import metrics
import plotly.io as pio

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
# Setting colour theme
    pio.templates["earthy"] = pio.templates["plotly_white"]
    pio.templates["earthy"].layout.colorway = ["#16588E","#21A06D","#FFB300","#F03AE7", "#90D73D", "#00BCD4", "#FF5722"]
    pio.templates.default = "earthy"
    
    st.title("Waste Management Analysis Dashboard 🗑️")
    data = load_data()

    country, years = sidebar.sidebar(data)
    data_filtered = data[
        (data['Region'] == country) & 
        (data['Year'] >= years[0]) & 
        (data['Year'] <= years[1])]
    
    kpi_data = metrics.kpi_metrics(data_filtered)

    col1,col2,col3 = st.columns(3)
    with col1:
        with st.container(border=True):
            trend = kpi_data['Waste Trend (%)']
            color = "green" if trend <= 0 else "red" #manually assigning colours for the trend values and arrows
            arrow = "↓" if trend <= 0 else "↑" #manually assigning arrows for the trend values
            st.metric("Total Waste Generated", 
                f"{kpi_data['Total Waste Generated']:.0f} Kg per capita")
            st.markdown(f":{color}[{arrow} {abs(trend):.1f}%]")
    
    with col2:
        with st.container(border=True):
            st.metric("Recycling Rate",
                    f"{kpi_data['Recycling Rate (%)']:.1f}%")
            st.markdown("Status: " + ("Good" if kpi_data['is_good'] else "Needs Improvement"))

    with col3:
        with st.container(border=True):
                st.metric("Treatment Coverage",
                    f"{kpi_data['Treatment Coverage (%)']:.1f}%")
                st.markdown(f"Status: " + (":green[Good]" if kpi_data['Treatment Coverage (%)'] >= 80 else ":red[Needs Improvement]"))

    col4, = st.columns(1)
    with col4:
        with st.container(border=True):
            visuals.plot_map(data,selected_country=country)
    
    col5,col6 = st.columns(2)
    with col5:
        with st.container(border=True):
            visuals.plot_waste_generated_time(data_filtered)
    with col6:
        with st.container(border=True):
            visuals.plot_donut(data_filtered)

    col7,col8 = st.columns(2)
    with col7:
        with st.container(border=True):
            visuals.waste_treatment_time(data_filtered)
    with col8:
        with st.container(border=True):
            visuals.recycle_rate(data_filtered,data)

if __name__ == "__main__":
    main()
