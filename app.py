import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

variable = 'Leq'
medida = 'Valor_mean'
cai = "CAI 20 de Julio"

# Data

df_hora = pd.read_csv(r'data/df_group_hora.csv', encoding='utf_8',delimiter=';')
df_dia = pd.read_csv(r'data/df_group_dia.csv', encoding='utf_8',delimiter=';')
df_fecha = pd.read_csv(r'data/df_group_fecha.csv', encoding='utf_8',delimiter=';')

# Serie de tiempo

df_cai = df_fecha[(df_fecha.Estación == cai)]


fig_day_series = go.Figure()
fig_day_series.add_trace(go.Scatter(x=df_cai["Fecha_Dia"],
                         y=df_cai[df_cai.Variable == variable][medida],
                         name=cai,
                         line=dict(color='blue', width=1)))

fig_day_series.update_layout(
                   xaxis_title='Fecha',
                   yaxis_title='Ruido Promedio/Día')

fig_day_series.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)


# Mapa por hora



fig_map_hour = px.density_mapbox(df_hora[df_hora['Variable'] == variable], lat='latitude', lon='longitude', z= medida,
                                 radius=50,
                                 animation_group = 'Estación',
                                 animation_frame  = 'Hora',
                                 hover_name = 'Estación',
                                 color_continuous_scale ='Jet',
                                 opacity=0.9
                                 )

fig_map_hour.update_layout(mapbox_style="stamen-toner",
                           mapbox_zoom=9.5,
                           mapbox_center = {"lat": 4.60971, "lon": -74.08175}
                           )

fig_map_hour.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


# Mapa por día

fig_map_day = px.density_mapbox(df_dia[df_dia['Variable']== variable], lat='latitude', lon='longitude', z=medida, radius=50
                        ,animation_group = 'Estación'
                        ,animation_frame  = 'Dia'
                        ,hover_name = 'Estación'
                        ,color_continuous_scale ="Jet"
                        ,color_continuous_midpoint =50
                       )
fig_map_day.update_layout(mapbox_style="stamen-toner"
                  ,mapbox_zoom=10
                  , mapbox_center = {"lat": 4.60971, "lon": -74.08175}
                 )
fig_map_day.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# Styles to be applied to the page
NAV_STYLE = {
    "background-color": "#f2f2f2",
    "padding": "0.5rem 1.5rem"
}
k2_gen_info = {
    'font-size': '0.8rem',
    'font-weight': '300'
}
k2_title = {
    'font-size': '1.5rem',
    'padding-top': '1rem',
}
k2_profile = {
    'font-size': '0.8rem'
}
k2_profile_image = {
    'height': '120px',
    'width': '120px',
    'background-color': '#eee',
    'display': 'inline-block',
    'margin': '0 auto',
    'padding': '3px'
}
k2_team_container = {
    'padding-top': '2.5rem'
}
k2_tabs_width = {
    'width': '100%',
    'padding-left': '1rem'
}
k2_tabs_info = {
    'font-size': '1.1rem',
    'font-weight': '500',
    'color': "#4b73d4ff"
}
k2_search_bar = {
    'color': '#fff',
    'font-size': '1.3rem'
}

search_bar = dbc.Row(
    [
        dbc.Col(html.H2("Team 78", style=k2_search_bar))
    ],
    no_gutters=True,
    className="ml-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)

mainheader = dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=app.get_asset_url("app-logo-2.png"), height="50px")),
                    #dbc.Col(dbc.NavbarBrand("2020", className="ml-2")),
                ],
                align="center",
                no_gutters=True,
            )
        ),
        dbc.NavbarToggler(id="navbar-toggler"),
        dbc.Collapse(search_bar, id="navbar-collapse", navbar=True),
    ],
    color="#4b73d4ff",
    dark=True,
)

# Main components
navbar = dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("Overview", active=True, href="/home", id="link-1")),
        dbc.NavItem(dbc.NavLink("Project", href="/project", id="link-2")),
        dbc.NavItem(dbc.NavLink("About Us", href="/team", id="link-3"))
    ],
    style = NAV_STYLE
)

