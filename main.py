import streamlit as st
import pandas as pd

# Load your CSV file
file_path = "data.csv"
df = pd.read_csv(file_path)

learning_scenarios = df[df['Category'] == 'Scenario']

module_counts = learning_scenarios['Target Audience'].value_counts()

# Sidebar
st.sidebar.title("Scenario Analysis")
selected_module = st.sidebar.selectbox("Select a Target Audience:", module_counts.index)
selected_scenario = st.sidebar.selectbox(f"Select Scenario Instances for {selected_module}:", learning_scenarios['Scenario Instances'].unique())

# Filter data based on selected module and scenario
filtered_scenarios_module = learning_scenarios[learning_scenarios['Target Audience'] == selected_module]
filtered_scenarios = filtered_scenarios_module[filtered_scenarios_module['Scenario Instances'] == selected_scenario]

# Main content
st.title(f"Chapter Titles for {selected_module} - {selected_scenario}")
table_data = filtered_scenarios[['Chapter Title']]

# Create two columns
col1, col2 = st.columns(2)

# Display the radio button list of Chapter Titles in the first column
with col1:
    selected_chapter_title = st.radio("Select a Chapter Title:", table_data['Chapter Title'].unique())

# Display Chapter Summary, Book Name, Chapter Number, and PDF link in the second column
with col2:
    if selected_chapter_title:
        # Filter the data based on the selected Chapter Title
        filtered_chapter = filtered_scenarios[filtered_scenarios['Chapter Title'] == selected_chapter_title]

        # Display Chapter Summary, Book Name, Chapter Number, and PDF link
        st.title(f"Chapter Summary for {selected_module} - {selected_scenario} - {selected_chapter_title}")
        st.write(f"Book Name: {filtered_chapter['Textbook'].iloc[0]}")
        st.write(f"Chapter Number: {filtered_chapter['Chapter Number'].iloc[0]}")
        st.write(filtered_chapter['Chapter Summary'].iloc[0])

        # Add a link to a PDF file based on the URL column in the DataFrame
        pdf_url = filtered_chapter['URL'].iloc[0]
        st.markdown(f"[Download PDF]({pdf_url})")
