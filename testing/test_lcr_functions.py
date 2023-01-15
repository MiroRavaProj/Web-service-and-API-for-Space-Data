import requests
import pandas as pd
import json

lcr_output = {'3': {'details': "First stage used for Electron's 26th flight (There and Back "
                               'Again).',
                    'first_launch_date': '2022-05-02T22:49:52Z',
                    'flight_proven': 'False',
                    'flights': 1,
                    'id': 110,
                    'image_url': 'https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launcher_core_images/110_image_20220420085303.jpg',
                    'last_launch_date': '2022-05-02T22:49:52Z',
                    'launcher_config_full_name': 'Electron',
                    'serial_number': '26',
                    'status': 'active'}}

lcr_in = '''{"id":11,"flight_proven":"False","serial_number":"B0006","status":"lost","details":"Suffered engine out at T+1:19 but primary mission successful","image_url":"https:\/\/spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com\/media\/launcher_core_images\/11_image_20191115082657.jpeg","flights":1,"last_launch_date":"2012-10-08T00:35:07Z","first_launch_date":"2012-10-08T00:35:07Z","launcher_config_full_name":"Falcon 9 v1.0"}'''
lcr_out = {'details': 'Suffered engine out at T+1:19 but primary mission successful',
 'first_launch_date': '2012-10-08T00:35:07Z',
 'flight_proven': 'False',
 'flights': 1.0,
 'id': 120,
 'image_url': 'https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launcher_core_images/11_image_20191115082657.jpeg',
 'last_launch_date': '2012-10-08T00:35:07Z',
 'launcher_config_full_name': 'Falcon 9 v1.0',
 'serial_number': 'B0006',
 'status': 'lost'}

lcr_update = '{"flight_proven":"False","serial_number":"26","status":"active","details":"Last stage used in lcr testing","image_url":"https:\\/\\/spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com\\/media\\/launcher_core_images\\/110_image_20220420085303.jpg","flights":1,"last_launch_date":"2022-05-02T22:49:52Z","first_launch_date":"2022-05-02T22:49:52Z","launcher_config_full_name":"Electron"}'


def test_lcr_get():
    url = "http://127.0.0.1:4533/launchers/id/110"
    r = requests.get(url)
    json = r.json()
    assert json == lcr_output


def test_lcr_search():
    url = "http://127.0.0.1:4533/launchers/search?id=110"
    r = requests.get(url)
    json = r.json()
    assert json == lcr_output


def test_lcr_post():
    requests.post(url='http://127.0.0.1:4533/launchers', json=lcr_in)
    df = pd.read_json('../web_service_app/data/launcher.json')
    x = df['id'].max()

    url = f"http://127.0.0.1:4533/launchers/id/{x}"
    r = requests.get(url)
    json = r.json()
    key = list(json.keys())[0]


    url = f"http://127.0.0.1:4533/launchers/id/'{x}'"
    r = requests.delete(url)

    lcr_out['id'] = x
    assert json[key] == lcr_out


def test_lcr_delete():
    df = pd.read_json('../web_service_app/data/launcher.json')
    x = df['id'].max()
    requests.post(url='http://127.0.0.1:4533/launchers', json=lcr_in)
    df = pd.read_json('../web_service_app/data/launcher.json')
    x = df['id'].max()

    checker = f"http://127.0.0.1:4533/launchers/id/{x}"
    url = f"http://127.0.0.1:4533/launchers/id/'{x}'"

    r1 = requests.get(checker)
    json1 = r1.json()
    key1 = list(json1.keys())[0]

    requests.delete(url)
    r2 = requests.get(checker)
    json2 = r2.json()
    key2 = list(json2.keys())[0]

    assert json1[key1] != json2[key2]


def test_lcr_update():
    requests.post(url='http://127.0.0.1:4533/launchers', json=lcr_in)
    df = pd.read_json('../web_service_app/data/launcher.json')
    x = df['id'].max()
    checker = f"http://127.0.0.1:4533/launchers/id/{x}"
    r1 = requests.get(checker)
    json = r1.json()
    key = list(json.keys())[0]

    assert json[key]["details"] == 'Suffered engine out at T+1:19 but primary mission successful'

    url = f"http://127.0.0.1:4533/launchers/id/'{x}'"
    requests.put(url=url, json=lcr_update)

    r1 = requests.get(checker)
    json = r1.json()
    key = list(json.keys())[0]
    assert json[key]["details"] == 'Last stage used in lcr testing'

    requests.delete(url)
