import requests
from library.class_folder.launcher import Launcher


def get():
    url = "http://127.0.0.1:4533/launchers/id/110"
    r = requests.get(url)
    json = r.json()
    key = list(json.keys())[0]
    a = Launcher(json[key])
    return a, key, json


def test_launcher_class():
    a, key, json = get()
    assert type(a) == type(Launcher(json[key]))


def test_launcher_description():
    a, key, json = get()
    assert a.description == json[key]['details']


def test_launcher_is_flight_proven():
    a, key, json = get()
    assert a.is_flight_proven == (json[key]['flight_proven'] == 'True')


def test_launcher_serial_number():
    a, key, json = get()
    assert a.serial_n == json[key]['serial_number']


def test_launcher_status():
    a, key, json = get()
    assert a.status == json[key]['status']


def test_launcher_image_url():
    a, key, json = get()
    assert a.launcher_image == json[key]['image_url']


def test_launcher_flights():
    a, key, json = get()
    assert a.flights_count == json[key]['flights']


def test_launcher_last_launch_date():
    a, key, json = get()
    assert a.last_launch == json[key]['last_launch_date']


def test_launcher_first_launch_date():
    a, key, json = get()
    assert a.first_launch == json[key]['first_launch_date']


def test_launcher_launcher_config_full_name():
    a, key, json = get()
    assert a.full_name == json[key]['launcher_config_full_name']


def test_launcher_repr():  # testing if function exists
    a, key, json = get()
    x = repr(a)
    assert repr(a) == x


def test_launcher_show_basic_info():  # testing if function exists
    a, key, json = get()
    x = (a.show_basic_info)
    assert a.show_basic_info == x


def test_launcher_jsonify():  # testing if function exists
    a, key, json = get()
    x = a.jsonify
    assert a.jsonify == x


def test_launcher_setters():
    a, b, c = get()
    a.launcher_config_full_name = 'name'
    a.serial_number = '23'
    a.status = 'active'
    a.details = 'exists'
    a.image_url = 'url'
    a.flights_count = '1'
    a.flights_count = 'kek'
    a.is_flight_proven = 'False'
    a.last_launch = '2012-05-02T22:49:52Z'
    a.first_launch = '2012-05-02T22:49:52Z'
    a.last_launch = 'value'
    a.first_launch = 'value'

    assert a.launcher_config_full_name == 'name'
    assert a.serial_number == '23'
    assert a.status == 'active'
    assert a.details == 'exists'
    assert a.image_url == 'url'
    assert a.flights_count == '1'
    assert a.is_flight_proven != 'False'
    assert a.is_flight_proven is False
    assert a.last_launch == '2012-05-02T22:49:52Z'
    assert a.first_launch == '2012-05-02T22:49:52Z'
    assert a.last_launch != 'value'
    assert a.first_launch != 'value'
