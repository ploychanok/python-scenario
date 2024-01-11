import pandas as pd

def process_data(file_path):
    df = pd.read_csv(file_path)

    # Split the 'Libraries' column into individual rows
    df_diagram = df.assign(Libraries=df['Libraries'].str.split(',')).explode('Libraries').reset_index(drop=True)

    # Group by 'Scenario Instances', 'Target Audience', and 'Libraries' and calculate counts
    df_diagram = df_diagram.groupby(['Scenario Instances', 'Target Audience', 'Libraries']).size().reset_index(name='Count')

    # # Group by 'Scenario Instances' and 'Target Audience' and calculate counts
    # scenario_audience_counts = df_diagram.groupby(['Scenario Instances', 'Target Audience']).size().reset_index(name='Count')

    return df_diagram
