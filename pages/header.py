import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

class HeaderPage():
    search_bar = dbc.Row(
        [
            dbc.Col(html.H2("Team 78", className='k2-search-bar'))
        ],
        no_gutters=True,
        className="ml-auto flex-nowrap mt-3 mt-md-0",
        align="center",
    )

    content = dbc.Navbar(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Div(className='logo')),
                    ],
                    align="center",
                    no_gutters=True,
                )
            ),
            dbc.NavbarToggler(id = "navbar-toggler"),
            dbc.Collapse(search_bar, id = "navbar-collapse", navbar = True),
        ],
        color="#4b73d4ff",
        dark=True,
    )