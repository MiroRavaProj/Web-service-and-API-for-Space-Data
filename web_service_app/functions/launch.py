import pandas as pd
from flask import request


def represents_int(s):
    try:
        s = s.replace("'", "")
        int(s)
        return True
    except ValueError:
        return False


def launch_search(args: dict):
    key = list(args.keys())[0]
    df = pd.read_json('data/launch.json')
    if key == "id" and not represents_int(args[key]):
        return {"error": f"Entry not found:  no {key} contains {args[key]}"}, 404
    try:
        x = df.loc[df[key].str.contains(args[key], case=False)].to_json(orient='index')
    except AttributeError:
        x = df.query(f'{key}=={args[key]}').to_json(orient='index')
    x = x.encode().decode('unicode-escape')
    if str(x) == '{}':
        return {"error": f"Entry not found:  no {key} contains {args[key]}"}, 404
    return x


def launch_get(variable, value):
    df = pd.read_json('data/launch.json')
    if variable == "id" and represents_int(value):
        x = df.loc[df[variable] == int(value.replace("'", ""))].to_json(orient='index')
    else:
        x = df.query(f'{variable}=={value}').to_json(orient='index')
    x = x.encode().decode('unicode-escape')
    if str(x) == '{}':
        return {"error": f"Entry not found:  {variable} == {value}"}, 404
    return x


def launch_get_all():
    df = pd.read_json('data/launch.json')
    x = df.to_json(orient='index')
    x = x.encode().decode('unicode-escape')
    if str(x) == '{}':
        return {"error": f"Entry not found: dataset is empty"}, 404
    return x


def launch_post(rq: request):
    df = pd.read_json('data/launch.json')
    value = str(rq.get_json()).replace("'", '"')
    value = '{"0":' + value + '}'
    value = pd.read_json(value).transpose()
    value['id'] = df['id'].max() + 1
    value.drop(columns=[item for item in list(value.columns) if item not in list(df.columns)], inplace=True)
    df_final = pd.concat([df, value], ignore_index=True)
    df_final.to_json('data/launch.json')
    return {"Success": "Entry added to database"}, 201


def launch_delete(name, value):
    if name == 'id':
        value = int(value)
    df = pd.read_json('data/launch.json')
    if value in df[name].values:
        df.drop(df.loc[df[name] == value].index, inplace=True)
        df.to_json('data/launch.json')
        return {"Success": "Entry deleted"}, 200
    else:
        return {"error": f"Entry not found:  {name} == {value}"}, 404


def launch_update(name, value, rq: request):
    x, y = launch_delete(name, value)
    if y == 404:
        return {"error": f"Entry not found:  {name} == {value} , cannot delete it"}, 404
    return launch_post(rq)
