from abc import ABC, abstractmethod
import os
import pandas as pd
import pyodbc


class Reader(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def read():
        pass

class CSVReader(Reader):
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
        return f"CSVReader(src_filepath='{self._src_filepath}',\
             target_filepath='{self._target_filepath}')"

    def __str__(self) -> str:
        return f"CSVReader with source file at '{self._src_filepath}'\
             and target file at '{self._target_filepath}'"

    def read(self):

        if not self._src_filepath.endswith('.csv'):
            raise ValueError("File format is not .csv")
        try:
            self.data = pd.read_csv(self._src_filepath)
            print("Data fetched successfully.")
        except FileNotFoundError:
            print(f"File not found at {self._src_filepath}.")
        except Exception as exc:
            print(f"An error occurred while fetching data: {exc}")
        return self.data


class JSONReader(Reader):
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
        return f"CSVReader(src_filepath='{self._src_filepath}',\
             target_filepath='{self._target_filepath}')"

    def __str__(self) -> str:
        return f"CSVReader with source file at '{self._src_filepath}'\
             and target file at '{self._target_filepath}'"

    def read(self):

        if not self._src_filepath.endswith('.json'):
            raise ValueError("File format is not .json")
        try:
            self.data = pd.read_json(self._src_filepath)
            print("Data fetched successfully.")
        except FileNotFoundError:
            print(f"File not found at {self._src_filepath}.")
        except Exception as exc:
            print(f"An error occurred while fetching data: {exc}")
        return self.data


class DatabaseReader(Reader):
    def __init__(self, query) -> None:
        super().__init__()
        self._query = query
        self.data = None

    def __repr__(self) -> str:
        return f"DatabaseReader(query='{self._query}')"

    def __str__(self) -> str:
        return f"DatabaseReader with query '{self._query}'"

    def read(self):

        conn_str = (
        r'DRIVER={SQL Server};'
        r'SERVER=BGW_SQL_ACADEMY;'
        r'DATABASE=AdventureWorksDW2012;'
        r'Trusted_Connection=yes;'
        )

        conn = pyodbc.connect(conn_str)
        self.data = pd.read_sql(self._query, conn)
        print(self.data)
        conn.close()

class ReaderFactory():

    @staticmethod
    def get_reader(reader_obj):
        return f"{reader_obj} \nis instance of Class:{type(reader_obj).__name__}."



def main():
    """main function"""
    try:
        # Define the source and target file paths
        csv_src_path = os.path.join(os.path.expanduser("~"),
        'OneDrive - Adastra, s.r.o\\Desktop\\employement-data.csv')
        csv_tgt_path = os.path.join(os.path.expanduser("~"),
        'OneDrive - Adastra, s.r.o\\Desktop\\employement-data_edited_Hristo_Parteniev.csv')
        json_src_path = os.path.join(os.path.expanduser("~"),
        'OneDrive - Adastra, s.r.o\\Desktop\\users_1k.json')
        json_tgt_path = os.path.join(os.path.expanduser("~"),
        'OneDrive - Adastra, s.r.o\\Desktop\\users_1k_edited_Hristo_Parteniev.json')

        csv_dataset = CSVReader(csv_src_path, csv_tgt_path)
        csv_dataset.read()
        print(csv_dataset.data.head(20))

        json_dataset = JSONReader(json_src_path, json_tgt_path)
        json_dataset.read()
        print(json_dataset.data.head(20))

        db_dataset = DatabaseReader("select  * from dbo.DimOrganization;")
        db_dataset.read()

        print('\n')
        print('*' * 120)
        print(ReaderFactory.get_reader(db_dataset))
        print('*' * 120)
        print(ReaderFactory.get_reader(json_dataset))
        print('*' * 120)
        print(ReaderFactory.get_reader(csv_dataset))
        print('*' * 120)
    except Exception as exc:
        print(f"Error {exc} occured.")


if __name__ == '__main__':
    main()
