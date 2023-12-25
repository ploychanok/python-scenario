import streamlit as st
import pandas as pd

# Load your CSV file
file_path = "data.csv"
df = pd.read_csv(file_path)

# Sidebar
st.sidebar.title("Scenario Analysis")
option = st.sidebar.radio("Select Analysis Option:", ["By Module", "By Library"])

# Initialize variables
selected_module = None
selected_scenario = None
selected_chapter_title = None
selected_library = None
filtered_chapter = pd.DataFrame()  # Initialize as an empty DataFrame

if option == "By Module":
    # Filter by scenario category
    learning_scenarios = df[df['Category'] == 'Scenario']

    # Display available modules and scenarios in the sidebar
    module_counts = learning_scenarios['Target Audience'].value_counts()
    selected_module = st.sidebar.selectbox("Select a Target Audience:", module_counts.index)

    # Filter by the selected module
    module_filter = learning_scenarios['Target Audience'] == selected_module
    module_scenarios = learning_scenarios[module_filter]
    selected_scenario = st.sidebar.selectbox(f"Select Scenario Instances for {selected_module}:", module_scenarios['Scenario Instances'].unique())

    # Filter by selected module and scenario
    scenario_filter = (learning_scenarios['Target Audience'] == selected_module) & (learning_scenarios['Scenario Instances'] == selected_scenario)
    filtered_chapter = learning_scenarios[scenario_filter]

    # Display available chapter titles for the selected module and scenario
    selected_chapter_title = st.sidebar.selectbox("Select a Chapter Title:", filtered_chapter['Chapter Title'].unique())

elif option == "By Library":
    # Extract unique libraries from the "Libraries" column and split them by ','
    libraries = set(df['Libraries'].str.split(',').explode().str.strip())

    # Display library selection in the sidebar
    selected_library = st.sidebar.selectbox("Select a Library:", list(libraries))

    # Filter DataFrame based on selected library
    library_filter = df['Libraries'].str.contains(selected_library, case=False, na=False)
    filtered_chapter = df[library_filter]

    # Display available chapter titles for the selected library
    if not filtered_chapter.empty:
        # Use st.sidebar.selectbox to display chapters in a dropdown menu
        selected_chapter_title = st.sidebar.selectbox("Select a Chapter:", filtered_chapter['Chapter Title'].tolist())

        # Get corresponding Scenario Instances and Target Audience for the selected chapter
        selected_row = filtered_chapter[filtered_chapter['Chapter Title'] == selected_chapter_title].iloc[0]
        selected_module = selected_row['Scenario Instances']
        selected_scenario = selected_row['Target Audience']

    else:
        st.sidebar.write("No chapters found for selected library:", selected_library)


# Main content
if not filtered_chapter.empty:
    st.markdown(f"**{selected_module}** > **{selected_scenario}** > **{selected_chapter_title}**")
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

    pdf_url = filtered_chapter['URL'].iloc[0]
    if pd.notna(pdf_url):
        st.markdown("---")
        st.markdown(f"[Download PDF]({pdf_url})")
else:
    st.warning("No data available for the selected criteria.")
