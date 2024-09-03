import datetime as dt

import talib as ta
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame, Series

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


class FinancialAnalyzer:
    """"""

    def __init__(self, df: DataFrame, symbol: str):
        """Initializes the Financial Analyzer object

        Parameters
        ----------
        df : pandas.DataFrame
            A pandas DataFrame containing some stock and financial data
            Usually it contains the columns
                Date, Open, Close, High, Low, Adj Close, Volume
        symbol : str
            The stock symbol of the dataset
        """

        self.df = df
        self.symbol = symbol

    @staticmethod
    def __calculate_simple_moving_average(df: DataFrame, window_size: int = 100):
        """Calculates the simple moving average for the data

        Parameters
        ----------
        :param df: the dataframe the contains the financial data
        :type df: DataFrame

        :param window_size: the window size for calculating the moving average
        :type window_size: int

        :return: The simple moving average of the data
        :rtype: Series
        """

        return ta.SMA(df["Close"], window_size)

    @staticmethod
    def __calculate_exponential_moving_average(df: DataFrame, window_size: int = 100):
        """Calculates the simple moving average for the data

        Parameters
        ----------
        :param df: the dataframe that contains the financial data
        :type df: DataFrame

        :param window_size: the window size for calculating the moving average
        :type window_size: int

        :return: The exponential moving average of the data
        :rtype: Series
        """

        return ta.EMA(df["Close"], window_size)

    @staticmethod
    def __calculate_relative_strength_index(df: DataFrame, timeperiod: int = 14):
        """Calculates the Relative Strength Index, RSI for the data

        Parameters
        ----------
        :param df: the DataFrame that contains the financial data
        :type df: DataFrame

        :param timeperiod: the time period to calculate the RSI
        :type timeperiod: int

        :return: The RSI of the data
        :rtype: Series
        """

        return ta.RSI(df["Close"], timeperiod)

    @staticmethod
    def __calculate_average_convergence_divergence(df: DataFrame):
        """Calculates the MACD for the financial data"""

        return ta.MACD(df["Close"])

    def calculate_technical_indicators(self):
        """Calculates technical indicators for the financial data"""

        self.df["SMA"] = self.__calculate_simple_moving_average(self.df, 100)
        self.df["EMA"] = self.__calculate_exponential_moving_average(self.df, 100)
        self.df["RSI"] = self.__calculate_relative_strength_index(self.df, 14)

        # MACD - Moving Average Convergence Divergence Indicator
        macd_line, macd_signal_line, _ = self.__calculate_average_convergence_divergence(self.df)
        self.df["MACD"] = macd_line
        self.df["MACD_Signal"] = macd_signal_line

    def plot_sma(self):
        """Plots the SMA for the give financial data"""
        fig = px.line(self.df, x="Date", y=["Close", "SMA"],
                      title=f"Stock Price with Moving Average for {self.symbol}")
        fig.show()

    def plot_rsi(self):
        """Plots the SMA for the given financial data"""

        # TODO: Update the height ratios to make the visuals more bigger
        fig = make_subplots(rows=2, cols=1)

        fig.add_trace(
            go.Scatter(x=self.df.index, y=self.df["Close"], mode="lines", name="Close Price"),
            row=1, col=1
        )

        fig.add_trace(
            go.Scatter(x=self.df.index, y=self.df["RSI"], mode="lines", name="RSI"),
            row=2,
            col=1,
        )

        fig.add_shape(
            type="line",
            x0=self.df.index.min(),
            x1=self.df.index.max(),
            y0=70,
            y1=70,
            row=2,
            col=1,
            line=dict(color="red")
        )

        fig.add_shape(
            type="line",
            x0=self.df.index.min(),
            x1=self.df.index.max(),
            y0=20,
            y1=20,
            row=2,
            col=1,
            line=dict(color="green", width=2)
        )

        fig.show()

    def plot_ema(self):
        """Plots the EMA for the given financial data"""

        fig = px.line(self.df, x="Date", y=["Close", "EMA"],
                      title=f"Stock Price with Exponential Moving Average for {self.symbol}")
        fig.show()

    def plot_macd(self):
        """Plots the MACD for the given financial data"""

        # TODO: Add the histogram for the MACD in the figure
        fig = px.line(self.df, x="Date", y=["MACD", "MACD_Signal"],
                      title=f"Moving Average Convergence Divergence (MACD) for {self.symbol}")

        fig.show()

    def plot_sma_vs_ema(self):
        """Plts the SMA vs the EMA for the given financial data"""

        fig = px.line(self.df, x="Date", y=["SMA", "EMA", "Close"], title=f"SMA vs EMA for {self.symbol}")
        fig.show()
