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
table_data = filtered_scenarios[['Chapter Title']]

# Display the table of Chapter Titles
st.table(table_data)

# Allow the user to select a Chapter Title from the displayed table
selected_chapter_title = st.text_input("Enter a Chapter Title:")
if selected_chapter_title:
    # Filter the data based on the selected Chapter Title
    filtered_chapter = filtered_scenarios[filtered_scenarios['Chapter Title'] == selected_chapter_title]

    # Display Chapter Summary directly without an expander
    st.title(f"Chapter Summary for {selected_module} - {selected_scenario} - {selected_chapter_title}")
    st.write(filtered_chapter['Chapter Summary'].iloc[0])  # Assuming there is only one unique Chapter Summary for the selected Chapter Title
