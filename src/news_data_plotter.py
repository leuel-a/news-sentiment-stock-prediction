import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import Any

months_of_year = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]


class NewsDataPlotter:
    def __init__(self, data: Any):
        self.data = data

    def plot_year_data(self, year: int, x_label: str, y_label: str):
        year_data = pd.Series(self.data.loc[year], index=[month[:3] for month in months_of_year])
        year_data.plot(kind='line', figsize=(20, 10), marker='o', lw='2')

        plt.xticks(ticks=np.arange(0, 12, 1), labels=[month[:3] for month in months_of_year])
        plt.yticks(ticks=np.arange(0, year_data.max() + 5, step=2))

        plt.savefig(f"./images/{year}_News_Month_News_Count_Plot", format='png')


