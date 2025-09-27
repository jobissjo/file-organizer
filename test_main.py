import os
from main import get_organize_folder_path


def test_env_variable():

    assert get_organize_folder_path() is not None
    print(get_organize_folder_path())
    assert get_organize_folder_path() == "C:/Users/JOBI/Downloads"