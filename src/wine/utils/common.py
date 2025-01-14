import os
import yaml
import json
import joblib
from src.wine.utils import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Reading the yaml file from the path: {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError :
        raise ValueError("yaml file is empty")
    except FileNotFoundError as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Creating directory: {path}")

@ensure_annotations
def save_json(path:Path,data:dict):
    with open (path,"w") as f:
        json.dump(data,f,indent=4)
    logger.info(f"Saving the data in the json file at: {path}")

@ensure_annotations
def load_json(path:Path)-> ConfigBox:
    with open(path) as f:
        content = json.load(f)

    logger.info(f"Reading the json file from the path: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data:Any,path:Path):
    joblib.dump(value=data,filename=path)
    logger.info(f"Saving the data in the binary file at: {path}")


@ensure_annotations
def load_bin(path:Path)-> Any:
    data = joblib.load(path)
    logger.info(f"Reading the binary file from the path: {path}")
    return data