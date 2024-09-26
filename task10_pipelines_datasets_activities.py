from abc import ABC, abstractmethod
import datetime
import os
from time import sleep
import pandas as pd


class Dataset(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def preview(self):
        pass

    @abstractmethod
    def show_schema(self):
        pass

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def write_data(self):
        pass

class JSONDataset(Dataset):
    def __init__(self, src_filepath: str) -> None:
        super().__init__()
        self._src_filepath = src_filepath
        self.data = None

    @property
    def src_filepath(self):
        """getter for src_filepath"""
        return self._src_filepath

    @src_filepath.setter
    def src_filepath(self, value):
        self._src_filepath = value


    def __repr__(self) -> str:
        return f"JSONDataset(src_filepath='{self._src_filepath}'"

    def __str__(self) -> str:
        return f"JSONDataset with source file at '{self._src_filepath}'"

    def preview(self):
        try:
            self.data = pd.read_json(self._src_filepath)
            print(self.data.head())
        except Exception as e:
            print(f"Error {e} occured while previewing data.")

    def show_schema(self):
        try:
            self.data = pd.read_json(self._src_filepath)
            print(self.data.dtypes)
        except Exception as e:
            print(f"Error {e} occured while showing schema.")

    def get_data(self):
        if not self._src_filepath.endswith('.json'):
            raise ValueError("File format is not .json")
        try:
            self.data = pd.read_json(self._src_filepath)
            print("Data fetched successfully.")
        except FileNotFoundError:
            print(f"File not found at {self._src_filepath}.")
        except Exception as exc:
            print(f"An error occurred while fetching data: {exc}")

    def write_data(self, target_filepath):
        if self.data is not None:
            try:
                self.data.to_json(target_filepath, index=False)
                print(f"Data saved successfully to {target_filepath}.")
            except Exception as exc:
                print(f"An error occurred while saving data: {exc}")
        else:
            print("No data to save as JSON.")

class CSVDataset(Dataset):

    def __init__(self, src_filepath) -> None:
        super().__init__()
        self._src_filepath: str = src_filepath
        self.data = None

    @property
    def src_filepath(self):
        """getter for src_filepath"""
        return self._src_filepath

    @src_filepath.setter
    def src_filepath(self, value):
        self._src_filepath = value


    def __repr__(self) -> str:
        return f"CSVDataset(src_filepath='{self._src_filepath}'"

    def __str__(self) -> str:
        return f"CSVDataset with source file at '{self._src_filepath}'"

    def preview(self):
        try:
            self.data = pd.read_csv(self._src_filepath)
            print(self.data.head())
        except Exception as e:
            print(f"Error {e} occured while previewing data.")

    def show_schema(self):
        try:
            self.data = pd.read_csv(self._src_filepath)
            print(self.data.dtypes)
        except Exception as e:
            print(f"Error {e} occured while showing schema.")

    def get_data(self):
        if not self._src_filepath.endswith('.csv'):
            raise ValueError("File format is not .csv")
        try:
            self.data = pd.read_csv(self._src_filepath)
            print("Data fetched successfully.")
        except FileNotFoundError:
            print(f"File not found at {self._src_filepath}.")
        except Exception as exc:
            print(f"An error occurred while fetching data: {exc}")

    def write_data(self, target_filepath):
        if self.data is not None:
            try:
                self.data.to_csv(target_filepath, index=False)
                print(f"Data saved successfully to {target_filepath}.")
            except Exception as exc:
                print(f"An error occurred while saving data: {exc}")
        else:
            print("No data to save as CSV.")

class Source:
    def __init__(self, dataset) -> None:
        self._dataset: Dataset = dataset


    @property
    def dataset(self):
        return self._dataset

    @dataset.setter
    def dataset(self, value):
        if isinstance(value, Dataset):
            self._dataset = value
        else:
            print("value is not of type 'Dataset'")
            raise TypeError

class Sink:
    def __init__(self, dataset, target_filepath) -> None:
        self._dataset: Dataset = dataset
        self._target_filepath: str = target_filepath

    @property
    def dataset(self):
        return self._dataset

    @dataset.setter
    def dataset(self, value):
        if isinstance(value, Dataset):
            self._dataset = value
        else:
            print("value is not of type 'Dataset'")
            raise TypeError

    @property
    def target_filepath(self):
        return self._target_filepath

    @target_filepath.setter
    def target_filepath(self, value):
        self._target_filepath = value

class Activity(ABC):
    def __init__(self) -> None:
        pass

    def start(self):
        pass

class WaitActivity(Activity):
    def __init__(self, time) -> None:
        self.time: int = time

    def start(self):
        if isinstance(self.time, int):
            print(f"\nSleep activity started @{datetime.datetime.now()}.")
            sleep(self.time)
            print(f"Sleep activity ended   @{datetime.datetime.now()}.")
            print(f"Time slept {self.time} seconds.\n")
        else:
            print(f"Wrong argument of type '{type(self.time).__name__}' instead of 'INT' type.")
        return self
class CopyActivity(Activity):
    def __init__(self, src, sink) -> None:
        self.src: Source = src
        self.sink: Sink = sink

    def start(self):
        start = datetime.datetime.now()
        print(f"Copy activity started @{start}.")

        try:
            self.src.dataset.get_data()
        except Exception as e:
            print(f"Error {e} occured while getting data to Source in CopyActivity.")

        try:
            self.sink.dataset.data = self.src.dataset.data
        except Exception as e:
            print(f"Error {e} occured while assigning data to the sink.")

        try:
            self.sink.dataset.write_data(self.sink.target_filepath)
        except Exception as e:
            print(f"Error {e} occured while writing data to Sink in CopyActivity.")

        end = datetime.datetime.now()
        print(f"Copy activity ended @{end}.")
        return self


class Pipeline:
    def __init__(self) -> None:
        self._activities: list[Activity] = []

    @property
    def activities(self):
        return self._activities


    def add_activity(self, activity):
        if isinstance(activity, Activity):
            self._activities.append(activity)
        else:
            print(f"Error {activity} is not of type 'Activity'")
            raise TypeError
        return self

    def execute(self): ##### – iterates through the activities and executes them in order
        return [x.start() for x in self._activities]



def main():

    try:
        # Define the source and target file paths
        csv_src_path = os.path.join(os.path.expanduser("~"),
        'OneDrive - Adastra, s.r.o\\Desktop\\employement-data.csv')
        csv_tgt_path = os.path.join(os.path.expanduser("~"),
        'OneDrive - Adastra, s.r.o\\Desktop\\old projects\\employement-data_edited_Hristo_Parteniev123.csv')
        json_src_path = os.path.join(os.path.expanduser("~"),
        'OneDrive - Adastra, s.r.o\\Desktop\\users_1k.json')
        json_tgt_path = os.path.join(os.path.expanduser("~"),
        'OneDrive - Adastra, s.r.o\\Desktop\\old projects\\users_1k_edited_Hristo_Parteniev.json')

        src: Source = Source(JSONDataset(json_src_path))
        sink: Sink = Sink(CSVDataset(csv_tgt_path), csv_tgt_path)

        src2: Source = Source(CSVDataset(csv_src_path))
        sink2: Sink = Sink(JSONDataset(json_tgt_path), json_tgt_path)

        wait = WaitActivity(1)
        copy = CopyActivity(src, sink)
        copy2 = CopyActivity(src2, sink2)

        pl = Pipeline()
        pl.add_activity(wait)
        pl.add_activity(copy)
        pl.add_activity(wait)
        pl.add_activity(copy2)
        pl.execute()

    except Exception as exc:
        print(f"Error {exc} occured!!!")

if __name__=="__main__":
    main()
