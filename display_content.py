import streamlit as st
import pandas as pd
from diagram import display_diagram


def display_content(df_diagram, filtered_chapter, selected_scenario, selected_chapter_title, option, selected_module=None, selected_library=None):    
    # Early exit if no data is available
    if filtered_chapter.empty or selected_chapter_title is None:
        st.warning("No data available for the selected criteria.")
        return

    st.markdown(f"**{selected_module}** > **{selected_scenario}** > **{selected_chapter_title}**")
    
    # Filter the DataFrame based on the selected chapter title
    selected_chapter = filtered_chapter[filtered_chapter['Chapter Title'] == selected_chapter_title]
    
    # Display chapter details
    chapter_details = selected_chapter.iloc[0]  # Assuming there's only one row per chapter title
    st.write(f"**Book Name:** {chapter_details['Display Book Name']}")
    st.write(f"**Chapter Number:** {chapter_details['Chapter Number']}")

    library_text = chapter_details['Libraries']
    if pd.notna(library_text):
        library_label = "Related Libraries" if "," in library_text else "Related Library"
        st.write(f"**{library_label}:** {library_text}")
    else:
        st.write("**Related Library in Chapter:** Not available")

    # Display diagram
    selected_value = selected_module if option == "By Audience" else selected_library
    display_diagram(df_diagram, option, selected_value)
    st.markdown("---")

    # Create two columns for chapter summary and code snippet
    col1, col2 = st.columns(2)

    with col1:
        chapter_summary = chapter_details['Chapter Summary']
        if pd.notna(chapter_summary):
            st.markdown("### Chapter Summary")
            st.write(chapter_summary)

    with col2:
        code_snippet = chapter_details['Code snippet']
        if pd.notna(code_snippet):
            st.markdown("### Example Code Snippet")
            st.code(code_snippet, language="python")

            code_snippet_description = chapter_details['Code snippet description']
            if pd.notna(code_snippet_description):
                st.write(code_snippet_description)

    # Optional: Link to the textbook
    # pdf_url = chapter_details['URL']
    # if pd.notna(pdf_url):
    #     st.markdown("---")
    #     st.markdown(f"[Link to TextBook]({pdf_url})")
