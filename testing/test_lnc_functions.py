import requests
import pandas as pd

lnc_output = {'841': {'agency_launch_attempt_count': 427,
         'agency_launch_attempt_count_year': 55,
         'failreason': 'None',
         'id': 841,
         'image': 'None',
         'infographic': 'None',
         'launch_service_provider_name': 'United States Air Force',
         'launch_service_provider_type': 'Government',
         'location_launch_attempt_count': 213,
         'location_launch_attempt_count_year': 21,
         'mission_description': 'Lunar probe which successfully landed on '
                                'November 10. It transmitted 30,027 pictures.',
         'mission_name': 'Surveyor 6',
         'mission_orbit_name': 'Lunar Impactor',
         'mission_type': 'Lunar Exploration',
         'name': 'Atlas SLV-3C Centaur | Surveyor 6',
         'net': '1967-11-07T07:39:01Z',
         'orbital_launch_attempt_count': 770.0,
         'orbital_launch_attempt_count_year': 124,
         'pad_latitude': 28.4705556,
         'pad_launch_attempt_count': 6,
         'pad_launch_attempt_count_year': 3,
         'pad_location_country_code': 'USA',
         'pad_location_name': 'Cape Canaveral, FL, USA',
         'pad_longitude': -80.542194,
         'pad_wiki_url': 'https://en.wikipedia.org/wiki/Cape_Canaveral_Launch_Complex_36',
         'rocket_configuration_full_name': 'Atlas SLV-3C Centaur',
         'rocket_id': 3728,
         'status_name': 'Launch Successful',
         'window_end': '1967-11-07T07:39:01Z',
         'window_start': '1967-11-07T07:39:01Z'}}


lnc_in = '{"id":914,"name":"Vostok 8A92M | Meteor-1 10","net":"1968-06-12T13:14:59Z","window_end":"1968-06-12T13:14:59Z","window_start":"1968-06-12T13:14:59Z","failreason":"None","image":"None","infographic":"None","orbital_launch_attempt_count":841.0,"location_launch_attempt_count":52,"pad_launch_attempt_count":34,"agency_launch_attempt_count":326,"orbital_launch_attempt_count_year":56,"location_launch_attempt_count_year":15,"pad_launch_attempt_count_year":8,"agency_launch_attempt_count_year":37,"status_name":"Launch Successful","launch_service_provider_name":"Soviet Space Program","launch_service_provider_type":"Government","rocket_id":3792,"rocket_configuration_full_name":"Vostok 8A92M","mission_name":"Meteor-1 10","mission_description":"The Meteor-1 series was the first series of Soviet meteorological satellites.","mission_type":"Earth Science","mission_orbit_name":"Low Earth Orbit","pad_wiki_url":"https:\/\/en.wikipedia.org\/wiki\/Plesetsk_Cosmodrome","pad_latitude":62.941,"pad_longitude":40.526806,"pad_location_name":"Plesetsk Cosmodrome, Russian Federation","pad_location_country_code":"RUS"}'

lnc_out = {'agency_launch_attempt_count': 326,
 'agency_launch_attempt_count_year': 37,
 'failreason': 'None',
 'image': 'None',
 'infographic': 'None',
 'launch_service_provider_name': 'Soviet Space Program',
 'launch_service_provider_type': 'Government',
 'location_launch_attempt_count': 52,
 'location_launch_attempt_count_year': 15,
 'mission_description': 'The Meteor-1 series was the first series of Soviet '
                        'meteorological satellites.',
 'mission_name': 'Meteor-1 10',
 'mission_orbit_name': 'Low Earth Orbit',
 'mission_type': 'Earth Science',
 'name': 'Vostok 8A92M | Meteor-1 10',
 'net': '1968-06-12T13:14:59Z',
 'orbital_launch_attempt_count': 841.0,
 'orbital_launch_attempt_count_year': 56,
 'pad_latitude': 62.941,
 'pad_launch_attempt_count': 34,
 'pad_launch_attempt_count_year': 8,
 'pad_location_country_code': 'RUS',
 'pad_location_name': 'Plesetsk Cosmodrome, Russian Federation',
 'pad_longitude': 40.526806,
 'pad_wiki_url': 'https://en.wikipedia.org/wiki/Plesetsk_Cosmodrome',
 'rocket_configuration_full_name': 'Vostok 8A92M',
 'rocket_id': 3792,
 'status_name': 'Launch Successful',
 'window_end': '1968-06-12T13:14:59Z',
 'window_start': '1968-06-12T13:14:59Z'}

