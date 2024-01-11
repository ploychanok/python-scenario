import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def display_diagram(df_diagram, selected_option, selected_value):
    # Filter the df_diagram DataFrame based on the selected option and value
    if selected_option == "By Audience":
        filtered_df = df_diagram[df_diagram['Target Audience'] == selected_value]
    elif selected_option == "By Library":
        filtered_df = df_diagram[df_diagram['Libraries'] == selected_value]
    else:
        st.warning("Invalid option selected.")
        return

    # Check if the filtered data frame is empty
    if filtered_df.empty:
        st.warning("No data available for the selected option.")
        return

    # Splitting and restructuring the data for the Sankey diagram
    df_target_to_scenario = filtered_df[['Target Audience', 'Scenario Instances']].copy()
    df_scenario_to_library = filtered_df[['Scenario Instances', 'Libraries']].copy()
    df_target_to_scenario.columns = ['Source', 'Target']
    df_scenario_to_library.columns = ['Source', 'Target']
    sankey_data = pd.concat([df_target_to_scenario, df_scenario_to_library])

    # Creating the Sankey diagram
    source = sankey_data['Source']
    target = sankey_data['Target']
    labels = pd.concat([source, target]).unique()

    # Create a mapping for labels to indices
    label_to_id = {label: i for i, label in enumerate(labels)}

    # Map the source and target to their respective indices
    source_indices = source.map(label_to_id)
    target_indices = target.map(label_to_id)

    # Create Sankey diagram
    fig = go.Figure(data=[go.Sankey(
        node=dict(
          pad=15,
          thickness=20,
          line=dict(color="black", width=0.5),
          label=labels,
          color="blue"
        ),
        link=dict(
          source=source_indices,
          target=target_indices,
          value=[1] * len(source)  # Assuming a default value of 1 for each link
        ))])

    # Display the figure using Streamlit
    st.plotly_chart(fig)
