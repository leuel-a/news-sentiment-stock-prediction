import talib as ta
import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt


# import pandas_datareader as web  # this is for downloading the finance data from the yahoo finance


class FinancialAnalyzer:
    """"""

    def __init__(self, df: pd.DataFrame, name: str):
        """Initializes the Financial Analyzer object

        Parameters
        ----------
        df : pandas.DataFrame
            A pandas DataFrame containing some stock and financial data
            Usually it contains the columns
                Date, Open, Close, High, Low, Adj Close, Volume
        """

        self.df = df
        self.name = name

    @staticmethod
    def __calculate_simple_moving_average(df: pd.DataFrame, window_size: int = 100):
        """Calculates the simple moving average for the data"""

        return ta.SMA(df["Close"], window_size)

    def calculate_technical_indicators(self):
        """Calculates technical indicators for the financial data"""

        self.df["SMA"] = self.__calculate_simple_moving_average(self.df, 100)

    def plot_sma(self):
        """Plots the SMA for the give financial data"""
        # TODO: if the sma is not calculated we need to call that before the visualization can be done

        # TODO: this visualization for testing purpose later it will be changed to plotly as per requirement
        plt.figure(figsize=(20, 10))

        # calculate the X and Y axis for the dataframe
        sma = self.df["SMA"]
        date = self.df["Date"]

        plt.title(f"SMI for {self.name}")

        plt.plot(sma, date, lw=2)

        plt.show()

    def plot_rsi(self):
        """Plots the SMA for the given financial data"""

        pass

    def plot_ema(self):
        """Plots the EMA for the given financial data"""

        pass
