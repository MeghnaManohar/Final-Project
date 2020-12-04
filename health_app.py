import dash
import dash_table
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State

app = dash.Dash(external_stylesheets=[dbc.themes.MINTY])


#Gather Loan Info from User
bmi_inputs = dbc.Card(
    [
        dbc.Col(html.H5(children = "Please Enter your Information to calculate your BMI")),
        dbc.FormGroup(
            [
                dcc.Input(id="height", placeholder='Height', type='number', min = 0),
                dcc.Input(id="weight", placeholder='Weight', type='number', min = 0),
                dcc.Input(id = "age", placeholder = "Age", type = 'number', min = 0)
            ],
        ),
        dbc.Button(id='buttonSearch', n_clicks=0, children='Submit', color = "success",),
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
                dbc.Col(bmi_inputs, md=6),
                dbc.Col(
                    dcc.Graph(id='output-bmi')),
            ],
            align="left",
        ),
    ],
    id="main-container",
    style={"display": "flex", "flex-direction": "column"},
    fluid=True
)


if __name__ == '__main__':
    app.run_server(debug=True, use_reloader = False)
