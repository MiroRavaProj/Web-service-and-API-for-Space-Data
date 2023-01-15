import requests
from library.class_folder.launch import Launch


def get():
    url = "http://127.0.0.1:4533/launches/id/110"
    r = requests.get(url)
    json = r.json()
    key = list(json.keys())[0]
    a = Launch(json[key])
    return a, key, json


def test_launch_class():
    a, key, json = get()
    assert type(a) == type(Launch(json[key]))


def test_launch_name():
    a, key, json = get()
    assert a.name == json[key]['name']


def test_launch_net():
    a, key, json = get()
    assert a.net == json[key]['net']


def test_launch_window_end():
    a, key, json = get()
    assert a.window_end == json[key]['window_end']


def test_launch_fail_reason():
    a, key, json = get()
    assert a.fail_reason == json[key]['failreason']


def test_launch_infographic():
    a, key, json = get()
    assert a.infographic == json[key]['infographic']


def test_launch_image():
    a, key, json = get()
    assert a.image == json[key]['image']


def test_launch_orbital_launch_attempt_count():
    a, key, json = get()
    assert a.orbital_launch_attempt_count == json[key]['orbital_launch_attempt_count']


def test_launch_location_launch_attempt_count():
    a, key, json = get()
    assert a.location_launch_attempt_count == json[key]['location_launch_attempt_count']


def test_launch_pad_launch_attempt_count():
    a, key, json = get()
    assert a.pad_launch_attempt_count == json[key]['pad_launch_attempt_count']


def test_launch_agency_launch_attempt_count():
    a, key, json = get()
    assert a.agency_launch_attempt_count == json[key]['agency_launch_attempt_count']


def test_launch_orbital_launch_attempt_count_year():
    a, key, json = get()
    assert a.orbital_launch_attempt_count_year == json[key]['orbital_launch_attempt_count_year']


def test_launch_location_launch_attempt_count_year():
    a, key, json = get()
    assert a.location_launch_attempt_count_year == json[key]['location_launch_attempt_count_year']


def test_launch_pad_launch_attempt_count_year():
    a, key, json = get()
    assert a.pad_launch_attempt_count_year == json[key]['pad_launch_attempt_count_year']


def test_launch_agency_launch_attempt_count_year():
    a, key, json = get()
    assert a.agency_launch_attempt_count_year == json[key]['agency_launch_attempt_count_year']


def test_launch_status_name():
    a, key, json = get()
    assert a.status_name == json[key]['status_name']


def test_launch_launch_service_provider_name():
    a, key, json = get()
    assert a.launch_service_provider_name == json[key]['launch_service_provider_name']


def test_launch_launch_service_provider_type():
    a, key, json = get()
    assert a.launch_service_provider_type == json[key]['launch_service_provider_type']


def test_launch_rocket_id():
    a, key, json = get()
    assert a.rocket_id == json[key]['rocket_id']


def test_launch_rocket_configuration_full_name():
    a, key, json = get()
    assert a.rocket_config_full_name == json[key]['rocket_configuration_full_name']


def test_launch_mission_name():
    a, key, json = get()
    assert a.mission_name == json[key]['mission_name']


def test_launch_mission_description():
    a, key, json = get()
    assert a.mission_description == json[key]['mission_description']


def test_launch_mission_type():
    a, key, json = get()
    assert a.mission_type == json[key]['mission_type']


def test_launch_mission_orbit_name():
    a, key, json = get()
    assert a.mission_orbit_name == json[key]['mission_orbit_name']


def test_launch_pad_wiki_url():
    a, key, json = get()
    assert a.pad_wiki_url == json[key]['pad_wiki_url']


def test_launch_pad_latitude():
    a, key, json = get()
    assert a.pad_latitude == json[key]['pad_latitude']


def test_pad_longitude():
    a, key, json = get()
    assert a.pad_longitude == json[key]['pad_longitude']


def test_launch_pad_location_name():
    a, key, json = get()
    assert a.pad_location_name == json[key]['pad_location_name']


def test_launch_pad_location_country_code():
    a, key, json = get()
    assert a.pad_location_country_code == json[key]['pad_location_country_code']


def test_launch_repr():  # testing if function exists
    a, key, json = get()
    x = repr(a)
    assert repr(a) == x


def test_launch_show_basic_info():  # testing if function exists
    a, key, json = get()
    x = (a.show_basic_info)
    assert a.show_basic_info == x


def test_launch_jsonify():  # testing if function exists
    a, key, json = get()
    x = a.jsonify
    assert a.jsonify == x

def test_launch_setters():
    a, key, json = get()

    a.name = 'name'
    a.net = '1951-03-18T22:57:58Z'
    a.window_end = '1951-03-18T22:57:58Z'
    a.window_start = '1951-03-18T22:57:58Z'
    a.fail_reason = 'none'
    a.image = 'image'
    a.infographic = 'info'
    a.orbital_launch_attempt_count = '1'
    a.location_launch_attempt_count = '1'
    a.pad_launch_attempt_count = '1'
    a.agency_launch_attempt_count = '1'
    a.orbital_launch_attempt_count_year = '1'
    a.location_launch_attempt_count_year = '1'
    a.pad_launch_attempt_count_year = '1'
    a.agency_launch_attempt_count_year = '1'
    a.launch_service_provider_name = 'name'
    a.status_name = 'stats'
    a.launch_service_provider_type = 'name'
    a.rocket_id = 2
    a.rocket_config_full_name = 'name'
    a.mission_name = 'name'
    a.mission_description = 'deesc'
    a.mission_type = 'type'
    a.mission_orbit_name = 'name'
    a.pad_wiki_url = 'url'
    a.pad_longitude = 3.02
    a.pad_latitude = 23.19
    a.pad_latitude = 'el'
    a.pad_longitude = 'le'
    a.pad_location_name = 'name'
    a.pad_location_country_code = 'name'

    assert a.name == 'name'
    assert a.net == '1951-03-18T22:57:58Z'
    assert a.window_end == '1951-03-18T22:57:58Z'
    assert a.window_start == '1951-03-18T22:57:58Z'
    assert a.fail_reason == 'none'
    assert a.image == 'image'
    assert a.infographic == 'info'
    assert a.orbital_launch_attempt_count == '1'
    assert a.location_launch_attempt_count == '1'
    assert a.pad_launch_attempt_count == '1'
    assert a.agency_launch_attempt_count == '1'
    assert a.orbital_launch_attempt_count_year == '1'
    assert a.location_launch_attempt_count_year == '1'
    assert a.pad_launch_attempt_count_year == '1'
    assert a.agency_launch_attempt_count_year == '1'
    assert a.launch_service_provider_name == 'name'
    assert a.status_name == 'stats'
    assert a.launch_service_provider_type == 'name'
    assert a.rocket_id == 2
    assert a.rocket_config_full_name == 'name'
    assert a.mission_name == 'name'
    assert a.mission_description == 'deesc'
    assert a.mission_type == 'type'
    assert a.mission_orbit_name == 'name'
    assert a.pad_wiki_url == 'url'
    assert a.pad_longitude == 3.02
    assert a.pad_latitude == 23.19
    assert a.pad_location_name == 'name'
    assert a.pad_location_country_code == 'name'
