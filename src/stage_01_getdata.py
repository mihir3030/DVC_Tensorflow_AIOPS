import os
import argparse
import logging
from tqdm import tqdm
from src.utils.common import read_yaml, create_directories, copy_files

logging.basicConfig(
    filename = os.path.join("logs", "running_log.log"),
    level = logging.INFO,
    format = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a",
)


def get_data(config_path: str) -> None:
    """get the image data from source to the present working directory
    Args:
        config_path (str): path to config file
    """
    config = read_yaml(config_path)

    source_data_dirs = config["source_data_dirs"]
    local_data_dirs = config["local_data_dirs"]

    N = len(source_data_dirs)
    for source_data_dir, local_data_dir in tqdm(
        zip(source_data_dirs, local_data_dirs),
        total=N,
        colour="red",
        desc="copying directory:",
    ):
        create_directories([local_data_dir])
        copy_files(source_data_dir, local_data_dir)


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="config/config.yaml")
    parsed_args = args.parse_args()

    try:
        logging.info("\n-----------------------------")
        logging.info(">>>>>>stage 1 started <<<<<<<")
        get_data(config_path = parsed_args.config)
        logging.info(">>>>> stage 1 compleated all the data saved in local <<<<<")

    except Exception as e:
        logging.exception(e)
        raise e 
    
