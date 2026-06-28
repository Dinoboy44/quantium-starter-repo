from dash import Dash, html, dcc, Input, Output, callback 
import plotly.express as px
import pandas as pd
app = Dash(__name__)


df = pd.read_csv("processed_data.csv")
df["date"]= pd.to_datetime(df["date"])
df= df.sort_values("date")

app.layout = html.Div([html.H1("Soul Foods Sales Dashboard",id="header",style={"textAlign":"center","color":"#10288C"}),dcc.RadioItems(id="region-filter",options=[{"label":"All","value":"all"},{"label":"North","value":"north"},{"label":"South","value":"south"},{"label":"East","value":"east"},{"label":"West","value":"west"}],value="all",inline=True,style={"textAlign":"center"}),dcc.Graph(id="filteredfig")],style={"padding":"30px","fontfamily":"Arial","background":"#EAF6AD"})

@callback(Output('filteredfig','figure'),Input('region-filter','value'))
def update_graph(value):
    if value == 'all':
        filtered_df = df
    else:
        filtered_df = df[df["region"]==value]

    fig = px.line(filtered_df, x="date", y="sales", title="Pink morsel sales over time",template="plotly_white")
    fig.update_layout(xaxis_title = "Date", yaxis_title = "Sales")

    return fig


if __name__ == "__main__":
    app.run(debug=True)