lnc_update = '{"id":914,"name":"it aint Vostok 8A92M | Meteor-1 10","net":"1968-06-12T13:14:59Z","window_end":"1968-06-12T13:14:59Z","window_start":"1968-06-12T13:14:59Z","failreason":"None","image":"None","infographic":"None","orbital_launch_attempt_count":841.0,"location_launch_attempt_count":52,"pad_launch_attempt_count":34,"agency_launch_attempt_count":326,"orbital_launch_attempt_count_year":56,"location_launch_attempt_count_year":15,"pad_launch_attempt_count_year":8,"agency_launch_attempt_count_year":37,"status_name":"Launch Successful","launch_service_provider_name":"Soviet Space Program","launch_service_provider_type":"Government","rocket_id":3792,"rocket_configuration_full_name":"Vostok 8A92M","mission_name":"Meteor-1 10","mission_description":"The Meteor-1 series was the first series of Soviet meteorological satellites.","mission_type":"Earth Science","mission_orbit_name":"Low Earth Orbit","pad_wiki_url":"https:\/\/en.wikipedia.org\/wiki\/Plesetsk_Cosmodrome","pad_latitude":62.941,"pad_longitude":40.526806,"pad_location_name":"Plesetsk Cosmodrome, Russian Federation","pad_location_country_code":"RUS"}'


def test_lnc_get():
    url = "http://127.0.0.1:4533/launches/id/841"
    r = requests.get(url)
    json = r.json()
    assert json == lnc_output


def test_lnc_search():
    url = "http://127.0.0.1:4533/launches/search?id=841"
    r = requests.get(url)
    json = r.json()
    assert json == lnc_output


def test_lnc_post():
    requests.post(url='http://127.0.0.1:4533/launches', json=lnc_in)

    df = pd.read_json('../web_service_app/data/launch.json')
    x = df['id'].max()

    url = f"http://127.0.0.1:4533/launches/id/{x}"
    r = requests.get(url)
    json = r.json()
    key = list(json.keys())[0]

    url = f"http://127.0.0.1:4533/launches/id/'{x}'"
    requests.delete(url)
    lnc_out['id'] = x

    assert json[key] == lnc_out


def test_lnc_delete():
    requests.post(url='http://127.0.0.1:4533/launches', json=lnc_in)
    df = pd.read_json('../web_service_app/data/launch.json')
    x = df['id'].max()

    checker = f"http://127.0.0.1:4533/launches/id/{x}"
    url = f"http://127.0.0.1:4533/launches/id/'{x}'"

    r1 = requests.get(checker)
    json1 = r1.json()
    key1 = list(json1.keys())[0]

    requests.delete(url)
    r2 = requests.get(checker)
    json2 = r2.json()
    key2 = list(json2.keys())[0]

    assert json1[key1] != json2[key2]


def test_lnc_update():
    requests.post(url='http://127.0.0.1:4533/launches', json=lnc_in)
    df = pd.read_json('../web_service_app/data/launch.json')
    x = df['id'].max()
    checker = f"http://127.0.0.1:4533/launches/id/{x}"
    r1 = requests.get(checker)
    json = r1.json()
    key = list(json.keys())[0]

    assert json[key]["name"] == 'Vostok 8A92M | Meteor-1 10'

    url = f"http://127.0.0.1:4533/launches/id/'{x}'"
    requests.put(url=url, json=lnc_update)

    r1 = requests.get(checker)
    json = r1.json()
    key = list(json.keys())[0]
    assert json[key]["name"] == 'it aint Vostok 8A92M | Meteor-1 10'

    requests.delete(url)
