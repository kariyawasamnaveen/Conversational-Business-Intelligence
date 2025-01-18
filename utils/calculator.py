import pandas as pd

class DataCalculator:
    def __init__(self, data_file):
        # Load data and remove extra spaces from column names
        self.data = pd.read_csv(data_file)
        self.data.columns = self.data.columns.str.strip()

    def calculate_average(self, column):
        if column in self.data.columns:
            return self.data[column].mean()
        return None

    def calculate_maximum(self, column):
        if column in self.data.columns:
            return self.data[column].max()
        return None
