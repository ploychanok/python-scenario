# PyEdu Streamlit Application for Scenario Analysis

## Overview

The PyEdu, developed as a Streamlit-based application, provides an interactive platform for Scenario Analysis in educational content, particularly focusing on Python programming. 

**Note that our prototype only uses a subset of 6 textbooks


## Features

### Interactive Sidebar
- **Selection Features**: The sidebar includes a radio button with two options: `by audience` and by library `by library`, followed by two select boxes for filtering data based on the chosen criteria.

### Visualization of Taxonomy
- **Data Visualization**: Utilizes Plotly for creating Sankey diagrams to illustrate relationships between various entities like Target Audience, Scenario Instances, and Libraries.

### Scenario Contents
- **Components**:
  - **Metadata**: Displays textbook title, chapter title, and related libraries.
  - **Chapter Summary**: Provides a summary of the selected chapter.
  - **Code Snippet**: Includes code snippets from the selected chapter.
- **Data Extraction**: Chapter summaries and code snippets are extracted using pdfgear and ChatGPT-4, with manual verification by the team.


## Interactive Walkthrough

### Selecting the Viewpoint
- Users can navigate through scenario viewpoints by selecting either `by audience` or `by library` in the sidebar. The content area updates dynamically to display relevant information.

### Searching by Audience (`by audience`)
- This feature allows users to select a target audience, filtering chapters relevant to that audience.

### Searching by Library (`by library`)
- Similar to the `by audience` feature, but focuses on Python libraries. Selecting a library filters the chapters associated with it.

## Installation and Running the Application

1. **Clone the repository or download the script**.
2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

Additional Modules: Make sure the custom modules (`data_processing`, `filter_chapters`, `display_content`) are present in your working directory.

## Running the Application

To launch the PyEdu Streamlit application, navigate to the directory containing the script and run:

```bash
streamlit run main.py
```

The application will open in your default web browser.