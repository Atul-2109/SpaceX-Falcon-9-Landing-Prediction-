# Import required libraries
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the data
spacex_df = pd.read_csv("spacex_launch_dash.csv")

max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create Dash app
app = dash.Dash(__name__)

# Get unique launch sites
launch_sites = spacex_df['Launch Site'].unique()

# App layout
app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),

    # TASK 1: Dropdown   
    dcc.Dropdown(
        id='site-dropdown',  
        options=[{'label': 'All Sites', 'value': 'ALL'}] +
                [{'label': site, 'value': site} for site in launch_sites],
        value='ALL',
        placeholder="Select a Launch Site here",
        searchable=True
    ),

    html.Br(),

    # TASK 2: Pie chart
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),


    html.P("Payload range (Kg):"),
    # TASK 3: Range Slider
    dcc.RangeSlider(
        id='payload-slider',
        min=0, max=10000, step=1000,
        marks={i: str(i) for i in range(0, 10001, 2000)},
        value=[min_payload, max_payload]
    ),

    html.Br(),


    # TASK 4: Scatter chart
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])

# TASK 2: Pie chart callback
@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def update_pie_chart(selected_site):

    if selected_site == 'ALL':
        # Count successful launches by site
        df = spacex_df[spacex_df['class'] == 1]
        fig = px.pie( df, names='Launch Site', title='Total Successful Launches by Site' )
    else:
        # Filter for selected site
        df = spacex_df[spacex_df['Launch Site'] == selected_site]
        fig = px.pie( df, names='class', title=f'Success vs Failure for {selected_site}' )

    return fig


# TASK 4: Scatter chart callback
@app.callback(
    Output('success-payload-scatter-chart', 'figure'),
    [Input('site-dropdown', 'value'),
     Input('payload-slider', 'value')]
)
def update_scatter_chart(selected_site, payload_range):

    low, high = payload_range

    # Filter by payload range
    filtered_df = spacex_df[ 
        (spacex_df['Payload Mass (kg)'] >= low) &
        (spacex_df['Payload Mass (kg)'] <= high)
    ]

    if selected_site == 'ALL':
        fig = px.scatter( filtered_df, x='Payload Mass (kg)', y='class', color='Booster Version Category', 
            title='Payload vs Launch Outcome (All Sites)')
    else:
        # Filter by site
        filtered_df = filtered_df[filtered_df['Launch Site'] == selected_site]

        fig = px.scatter( filtered_df, x='Payload Mass (kg)', y='class', color='Booster Version Category',
            title=f'Payload vs Launch Outcome ({selected_site})'
        )
    return fig


# Run the app
if __name__ == '__main__':
    app.run(debug=True)

