import streamlit as st

def filter_chapters_by_module(learning_scenarios, selected_module, selected_scenario):
    module_filter = (learning_scenarios['Target Audience'] == selected_module)
    module_scenarios = learning_scenarios[module_filter]

    if selected_scenario is None:
        selected_scenario = module_scenarios['Scenario Instances'].iloc[0]

    scenario_filter = (module_scenarios['Scenario Instances'] == selected_scenario)
    return module_scenarios[scenario_filter], selected_scenario

def filter_chapters_by_library(df, selected_library):
    library_filter = df['Libraries'].str.contains(selected_library, case=False, na=False)
    return df[library_filter]

def display_chapter_selection(filtered_chapter):
    if not filtered_chapter.empty:
        selected_chapter_title = st.sidebar.selectbox("Select a Chapter:", filtered_chapter['Chapter Title'].tolist())
        selected_row = filtered_chapter[filtered_chapter['Chapter Title'] == selected_chapter_title].iloc[0]
        selected_scenario = selected_row['Scenario Instances']
        selected_module = selected_row['Target Audience']
        return selected_chapter_title, selected_scenario, selected_module
    return None, None, None
