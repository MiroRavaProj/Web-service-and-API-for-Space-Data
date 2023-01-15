__definitely_not_oleg_token = '1enDD3J4_gBB4VtL826j'
__definitely_not_miro_token = "hxGZKf1YD6PH7yzdZpBA"


def script(thatlist):
    for i in (thatlist):
        print(i + "="+'request.form["' + i + '"]')

if __name__ == '__main__':
    astronauts = ['id', 'name', 'age', 'date_of_birth', 'date_of_death', 'nationality',
                  'bio', 'wiki', 'profile_image', 'flights_count', 'landings_count',
                  'last_flight', 'first_flight', 'status_name', 'type_name',
                  'agency_name', 'agency_type', 'agency_country_code', 'agency_abbrev',
                  'agency_logo_url']

    launch = ['id', 'url', 'slug', 'name', 'last_updated', 'net', 'window_end',
       'window_start', 'probability', 'holdreason', 'failreason', 'hashtag',
       'webcast_live', 'image', 'infographic', 'program',
       'orbital_launch_attempt_count', 'location_launch_attempt_count',
       'pad_launch_attempt_count', 'agency_launch_attempt_count',
       'orbital_launch_attempt_count_year',
       'location_launch_attempt_count_year', 'pad_launch_attempt_count_year',
       'agency_launch_attempt_count_year', 'status_id', 'status_name',
       'status_abbrev', 'status_description', 'launch_service_provider_id',
       'launch_service_provider_url', 'launch_service_provider_name',
       'launch_service_provider_type', 'rocket_id', 'pad_id', 'pad_name',
       'pad_latitude', 'pad_longitude', 'pad_location_name']

    launcher = ['id', 'url', 'flight_proven', 'serial_number', 'status', 'details',
       'image_url', 'flights', 'last_launch_date', 'first_launch_date',
       'launcher_config_family', 'launcher_config_full_name',
       'launcher_config_variant']
    script(astronauts)

