import yaml
from utils import jsonutils


def load(file_name, success_callback):
    with open(file_name, encoding="UTF-8") as file:
        success_callback(yaml.load(file, Loader=yaml.FullLoader), jsonutils)
