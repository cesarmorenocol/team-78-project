import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from pages.header import HeaderPage
from pages.home import HomePage
from pages.team import TeamPage
from pages.project import ProjectPage

# External jquery
external_scripts = [{'src': 'https://code.jquery.com/jquery-3.2.1.min.js'}]

app = dash.Dash(__name__,
                external_scripts=external_scripts,
                external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
app.config['suppress_callback_exceptions'] = True


######################################################################
# Html elements:
######################################################################
# Main components
navbar = dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("Overview", active=True, href="/home", id="link-1")),
        dbc.NavItem(dbc.NavLink("Project", href="/project", id="link-2")),
        dbc.NavItem(dbc.NavLink("About Us", href="/team", id="link-3"))
    ],
    className='nav-elements'
)

# Access Pages
home = HomePage()
team = TeamPage()
project = ProjectPage()
header = HeaderPage()
# Content element
content = html.Div(id = "page-content")

##################################################
# Render the application:
##################################################
app.layout = html.Div(
    [
        dcc.Location(id="url"),
        header.content,
        navbar,
        content
])

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

@app.callback(
    Output("page-content", "children"), 
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname in ["/", "/home"]:
        return home.content
    elif pathname == "/project":
        return project.content
    elif pathname == "/team":
        return team.content
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

##################################################
# Add callback for toggling the collapse on small 
# screens
##################################################
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

##################################################
# Callbacks for ploting time seriesfgures:
##################################################
@app.callback(
    Output('time-series-15days', 'figure'),
    [Input('stations-selector', 'value')]
)
def get_selected_station(station):
    return project.time_series.get_15_days_figure(station)

@app.callback(
    Output('time-series-figure', 'figure'),
    [Input('stations-selector', 'value')]
)
def plot_time_series_figure(station):
    return project.time_series.get_time_series_figure(station, project.variable, project.medida)

@app.callback(
    Output('time-series-bar', 'figure'),
    [Input('stations-selector', 'value')]
)
def plot_bar_figure(station):
    return project.time_series.get_bar_figure(station)

##################################################
# Callbacks for predictions:
##################################################
@app.callback(
    Output('noise-level-pred', 'figure'),
    [Input('stations-predictions', 'value')]
)
def plot_bar_figure(station):
    return project.predictions.get_noise_level(station)

if __name__ == '__main__':
    app.run_server()