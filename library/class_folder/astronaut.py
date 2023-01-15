import datetime
from datetime import date, datetime
from library.class_folder.checker import isValidDate, int_check, float_check, isValidDateFlight


class Astronaut:
    def __init__(self, json: dict = None):
        if json is not None:
            self.__name = json['name']
            self.__date_of_birth = json['date_of_birth']
            self.__date_of_death = json['date_of_death']
            self.__nationality = json['nationality']
            self.__bio = json['bio']
            self.__twitter = json['twitter']
            self.__instagram = json['instagram']
            self.__wiki = json['wiki']
            self.__profile_image = json['profile_image']
            self.__profile_image_thumbnail = json['profile_image_thumbnail']
            self.__flights_count = json['flights_count']
            self.__landings_count = json['landings_count']
            self.__last_flight = json['last_flight']
            self.__first_flight = json['first_flight']
            self.__status_name = json['status_name']
            self.__type_name = json['type_name']
            self.__agency_name = json['agency_name']
            self.__agency_type = json['agency_type']
            self.__agency_country_code = json['agency_country_code']
            self.__agency_abbrev = json['agency_abbrev']
            self.__agency_logo_url = json['agency_logo_url']
        else:
            self.__name = "None"
            self.__date_of_birth = "None"
            self.__date_of_death = "None"
            self.__nationality = "None"
            self.__bio = "None"
            self.__twitter = "None"
            self.__instagram = "None"
            self.__wiki = "None"
            self.__profile_image = "None"
            self.__profile_image_thumbnail = "None"
            self.__flights_count = "None"
            self.__landings_count = "None"
            self.__last_flight = "None"
            self.__first_flight = "None"
            self.__status_name = "None"
            self.__type_name = "None"
            self.__agency_name = "None"
            self.__agency_type = "None"
            self.__agency_country_code = "None"
            self.__agency_abbrev = "None"
            self.__agency_logo_url = "None"

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        today = date.today()
        try:
            return today.year - datetime.strptime(self.__date_of_birth, '%Y-%m-%d').year - ((today.month, today.day) < (
                datetime.strptime(self.__date_of_birth, '%Y-%m-%d').month,
                datetime.strptime(self.__date_of_birth, '%Y-%m-%d').day))
        except (ValueError, TypeError):
            return "The birth date was not found."

    @property
    def birth_date(self):
        return self.__date_of_birth

    @property
    def death_date(self):
        return self.__date_of_death

    @property
    def age_of_death(self):
        if self.death_date == "" or self.death_date == "None":
            return "Still Alive!!"
        else:
            death = datetime.strptime(self.__date_of_death, '%Y-%m-%d')
            return death.year - datetime.strptime(self.__date_of_birth, '%Y-%m-%d').year - ((death.month, death.day) < (
                datetime.strptime(self.__date_of_birth, '%Y-%m-%d').month,
                datetime.strptime(self.__date_of_birth, '%Y-%m-%d').day))

    @property
    def nationality(self):
        return self.__nationality

    @property
    def bio(self):
        return self.__bio

    @property
    def twitter(self):
        return self.__twitter

    @property
    def instagram(self):
        return self.__instagram

    @property
    def wiki(self):
        return self.__wiki

    @property
    def profile_image(self):
        return self.__profile_image

    @property
    def profile_image_thumbnail(self):
        return self.__profile_image_thumbnail

    @property
    def flights_count(self):
        return self.__flights_count

    @property
    def landings_count(self):
        return self.__landings_count

    @property
    def last_flight(self):
        return self.__last_flight

    @property
    def first_flight(self):
        return self.__first_flight

    @property
    def status_name(self):
        return self.__status_name

    @property
    def type_name(self):
        return self.__type_name

    @property
    def agency_name(self):
        return self.__agency_name

    @property
    def agency_type(self):
        return self.__agency_type

    @property
    def agency_country_code(self):
        return self.__agency_country_code

    @property
    def agency_abbrev(self):
        return self.__agency_abbrev

    @property
    def agency_logo_url(self):
        return self.__agency_logo_url

    def __repr__(self):
        return f"\nEXTENDED ASTRONAUT INFO:\n" \
               f"Name: {self.__name}\nAge: {self.age}\nBirth Date: {self.__date_of_birth}\nDeath Date: {self.__date_of_death}\n" \
               f"Nationality: {self.__nationality}\nDescription: {self.__bio}\nTwitter link: {self.__twitter}\n" \
               f"Instagram link: {self.__instagram}\nWikipedia page: {self.__wiki}\nProfile image link: {self.__profile_image}\n" \
               f"Profile image thumbnail link: {self.__profile_image_thumbnail}\nFlights count: {self.__flights_count}\n" \
               f"Landings count: {self.__landings_count}\nLast flight: {self.__last_flight}\nFirst flight: {self.__first_flight}\n" \
               f"Status: {self.__status_name}\nEnrollment type: {self.__type_name}\nAgency Name: {self.__agency_name}\n" \
               f"Agency type: {self.__agency_type}\nAgency participating Counties: {self.__agency_country_code}\n" \
               f"Agency acronym: {self.__agency_abbrev}\nAgency logo link: {self.__agency_logo_url}"

    @property
    def show_basic_info(self):
        return f"\nBASIC ASTRONAUT INFO:\n" \
               f"Name: {self.__name}\nAge: {self.age}\nBirth Date: {self.__date_of_birth}\nDeath Date: {self.__date_of_death}\n" \
               f"Nationality: {self.__nationality}\nDescription: {self.__bio}\nProfile image link: {self.__profile_image}\n" \
               f"Flights count: {self.__flights_count}\n" \
               f"Landings count: {self.__landings_count}\nLast flight: {self.__last_flight}\n" \
               f"Agency acronym: {self.__agency_abbrev}"

    @property
    def jsonify(self):
        return {"name": self.__name, "date_of_birth": self.__date_of_birth, "date_of_death": self.__date_of_death,
                "nationality": self.__nationality,
                "bio": self.__bio,
                "twitter": self.__twitter, "instagram": self.__instagram, "wiki": self.__wiki,
                "profile_image": self.__profile_image,
                "profile_image_thumbnail": self.__profile_image_thumbnail,
                "flights_count": self.__flights_count, "landings_count": self.__landings_count,
                "last_flight": self.__last_flight,
                "first_flight": self.__first_flight, "status_name": self.__status_name, "type_name": self.__type_name,
                "agency_name": self.__agency_name, "agency_type": self.__agency_type,
                "agency_country_code": self.__agency_country_code, "agency_abbrev": self.__agency_abbrev,
                "agency_logo_url": self.__agency_logo_url}

    @name.setter
    def name(self, value):
        self.__name = value

    @birth_date.setter
    def birth_date(self, value):
        if isValidDate(value):
            self.__date_of_birth = value

    @death_date.setter
    def death_date(self, value):

        if isValidDate(value):
            self.__date_of_death = value

    @nationality.setter
    def nationality(self, value):
        self.__nationality = value

    @bio.setter
    def bio(self, value):
        self.__bio = value

    @twitter.setter
    def twitter(self, value):
        self.__twitter = value

    @instagram.setter
    def instagram(self, value):
        self.__instagram = value

    @wiki.setter
    def wiki(self, value):
        self.__wiki = value

    @profile_image.setter
    def profile_image(self, value):
        self.__profile_image = value

    @profile_image_thumbnail.setter
    def profile_image_thumbnail(self, value):
        self.__profile_image_thumbnail = value

    @flights_count.setter
    def flights_count(self, value):
        if int_check(value):
            self.__flights_count = value

    @landings_count.setter
    def landings_count(self, value):
        if int_check(value):
            self.__landings_count = value

    @last_flight.setter
    def last_flight(self, value):
        if isValidDateFlight(value):
            self.__last_flight = value

    @first_flight.setter
    def first_flight(self, value):
        if isValidDateFlight(value):
            self.__first_flight = value

    @status_name.setter
    def status_name(self, value):
        self.__status_name = value

    @type_name.setter
    def type_name(self, value):
        self.__type_name = value

    @agency_name.setter
    def agency_name(self, value):
        self.__agency_name = value

    @agency_type.setter
    def agency_type(self, value):
        self.__agency_type = value

    @agency_country_code.setter
    def agency_country_code(self, value):
        self.__agency_country_code = value

    @agency_abbrev.setter
    def agency_abbrev(self, value):
        self.__agency_abbrev = value

    @agency_logo_url.setter
    def agency_logo_url(self, value):
        self.__agency_logo_url = value
