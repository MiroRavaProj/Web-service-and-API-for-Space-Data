# Rocket-Space-Stuff Project
Rocket Space Stuff Project is a Web-Service-Application, Library, and Demo Application ensemble.
* Developed by Miro Rava and Oleg Lastocichin, two undergraduate students at SUPSI, (Lugano, CH)

This Readme contains information mainly for the Library, all the information about the Web-Service-Application and the Demo App, will be contained in a separate report.

# Rocket Space Stuff Library

Rocket Space Stuff is a Python library that allows you to interact with various space-related API endpoints. With this library, you can retrieve information about astronauts, launches, and launchers.
## Links and Creators:

* Library Creator: Miro Rava                        [Linkedin profile](https://www.linkedin.com/in/miro-rava/)
* Library Tester: Oleg Lastocichin                  [Linkedin profile](https://www.linkedin.com/in/oleg-lastocichin-845733252/)

* [Github page for the entire project](https://github.com/MiroRavaProj/Web-service-and-API-for-Space-Data)
## Installation
```shell
python -m pip install rocket-space-stuff
```
## Usage and methods for Astronaut Objects
### Initialize Astronaut Object
* From Database:
```python
# Initialize the SpaceAPI client
from space_py import SpaceApi
api = SpaceApi()

# Find astronaut by name
astro = api.find_astro_by('name', 'John Smith')
```
* Manually
```python
from space_py import Astronaut
astro = Astronaut({"name": name, "date_of_birth": birth, "date_of_death": death, "nationality": nationality,
                     "bio": description,
                     "twitter": twitter, "instagram": insta, "wiki": wiki,
                     "profile_image": profile_img,
                     "profile_image_thumbnail": profile_img_thmb,
                     "flights_count": flights, "landings_count": landings, "last_flight": last_fl,
                     "first_flight": first_fl, "status_name": status, "type_name": enroll,
                     "agency_name": agency, "agency_type": agency_type,
                     "agency_country_code": agency_countries, "agency_abbrev": agency_acr,
                     "agency_logo_url": agency_logo})
```
### Getters and Setters
`age`
Retrieves the astronaut's age.
```python
# Get astronaut's age
age = astro.age
```
`age_of_death`
Retrieves the astronaut's age of death.
```python
# Get astronaut's age_of_death
age_of_death = astro.age_of_death
```
`agency_abbrev`
Retrieves and Set the astronaut's agency abbreviation.
```python
# Get astronaut's agency abbreviation
agency_abbrev = astro.agency_abbrev
# Set astronaut's agency abbreviation
astro.agency_abbrev = "NASA"

```
`agency_country_code`
Retrieves and Set the astronaut's agency country code.
```python
# Get astronaut's agency country code
agency_country_code = astro.agency_country_code
# Set astronaut's agency country code
astro.agency_country_code = "US"

```
`agency_logo_url`
Retrieves and Set the astronaut's agency logo url.
```python
# Get astronaut's agency logo url
agency_logo_url = astro.agency_logo_url
# Set astronaut's agency logo url
astro.agency_logo_url = "https://www.nasa.gov/sites/default/files/images/nasa-logo.png"

```
`agency_name`
Retrieves and Set the astronaut's agency name.
```python
# Get astronaut's agency name
agency_name = astro.agency_name
# Set astronaut's agency name
astro.agency_name = "National Aeronautics and Space Administration"

```
`agency_type`
Retrieves and Set the astronaut's agency type.
```python
# Get astronaut's agency type
agency_type = astro.agency_type
# Set astronaut's agency type
astro.agency_type = "Governmental"

```
`bio`
Retrieves and Set the astronaut's bio.
```python
# Get astronaut's bio
bio = astro.bio
# Set astronaut's bio
astro.bio = "John Smith is an astronaut with NASA. He has flown on 3 space missions."

```
`birth_date`
Retrieves and Set the astronaut's birth date.
```python
# Get astronaut's birth date
birth_date = astro.birth_date
# Set astronaut's birth date
astro.birth_date = "1970-01-01"

```
`death_date`
Retrieves and Set the astronaut's death date.
```python
# Get astronaut's death date
death_date = astro.death_date
# Set astronaut's death date
astro.death_date = "2050-01-01"

```
`first_flight`
Retrieves and Set the astronaut's first flight.
```python
# Get astronaut's first flight
first_flight = astro.first_flight
# Set astronaut's first flight
astro.first_flight = "2000-01-01"

```
`flights_count`
Retrieves and Set the astronaut's flights count.
```python
# Get astronaut's flights count
flights_count = astro.flights_count
# Set astronaut's flights count
astro.flights_count = "3"

```
`instagram`
Retrieves and Set the astronaut's Instagram page url.
```python
# Get astronaut's Instagram page url
instagram = astro.instagram
# Set astronaut's Instagram handle
astro.instagram = "https://www.instagram.com/j_smith_astro"

```
`jsonify`
Retrieves the astronaut's information in JSON format.
```python
# Get astronaut's information in JSON format
json_data = astro.jsonify

```
`landings_count`
Retrieves and Set the astronaut's landings count.
```python
# Get astronaut's landings count
landings_count = astro.landings_count
# Set astronaut's landings count
astro.landings_count = "2"
```
`last_flight`
Retrieves and Set the astronaut's last flight.
```python
# Get astronaut's last flight
last_flight = astro.last_flight
# Set astronaut's last flight
astro.last_flight = "2022-01-01"

```
`name`
Retrieves and Set the astronaut's name.
```python
# Get astronaut's name
name = astro.name
# Set astronaut's name
astro.name = "John Smith"

```
`nationality`
Retrieves and Set the astronaut's nationality.
```python
# Get astronaut's nationality
nationality = astro.nationality
# Set astronaut's nationality
astro.nationality = "USA"

```
`profile_image`
Retrieves and Set the astronaut's profile image url.
```python
# Get astronaut's profile image url
profile_image = astro.profile_image
# Set astronaut's profile image url
astro.profile_image = "https://www.example.com/images/j_smith_astro.jpg"

```
`profile_image_thumbnail`
Retrieves and Set the astronaut's profile image thumbnail url.
```python
# Get astronaut's profile image thumbnail url
profile_image_thumbnail = astro.profile_image_thumbnail
# Set astronaut's profile image thumbnail url
astro.profile_image_thumbnail = "https://www.example.com/images/j_smith_astro_thumbnail.jpg"

```
`show_basic_info`
Retrieves the astronaut's basic information.
```python
# Get astronaut's basic information
basic_info = astro.show_basic_info

```
`status_name`
Retrieves and Set the astronaut's status name.
```python
# Get astronaut's status name
status_name = astro.status_name
# Set astronaut's status name
astro.status_name = "Active"

```
`twitter`
Retrieves and Set the astronaut's twitter url.
```python
# Get astronaut's twitter url
twitter = astro.twitter
# Set astronaut's twitter handle
astro.twitter = "https://twitter.com/j_smith_astro"

```
`type_name`
Retrieves and Set the astronaut's type name.
```python
# Get astronaut's type name
type_name = astro.type_name
# Set astronaut's type name
astro.type_name = "Government"

```
`wiki`
Retrieves and Set the astronaut's wiki page url.
```python
# Get astronaut's wiki page url
wiki = astro.wiki
# Set astronaut's wiki page url
astro.wiki = "https://en.wikipedia.org/wiki/John_Smith_(astronaut)"

```
## Usage and methods for Launcher Objects
### Initialize Launcher Object
* From Database:
```python
# Initialize the SpaceAPI client
api = SpaceApi()

# Find astronaut by name
launcher = api.find_launcher_by('full_name', 'Atlas V')
```
* Manually
```python
from space_py import Launcher
launcher = Launcher({"flight_proven": flight_proven, "serial_number": serial_number, "status": status,
                     "details": details, "image_url": image_url, "flights": flights,
                     "last_launch_date": last_launch_date, "first_launch_date": first_launch_date,
                     "launcher_config_full_name": launcher_config_full_name})
```
* The methods `jsonify` and `show_basic_info` are similar to the Astronaut's ones.
* All these following methods are both Getters and Setters similarly to the Astronaut's ones:
```python
[launcher.description, launcher.first_launch, launcher.flights_count, launcher.full_name, launcher.is_flight_proven, 
 launcher.last_launch, launcher.launcher_image, launcher.serial_n, launcher.status]
```
## Usage and methods for Launch Objects
### Initialize Launch Object
* From Database:
```python
# Initialize the SpaceAPI client
api = SpaceApi()

# Find astronaut by name
launch = api.find_launch_by('name', 'Atlas V')
```
* Manually
```python
from space_py import Launch
launch = Launch({"name": name, "net": net, "window_start": window_start,
                     "window_end": window_end, "failreason": fail_reason, "image": image,
                     "infographic": infographic, "orbital_launch_attempt_count": orbital_launch_attempt_count,
                     "orbital_launch_attempt_count_year": orbital_launch_attempt_count_year,
                     "location_launch_attempt_count": location_launch_attempt_count,
                     "location_launch_attempt_count_year": location_launch_attempt_count_year,
                     "pad_launch_attempt_count": pad_launch_attempt_count,
                     "pad_launch_attempt_count_year": pad_launch_attempt_count_year,
                     "agency_launch_attempt_count": agency_launch_attempt_count,
                     "agency_launch_attempt_count_year": agency_launch_attempt_count_year,
                     "status_name": status_name, "launch_service_provider_name": launch_service_provider_name,
                     "launch_service_provider_type": launch_service_provider_type, "rocket_id": rocket_id,
                     "rocket_configuration_full_name": rocket_config_full_name,
                     "mission_name": mission_name, "mission_description": mission_description,
                     "mission_type": mission_type, "mission_orbit_name": mission_orbit_name,
                     "pad_wiki_url": pad_wiki_url, "pad_longitude": pad_longitude,
                     "pad_latitude": pad_latitude, "pad_location_name": pad_location_name,
                     "pad_location_country_code": pad_location_country_code})
```
* The methods `jsonify` and `show_basic_info` are similar to the Astronaut's ones.
* All these methods are both Getters and Setters similarly to the Astronaut's ones:
```python
[launch.agency_launch_attempt_count, launch.agency_launch_attempt_count_year, launch.fail_reason, launch.image, 
 launch.infographic, launch.jsonify, launch.launch_service_provider_name, launch.launch_service_provider_type, 
 launch.location_launch_attempt_count, launch.location_launch_attempt_count_year, launch.mission_description, 
 launch.mission_name, launch.mission_orbit_name, launch.mission_type, launch.name, launch.net, 
 launch.orbital_launch_attempt_count, launch.orbital_launch_attempt_count_year, launch.pad_latitude, 
 launch.pad_launch_attempt_count, launch.pad_launch_attempt_count_year, launch.pad_location_country_code, 
 launch.pad_location_name, launch.pad_longitude, launch.pad_wiki_url, launch.rocket_config_full_name, launch.rocket_id, 
 launch.show_basic_info, launch.status_name, launch.window_end, launch.window_start]
```

## Usage and methods for SpaceApi Objects
### Populate Astronaut Launch and Launcher with SpaceApi
* Instead of Initializing manually Astronaut, Launch or Launcher Objects, we can use SpaceApi `populate` methods.
```python
from space_py import SpaceApi
api = SpaceApi()
astro = api.populate_astro(name: str, birth: str, death: str, nationality: str, description: str, flights: str,
                            landings: str, last_fl: str, agency_acr: str, twitter: str = "None", insta: str = "None",
                            wiki: str = "None", profile_img: str = "None", profile_img_thmb: str = "None",
                            first_fl: str = "None",
                            status: str = "None", enroll: str = "None", agency: str = "None", agency_type: str = "None",
                            agency_countries: str = "None", agency_logo: str = "None")

launch = api.populate_launch(name: str, net: str, status_name: str, launch_service_provider_name: str,
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
                            pad_location_country_code: str = "None")

launcher = api.populate_launcher(launcher_config_full_name: str, serial_number: str, status: str, details: str, flights: str,
                                image_url: str = "None",
                                last_launch_date: str = "None", first_launch_date: str = "None",
                                flight_proven: str = "False")
```
### Url methods
* `default_url`: Returns the default API URL.
```python
from space_py import SpaceApi
api = SpaceApi()
default_url = api.default_url
```

* `url`: Returns the current API URL and can permit you to change it.
```python
from space_py import SpaceApi
api = SpaceApi()
print(api.url)
# https://current-api-url.com

new_url = 'https://new-api-url.com'
api.url = new_url
print(api.url)
# https://new-api-url.com
```
### Add methods
* `add_astro(astro: Astronaut)`: Adds a new astronaut to the API. The `astro` parameter should be an Astronaut object containing the astronaut's information.
```python
from space_py import SpaceApi, Astronaut
api = SpaceApi()
new_astro = Astronaut({"name": name, "date_of_birth": birth, "date_of_death": death, "nationality": nationality,
                     "bio": description,
                     "twitter": twitter, "instagram": insta, "wiki": wiki,
                     "profile_image": profile_img,
                     "profile_image_thumbnail": profile_img_thmb,
                     "flights_count": flights, "landings_count": landings, "last_flight": last_fl,
                     "first_flight": first_fl, "status_name": status, "type_name": enroll,
                     "agency_name": agency, "agency_type": agency_type,
                     "agency_country_code": agency_countries, "agency_abbrev": agency_acr,
                     "agency_logo_url": agency_logo})
api.add_astro(new_astro)
   ```
* `add_launch(launch: Launch)`: Adds a new launch to the API. The `launch` parameter should be a Launch Object containing the launch's information.
```python
from space_py import SpaceApi, Launch
api = SpaceApi()
new_astro = Launch({"name": name, "net": net, "window_start": window_start,
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
                     "pad_location_country_code": pad_location_country_code})
api.add_launch(new_astro)
   ```
* `add_launcher(launcher: Launcher)`: Adds a new launcher to the API. The `launcher` parameter should be a Launch Object containing the launcher's information.
```python
from space_py import SpaceApi, Launcher
api = SpaceApi()
new_astro = Launcher({"flight_proven": flight_proven, "serial_number": serial_number, "status": status,
                     "details": details, "image_url": image_url, "flights": flights,
                     "last_launch_date": last_launch_date, "first_launch_date": first_launch_date,
                     "launcher_config_full_name": launcher_config_full_name})
api.add_launcher(new_astro)
   ```
### Delete methods
* `delete_astro_by(field: str, value: str)`: Deletes an astronaut from the API based on the specified field and value.
```python
from space_py import SpaceApi
api = SpaceApi()
api.delete_astro_by('name', 'John Smith')
```
* `delete_launch_by(field: str, value: str)`: Deletes a launch from the API based on the specified field and value.
```python
from space_py import SpaceApi
api = SpaceApi()
api.delete_launch_by('name', 'Falcon 9')
```
* `delete_launcher_by(field: str, value: str)`: Deletes a launcher from the API based on the specified field and value.
```python
from space_py import SpaceApi
api = SpaceApi()
api.delete_launcher_by('full_name', 'Atlas V')
```
### Find methods
#### Used to find an entry with exact match
* `find_astro_by(field: str, value: str)`: Retrieves an astronaut from the API based on the specified field and value. If astronaut is found, `astro` is an Astronaut Object, otherwise it is a string like: `'entry non found'`
```python
from space_py import SpaceApi
api = SpaceApi()
astro = api.find_astro_by('name', 'John Smith')
```
* `find_launch_by(field: str, value: str)`: Retrieves a launch from the API based on the specified field and value. If launch is found, `launch` is a Launch Object, otherwise it is a string like: `'entry non found'`
```python
from space_py import SpaceApi
api = SpaceApi()
launch = api.find_launch_by('name', 'Falcon 9')
```
* `find_launcher_by(field: str, value: str)`: Retrieves a launcher from the API based on the specified field and value. If launcher is found, `launcher` is a Launcher Object, otherwise it is a string like: `'entry non found'`
```python
from space_py import SpaceApi
api = SpaceApi()
launcher = api.find_launcher_by('full_name', 'Atlas V')
```
### Search methods
#### Used to search for and entry that contains `value` in the `field`
* `search_astro_by(field: str, value: str)`: Retrieves an astronaut from the API based on the specified field and value. If astronaut is found, `astro` is a dictionary containing Astronaut Objects, otherwise it is a dictionary like: `{'error':'entry non found'}`
```python
from space_py import SpaceApi
api = SpaceApi()
astro = api.search_astro_by('name', 'John Smith')
```
* `search_launch_by(field: str, value: str)`: Retrieves a launch from the API based on the specified field and value. If launch is found, `launch` is a dictionary containing Launch Objects, otherwise it is a dictionary like: `{'error':'entry non found'}`
```python
from space_py import SpaceApi
api = SpaceApi()
launch = api.search_launch_by('name', 'Falcon 9')
```
* `search_launcher_by(field: str, value: str)`: Retrieves a launcher from the API based on the specified field and value. If launcher is found, `launcher` is a dictionary containing Launcher Objects, otherwise it is a dictionary like: `{'error':'entry non found'}`
```python
from space_py import SpaceApi
api = SpaceApi()
launcher = api.search_launcher_by('full_name', 'Atlas V')
```
### Update methods
#### Used to overwrite an entry that exactly mach `value` in `field`
* `update_astro_by(field: str, value: str, update: Astronaut)`: Updates an astronaut record in the API based on the specified field and value. The `astro` parameter should be an Astronaut object containing the astronaut's information.
```python
from space_py import SpaceApi, Astronaut
api = SpaceApi()
updated_astro = Astronaut({"name": name, "date_of_birth": birth, "date_of_death": death, "nationality": nationality,
                     "bio": description,
                     "twitter": twitter, "instagram": insta, "wiki": wiki,
                     "profile_image": profile_img,
                     "profile_image_thumbnail": profile_img_thmb,
                     "flights_count": flights, "landings_count": landings, "last_flight": last_fl,
                     "first_flight": first_fl, "status_name": status, "type_name": enroll,
                     "agency_name": agency, "agency_type": agency_type,
                     "agency_country_code": agency_countries, "agency_abbrev": agency_acr,
                     "agency_logo_url": agency_logo})
api.update_astro_by('name', 'John Smith', updated_astro)
   ```
* `update_launch_by(field: str, value: str, update: Launch)`: Updates a launch record in the API based on the specified field and value. The `launch` parameter should be a Launch Object containing the launch's information.
```python
from space_py import SpaceApi, Launch
api = SpaceApi()
updated_astro = Launch({"name": name, "net": net, "window_start": window_start,
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
                     "pad_location_country_code": pad_location_country_code})
api.update_launch_by('name', 'Falcon 9', updated_astro)
   ```
* `update_launcher_by(field: str, value: str, update: Launcher)`: Updates a launcher record in the API based on the specified field and value. The `launcher` parameter should be a Launch Object containing the launcher's information.
```python
from space_py import SpaceApi, Launcher
api = SpaceApi()
updated_astro = Launcher({"flight_proven": flight_proven, "serial_number": serial_number, "status": status,
                     "details": details, "image_url": image_url, "flights": flights,
                     "last_launch_date": last_launch_date, "first_launch_date": first_launch_date,
                     "launcher_config_full_name": launcher_config_full_name})
api.update_launcher_by('full_name', 'Atlas V', updated_astro)
```
## Contributing

If you would like to contribute to the development of SpaceApi, please feel free to submit a pull request.






























