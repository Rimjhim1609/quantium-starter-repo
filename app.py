import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load the processed data
df = pd.read_csv("data/output.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

app = dash.Dash(__name__)

price_increase_date = pd.Timestamp("2021-01-15").timestamp() * 1000

app.layout = html.Div([
    html.H1(
        "Pink Morsel Sales Visualiser",
        style={
            "textAlign": "center",
            "color": "#ff69b4",
            "fontFamily": "Arial",
            "padding": "20px",
            "backgroundColor": "#1a1a2e",
            "margin": "0"
        }
    ),
    html.Div([
        html.Label(
            "Filter by Region:",
            style={"color": "white", "fontFamily": "Arial", "fontSize": "18px"}
        ),
        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": " All", "value": "all"},
                {"label": " North", "value": "north"},
                {"label": " South", "value": "south"},
                {"label": " East", "value": "east"},
                {"label": " West", "value": "west"},
            ],
            value="all",
            inline=True,
            style={"color": "white", "fontFamily": "Arial", "fontSize": "16px"}
        )
    ], style={
        "backgroundColor": "#16213e",
        "padding": "20px",
        "textAlign": "center"
    }),
    dcc.Graph(id="sales-chart")
], style={"backgroundColor": "#1a1a2e", "minHeight": "100vh"})

@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(region):
    if region == "all":
        filtered = df
    else:
        filtered = df[df["region"] == region]

    fig = px.line(
        filtered,
        x="date",
        y="sales",
        color="region",
        title="Pink Morsel Sales Over Time",
        labels={"date": "Date", "sales": "Sales ($)", "region": "Region"}
    )
    fig.add_vline(
        x=price_increase_date,
        line_dash="dash",
        line_color="red",
        annotation_text="Price Increase"
    )
    fig.update_layout(
        plot_bgcolor="#0f3460",
        paper_bgcolor="#16213e",
        font_color="white",
        title_font_color="#ff69b4"
    )
    return fig

if __name__ == "__main__":
    app.run(debug=True)