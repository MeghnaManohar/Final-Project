from bmi import *
import dash
import dash_table
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State

app = dash.Dash(external_stylesheets=[dbc.themes.MINTY])


#Gather Loan Info from User
inputs = dbc.Card(
    [
        dbc.Col(html.H6(children = "Please Enter your Information")),
        dbc.FormGroup(
            [
                dbc.RadioItems(
                    options=[
                        {'label': 'Male', 'value': "m"},
                        {'label': 'Female', 'value': 'f'},
                    ],
                    id= "sex", 
                    inline = True,
                ),
            ],
        ),
        dbc.Form(
            [
                dbc.FormGroup(
                    [
                        dbc.Label("Height"),
                        dbc.Input(id="height", placeholder='cm', type='number', min = 0)
                    ],
                    className = 'mr-3',
                ),
            ],
            inline = True,
        ),
        dbc.Form(
            [
                dbc.FormGroup(
                    [
                        dbc.Label("Weight"),
                        dbc.Input(id="weight", placeholder='kg', type='number', min = 0),
                    ],
                    className = 'mr-3',
                ),
            ],
            inline = True,
        ),
        dbc.Form(
            [
                dbc.FormGroup(
                    [
                        dbc.Label("Age"),
                        dbc.Input(id = "age", placeholder = "years", type = 'number', min = 0),
                    ],
                    className = 'mr-3',
                ),  
            ],
            inline = True,
        ),
        dbc.DropdownMenu(
            label= "Activity Level",
            color = "info",
            children=[
                dbc.DropdownMenuItem('Baseline BMR'),
                dbc.DropdownMenuItem("Litle to no excercise"),
                dbc.DropdownMenuItem("Light Excercise"),
                dbc.DropdownMenuItem("Moderate Exercise"),
                dbc.DropdownMenuItem("Heavy Exercise"),
                dbc.DropdownMenuItem("Very Heavy Exercise"),
                ],
            id = "activity"
        ), 
    dbc.Button(id='Sumbit', n_clicks=0, children='Submit', color = "success",)
   ],
   body=True
)

#Results Section 
results = dbc.Card(
    [
        dbc.Col(html.H5(children = "Results:")),
        dbc.FormGroup(
            [
                    html.Div(id="output")
            ],
        )
    ],
    body=True
)


#App Layout
app.layout = dbc.Container(
    [
        #Title
        dbc.Row(
            dbc.Col(
                html.H2(children = "Health App")
            )
        ), 
        #BMI
        dbc.Row(
            [
                dbc.Col(inputs, md=4),
                dbc.Col(results, md = 8),
            ],
            align="left",
        ),
    ],
    id="main-container",
    style={"display": "flex", "flex-direction": "column"},
    fluid=True
)

#Backend 
@app.callback(
    Output("output", "children"),
    [Input('submit', 'n_clicks')],
    [State("height", "value"), 
     State("weight", "value"),
     State("age", "value"),
     State("sex", "value"),
     State("activity", "value")]
)

def compute(height, weight, age, sex, actvity):
    if (height ==None, weight ==None, age ==None, sex==None, activity == None):
        return None
    height = height
    weight = weight
    age = age
    sex = sex
    activity = activity
    










if __name__ == '__main__':
    app.run_server(debug=True, use_reloader = False)
