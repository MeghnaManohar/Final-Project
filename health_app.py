# Import all the necessary packages needed
# Citation: Layout code and comments are from Dash website. Sinly google Dash dbc layout
from bmi import *
from data import *
from test import *
import pytest
import dash
import dash_table
import dash_table as dt
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output, State

# Set the theme
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

#######################################################################################################################
# LAYOUT DESIGN

# the style arguments for the sidebar.
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "20rem",
    "padding": "2rem 1rem",
    "background-color": "#dbf3ff",
}

# Build the style for the main content. Situate it to the right of the sidebar and add some padding.
CONTENT_STYLE = {
    "margin-left": "22rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

# Content for the sidebar
sidebar = html.Div(
    [
        html.H1("The MP Health App", className="display-4", style={'font-weight': 'bold'}),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Overview", href="/page-1", id="page-1-link"),
                dbc.NavLink("BMI Calculator", href="/page-2", id="page-2-link"),
                dbc.NavLink("Calorie Calculator", href="/page-3", id="page-3-link"),
                dbc.NavLink("Exercise Schedule", href="/page-4", id="page-4-link"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)
#######################################################################################################################


# Build energy table
# Energy Table
energy_card = dbc.Card(
    [
        dbc.Col(html.H5(children="Energy from Common Food Components:",
                        style={'font-weight': 'bold'})),
        dbc.Col(
            dash_table.DataTable(
                id='energy-table',
                columns=[{"name": i, "id": i} for i in energy_df.columns],
                data=energy_df.to_dict('records'),
                style_cell={'textAlign': 'left',
                            'margin-left': 'auto',
                            'margin-right': 'auto',
                            'padding-left': '20px',
                            'whiteSpace': 'normal',
                            'height': 'auto',
                            },
                style_header={
                    'backgroundColor': 'green',
                    'fontWeight': 'bold',
                    'color': 'white',
                },
                style_cell_conditional=[
                    {'if': {'column_id': 'Food Components'},
                     'width': '30%'}
                ],
                sort_action="native",
                fixed_rows={'headers': True},
                style_table={'overflowX': 'scroll'},
            )
        )
    ],
    body=True
)

# Build Exercise card
exercise_card = dbc.Card(
    [
        dbc.Col(html.H5(children="Calories Burned from Common Exercises:",
                        style={'font-weight': 'bold'})
                ),
        dbc.Col(
            dash_table.DataTable(
                id='exercise-table',
                columns=[{"name": i, "id": i, "deletable": True, } for i in exercise_df.columns],
                data=exercise_df.to_dict('records'),
                style_cell={
                    'margin-left': 'auto',
                    'margin-right': 'auto',
                    'padding-left': '20px',
                    'whiteSpace': 'normal',
                    'height': 'auto',
                },
                style_header={
                    'textAlign': 'center',
                    'backgroundColor': ' blue',
                    'fontWeight': 'bold',
                    'color': 'white',
                },
                style_data={
                    'textAlign': 'left',
                },
                style_cell_conditional=[
                    {'if': {'column_id': 'Activity (1 hour)'},
                     'width': '30%'}
                ],
                filter_action="native",
                sort_action="native",
                page_size=25,
                fixed_rows={'headers': True},
                style_table={'overflowX': 'scroll'}
            )
        )
    ],
    body=True
)

# Build the exercise tab
tab4_exercise_schedule = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                html.H1(children="The Exercise and Enery Table", style={'font-weight': 'bold'}),
            )
        ),

        html.Br(),

        dbc.Row(
            dbc.Col(
                [
                    exercise_card
                ]
            )
        ),
        dbc.Row(
            dbc.Col(
                [
                    energy_card
                ]
            )
        )
    ]
)

# Build table for the calorie tab
table = dbc.Card(
    [
        dbc.Col(html.H3("Calorie Table:")),

        dbc.Col(
            html.Div(
                id='calorie-table',
            )
        )
    ]
)

