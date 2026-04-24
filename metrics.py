import pandas as pd

def kpi_metrics(data_filtered):
    #data_filtered = data_filtered.sort_values('Year')
    total_waste = data_filtered['Waste generated'].sum()
    
    years = sorted(data_filtered['Year'].unique())
    

    if len(years)>=2:
        last = data_filtered[data_filtered['Year'] == years[-1]]['Waste generated'].sum()
        previous = data_filtered[data_filtered['Year'] == years[-2]]['Waste generated'].sum()
        trend = ((last - previous) / previous) * 100
    else:
        trend = 0.0

    #recycling vs landfill/incineration
    recycled = data_filtered['Recycling'].sum()
    other = data_filtered['Energy Recovery'].sum() + data_filtered['Landfill'].sum()
    total = recycled + other    
    recycling_rate = (recycled/ total) * 100 if total_waste > 0 else 0
    
    is_good = recycling_rate >= 40.0
    
    total_gen = data_filtered['Waste generated'].sum()
    total_treated = data_filtered['Waste treatment'].sum()
    treatment_coverage = (total_treated / total_gen) * 100 if total_gen > 0 else 0

    return {
        'Total Waste Generated': float(total_waste),
        'Waste Trend (%)': trend,
        'Recycling Rate (%)': recycling_rate,
        'is_good': is_good,
        'Treatment Coverage (%)': treatment_coverage
    }