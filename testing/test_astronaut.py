import requests
from library.class_folder.astronaut import Astronaut


def get():
    url = "http://127.0.0.1:4533/astronauts/name/'Tim%20Peake'"
    r = requests.get(url)
    json = r.json()
    key = list(json.keys())[0]
    a = Astronaut(json[key])
    return a, key, json


def test_astro_class():
    a, key, json = get()
    assert type(a) == type(Astronaut(json[key]))


def test_astro_name():
    a, key, json = get()
    assert a.name == json[key]['name']


def test_astro_birth_date():
    a, key, json = get()
    assert a.birth_date == json[key]['date_of_birth']


def test_astro_death_date():
    a, key, json = get()
    assert a.death_date == json[key]['date_of_death']


def test_astro_nationality():
    a, key, json = get()
    assert a.nationality == json[key]['nationality']


def test_astro_bio():
    a, key, json = get()
    assert a.bio == json[key]['bio']


def test_astro_twitter():
    a, key, json = get()
    assert a.twitter == json[key]['twitter']


def test_astro_instagram():
    a, key, json = get()
    assert a.instagram == json[key]['instagram']


def test_astro_wiki():
    a, key, json = get()
    assert a.wiki == json[key]['wiki']


def test_astro_profile_image():
    a, key, json = get()
    assert a.profile_image == json[key]['profile_image']


def test_astro_profile_image_thumbnail():
    a, key, json = get()
    assert a.profile_image_thumbnail == json[key]['profile_image_thumbnail']


def test_astro_flights_count():
    a, key, json = get()
    assert a.flights_count == json[key]['flights_count']


def test_astro_landings_count():
    a, key, json = get()
    assert a.landings_count == json[key]['landings_count']


def test_astro_last_flight():
    a, key, json = get()
    assert a.last_flight == json[key]['last_flight']


def test_astro_first_flight():
    a, key, json = get()
    assert a.first_flight == json[key]['first_flight']


def test_astro_status_name():
    a, key, json = get()
    assert a.status_name == json[key]['status_name']


def test_astro_type_name():
    a, key, json = get()
    assert a.type_name == json[key]['type_name']


def test_astro_agency_name():
    a, key, json = get()
    assert a.agency_name == json[key]['agency_name']


def test_astro_agency_type():
    a, key, json = get()
    assert a.agency_type == json[key]['agency_type']


def test_astro_agency_country_code():
    a, key, json = get()
    assert a.agency_country_code == json[key]['agency_country_code']


def test_astro_agency_abbrev():
    a, key, json = get()
    assert a.agency_abbrev == json[key]['agency_abbrev']


def test_astro_agency_logo_url():
    a, key, json = get()
    assert a.agency_logo_url == json[key]['agency_logo_url']


def test_astro_repr():  # testing if function exists
    a, key, json = get()
    x = repr(a)
    assert repr(a) == x


def test_astro_show_basic_info():  # testing if function exists
    a, key, json = get()
    x = (a.show_basic_info)
    assert a.show_basic_info == x


def test_astro_jsonify():  # testing if function exists
    a, key, json = get()
    x = a.jsonify
    assert a.jsonify == x

def test_astro_setters():
    a, key, json = get()
    a.name = 'name'
    a.nationality = 'gone'
    a.bio = 'human born in human city'
    a.twitter = 'twitter.com'
    a.instagram = 'instagram.com'
    a.wiki = 'wikipedia?'
    a.profile_image = 'link.link'
    a.profile_image_thumbnail = 'link.link.link'
    a.flights_count = '2'
    a.landings_count = '2'
    a.last_flight = '1973-04-09T11:03:00Z'
    a.first_flight = '1970-04-09T11:03:00Z'
    a.status_name = 'alive'
    a.type_name = 'idk'
    a.agency_name = 'spongebob space program'
    a.agency_type = 'spacial'
    a.agency_country_code = 'square'
    a.agency_abbrev = 'SSP'
    a.agency_logo_url = 'link.ssp'
    a.birth_date = '1973-04-09'

    assert a.nationality == 'gone'
    assert a.bio == 'human born in human city'
    assert a.twitter == 'twitter.com'
    assert a.instagram == 'instagram.com'
    assert a.wiki == 'wikipedia?'
    assert a.profile_image == 'link.link'
    assert a.profile_image_thumbnail == 'link.link.link'
    assert a.flights_count == '2'
    assert a.landings_count == '2'
    assert a.last_flight == '1973-04-09T11:03:00Z'
    assert a.first_flight == '1970-04-09T11:03:00Z'
    assert a.status_name == 'alive'
    assert a.type_name == 'idk'
    assert a.agency_name == 'spongebob space program'
    assert a.agency_type == 'spacial'
    assert a.agency_country_code == 'square'
    assert a.agency_abbrev == 'SSP'
    assert a.agency_logo_url == 'link.ssp'
    assert a.birth_date == '1973-04-09'
    assert a.name == 'name'
