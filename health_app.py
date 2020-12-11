# Import all the necessary packages needed
from bmi import *
from test import *
import pytest
import dash
import dash_table
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output, State


#Set the theme
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)


#######################################################################################################################
# LAYOUT DESIGN

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "20rem",
    "padding": "2rem 1rem",
    "background-color": "#dbf3ff",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "22rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H1("The MP Health App", className="display-4"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Overview", href="/page-1", id="page-1-link"),
                dbc.NavLink("BMI Calculator", href="/page-2", id="page-2-link"),
                dbc.NavLink("Calorie Calculator", href="/page-3", id="page-3-link"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)
#######################################################################################################################

#Build BMI Chart
bmi_card = dbc.Card(
    [
        dbc.CardImg(src = "https://sfc-mma.com/wp-content/uploads/2019/11/bmi-featured.png"),
    ],
 body=True,
 style={"width": "92rem"},
)


#######################################################################################################################

# Build the BMI and BMR results table which will be displayed

row1 = html.Tr([html.Td("BMI:"), html.Td(id ='bmi-output'), html.Td(id ='bmi-range')])
row2 = html.Tr([html.Td("To maintain your weight you need:"), html.Td(id="maintain-output"), html.Td("Kcal/day")])
row3 = html.Tr([html.Td("To lose .45 kg (1 lb) per week you need:"), html.Td(id="lose-output"), html.Td("Kcal/day")])
row4 = html.Tr([html.Td("To gain .45 kg (1 lb) per week you need:"), html.Td(id="gain-output"), html.Td("Kcal/day")])

table_body = [html.Tbody([row1, row2, row3, row4])]

results = dbc.Table(table_body, 
                    bordered=True,
                    striped=True,)

#######################################################################################################################
#Build activity level
activity_level = dbc.FormGroup(
    [
        dbc.Label("Activity Level", html_for="activity-dropdown", width=2),
        dbc.Col(
            [
                dcc.Dropdown(
                    id="activity-dropdown",
                    placeholder="Select Activity Level",
                    style={"min-width": "250px"},
                    options=[
                        {'label': 'Baseline BMR', 'value': '0'},
                        {'label': "Sedentary", 'value': '1'},
                        {'label': "Lightly Active", 'value': '2'},
                        {'label': "Moderately Active", 'value': '3'},
                        {'label': "Very Active", 'value': '4'},
                        {'label': "Extra Active", 'value': '5'},
                    ],
                ),
            ],

            width=10,
        ),
    ],
    row=True,
)

#Build the age input
age = dbc.FormGroup(
    [
        dbc.Label("Age", html_for="age", width=2),
        dbc.Col(
            dbc.Input(id="age", placeholder="years", type='float', min=0),

            width=10,
        ),
    ],
    row=True,
)

# Build the weight input
weight = dbc.FormGroup(
    [
        dbc.Label("Weight", html_for="weight", width=2),
        dbc.Col(
            [
                dbc.Input(id="weight", placeholder='-', type='float', min=0),
            ],
            width = 6,
        ),
        dbc.Col(
            [
                dcc.Dropdown(
                    id="weight-dropdown",
                    placeholder="kg",
                    style={"min-width": "100px"},
                    options=[
                        {'label': 'kg', 'value': 'metric'},
                        {'label': 'lbs', 'value': 'imperial'},
                    ],
                ),
            ],

            width=4,
        ),
    ],
    row=True,
)


# Build the height input
height = dbc.FormGroup(
    [
        dbc.Label("Height", html_for="height", width=2),
        dbc.Col(
            [
                dbc.Input(id="height", placeholder='-', type='float', min = 0),
            ],
            width = 6,
        ),
        dbc.Col(
            [
                dcc.Dropdown(
                    id = "height-dropdown",
                    placeholder = "cm",
                    style={"min-width": "100px"},
                    options=[
                        {'label': 'cm', 'value': 'metric'},
                        {'label': 'inch', 'value': 'imperial'},
                        ],
                ),
            ],

            width=4,
        ),
    ],
    row=True,
)

#Build the sex input
sex = dbc.FormGroup(
    [
        dbc.Label("Sex", html_for="sex", width=2),
        dbc.Col(
            dbc.RadioItems(
                id="sex",
                options=[
                    {"label": "Male", "value": "m"},
                    {"label": "Female", "value": "f"},
                ],
            ),
            width=10,
        ),
    ],
    row=True,
)

#Build Inputs
inputs = dbc.Form(
    [
        sex, height, weight, age, activity_level,
    ],
)
#######################################################################################################################