## Build the calorie content in tab 3
tab3_calorie_content = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                html.H1(children="Calorie Counter and Food Calculator", style={'font-weight': 'bold'}),
            )
        ),

        html.Br(),

        dbc.Row(
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardImg(
                            src= calorie_img),

                    ],
                )
            )
        ),

        html.Br(),

        dbc.Row(
            dbc.Col(
                dbc.Card(
                    [
                        dbc.FormGroup(
                            [
                                dbc.Label(html.H4("Search")),
                                dcc.Dropdown(placeholder="e.g., apples, Sangria,...",
                                             value="search",
                                             id="counter",
                                             options=[{"label": col, "value": col} for col in
                                                      foodData_df["Food"].unique()],
                                             multi=True
                                             ),
                                dbc.FormText("Tip: do not include restaurant names "),
                            ]
                        ),
                        dbc.Button("Submit", id='submitC', n_clicks=0, color="success"),
                    ]
                )
            )
        ),
        html.Br(),

        dbc.Row(
            [
                dbc.Col(table),
                html.Br(),
            ]
        ),

        html.Br(),

        dbc.Row(
            [
                dbc.Col(
                    (dbc.Alert(html.H2(id="sum-calories"), color="primary"))
                )
            ]
        )
    ]
)

#######################################################################################################################

# Build BMI Chart
bmi_card = dbc.Card(
    [
        dbc.CardImg(src="https://sfc-mma.com/wp-content/uploads/2019/11/bmi-featured.png"),

    ],
)

#######################################################################################################################


# Build the BMI and BMR results table which will be displayed

row1 = html.Tr([html.Td("BMI:"), html.Td(id='bmi-output'), html.Td(id='bmi-range')])
row2 = html.Tr([html.Td("To maintain your weight you need:"), html.Td(id="maintain-output"), html.Td("Kcal/day")])
row3 = html.Tr([html.Td("To lose .45 kg (1 lb) per week you need:"), html.Td(id="lose-output"), html.Td("Kcal/day")])
row4 = html.Tr([html.Td("To gain .45 kg (1 lb) per week you need:"), html.Td(id="gain-output"), html.Td("Kcal/day")])

table_body = [html.Tbody([row1, row2, row3, row4])]

results = dbc.Table(table_body,
                    bordered=True,
                    striped=True, )

#######################################################################################################################

# Build activity level
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

