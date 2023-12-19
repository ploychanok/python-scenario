import streamlit as st
import pandas as pd

# Load your CSV file
file_path = "data.csv"
df = pd.read_csv(file_path)

learning_scenarios = df[df['Category'] == 'Scenario']

module_counts = learning_scenarios['Target Audience'].value_counts()

selected_module = st.selectbox("Select a Target Audience:", module_counts.index)

filtered_scenarios_module = learning_scenarios[learning_scenarios['Target Audience'] == selected_module]

selected_scenario = st.selectbox(f"Select Scenario Instances for {selected_module}:", filtered_scenarios_module['Scenario Instances'].unique())

filtered_scenarios = filtered_scenarios_module[filtered_scenarios_module['Scenario Instances'] == selected_scenario]

# Display Chapter Titles for the selected Scenario Instances
st.title(f"Chapter Titles for {selected_module} - {selected_scenario}")
st.write(filtered_scenarios[['Chapter Title']])

