import os
import yaml
import logging
from tqdm import tqdm
import shutil

def read_yaml(path_to_yaml: str) -> dict:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
    
    logging.info(f"content from {path_to_yaml} read successfully")
    return content


def create_directories(list_of_directories: list) -> None:
    for dir_path in list_of_directories:
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
            logging.info(f"directory is created at {dir_path}")

def copy_files(source_data_dir: str, local_data_dir: str) -> None:
    """Copies file from source to destination directory
    Args:
        source_data_dir (str): source data directory
        local_data_dir (str): local data directory
    """
    list_of_files = os.listdir(source_data_dir)
    N = len(list_of_files)

    for filename in tqdm(
        list_of_files,
        total=N,
        desc=f"copying file from {source_data_dir} to {local_data_dir}",
        colour="green",
    ):
        src = os.path.join(source_data_dir, filename)
        dest = os.path.join(local_data_dir, filename)
        shutil.copy(src, dest)

    logging.info(
        f"all the files has been copied from {source_data_dir} to {local_data_dir}"
    )