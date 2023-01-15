from library.class_folder.checker import isValidDate, int_check, float_check, isValidDateFlight


class Launcher:
    def __init__(self, json: dict = None):
        if json is not None:
            self.__flight_proven = json["flight_proven"]
            self.__serial_number = json["serial_number"]
            self.__status = json["status"]
            self.__details = json["details"]
            self.__image_url = json["image_url"]
            self.__flights = json["flights"]
            self.__last_launch_date = json["last_launch_date"]
            self.__first_launch_date = json["first_launch_date"]
            self.__launcher_config_full_name = json["launcher_config_full_name"]
        else:
            self.__flight_proven = "None"
            self.__serial_number = "None"
            self.__status = "None"
            self.__details = "None"
            self.__image_url = "None"
            self.__flights = "None"
            self.__last_launch_date = "None"
            self.__first_launch_date = "None"
            self.__launcher_config_full_name = "None"

    @property
    def full_name(self):
        return self.__launcher_config_full_name

    @property
    def serial_n(self):
        return self.__serial_number

    @property
    def status(self):
        return self.__status

    @property
    def description(self):
        return self.__details

    @property
    def launcher_image(self):
        return self.__image_url

    @property
    def flights_count(self):
        return self.__flights

    @property
    def is_flight_proven(self):
        return self.__flight_proven == "True"

    @property
    def last_launch(self):
        return self.__last_launch_date

    @property
    def first_launch(self):
        return self.__first_launch_date

    def __repr__(self):
        return f"\nEXTENDED LAUNCHER INFO:\nFull Name: {self.__launcher_config_full_name}\nSerial Number: {self.__serial_number}\n" \
               f"Status: {self.__status}\nDescription: {self.__details}\nLauncher Image: {self.__image_url}\n" \
               f"Flights count: {self.__flights}\nIs Flight Proven: {self.__flight_proven}\nLast launch date: {self.__last_launch_date}\n" \
               f"First launch date: {self.__first_launch_date}"

    @property
    def show_basic_info(self):
        return f"\nBASIC LAUNCHER INFO:\nFull Name: {self.__launcher_config_full_name}\n" \
               f"Status: {self.__status}\nDescription: {self.__details}\nLauncher Image: {self.__image_url}\n"

    @property
    def jsonify(self):
        return {"flight_proven": self.__flight_proven, "serial_number": self.__serial_number, "status": self.__status,
                "details": self.__details, "image_url": self.__image_url, "flights": self.__flights,
                "last_launch_date": self.__last_launch_date, "first_launch_date": self.__first_launch_date,
                "launcher_config_full_name": self.__launcher_config_full_name}

    @full_name.setter
    def full_name(self, value: str):
        self.__launcher_config_full_name = value

    @serial_n.setter
    def serial_n(self, value: str):
        if int_check(value):
            self.__serial_number = value

    @status.setter
    def status(self, value: str):
        self.__status = value

    @description.setter
    def description(self, value: str):
        self.__details = value

    @launcher_image.setter
    def launcher_image(self, value: str):
        self.__image_url = value

    @flights_count.setter
    def flights_count(self, value: str):
        if int_check(value):
            self.__flights = value

    @is_flight_proven.setter
    def is_flight_proven(self, value):
        if value == bool:
            self.__flight_proven = value
        elif value == str:
            self.__flight_proven = bool(value)

    @last_launch.setter
    def last_launch(self, value: str):
        if isValidDateFlight(value):
            self.__last_launch_date = value

    @first_launch.setter
    def first_launch(self, value: str):
        if isValidDateFlight(value):
            self.__first_launch_date = value
