import streamlit as st
import pandas as pd

def filter_chapters_by_module(learning_scenarios, selected_module, selected_scenario):
    module_filter = (learning_scenarios['Target Audience'] == selected_module)
    module_scenarios = learning_scenarios[module_filter]

    # Use the provided selected_scenario if available, otherwise, use the first one
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

# Load your CSV file
file_path = "data.csv"
df = pd.read_csv(file_path)

# Sidebar
st.sidebar.title("Scenario Analysis")
option = st.sidebar.radio("Select Analysis Option:", ["By Module", "By Library"])

# Initialize variables
selected_module, selected_scenario, selected_chapter_title, selected_library = None, None, None, None
filtered_chapter = pd.DataFrame()

if option == "By Module":
    learning_scenarios = df[df['Category'] == 'Scenario']
    module_counts = learning_scenarios['Target Audience'].value_counts()
    selected_module = st.sidebar.selectbox("Select a Target Audience:", module_counts.index)
    filtered_chapter, selected_scenario = filter_chapters_by_module(learning_scenarios, selected_module, selected_scenario)
    selected_chapter_title, _, _ = display_chapter_selection(filtered_chapter)

elif option == "By Library":
    libraries = set(df['Libraries'].str.split(',').explode().str.strip())
    selected_library = st.sidebar.selectbox("Select a Library:", sorted(map(str, libraries)))
    
    # Filter chapters based on the selected library
    filtered_chapter = filter_chapters_by_library(df, selected_library)
    
    # Display available chapter titles for the selected library
    selected_chapter_title, selected_scenario, selected_module = display_chapter_selection(filtered_chapter)

# Main content
if not filtered_chapter.empty and selected_chapter_title is not None:
    st.markdown(f"**{selected_module}** > **{selected_scenario}** > **{selected_chapter_title}**")
    
    # Filter the DataFrame based on the selected chapter title
    selected_chapter = filtered_chapter[filtered_chapter['Chapter Title'] == selected_chapter_title]

    st.markdown("### Chapter Summary")
    st.write(f"**Book Name:** {selected_chapter['Display Book Name'].iloc[0]}")
    st.write(f"**Chapter Number:** {selected_chapter['Chapter Number'].iloc[0]}")

    chapter_summary = selected_chapter['Chapter Summary'].iloc[0]
    if pd.notna(chapter_summary):
        st.write(chapter_summary)

        code_snippet = selected_chapter['Code snippet'].iloc[0]
        if pd.notna(code_snippet):
            st.markdown("---")
            st.markdown("### Sample Code Snippet")
            st.code(code_snippet, language="python")
            
            code_snippet_description = selected_chapter['Code snippet description'].iloc[0]
            if pd.notna(code_snippet_description):
                st.write(code_snippet_description)

    pdf_url = selected_chapter['URL'].iloc[0]
    if pd.notna(pdf_url):
        st.markdown("---")
        st.markdown(f"[Download PDF]({pdf_url})")
else:
    st.warning("No data available for the selected criteria.")