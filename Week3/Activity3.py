# Week 3 - Activity 3: Convert Dataset to Parquet and Compute Statistics
# Student: Fredierick Saladas
# Dataset: UCI Machine Learning Repository - Tic-Tac-Toe Endgame https://archive.ics.uci.edu/dataset/101/tic+tac+toe+endgame

import numpy as np
import pandas as pd
from ucimlrepo import fetch_ucirepo


class ParquetDataProcessor:
    def __init__(self, dataset_id, parquet_file):
        self.dataset_id = dataset_id
        self.parquet_file = parquet_file
        self.data = None

    def fetch_dataset(self):
        """Fetch the dataset from UCI Machine Learning Repository."""
        print("Fetching dataset...")
        dataset = fetch_ucirepo(id=self.dataset_id)
        X = dataset.data.features
        y = dataset.data.targets
        self.data = pd.concat([X, y], axis=1)
        print("Dataset fetched successfully!")
        return self.data

    def save_to_parquet(self):
        """Save the dataset to Parquet format."""
        if self.data is None:
            raise ValueError("No data to save. Please fetch the dataset first.")
        self.data.to_parquet(self.parquet_file, index=False)
        print(f"Dataset saved to Parquet file: {self.parquet_file}")

    def compute_statistics(self):
        """Compute max, min, mean, and absolute values."""
        if self.data is None:
            raise ValueError("No data available. Please fetch the dataset first.")

        # Convert categorical values to numeric for calculations
        numeric_data = self.data.copy()
        for col in numeric_data.columns:
            if numeric_data[col].dtype == object:
                numeric_data[col] = pd.factorize(numeric_data[col])[0]

        max_values = numeric_data.max()
        min_values = numeric_data.min()
        mean_values = numeric_data.mean()
        abs_values = numeric_data.abs()

        print("\n=== Dataset Statistics ===")
        print("\nMaximum values:\n", max_values)
        print("\nMinimum values:\n", min_values)
        print("\nAverage values:\n", mean_values)
        print("\nAbsolute values (first 5 rows):\n", abs_values.head())


def main():
    parquet_path = r"C:\Users\freds\MSE800-2025-2026\Week3\tic_tac_toe_endgame.parquet"
    processor = ParquetDataProcessor(dataset_id=101, parquet_file=parquet_path)

    # 1. Fetch dataset
    processor.fetch_dataset()

    # 2. Save to Parquet format
    processor.save_to_parquet()

    # 3. Compute and display statistics
    processor.compute_statistics()


if __name__ == "__main__":
    main()