home_info = html.Div(
    [
        html.H2("About the Project", style=k2_title),
        html.P(
            "General information about the client and the project",
            style=k2_gen_info,
        ),
        html.Hr(className="my-2")
    ],
    className='col-md-12'
)

home_content = html.Div(
    [
        dbc.Row(home_info),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [

                            html.P("K2 Ingeniería, is a Colombian company, established in 1999, that integrates "+
                                   "experience in different areas of environmental, civil, mechanical, electronic "+
                                   "and systems engineering to offer a broad portfolio of consulting, monitoring "+
                                   "and technology integration. K2 Ingeniería, has specialized in the environmental "+
                                   "area, sector in the one that develops outstanding projects nationwide."),

                            html.P("Noise is an important variable that affects city planning, "+
                                   "wild life, and human health. K2 has many stations which are "+
                                   "used to measure noise and in some cases other environmental variables. "),

                            html.P("At this moment K2  is interested in understanding and  predicting noise \
                            based on that information. "),
                        ]
                    ),
                    className='col-md-6'
                ),
                dbc.Col(
                    html.Div(
                        [
                            html.P("The monitoring of environmental variables in real time (noise, meteorology,\
                                    air quality, water, etc.) from automatic stations or even from specific \
                                    campaigns usually generates a high volume of data that is normally difficult \
                                    to consult and is rarely used more beyond what is strictly required."),

                            html.Div(
                                [
                                    html.Img(src=app.get_asset_url("noise.png"), height="180px", className="center"),
                                ], style={'textAlign': 'center'}
                            ),
                        ]
                    ),
                    className='col-md-6'
                )
            ], style=k2_team_container
        )
    ],
    className='container'
)

# Team Page
team_info = html.Div(
    [
        html.H2("Meet the Team", style=k2_title),
        html.P(
            "We are Team #78 from Data Science 4 All: Colombia - 3rd edition ",
            style=k2_gen_info,
        ),
        html.Hr(className="my-2")
    ],
    className='col-md-12'
)

team_content = html.Div(
    [
        dbc.Row(team_info),
        dbc.Row([
            html.Div([
                html.Div(style=k2_profile_image, className='bd-placeholder-img rounded-circle'),
                html.H2("Mario Alejandro Benítez", style=k2_title),
                html.P("Mechanics Engineer  - MSc Mechanics Engineering", style=k2_profile)
                ],
                className='col-md-4 text-center'
            ),
            html.Div([
                html.Div(style=k2_profile_image, className='bd-placeholder-img rounded-circle'),
                html.H2("Hernán David Torres", style=k2_title),
                html.P("Statistic - Licensed at German Philology", style=k2_profile)
                ],
                className='col-md-4 text-center'
            ),
            html.Div([
                html.Div(style=k2_profile_image, className='bd-placeholder-img rounded-circle'),
                html.H2("Luz Adriana Moyano", style=k2_title),
                html.P("Telematics Engineer", style=k2_profile)
                ],
                className='col-md-4 text-center'
            ),
        ], style=k2_team_container),
        dbc.Row([
            html.Div([
                html.Div(style=k2_profile_image, className='bd-placeholder-img rounded-circle'),
                html.H2("David Pinzon Marroquin", style=k2_title),
                html.P("Industrial Engineer - MSc Operations Research", style=k2_profile)
                ],
                className='col-md-4 text-center'
            ),
            html.Div([
                html.Div(style=k2_profile_image, className='bd-placeholder-img rounded-circle'),
                html.H2("Fidel Olarte", style=k2_title),
                html.P("Industrial Engineer - MSc Industrial Engineering Candidate", style=k2_profile)
                ],
                className='col-md-4 text-center'
            ),
            html.Div([
                html.Div(style=k2_profile_image, className='bd-placeholder-img rounded-circle'),
                html.H2("Cesar Augusto Moreno", style=k2_title),
                html.P("Automation Engineer - MSc Business & Information Technologies", style=k2_profile)
                ],
                className='col-md-4 text-center'
            ),
        ]),
    ],
    className='container'
)

