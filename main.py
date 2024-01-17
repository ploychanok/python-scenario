import streamlit as st
import pandas as pd
from data_processing import process_data
from filter_chapters import filter_chapters_by_module, filter_chapters_by_library, display_chapter_selection
from display_content import display_content

file_path = "data.csv"
df = pd.read_csv(file_path)
df_diagram = process_data(file_path)

st.set_page_config(page_title="Tatoeba", layout="wide")

# Sidebar
st.sidebar.title("Scenario Viewpoint")
option = st.sidebar.radio("Select Viewpoint Option:", ["By Audience", "By Library"])

selected_module, selected_scenario, selected_chapter_title, selected_library = None, None, None, None
filtered_chapter = pd.DataFrame()

if option == "By Audience":
    learning_scenarios = df[df['Category'] == 'Scenario']
    module_counts = learning_scenarios['Target Audience'].value_counts()
    selected_module = st.sidebar.selectbox("Select a Target Audience:", module_counts.index)
    filtered_chapter, selected_scenario = filter_chapters_by_module(learning_scenarios, selected_module, selected_scenario)
    selected_chapter_title, _, _ = display_chapter_selection(filtered_chapter)
    # Main content
    display_content(df_diagram, filtered_chapter, selected_scenario, selected_chapter_title, "By Audience", selected_module)

elif option == "By Library":
    libraries = set(df['Libraries'].str.split(',').explode().str.strip())
    selected_library = st.sidebar.selectbox("Select a Library:", sorted(map(str, libraries)))
    
    # Filter chapters based on the selected library
    filtered_chapter = filter_chapters_by_library(df, selected_library)
    
    # Display available chapter titles for the selected library
    selected_chapter_title, selected_scenario, selected_module = display_chapter_selection(filtered_chapter)

    # Main content
    display_content(df_diagram, filtered_chapter, selected_scenario, selected_chapter_title, "By Library", selected_module, selected_library)
