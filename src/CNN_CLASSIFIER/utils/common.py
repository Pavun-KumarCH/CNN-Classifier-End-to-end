import os 
from box.exceptions import BoxValueError #$ which gives were the error is located in line
import yaml
from CNN_CLASSIFIER import logger #$
import json
import joblib
from ensure import ensure_annotations #$
from box import ConfigBox #$
from pathlib import Path 
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns
    
    Args:
        path_to_yaml (str): path like input
        
    Raises:
           ValueError if yaml file is empty
           e: empty file
           
    Returns:
           ConfigBox: ConfigBox type
    """
  
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file:{path_to_yaml} loaded Successfully")
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):
    """
    create list of directories

    Args:
        path_to_directories (list): list of directories to be created
        ignore_log (bool, optional): ignore if multiplt dirs is to be created. Defaults

    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok = True)
        if verbose:
            logger.info(f"Created Directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """
        save json data

        Args:
            path (Path): path to jspn file
            data (dict): data to be saved in json file
    
    """
    with open(path,"w") as f:
        json.dump(data,f, indent = 4)
         
    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
        load json data

        Args:
            path (Path): path to json file
        
        Returns:
            ConfigBox: data as class attributes insted of dict
    
    """
    with open(path) as f:
        data = json.load(f)

    logger.info(f"json file loaded successfully from: {path}")

    return ConfigBox(data)


@ensure_annotations
def save_bin(path: Path, data: Any):
    """
        save binary data file

        Args:
            path (Path): path to binary file
            data (Any): data to be saved in binary file
    
    """
    joblib.dump(data, path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """
        load binary data file

        Args:
            path (Path): path to binary file
        
        Returns:
            Any: data as class attributes insted of dict
    
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded successfully from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """
        get size of file

        Args:
            path (Path): path to file
        
        Returns:
            str: size of file
    
    """
    size = round(os.path.getsize(path)/1024)
    return f"~ {size} KB"


def decodeImage(Imagestring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName,'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
