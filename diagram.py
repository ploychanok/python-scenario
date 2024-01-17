import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def display_diagram(df_diagram, selected_option, selected_value):
    # Check for valid option and filter the DataFrame
    if selected_option == "By Audience":
        column_filter, column_other = 'Target Audience', 'Libraries'
    elif selected_option == "By Library":
        column_filter, column_other = 'Libraries', 'Target Audience'
    else:
        st.warning("Invalid option selected.")
        return

    filtered_df = df_diagram[df_diagram[column_filter] == selected_value]

    # Check if the filtered DataFrame is empty
    if filtered_df.empty:
        st.warning("No data available for the selected option.")
        return

    # Preparing data for the Sankey diagram
    df_source_target = filtered_df[[column_filter, 'Scenario Instances']].copy()
    df_intermediate_target = filtered_df[['Scenario Instances', column_other]].copy()
    df_source_target.columns = df_intermediate_target.columns = ['Source', 'Target']

    sankey_data = pd.concat([df_source_target, df_intermediate_target])

    # Create labels and indices for the Sankey diagram
    labels = pd.concat([sankey_data['Source'], sankey_data['Target']]).unique()
    label_to_id = {label: i for i, label in enumerate(labels)}
    source_indices = sankey_data['Source'].map(label_to_id)
    target_indices = sankey_data['Target'].map(label_to_id)

    # Create and display the Sankey diagram
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="white", width=0.5),
            label=labels,
            color=["#FEBF57", "#56CFE1", "#9D4EDD", "#FB5607", "#FF006E", "#8338EC", "#3A86FF"]
        ),
        link=dict(
            source=source_indices,
            target=target_indices,
            value=[1] * len(sankey_data),
            color="#EAEAEA"
        ))])

    st.plotly_chart(fig)
