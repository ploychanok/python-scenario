import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

def display_chord_diagram(df):
    # Create a pivot table to get the count of connections
    chord_data = pd.crosstab(df['Scenario Instances'], df['Target Audience'])

    # Normalize the data to create percentages
    chord_data_percent = chord_data.div(chord_data.sum(axis=1), axis=0) * 100

    # Create a chord diagram using Plotly
    fig = go.Figure(data=[go.Choropleth(
        z=chord_data_percent.values,
        locations=chord_data_percent.index,
        locationmode='geojson-id',  # Corrected value here
        colorscale='Viridis',
        colorbar_title='Percentage'
    )])

    fig.update_layout(
        title_text='Chord Diagram',
        geo=dict(showframe=False, projection_type='equirectangular')
    )

    st.plotly_chart(fig)