# Build the age input
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
            width=6,
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
                dbc.Input(id="height", placeholder='-', type='float', min=0),
            ],
            width=6,
        ),
        dbc.Col(
            [
                dcc.Dropdown(
                    id="height-dropdown",
                    placeholder="cm",
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

# Build the sex input
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

# Build Inputs
inputs = dbc.Form(
    [
        sex, height, weight, age, activity_level,
    ],
)

## Tab-2 Content
tab2_BMI_content = html.Div(
    [
        dbc.Row(
            dbc.Col(
                html.H1("The BMI Calculator", style={'font-weight': 'bold'}),
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
# tab1-founder
founder = dbc.Row(
    [
        dbc.Col(
            [
                dbc.Card(
                    [
                        dbc.CardBody(html.H5("Meghna Manohar ('21 BA/MA)")),
                        dbc.CardImg(src=meg_img, bottom=True)
                    ]
                )
            ]
        ),
        html.Br(),

        dbc.Col(
            [
                dbc.Card(
                    [
                        dbc.CardBody(html.H5("Precious Ufomadu ('21 BA/MA)")),
                        dbc.CardImg(src=precious_img, bottom=True)
                    ]
                )
            ]
        ),
    ]
)

# Tab-1 Content
tab1_content = dbc.Row(
    [
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            html.P(
                                "The MP Health App helps users live a healthier lifestyle! After obtaining information, "
                                "Our app outputs the user's BMI, BMR, and suggests daily calories depending on whether "
                                "you want to maintain/lose/gain weight. Learn about common exercises and create your "
                                "own daily menu!"
                            ),
                            html.P(
                                "How to Use: Just input your sex, weight, height, age, and activity levels (in metric "
                                "system or in the imperial system) and the MP Health App will calculate your Body "
                                "Mass Index (BMI) which you can crosscheck with the BMI Range Chart. We'll also "
                                "calculate your Basal Metabloic Rate (BMR) which helps determine how many calories "
                                "you should have daily. We've also included common exercises to help you figure out "
                                "how to burn calories. Finally, in our last tab, you can search of food database and "
                                "build a menu, noting the calories associated with the food. "
                            ),
                            html.P(
                                "Notes: Your BMR is calculated using the revised Harris-Benedict Equation.",

                                className="card-text",
                            ),
                        ]
                    ),
                    # Brandeis Logo
                    dbc.CardImg(src=brandeis_logo, top=False),
                    dbc.CardBody(
                        html.P("Creators: Meghna Manohar & Precious Ufomadu", className="card-text")
                    ),
                ],
            )
        ),
        html.Br(),

    ]
)

## Tab-1 Content
tab1_overview_content = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                html.H1("The BMI and Calorie Counter", style={'font-weight': 'bold'}),
            ),
        ),

        html.Br(),

        dbc.Row(
            dbc.Col(
                tab1_content
            )
        ),

        html.Br(),

        dbc.Row(
            dbc.Col(
                founder
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
        return tab3_calorie_content
    elif pathname == "/page-4":
        return tab4_exercise_schedule
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
# Test
@pytest.mark.parametrize('height, weight, h_system, w_system',
                         [
                             (180, 165, 'metric', 'imperial'),
                             (152.4, 118.9, 'metric', 'imperial'),
                         ])
# Callback
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
    if (height == None or weight == None):
        return None, None
    # Use function from bmi.py to calculate bmi and bmi_range
    return bmi(float(height), float(weight), str(h_system), str(w_system))


#######################################################################################################################
##Backend
# Test
@pytest.mark.parametrize('height, weight, age, sex, activity, h_system, w_system',
                         [
                             (180, 60, 22, 'm', 2, 'metric', 'metric'),
                             (60.1, 118.9, 'f', 22, 3, 'imperial', 'imperial'),
                         ])
# Callback
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
    if (height == None or weight == None or age == None or sex == None or activity == None):
        return None, None, None
    # Use function from bmi.py to calculate bmr values
    return bmr(float(height), float(weight), float(age), str(sex), int(activity), str(h_system), str(w_system))


#######################################################################################################################

# Build the Calorie Table
@app.callback(
    Output("calorie-table", "children"),
    Input("submitC", "n_clicks"),
    [State("counter", "value")
     ]
)
def update_dataTable(nclicksC, foods):
    if nclicksC:
        total_food_df = pd.DataFrame()
        for food in foods:
            food_df = foodData_df[foodData_df["Food"] == food]
            total_food_df = total_food_df.append(food_df)

        # Remove cols where everything is zero
        total_food_df = total_food_df.loc[:, (total_food_df != 0).any(axis=0)]

        data = total_food_df.to_dict('records')
        columns = [{"name": i, "id": i} for i in total_food_df.columns]

        return dt.DataTable(data=data, columns=columns,
                            style_cell={'textAlign': 'left',
                                        'margin-left': 'auto',
                                        'margin-right': 'auto',
                                        'padding-left': '20px'
                                        },
                            style_header={'backgroundColor': 'blue',
                                          'fontWeight': 'bold',
                                          'color': 'white',
                                          },
                            style_table={'overflowX': 'scroll'}

                            )


# Return the amount of calories consumed
# Build the Calorie Table
@app.callback(
    Output("sum-calories", "children"),
    Input("submitC", "n_clicks"),
    [State("counter", "value")
     ]
)
def display_total_calories(nclicksC, foods):
    if nclicksC:
        total_food_df = pd.DataFrame()
        for food in foods:
            food_df = foodData_df[foodData_df["Food"] == food]
            total_food_df = total_food_df.append(food_df)
        sum = round(total_food_df['Calories'].sum(), 2)

        return 'You consumed: {} worth of calories today'.format(sum)


if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)