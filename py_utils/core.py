import json
import dataclasses


def bootstrap_config(config_file_path: str) -> dict:
    ret: dict
    with open(file=config_file_path, mode="r") as f:
        ret = json.loads(f.read())
    return ret

