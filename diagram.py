import streamlit as st
import plotly.graph_objects as go

def display_diagram():
    scenarios = ["API", "Data and Processing", "GUI", "Others/Generic"]
    target_audiences = ["Data analysis", "Educational purposes", "Generic", "Software testing", "Web development",
                        "DevOps", "Game development", "Machine learning", "Others", "Software development", "Computer graphics"]
    counts = [7, 7, 28, 4, 15, 23, 4, 16, 1, 25, 10, 3, 3, 21, 4, 4, 1, 14, 27, 4, 2, 7, 2, 17, 2, 25, 2, 66, 1, 1, 2, 4, 50]

    # Create links
    link_sources = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    link_targets = [3, 2, 1, 4, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 5, 6, 7, 8, 9, 10, 11, 12, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    link_values = counts

    # Create Sankey diagram
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=scenarios + target_audiences
        ),
        link=dict(
            source=link_sources,
            target=link_targets,
            value=link_values
        )
    )])

    # Update layout
    fig.update_layout(title_text="Sankey Diagram of Scenario Instances and Target Audiences")
    st.plotly_chart(fig)