# Analysis Page
project_info = html.Div(
    [
        html.H2("Noise analysis", style=k2_title),
        html.P(
            "In this view you will find analysis for the information provided for noise in \
            different locations of Bogotá, Colombia",
            style=k2_gen_info,
        ),
        html.Hr(className="my-2")
    ],
    className='col-md-12'
)


tab_maps = dbc.Card(
    dbc.CardBody(
        [
            html.P("Noise changes during the day in Bogotá:", style=k2_tabs_info),
            html.P("Use the sliders to explore how the average noise changes during the day in Bogotá. You can Zoom-In and Zoom-out ", className="card-text"),
            html.Hr(className="my-2"),
            html.Div([dcc.Graph(figure=fig_map_hour)]),

            html.Hr(className="my-2"),
            html.P("Noise changes during the week in Bogotá:", style=k2_tabs_info),
            html.P(
                "Use the sliders to explore how the average noise changes during the day in Bogotá. You can Zoom-In and Zoom-out ",
                className="card-text"),
            html.Hr(className="my-2"),
            html.Div([dcc.Graph(figure=fig_day_series)]),

            #html.P("This is a tab!", className="card-text"),
            #dbc.Button("Click here", color="secondary"),
        ]
    ),
    className="mt-3",
)

tab_time_series = dbc.Card(
    dbc.CardBody(
        [
            html.P("Evolution of noise over time:", style=k2_tabs_info),
            html.Hr(className="my-2"),
            html.P("There are different sensors located in the City. Used the dropdown to select a sensor of interest.", className="card-text"),
            html.Div(
                [
                    dcc.Dropdown(
                        id='cai-dropdown',
                        options=[
                            {'label': 'New York City', 'value': 'NYC'},
                            {'label': 'Montreal', 'value': 'MTL'},
                            {'label': 'San Francisco', 'value': 'SF'}
                        ],
                        value='NYC'
                    ),
                    html.Div([dcc.Graph(figure=fig_day_series)]),
                ], className='container'
            ),
            #html.P("This is a tab!", className="card-text"),
            #dbc.Button("Click here", color="secondary"),
        ]
    ),
    className="mt-3",
)

tab_predictions = dbc.Card(
    dbc.CardBody(
        [
            html.P("Other graph:", style=k2_tabs_info),
            html.Hr(className="my-2"),
            html.P("Under construction...", className="card-text"),
            dbc.Button("Click here", color="secondary"),
        ]
    ),
    className="mt-3",
)

tabs = dbc.Tabs(
    [
        dbc.Tab(tab_maps, label="Maps"),
        dbc.Tab(tab_time_series, label="Time series"),
        dbc.Tab(tab_predictions, label="Predictions"),
    ]
)

project_content = html.Div(
    [
        dbc.Row(project_info),
        dbc.Row(
            [
                html.Div(tabs, style=k2_tabs_width)
            ],
            style=k2_team_container,
            className='col-md-12'
        )
    ],
    className='container'
)

content = html.Div(id="page-content")

##################################################
# Render the application:
##################################################
app.layout = html.Div(
    [
        dcc.Location(id="url"),
        mainheader,
        navbar,
        content
])

##################################################
# Filtering using dropdowns:
##################################################




##################################################
# Handling the render of the pages:
##################################################
@app.callback(
    [Output(f"link-{i}", "active") for i in range(1, 4)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/":
        # Treat page 1 as the homepage / index
        return True, False, False
    return [pathname == f"/page-{i}" for i in range(1, 4)]

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/home"]:
        return home_content
    elif pathname == "/project":
        return project_content
    elif pathname == "/team":
        return team_content
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

# add callback for toggling the collapse on small screens
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

if __name__ == '__main__':
    app.run_server(host='0.0.0.0',debug=True, port=8050)