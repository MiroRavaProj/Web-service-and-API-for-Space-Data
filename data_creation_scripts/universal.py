import pandas as pd


def opener(name: str):
    import json
    with open(name) as data_file:
        data = json.load(data_file)

    df = pd.json_normalize(data)
    df.to_json(name)

