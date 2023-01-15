from library.class_folder.astronaut import Astronaut
from library.class_folder.launcher import Launcher
from library.class_folder.launch import Launch
import requests


class SpaceApi:
    def __init__(self):
        self.__default_url = "http://127.0.0.1:4533"
        self.__url = self.__default_url

    @staticmethod
    def populate_launch(name: str, net: str, status_name: str, launch_service_provider_name: str,
                        rocket_config_full_name: str,
                        mission_description: str, pad_location_name: str,
                        window_start: str = "None", window_end: str = "None", fail_reason: str = "None",
                        image: str = "None",
                        infographic: str = "None", orbital_launch_attempt_count: str = "None",
                        orbital_launch_attempt_count_year: str = "None",
                        location_launch_attempt_count: str = "None", location_launch_attempt_count_year: str = "None",
                        pad_launch_attempt_count: str = "None", pad_launch_attempt_count_year: str = "None",
                        agency_launch_attempt_count: str = "None", agency_launch_attempt_count_year: str = "None",
                        launch_service_provider_type: str = "None", rocket_id: str = "None",
                        mission_name: str = "None", mission_type: str = "None",
                        mission_orbit_name: str = "None", pad_wiki_url: str = "None", pad_longitude: str = "None",
                        pad_latitude: str = "None",
                        pad_location_country_code: str = "None"):
        temp_dict = {"name": name, "net": net, "window_start": window_start,
                     "window_end": window_end, "failreason": fail_reason, "image": image,
                     "infographic": infographic,
                     "orbital_launch_attempt_count": orbital_launch_attempt_count,
                     "orbital_launch_attempt_count_year": orbital_launch_attempt_count_year,
                     "location_launch_attempt_count": location_launch_attempt_count,
                     "location_launch_attempt_count_year": location_launch_attempt_count_year,
                     "pad_launch_attempt_count": pad_launch_attempt_count,
                     "pad_launch_attempt_count_year": pad_launch_attempt_count_year,
                     "agency_launch_attempt_count": agency_launch_attempt_count,
                     "agency_launch_attempt_count_year": agency_launch_attempt_count_year,
                     "status_name": status_name,
                     "launch_service_provider_name": launch_service_provider_name,
                     "launch_service_provider_type": launch_service_provider_type, "rocket_id": rocket_id,
                     "rocket_configuration_full_name": rocket_config_full_name,
                     "mission_name": mission_name, "mission_description": mission_description,
                     "mission_type": mission_type, "mission_orbit_name": mission_orbit_name,
                     "pad_wiki_url": pad_wiki_url, "pad_longitude": pad_longitude,
                     "pad_latitude": pad_latitude, "pad_location_name": pad_location_name,
                     "pad_location_country_code": pad_location_country_code}
        return Launch(temp_dict)

    @staticmethod
    def populate_launcher(launcher_config_full_name: str, serial_number: str, status: str, details: str, flights: str,
                          image_url: str = "None",
                          last_launch_date: str = "None", first_launch_date: str = "None",
                          flight_proven: str = "False"):
        temp_dict = {"flight_proven": flight_proven, "serial_number": serial_number, "status": status,
                     "details": details, "image_url": image_url, "flights": flights,
                     "last_launch_date": last_launch_date, "first_launch_date": first_launch_date,
                     "launcher_config_full_name": launcher_config_full_name}
        return Launcher(temp_dict)

    @staticmethod
    def populate_astro(name: str, birth: str, death: str, nationality: str, description: str, flights: str,
                       landings: str, last_fl: str, agency_acr: str, twitter: str = "None", insta: str = "None",
                       wiki: str = "None", profile_img: str = "None", profile_img_thmb: str = "None",
                       first_fl: str = "None",
                       status: str = "None", enroll: str = "None", agency: str = "None", agency_type: str = "None",
                       agency_countries: str = "None", agency_logo: str = "None"):
        temp_dict = {"name": name, "date_of_birth": birth, "date_of_death": death, "nationality": nationality,
                     "bio": description,
                     "twitter": twitter, "instagram": insta, "wiki": wiki,
                     "profile_image": profile_img,
                     "profile_image_thumbnail": profile_img_thmb,
                     "flights_count": flights, "landings_count": landings, "last_flight": last_fl,
                     "first_flight": first_fl, "status_name": status, "type_name": enroll,
                     "agency_name": agency, "agency_type": agency_type,
                     "agency_country_code": agency_countries, "agency_abbrev": agency_acr,
                     "agency_logo_url": agency_logo}
        return Astronaut(temp_dict)

    @property
    def url(self):
        return self.__url

    def set_new_url(self, value: str):
        self.__url = value

    @property
    def default_url(self):
        return self.__default_url

    # Start of Astronaut methods

    def find_all_astro(self):
        astro_dict = {}
        url = f"{self.url}/astronauts"
        r = requests.get(url)
        if str(r) == "<Response [404]>":
            return {"error": f"Entry not found: dataset is empty"}, 404
        key_list = list(r.json(strict=False).keys())
        for key in key_list:
            astro_dict[int(key)] = Astronaut(r.json(strict=False)[key])
        return astro_dict

    def find_astro_by(self, variable: str, value):
        url = f"{self.url}/astronauts/{variable}/'{value}'"
        r = requests.get(url)
        if str(r) == "<Response [404]>":
            return {"error": f"Entry not found:  {variable} == {value}"}
        key = list(r.json(strict=False).keys())[0]
        response = r.json(strict=False)[key]
        return Astronaut(response)

    def search_astro_by(self, variable: str, value):
        astro_dict = {}
        url = f"{self.url}/astronauts/search?{variable}={value}"
        r = requests.get(url)
        if str(r) == "<Response [404]>":
            return {"error": f"Entry not found:  {variable} == {value}"}
        key_list = list(r.json(strict=False).keys())
        for key in key_list:
            astro_dict[int(key)] = Astronaut(r.json(strict=False)[key])
        return astro_dict

    def add_astro(self, astro: Astronaut):
        url = f"{self.url}/astronauts"
        r = requests.post(url, json=astro.jsonify)
        return r.json()

    def delete_astro_by(self, variable: str, value):
        url = f"{self.url}/astronauts/{variable}/'{value}'"
        r = requests.delete(url)
        return r.json()

    def update_astro_by(self, variable: str, value, astro: Astronaut):
        url = f"{self.url}/astronauts/{variable}/'{value}'"
        r = requests.put(url, json=astro.jsonify)
        return r.json()

    # Start of Launcher methods

    def find_all_launcher(self):
        launcher_dict = {}
        url = f"{self.url}/launchers"
        r = requests.get(url)
        if str(r) == "<Response [404]>":
            return {"error": f"Entry not found: dataset is empty"}, 404
        key_list = list(r.json(strict=False).keys())
        for key in key_list:
            launcher_dict[int(key)] = Launcher(r.json(strict=False)[key])
        return launcher_dict

    def find_launcher_by(self, variable: str, value):
        url = f"{self.url}/launchers/{variable}/'{value}'"
        r = requests.get(url)
        if str(r) == "<Response [404]>":
            return {"error": f"Entry not found:  {variable} == {value}"}
        key = list(r.json(strict=False).keys())[0]
        response = r.json(strict=False)[key]
        return Launcher(response)

    def search_launcher_by(self, variable: str, value):
        launcher_dict = {}
        url = f"{self.url}/launchers/search?{variable}={value}"
        r = requests.get(url)
        if str(r) == "<Response [404]>":
            return {"error": f"Entry not found:  {variable} == {value}"}
        key_list = list(r.json(strict=False).keys())
        for key in key_list:
            launcher_dict[int(key)] = Launcher(r.json(strict=False)[key])
        return launcher_dict

    def add_launcher(self, launcher: Launcher):
        url = f"{self.url}/launchers"
        r = requests.post(url, json=launcher.jsonify)
        return r.json()

    def delete_launcher_by(self, variable: str, value):
        url = f"{self.url}/launchers/{variable}/'{value}'"
        r = requests.delete(url)
        return r.json()

    def update_launcher_by(self, variable: str, value, launcher: Launcher):
        url = f"{self.url}/launchers/{variable}/'{value}'"
        r = requests.put(url, json=launcher.jsonify)
        return r.json()

    # Start of Launch methods

    def find_all_launch(self):
        launch_dict = {}
        url = f"{self.url}/launches"
        r = requests.get(url)
        if str(r) == "<Response [404]>":
            return {"error": f"Entry not found: dataset is empty"}, 404
        key_list = list(r.json(strict=False).keys())
        for key in key_list:
            launch_dict[int(key)] = Launch(r.json(strict=False)[key])
        return launch_dict

    def find_launch_by(self, variable: str, value):
        url = f"{self.url}/launches/{variable}/'{value}'"
        r = requests.get(url)
        if str(r) == "<Response [404]>":
            return {"error": f"Entry not found:  {variable} == {value}"}
        key = list(r.json(strict=False).keys())[0]
        response = r.json(strict=False)[key]
        return Launch(response)

    def search_launch_by(self, variable: str, value):
        launch_dict = {}
        url = f"{self.url}/launches/search?{variable}={value}"
        r = requests.get(url)
        if str(r) == "<Response [404]>":
            return {"error": f"Entry not found:  {variable} == {value}"}
        key_list = list(r.json(strict=False).keys())
        for key in key_list:
            launch_dict[int(key)] = Launch(r.json(strict=False)[key])
        return launch_dict

    def add_launch(self, launch: Launch):
        url = f"{self.url}/launches"
        r = requests.post(url, json=launch.jsonify)
        return r.json()

    def delete_launch_by(self, variable: str, value):
        url = f"{self.url}/launches/{variable}/'{value}'"
        r = requests.delete(url)
        return r.json()

    def update_launch_by(self, variable: str, value, launch: Launch):
        url = f"{self.url}/launches/{variable}/'{value}'"
        r = requests.put(url, json=launch.jsonify)
        return r.json()


    '''
if __name__ == '__main__':
    finder = SpaceApi()
    print()
    print(finder.search_astro_by("flights_count", "30"))
    print()
    print(finder.find_astro_by("name", "Shaun the Sheep").show_basic_info)
    print()
    a = finder.populate_astro("miro rava", "2001-05-22", "None", "italy", "test di prova post", "100", "100",
                              "prova-landing01", "TST")
    print(finder.add_astro(a))
    print()
    print(finder.find_astro_by("name", "miro rava").show_basic_info)
    print()
    print(finder.delete_astro_by("name", "miro rava"))
    print()
    print(finder.find_astro_by("name", "miro rava"))
    print()
    print(finder.add_astro(a))
    print()
    b = finder.populate_astro("Oleg Lastocichin", "boh", "None", "moldova", "test di prova update", "300", "300",
                              "prova-landing02", "KKK")
    print(finder.update_astro_by("name", "miro rava", b))
    print()
    print(finder.delete_astro_by("name", "Oleg Lastocichin"))

if __name__ == '__main__':
    finder = SpaceApi()
    print()
    print(finder.search_launcher_by("flights", "9"))
    print()
    print(finder.find_launcher_by("serial_number", "B1060").show_basic_info)
    print()
    a = finder.populate_launcher("Razzo super spaziale", "a1b2c3", "imaginary", "Razzo di prova per api versione 01",
                                 "250")
    print(finder.add_launcher(a))
    print()
    print(finder.find_launcher_by("serial_number", "a1b2c3").show_basic_info)
    print()
    print(finder.delete_launcher_by("serial_number", "a1b2c3"))
    print()
    print(finder.find_launcher_by("serial_number", "a1b2c3"))
    print()
    print(finder.add_launcher(a))
    print()
    b = finder.populate_launcher("Mucca spaziale", "aabbcc", "imaginary", "Razzo di prova per api versione 02",
                                 "800")
    print(finder.update_launcher_by("serial_number", "a1b2c3", b))
    print()
    print(finder.delete_launcher_by("serial_number", "aabbcc"))

if __name__ == '__main__':
    finder = SpaceApi()
    print()
    print(finder.search_launch_by("name", "sputnik"))
    print()
    print(finder.find_launch_by("name", "Sputnik 8K74PS | Sputnik 1").show_basic_info)
    print()
    a = finder.populate_launch("Sopra la panca", "2023-09-10", "imaginary", "Balle spaziali",
                               "Star destroyer", "test for the api, number 01", "Uranus")
    print(finder.add_launch(a))
    print()
    print(finder.find_launch_by("rocket_configuration_full_name", "Star destroyer").show_basic_info)
    print()
    print(finder.delete_launch_by("rocket_configuration_full_name", "Star destroyer"))
    print()
    print(finder.find_launch_by("rocket_configuration_full_name", "Star destroyer"))
    print()
    print(finder.add_launch(a))
    print()
    b = finder.populate_launch("Antonucci_space_stuff", "0001-01-01", "imaginary", "Python guys",
                               "Cosmetics", "test for the api, number 02", "Help me")
    print(finder.update_launch_by("launch_service_provider_name", "Balle spaziali", b))
    print()
    print(finder.delete_launch_by("rocket_configuration_full_name", "Cosmetics"))
'''