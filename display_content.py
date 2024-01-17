import streamlit as st
import pandas as pd
from data_processing import process_data
from diagram import display_diagram

def display_content(df_diagram, filtered_chapter, selected_scenario, selected_chapter_title, option, selected_module=None, selected_library=None):    
    if not filtered_chapter.empty and selected_chapter_title is not None:
        st.markdown(f"**{selected_module}** > **{selected_scenario}** > **{selected_chapter_title}**")
        
        # Filter the DataFrame based on the selected chapter title
        selected_chapter = filtered_chapter[filtered_chapter['Chapter Title'] == selected_chapter_title]

        st.markdown("### Chapter Summary")
        st.write(f"**Book Name:** {selected_chapter['Display Book Name'].iloc[0]}")
        st.write(f"**Chapter Number:** {selected_chapter['Chapter Number'].iloc[0]}")
        
        library_text = selected_chapter['Libraries'].iloc[0]
        if pd.notna(library_text):  # Check if library_text is not NaN
            if "," in library_text:
                st.write(f"**Related Libraries:** {library_text}")
            else:
                st.write(f"**Related Library:** {library_text}")
        else:
            st.write("**Related Library:** Not available")

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
                    
        st.markdown("---")
        selected_value = selected_module if option == "By Audience" else selected_library
        display_diagram(df_diagram, option, selected_value)

        pdf_url = selected_chapter['URL'].iloc[0]
        if pd.notna(pdf_url):
            st.markdown("---")
            st.markdown(f"[Link to TextBook]({pdf_url})")
    else:
        st.warning("No data available for the selected criteria.")