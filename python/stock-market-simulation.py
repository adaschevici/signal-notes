from shiny import App, render, ui, reactive
import numpy as np
import pandas as pd
import yfinance as yf
from loguru import logger

# stock_data: pd.DataFrame = yf.download(
#     tickers="GOOGL AAPL MSFT META NVDA",
#     period="1d",
#     interval="1m",
#     group_by="ticker",
#     auto_adjust=True,
#     prepost=True,
#     threads=True,
#     proxy=None,
# )
# Define the app UI
app_ui = ui.page_fluid(
    ui.h2("Stock Data Viewer"),
    ui.input_dark_mode(),
    ui.input_select(
        id="dropdown",
        label="Choose an option:",
        choices=("GOOGL", "AAPL", "MSFT", "META", "NVDA"),
    ),
    ui.input_date_range(
        "date_range", "Select Date Range:", start="2023-01-01", end="2023-12-31"
    ),
    ui.input_action_button("load_data", "Load Data"),
    ui.output_data_frame("stock_data"),
)


# Define the server logic
def server(input, output, session):
    @output
    @render.data_frame
    @reactive.event(input.load_data)
    def stock_data():
        stock_hist = yf.download(
            input.dropdown.get(),
            start="2023-01-01",
            end="2024-11-01",
            group_by="ticker",
        )
        if isinstance(stock_hist.columns, pd.MultiIndex):
            stock_hist.columns = [col[1] for col in stock_hist.columns]
        stock_hist.reset_index(inplace=True)
        logger.info(stock_hist.head())
        return render.DataTable(stock_hist.head())


# Create the app
app = App(app_ui, server)

# To run this script, use: shiny run <script_name.py>
