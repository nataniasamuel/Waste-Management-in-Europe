# Waste Management Dashboard

## Features
* **Interactive Maps:** View waste generation per country.
* **Treatment Analysis:** Compare Recycling, Energy Recovery, and Landfill rates over time.
* **Comparative Insights:** Compare specific country recycling rates against the EU average.
* **Time-Series Analysis:** Compare data over time to understand trend and progress.

## Project Structure
* `dashboard.py`: The main application entry point.
* `visuals.py`: Contains all visualisation functions.
* `sidebar.py`: Contains all sidebar functions.
* `eda_and_cleaning.py`: Contains all cleaning and eda performed on the dataset.
* `cleaned_data.csv`: The processed dataset.

## Libraries Used
* pandas
* matplotlib
* seaborn
* plotly
* streamlit

## How to Run
1. Clone this repository.
2. Install the requirements:
   `pip install -r requirements.txt`
3. Run the dashboard:
   `streamlit run dashboard.py`
