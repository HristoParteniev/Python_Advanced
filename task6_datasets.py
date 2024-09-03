"""imports"""
from abc import ABC, abstractmethod
import os
from datetime import datetime
import pandas as pd

class Dataset(ABC):

    @abstractmethod
    def _fetch_data():
        pass

    @abstractmethod
    def save_data():
        pass

    @abstractmethod
    def _transform_data():
        pass

    @abstractmethod
    def _clean_data():
        pass

class CSVDataset(Dataset): # – inherits Dataset and implements all its methods

    def __init__(self, src_filepath, target_filepath) -> None:
        super().__init__()
        self._src_filepath = src_filepath
        self._target_filepath = target_filepath
        self.data = None

    @property
    def src_filepath(self):
        """getter for src_filepath"""
        return self._src_filepath

    @src_filepath.setter
    def src_filepath(self, value):
        self._src_filepath = value

    @property
    def target_filepath(self):
        """setter for src_filepath"""
        return self._target_filepath

    @target_filepath.setter
    def target_filepath(self, value):
        self._target_filepath = value

    def __repr__(self) -> str:
        return f"CSVDataset(src_filepath='{self._src_filepath}',\
             target_filepath='{self._target_filepath}')"

    def __str__(self) -> str:
        return f"CSVDataset with source file at '{self._src_filepath}'\
             and target file at '{self._target_filepath}'"

    def _fetch_data(self):
        # Assuming the file contains CSV data
        try:
            self.data = pd.read_csv(self._src_filepath)
            print("Data fetched successfully.")
        except FileNotFoundError:
            print(f"File not found at {self._src_filepath}.")
        except Exception as exc:
            print(f"An error occurred while fetching data: {exc}")

    def _clean_data(self):
        if self.data is not None:
            self.data.dropna(axis=1, inplace=True) # removes columns with only BLANKS
            self.data.dropna(axis=0, inplace=True) # removes rows if there are any BLANKS
            print("Data cleaned successfully.")
        else:
            print("No data to clean.")

    def _transform_data(self):
        if self.data is not None:
            self.data['timestamp'] = datetime.now()
            print("Data transformed successfully.")
        else:
            print("No data to transform.")

    def fetch_and_prepare_data(self):
        """Public method to fetch, clean, and transform the data and not run protected methods."""
        self._fetch_data()
        self._clean_data()
        self._transform_data()

    def save_data(self):
        if self.data is not None:
            try:
                self.data.to_csv(self._target_filepath, index=False)
                print(f"Data saved successfully to {self._target_filepath}.")
            except Exception as exc:
                print(f"An error occurred while saving data: {exc}")
        else:
            print("No data to save. Fetch and transform data first.")

def main():
    """main function"""

    # Define the source and target file paths
    src_path = os.path.join(os.path.expanduser("~"),
    'OneDrive - Adastra, s.r.o\\Desktop\\employement-data.csv')
    tgt_path = os.path.join(os.path.expanduser("~"),
    'OneDrive - Adastra, s.r.o\\Desktop\\employement-data_edited_Hristo_Parteniev.csv')

    dataset = CSVDataset(src_path, tgt_path)
    dataset.fetch_and_prepare_data()
    dataset.save_data()

if __name__ == '__main__':
    main()
