from abc import ABC, abstractmethod
import os
import pandas as pd
import pyodbc


class Reader(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def read(self):
        pass

class CSVReader(Reader):
    def __init__(self, src_filepath, target_filepath) -> None:
        super().__init__()
        self._src_filepath = src_filepath
        self._target_filepath = target_filepath
        self.data = None
        self.reader_type = "CSVReader"

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
        self.reader_type = "JSONReader"

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
        self.reader_type = "DatabaseReader"

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
    def get_reader(reader_type: str, *args)-> Reader:

        type = reader_type.lower()
        readers = {
            'csv': CSVReader,
            'json': JSONReader,
            'db': DatabaseReader
        }

        if type not in readers.keys():
            raise ValueError(f"Unknown reader type: {reader_type}")
        else:
            return readers[type](*args)


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
        query = "select  * from dbo.DimOrganization;"

        csv_reader = ReaderFactory.get_reader('csv', csv_src_path, csv_tgt_path)
        print('#' * 120)
        print(csv_reader)
        print('#' * 120)
        #print(csv_reader.read())
        json_reader = ReaderFactory.get_reader('json', json_src_path, json_tgt_path)
        print(json_reader)
        print('#' * 120)
        #print(json_reader.read())
        db_reader = ReaderFactory.get_reader('db', query)
        print(db_reader)
        print('#' * 120)
        #print(db_reader.read())
    except Exception as exc:
        print(f"Error {exc} occured!!!")

if __name__ == '__main__':
    main()
