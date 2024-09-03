from typing import Any

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class NewsDataPlotter:
    _months_of_year = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    @staticmethod
    def plot_monthly_data(data: pd.DataFrame, year: int, month: int) -> None:
        pass

    @staticmethod
    def plot_yearly_data(data: pd.DataFrame, year: int):
        pass
