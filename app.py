from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
app = Dash()


df = pd.read_csv("processed_data.csv")
df["date"]= pd.to_datetime(df["date"])
df= df.sort_values("date")
fig = px.line(df, x="date", y="sales", title="Pink morsel sales over time")
fig.update_layout(xaxis_title = "Date", yaxis_title = "Sales")

app.layout = html.Div([html.H1("Soul Foods Sales Dashboard"),dcc.Graph(figure=fig)])

if __name__ == "__main__":
    app.run(debug=True)