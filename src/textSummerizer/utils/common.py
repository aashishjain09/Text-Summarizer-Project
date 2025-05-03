import os
from box.exceptions import BoxValueError
import yaml
from textSummerizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its contents as a ConfigBox object.

    Args:
        path_to_yaml (str): Path like input

    Raises:
        ValueError: If yaml file is empty or not found.
        e: empty file

    Returns:
        ConfigBox: Contents of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError:
        logger.error(f"YAML file is empty")
    except Exception as e:
        raise e
    # except FileNotFoundError as e:
    #     logger.error(f"File not found: {path_to_yaml}")
    #     raise e
    # except yaml.YAMLError as e:
    #     logger.error(f"Error parsing YAML file: {e}")
    #     raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose: bool = True):
    """
    Create directories if they do not exist.

    Args:
        path_to_directories (list): List of directory paths to create.
        ignore_log (bool, optional): Ignore if multiple directories are passed. Defaults to False.
        verbose (bool): If True, print the created directories.

    Returns:
        None
    """
    for dir_path in path_to_directories:
        os.makedirs(dir_path, exist_ok=True)
        if verbose:
            logger.info(f"Directory {dir_path} created successfully.")


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the size of a file or directory in kB.

    Args:
        path (Path): Path to the file or directory.

    Returns:
        str: Size of the file or directory in kB.
    """
    size_in_kb = round(os.path.getsize(path) / 1024, 2)
    return f"Size: {size_in_kb} kB"

    # if os.path.isfile(path):
    #     return f"File size: {os.path.getsize(path)} bytes"
    # elif os.path.isdir(path):
    #     total_size = 0
    #     for dirpath, dirnames, filenames in os.walk(path):
    #         for filename in filenames:
    #             fp = os.path.join(dirpath, filename)
    #             total_size += os.path.getsize(fp)
    #     return f"Directory size: {total_size} bytes"
    # else:
    #     return "Path does not exist."
