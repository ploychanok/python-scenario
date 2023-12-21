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
selected_chapter_title = st.sidebar.selectbox("Select a Chapter Title:", learning_scenarios[learning_scenarios['Scenario Instances'] == selected_scenario]['Chapter Title'].unique())

# Filter data based on selected module, scenario, and chapter title
filtered_chapter = learning_scenarios[
    (learning_scenarios['Target Audience'] == selected_module) &
    (learning_scenarios['Scenario Instances'] == selected_scenario) &
    (learning_scenarios['Chapter Title'] == selected_chapter_title)
]

# Main content
st.markdown(f"**{selected_module}** > **{selected_scenario}** > **{selected_chapter_title}**")

# Display Chapter Summary, Book Name, Chapter Number, Code snippet, Code snippet description, and Download PDF link
if not filtered_chapter.empty:
    st.markdown("### Chapter Summary")
    st.write(f"**Book Name:** {filtered_chapter['Dispaly Book Name'].iloc[0]}")
    st.write(f"**Chapter Number:** {filtered_chapter['Chapter Number'].iloc[0]}")
    
    chapter_summary = filtered_chapter['Chapter Summary'].iloc[0]
    if pd.notna(chapter_summary):
        st.write(chapter_summary)

        code_snippet = filtered_chapter['Code snippet'].iloc[0]
        if pd.notna(code_snippet):
            st.markdown("---")
            st.markdown("### Sample Code Snippet")
            st.code(code_snippet, language="python")
            code_snippet_description = filtered_chapter['Code snippet description'].iloc[0]
            if pd.notna(code_snippet_description):
                st.write(code_snippet_description)
   
    st.markdown("---")

    # Add a link to a PDF file based on the URL column in the DataFrame
    pdf_url = filtered_chapter['URL'].iloc[0]
    st.markdown(f"[Download PDF]({pdf_url})")
else:
    st.warning("No data available for the selected criteria.")
