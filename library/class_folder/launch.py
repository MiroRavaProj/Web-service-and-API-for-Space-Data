from library.class_folder.checker import isValidDate, int_check, float_check, isValidDateFlight


class Launch:
    def __init__(self, json: dict = None):
        if json is not None:
            self.__name = json["name"]
            self.__net = json["net"]
            self.__window_end = json["window_end"]
            self.__window_start = json["window_start"]
            self.__fail_reason = json["failreason"]
            self.__image = json["image"]
            self.__infographic = json["infographic"]
            self.__orbital_launch_attempt_count = json["orbital_launch_attempt_count"]
            self.__location_launch_attempt_count = json["location_launch_attempt_count"]
            self.__pad_launch_attempt_count = json["pad_launch_attempt_count"]
            self.__agency_launch_attempt_count = json["agency_launch_attempt_count"]
            self.__orbital_launch_attempt_count_year = json["orbital_launch_attempt_count_year"]
            self.__location_launch_attempt_count_year = json["location_launch_attempt_count_year"]
            self.__pad_launch_attempt_count_year = json["pad_launch_attempt_count_year"]
            self.__agency_launch_attempt_count_year = json["agency_launch_attempt_count_year"]
            self.__status_name = json["status_name"]
            self.__launch_service_provider_name = json["launch_service_provider_name"]
            self.__launch_service_provider_type = json["launch_service_provider_type"]
            self.__rocket_id = json["rocket_id"]
            self.__rocket_config_full_name = json["rocket_configuration_full_name"]
            self.__mission_name = json["mission_name"]
            self.__mission_description = json["mission_description"]
            self.__mission_type = json["mission_type"]
            self.__mission_orbit_name = json["mission_orbit_name"]
            self.__pad_wiki_url = json["pad_wiki_url"]
            self.__pad_latitude = json["pad_latitude"]
            self.__pad_longitude = json["pad_longitude"]
            self.__pad_location_name = json["pad_location_name"]
            self.__pad_location_country_code = json["pad_location_country_code"]
        else:
            self.__name = "None"
            self.__net = "None"
            self.__window_end = "None"
            self.__window_start = "None"
            self.__fail_reason = "None"
            self.__image = "None"
            self.__infographic = "None"
            self.__orbital_launch_attempt_count = "None"
            self.__location_launch_attempt_count = "None"
            self.__pad_launch_attempt_count = "None"
            self.__agency_launch_attempt_count = "None"
            self.__orbital_launch_attempt_count_year = "None"
            self.__location_launch_attempt_count_year = "None"
            self.__pad_launch_attempt_count_year = "None"
            self.__agency_launch_attempt_count_year = "None"
            self.__status_name = "None"
            self.__launch_service_provider_name = "None"
            self.__launch_service_provider_type = "None"
            self.__rocket_id = "None"
            self.__rocket_config_full_name = "None"
            self.__mission_name = "None"
            self.__mission_description = "None"
            self.__mission_type = "None"
            self.__mission_orbit_name = "None"
            self.__pad_wiki_url = "None"
            self.__pad_latitude = "None"
            self.__pad_longitude = "None"
            self.__pad_location_name = "None"
            self.__pad_location_country_code = "None"

    @property
    def name(self):
        return self.__name

    @property
    def net(self):
        return self.__net

    @property
    def window_end(self):
        return self.__window_end

    @property
    def window_start(self):
        return self.__window_start

    @property
    def fail_reason(self):
        return self.__fail_reason

    @property
    def image(self):
        return self.__image

    @property
    def infographic(self):
        return self.__infographic

    @property
    def orbital_launch_attempt_count(self):
        return self.__orbital_launch_attempt_count

    @property
    def location_launch_attempt_count(self):
        return self.__location_launch_attempt_count

    @property
    def pad_launch_attempt_count(self):
        return self.__pad_launch_attempt_count

    @property
    def agency_launch_attempt_count(self):
        return self.__agency_launch_attempt_count

    @property
    def orbital_launch_attempt_count_year(self):
        return self.__orbital_launch_attempt_count_year

    @property
    def location_launch_attempt_count_year(self):
        return self.__location_launch_attempt_count_year

    @property
    def pad_launch_attempt_count_year(self):
        return self.__pad_launch_attempt_count_year

    @property
    def agency_launch_attempt_count_year(self):
        return self.__agency_launch_attempt_count_year

    @property
    def launch_service_provider_name(self):
        return self.__launch_service_provider_name

    @property
    def status_name(self):
        return self.__status_name

    @property
    def launch_service_provider_type(self):
        return self.__launch_service_provider_type

    @property
    def rocket_id(self):
        return self.__rocket_id

    @property
    def rocket_config_full_name(self):
        return self.__rocket_config_full_name

    @property
    def mission_name(self):
        return self.__mission_name

    @property
    def mission_description(self):
        return self.__mission_description

    @property
    def mission_type(self):
        return self.__mission_type

    @property
    def mission_orbit_name(self):
        return self.__mission_orbit_name

    @property
    def pad_wiki_url(self):
        return self.__pad_wiki_url

    @property
    def pad_latitude(self):
        return self.__pad_latitude

    @property
    def pad_longitude(self):
        return self.__pad_longitude

    @property
    def pad_location_name(self):
        return self.__pad_location_name

    @property
    def pad_location_country_code(self):
        return self.__pad_location_country_code

    def __repr__(self):
        return f"\nEXTENDED LAUNCH INFO:\n" \
               f"Name: {self.__name}\nNet launch: {self.__net}\nWindow start: {self.__window_start}\nWindow end: {self.__window_end}\n" \
               f"Fail reason: {self.__fail_reason}\nImage url: {self.__image}\nInfographic url: {self.__infographic}\n" \
               f"All_time Orbital launch attempt count: {self.__orbital_launch_attempt_count}\n" \
               f"Current_year Orbital launch attempt count: {self.__orbital_launch_attempt_count_year}\n" \
               f"All_time Location launch attempt count: {self.__location_launch_attempt_count}\n" \
               f"Current_year Location launch attempt count: {self.__location_launch_attempt_count_year}\n" \
               f"All_time Pad launch attempt count: {self.__pad_launch_attempt_count}\n" \
               f"Current_year Pad launch attempt count: {self.__pad_launch_attempt_count_year}\n" \
               f"All_time Agency launch attempt count: {self.__agency_launch_attempt_count}\n" \
               f"Current_year Agency launch attempt count: {self.__agency_launch_attempt_count_year}\n" \
               f"Launch status: {self.__status_name}\nService provider name: {self.__launch_service_provider_name}\n" \
               f"Service provider type: {self.__launch_service_provider_type}\nRocket ID: {self.__rocket_id}\n" \
               f"Rocket name: {self.__rocket_config_full_name}\nMission name: {self.__mission_name}\n" \
               f"Mission description: {self.__mission_description}\nMission type: {self.__mission_type}\n" \
               f"Mission orbit: {self.__mission_orbit_name}\nPad wikipedia link: {self.__pad_wiki_url}\n" \
               f"Pad longitude: {self.__pad_longitude}\nPad latitude: {self.__pad_latitude}\n" \
               f"Pad location name: {self.__pad_location_name}\nPad location country code: {self.__pad_location_country_code}"

    @property
    def show_basic_info(self):
        return f"\nBASIC LAUNCH INFO:\n" \
               f"Name: {self.__name}\nNet launch: {self.__net}\nImage url: {self.__image}\n" \
               f"Launch status: {self.__status_name}\nService provider name: {self.__launch_service_provider_name}\n" \
               f"Rocket name: {self.__rocket_config_full_name}\nMission description: {self.__mission_description}\n" \
               f"Pad longitude: {self.__pad_longitude}\nPad latitude: {self.__pad_latitude}\n" \
               f"Pad location name: {self.__pad_location_name}\n"

    @property
    def jsonify(self):
        return {"name": self.__name, "net": self.__net, "window_start": self.__window_start,
                "window_end": self.__window_end, "failreason": self.__fail_reason, "image": self.__image,
                "infographic": self.__infographic,
                "orbital_launch_attempt_count": self.__orbital_launch_attempt_count,
                "orbital_launch_attempt_count_year": self.__orbital_launch_attempt_count_year,
                "location_launch_attempt_count": self.__location_launch_attempt_count,
                "location_launch_attempt_count_year": self.__location_launch_attempt_count_year,
                "pad_launch_attempt_count": self.__pad_launch_attempt_count,
                "pad_launch_attempt_count_year": self.__pad_launch_attempt_count_year,
                "agency_launch_attempt_count": self.__agency_launch_attempt_count,
                "agency_launch_attempt_count_year": self.__agency_launch_attempt_count_year,
                "status_name": self.__status_name,
                "launch_service_provider_name": self.__launch_service_provider_name,
                "launch_service_provider_type": self.__launch_service_provider_type, "rocket_id": self.__rocket_id,
                "rocket_configuration_full_name": self.__rocket_config_full_name,
                "mission_name": self.__mission_name, "mission_description": self.__mission_description,
                "mission_type": self.__mission_type, "mission_orbit_name": self.__mission_orbit_name,
                "pad_wiki_url": self.__pad_wiki_url, "pad_longitude": self.__pad_longitude,
                "pad_latitude": self.__pad_latitude, "pad_location_name": self.__pad_location_name,
                "pad_location_country_code": self.__pad_location_country_code}

    @name.setter
    def name(self, value: str):
        self.__name = value

    @net.setter
    def net(self, value: str):
        if isValidDateFlight(value):
            self.__net = value

    @window_end.setter
    def window_end(self, value: str):
        if isValidDateFlight(value):
            self.__window_end = value

    @window_start.setter
    def window_start(self, value: str):
        if isValidDateFlight(value):
            self.__window_start = value

    @fail_reason.setter
    def fail_reason(self, value: str):
        self.__fail_reason = value

    @image.setter
    def image(self, value: str):
        self.__image = value

    @infographic.setter
    def infographic(self, value: str):
        self.__infographic = value

    @orbital_launch_attempt_count.setter
    def orbital_launch_attempt_count(self, value: str):
        if int_check(value):
            self.__orbital_launch_attempt_count = value

    @location_launch_attempt_count.setter
    def location_launch_attempt_count(self, value: str):
        if int_check(value):
            self.__location_launch_attempt_count = value

    @pad_launch_attempt_count.setter
    def pad_launch_attempt_count(self, value: str):
        if int_check(value):
            self.__pad_launch_attempt_count = value

    @agency_launch_attempt_count.setter
    def agency_launch_attempt_count(self, value: str):
        if int_check(value):
            self.__agency_launch_attempt_count = value

    @orbital_launch_attempt_count_year.setter
    def orbital_launch_attempt_count_year(self, value: str):
        if int_check(value):
            self.__orbital_launch_attempt_count_year = value

    @location_launch_attempt_count_year.setter
    def location_launch_attempt_count_year(self, value: str):
        if int_check(value):
            self.__location_launch_attempt_count_year = value

    @pad_launch_attempt_count_year.setter
    def pad_launch_attempt_count_year(self, value: str):
        if int_check(value):
            self.__pad_launch_attempt_count_year = value

    @agency_launch_attempt_count_year.setter
    def agency_launch_attempt_count_year(self, value: str):
        if int_check(value):
            self.__agency_launch_attempt_count_year = value

    @launch_service_provider_name.setter
    def launch_service_provider_name(self, value: str):
        self.__launch_service_provider_name = value

    @status_name.setter
    def status_name(self, value: str):
        self.__status_name = value

    @launch_service_provider_type.setter
    def launch_service_provider_type(self, value: str):
        self.__launch_service_provider_type = value

    @rocket_id.setter
    def rocket_id(self, value):
        if int_check(value):
            self.__rocket_id = int(value)

    @rocket_config_full_name.setter
    def rocket_config_full_name(self, value: str):
        self.__rocket_config_full_name = value

    @mission_name.setter
    def mission_name(self, value: str):
        self.__mission_name = value

    @mission_description.setter
    def mission_description(self, value: str):
        self.__mission_description = value

    @mission_type.setter
    def mission_type(self, value: str):
        self.__mission_type = value

    @mission_orbit_name.setter
    def mission_orbit_name(self, value: str):
        self.__mission_orbit_name = value

    @pad_wiki_url.setter
    def pad_wiki_url(self, value: str):
        self.__pad_wiki_url = value

    @pad_latitude.setter
    def pad_latitude(self, value: str):
        if float_check(value):
            self.__pad_latitude = value

    @pad_longitude.setter
    def pad_longitude(self, value: str):
        if float_check(value):
            self.__pad_longitude = value

    @pad_location_name.setter
    def pad_location_name(self, value: str):
        self.__pad_location_name = value

    @pad_location_country_code.setter
    def pad_location_country_code(self, value: str):
        self.__pad_location_country_code = value
