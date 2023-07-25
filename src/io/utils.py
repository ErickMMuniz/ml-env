import pandas as pd
import os
from typing import List, Union, Tuple


def read_data(path: str = "data") -> List[Tuple[str, Union[pd.DataFrame, None]]]:
    """
    Lazy function to read all CSV files
    :param path:
    :return:
    """
    assert path in os.listdir(os.getcwd())
    assert os.path.isdir(os.path.join(os.getcwd(), path))

    data_path: str = os.path.join(os.getcwd(), path)
    file_names = os.listdir(data_path)

    def make_single_file(file: str) -> Tuple[str, Union[pd.DataFrame, None]]:
        name = file.split(".")[0]  # Ignore the prefix file
        path_file = (
            os.path.join(data_path, file) if file.split(".")[1] == "csv" else None
        )
        return name, pd.read_csv(path_file)

    return map(make_single_file, file_names)
