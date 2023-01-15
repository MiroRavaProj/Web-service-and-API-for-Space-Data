import requests
import pandas as pd

ast_output = {'2': {'agency_abbrev': 'ESA',
       'agency_country_code': 'AUT,BEL,CZE,DNK,FIN,FRA,DEU,GRC,IRE,ITA,LUZ,NLD,NOR,POL,PRT,ROU,ESP,SWE,CHE,GBR',
       'agency_logo_url': 'https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/logo/european2520space2520agency_logo_20190207032435.png',
       'agency_name': 'European Space Agency',
       'agency_type': 'Multinational',
       'bio': 'Major Timothy Nigel Peake CMG is a British Army Air Corps '
              'officer, European Space Agency astronaut and a former '
              'International Space Station (ISS) crew member.  He is the first '
              'British ESA astronaut, the second astronaut to bear a flag of '
              'the United Kingdom patch, the sixth person born in the United '
              'Kingdom to go on board the International Space Station and the '
              "seventh UK-born person in space. He began the ESA's intensive "
              'astronaut basic training course in September 2009 and graduated '
              'on 22 November 2010',
       'date_of_birth': '1972-04-07',
       'date_of_death': None,
       'first_flight': '2015-12-15T11:03:09Z',
       'flights_count': 1,
       'id': 3,
       'instagram': 'https://www.instagram.com/astro_timpeake/',
       'landings_count': 1,
       'last_flight': '2015-12-15T11:03:09Z',
       'name': 'Tim Peake',
       'nationality': 'British',
       'profile_image': 'https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/astronaut_images/tim_peake_image_20220911033713.jpeg',
       'profile_image_thumbnail': 'https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/astronaut_images/tim_peake_thumbnail_20220911033713.jpeg',
       'status_name': 'Active',
       'twitter': 'https://twitter.com/astro_timpeake',
       'type_name': 'Government',
       'wiki': 'https://en.wikipedia.org/wiki/Tim_Peake'}}

snoopy_in = '{"id":745,"name":"Snoopy","date_of_birth":null,"date_of_death":null,"nationality":"Earthling","bio":"This Snoopy plushie serves as zero-G indicator on the Artemis-1 mission.","twitter":null,"instagram":null,"wiki":"https:\/\/en.wikipedia.org\/wiki\/Snoopy","profile_image":"https:\/\/spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com\/media\/astronaut_images\/snoopy_image_20220911033852.jpeg","profile_image_thumbnail":"https:\/\/spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com\/media\/astronaut_images\/snoopy_thumbnail_20220911033853.jpeg","flights_count":1,"landings_count":0,"last_flight":"2022-11-16T06:47:44Z","first_flight":"2022-11-16T06:47:44Z","status_name":"Active","type_name":"Non-Human","agency_name":"National Aeronautics and Space Administration","agency_type":"Government","agency_country_code":"USA","agency_abbrev":"NASA","agency_logo_url":"https:\/\/spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com\/media\/logo\/national2520aeronautics2520and2520space2520administration_logo_20190207032448.png"}'
snoopy_out = {'agency_abbrev': 'NASA',
 'agency_country_code': 'USA',
 'agency_logo_url': 'https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/logo/national2520aeronautics2520and2520space2520administration_logo_20190207032448.png',
 'agency_name': 'National Aeronautics and Space Administration',
 'agency_type': 'Government',
 'bio': 'This Snoopy plushie serves as zero-G indicator on the Artemis-1 '
        'mission.',
 'date_of_birth': None,
 'date_of_death': None,
 'first_flight': '2022-11-16T06:47:44Z',
 'flights_count': 1,
 'id': 746,
 'instagram': None,
 'landings_count': 0,
 'last_flight': '2022-11-16T06:47:44Z',
 'name': 'Snoopy',
 'nationality': 'Earthling',
 'profile_image': 'https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/astronaut_images/snoopy_image_20220911033852.jpeg',
 'profile_image_thumbnail': 'https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/astronaut_images/snoopy_thumbnail_20220911033853.jpeg',
 'status_name': 'Active',
 'twitter': None,
 'type_name': 'Non-Human',
 'wiki': 'https://en.wikipedia.org/wiki/Snoopy'}

snoopy_update = '{"id":745,"name":"No mo snoopy","date_of_birth":null,"date_of_death":null,"nationality":"Earthling","bio":"This Snoopy plushie serves as zero-G indicator on the Artemis-1 mission.","twitter":null,"instagram":null,"wiki":"https:\/\/en.wikipedia.org\/wiki\/Snoopy","profile_image":"https:\/\/spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com\/media\/astronaut_images\/snoopy_image_20220911033852.jpeg","profile_image_thumbnail":"https:\/\/spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com\/media\/astronaut_images\/snoopy_thumbnail_20220911033853.jpeg","flights_count":1,"landings_count":0,"last_flight":"2022-11-16T06:47:44Z","first_flight":"2022-11-16T06:47:44Z","status_name":"Active","type_name":"Non-Human","agency_name":"National Aeronautics and Space Administration","agency_type":"Government","agency_country_code":"USA","agency_abbrev":"NASA","agency_logo_url":"https:\/\/spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com\/media\/logo\/national2520aeronautics2520and2520space2520administration_logo_20190207032448.png"}'


def test_ast_get():
    url = "http://127.0.0.1:4533/astronauts/name/'Tim%20Peake'"
    r = requests.get(url)
    json = r.json()
    assert json == ast_output


def test_ast_search():
    url = "http://127.0.0.1:4533/astronauts/search?name=Tim%20Peake"
    r = requests.get(url)
    json = r.json()
    assert json == ast_output


def test_ast_post():
    requests.post(url='http://127.0.0.1:4533/astronauts', json=snoopy_in)

    df = pd.read_json('../web_service_app/data/astronaut.json')
    x = df['id'].max()

    url = f"http://127.0.0.1:4533/astronauts/id/{x}"
    r = requests.get(url)
    json = r.json()
    key = list(json.keys())[0]

    url = f"http://127.0.0.1:4533/astronauts/id/'{x}'"
    requests.delete(url)
    snoopy_out['id'] = x

    assert json[key] == snoopy_out


def test_ast_delete():
    requests.post(url='http://127.0.0.1:4533/astronauts', json=snoopy_in)
    df = pd.read_json('../web_service_app/data/astronaut.json')
    x = df['id'].max()

    checker = f"http://127.0.0.1:4533/astronauts/id/{x}"
    url = f"http://127.0.0.1:4533/astronauts/id/'{x}'"

    r1 = requests.get(checker)
    json1 = r1.json()
    key1 = list(json1.keys())[0]

    r = requests.delete(url)

    r2 = requests.get(checker)
    json2 = r2.json()
    key2 = list(json2.keys())[0]

    assert json1[key1] != json2[key2]


def test_ast_update():
    requests.post(url='http://127.0.0.1:4533/astronauts', json=snoopy_in)
    df = pd.read_json('../web_service_app/data/astronaut.json')
    x = df['id'].max()
    checker = f"http://127.0.0.1:4533/astronauts/id/{x}"
    r1 = requests.get(checker)
    json = r1.json()
    key = list(json.keys())[0]

    assert json[key]["name"] == 'Snoopy'

    url = f"http://127.0.0.1:4533/astronauts/id/'{x}'"
    requests.put(url=url, json=snoopy_update)

    r1 = requests.get(checker)
    json = r1.json()
    key = list(json.keys())[0]
    assert json[key]["name"] == 'No mo snoopy'

    requests.delete(url)