#Tab-2 Content
tab2_BMI_content = html.Div(
    [
        dbc.Row(
            dbc.Col(
                html.H2("The BMI Calculator"),
            ),
        ),

        html.Br(),

        dbc.Row(
            dbc.Col(
                html.H5("Enter your information", style={'font-weight': 'bold'}),
            )
        ),

        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        [
                            inputs,
                            dbc.Button(id='submit', n_clicks=0, children='Submit', color="success"),
                        ]

                    )
                ),
            ]
        ),

        html.Br(),

        dbc.Row(
            dbc.Col(
                html.H5("Results", style={'font-weight': 'bold'}),
            )
        ),

        dbc.Row(
            dbc.Col(
                dbc.Card(
                    results
                )
            )
        ),

        html.Br(),

        dbc.Row(
            dbc.Col(
                html.H5("BMI Chart", style={'font-weight': 'bold'}),
            )
        ),

        dbc.Row(
            dbc.Col(
                bmi_card
            )
        ),

    ]
)

#######################################################################################################################
#Tab-1 Content
tab1_content = dbc.Card(
    [
        dbc.CardBody(
            [
                html.P(
                    "The MP Health App helps users live a healthier lifestyle! After obtaining information, "
                    "Our app outputs the user's BMI, BMR, and suggests daily calories depending on whether you want to "
                    "maintain/lose/gain weight. Learn about common exercises and create your own daily menu!"
                    ),
                html.P(
                    "How to Use: Just input your sex, weight, height, age, and activity levels (in metric system or in the "
                    "imperial system) and the MP Health App will calculate your Body Mass Index (BMI) which you can crosscheck "
                    "with the BMI Range Chart. We'll also calculate your Basal Metabloic Rate (BMR) "
                    "which helps determine how many calories you should have daily. We've also included "
                    "common exercises to help you figure out how to burn calories. "
                    "Finally, in our last tab, you can search of food database and build a menu, noting "
                    "the calories associated with the food. "
                    ),
                html.P( 
                    "Notes: Your BMR is calculated using the revised Harris-Benedict Equation.",
                    
                    className="card-text",
                ),
            ]
        ),
        #Brandeis Logo
        dbc.CardImg(src="data:image/jpeg;base64,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", top=False),
        dbc.CardBody(
            html.P("Creators: Meghna Manohar & Precious Ufomadu", className="card-text")
        ),
    ]
)


#Tab-1 Content
tab1_overview_content = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                html.H2("The BMI and Calorie Counter"),
            ),
        ),

        html.Br(),

        dbc.Row(
            dbc.Col(
                tab1_content
            )
        ),
    ]
)

#######################################################################################################################


# Content style for each page
content = html.Div(id="page-content", style=CONTENT_STYLE)

# Build Page layout
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


# this callback uses the current pathname to set the active state of the
# corresponding nav link to true, allowing users to tell see page they are on
@app.callback(
    [Output(f"page-{i}-link", "active") for i in range(1, 4)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/":
        # Treat page 1 as the homepage / index
        return True, False, False
    return [pathname == f"/page-{i}" for i in range(1, 4)]


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/page-1"]:
        return tab1_overview_content
    elif pathname == "/page-2":
        return tab2_BMI_content
    elif pathname == "/page-3":
        return html.P("Oh cool, this is page 3!")
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )
#######################################################################################################################
###Backend
##BMI Calculator
#Test
@pytest.mark.parametrize('height, weight, h_system, w_system',
                         [
                             (180, 165, 'metric', 'imperial'),
                             (152.4, 118.9, 'metric', 'imperial'),
                         ])
#Callback
@app.callback(
    [Output("bmi-output", "children"),
    Output("bmi-range", "children")],
    
    [Input('submit', 'n_clicks')],
    
    [State("height", "value"), 
     State("weight", "value"),
     State("height-dropdown", "value"),
     State("weight-dropdown", "value")]
)

def compute(nclicks, height, weight, h_system, w_system):
    if (height == None or weight ==None):
        return None, None
    #Use function from bmi.py to calculate bmi and bmi_range
    return bmi(float(height), float(weight), str(h_system), str(w_system))


##BMR Calculator
#Test
@pytest.mark.parametrize('height, weight, age, sex, activity, h_system, w_system',
                          [
                              (180, 60, 22,'m', 2, 'metric', 'metric'),
                              (60.1, 118.9, 'f',22, 3, 'imperial', 'imperial'),
                          ])
#Callback
@app.callback(
    [Output("maintain-output", "children"),
     Output('lose-output', "children"),
     Output("gain-output", "children")],

    [Input('submit', 'n_clicks')],

    [State("height", "value"), State("weight", "value"), State("age", "value"),
     State("sex", "value"), State("activity-dropdown", "value"),
     State("height-dropdown", "value"),
     State("weight-dropdown", "value")]
)

def compute(nclicks, height, weight, age, sex, activity, h_system, w_system):
    if (height == None or weight ==None or age ==None or sex==None or activity == None):
        return None, None, None
    #Use function from bmi.py to calculate bmr values
    return bmr(float(height), float(weight), float(age), str(sex), int(activity), str(h_system), str(w_system))


if __name__ == '__main__':
    app.run_server(debug=True, use_reloader = False)