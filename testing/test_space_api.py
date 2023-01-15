from library.space_api import SpaceApi
from library.class_folder.astronaut import Astronaut
from library.class_folder.launcher import Launcher
from library.class_folder.launch import Launch

finder = SpaceApi()

launch_out = {0: Launch(
    {'name': 'Sputnik 8K74PS | Sputnik 1', 'net': '1957-10-04T19:28:34Z', 'window_start': '1957-10-04T19:28:34Z',
     'window_end': '1957-10-04T19:28:34Z', 'failreason': 'None',
     'image': 'https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launcher_images/sputnik_8k74ps_image_20210830185541.jpg',
     'infographic': 'None', 'orbital_launch_attempt_count': 1.0, 'orbital_launch_attempt_count_year': 1,
     'location_launch_attempt_count': 1, 'location_launch_attempt_count_year': 1, 'pad_launch_attempt_count': 1,
     'pad_launch_attempt_count_year': 1, 'agency_launch_attempt_count': 1, 'agency_launch_attempt_count_year': 1,
     'status_name': 'Launch Successful', 'launch_service_provider_name': 'Soviet Space Program',
     'launch_service_provider_type': 'Government', 'rocket_id': 3003,
     'rocket_configuration_full_name': 'Sputnik 8K74PS', 'mission_name': 'Sputnik 1',
     'mission_description': 'First artificial satellite consisting of a 58 cm pressurized aluminium shell containing two 1 W transmitters for a total mass of 83.6 kg.',
     'mission_type': 'Test Flight', 'mission_orbit_name': 'Low Earth Orbit', 'pad_wiki_url': '',
     'pad_longitude': 63.342, 'pad_latitude': 45.92, 'pad_location_name': 'Baikonur Cosmodrome, Republic of Kazakhstan',
     'pad_location_country_code': 'KAZ'}), 1: Launch(
    {'name': 'Sputnik 8K74PS | Sputnik 2', 'net': '1957-11-03T02:30:00Z', 'window_start': '1957-11-03T02:30:00Z',
     'window_end': '1957-11-03T02:30:00Z', 'failreason': 'None',
     'image': 'https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launcher_images/sputnik_8k74ps_image_20210830185541.jpg',
     'infographic': 'None', 'orbital_launch_attempt_count': 2.0, 'orbital_launch_attempt_count_year': 2,
     'location_launch_attempt_count': 2, 'location_launch_attempt_count_year': 2, 'pad_launch_attempt_count': 2,
     'pad_launch_attempt_count_year': 2, 'agency_launch_attempt_count': 2, 'agency_launch_attempt_count_year': 2,
     'status_name': 'Launch Successful', 'launch_service_provider_name': 'Soviet Space Program',
     'launch_service_provider_type': 'Government', 'rocket_id': 3004,
     'rocket_configuration_full_name': 'Sputnik 8K74PS', 'mission_name': 'Sputnik 2',
     'mission_description': 'Second artificial satellite and first to carry an animal into orbit.',
     'mission_type': 'Test Flight', 'mission_orbit_name': 'Low Earth Orbit', 'pad_wiki_url': '',
     'pad_longitude': 63.342, 'pad_latitude': 45.92, 'pad_location_name': 'Baikonur Cosmodrome, Republic of Kazakhstan',
     'pad_location_country_code': 'KAZ'}), 8: Launch(
    {'name': 'Sputnik 8A91 | D-1 1', 'net': '1958-04-27T07:00:35Z', 'window_start': '1958-04-27T07:00:35Z',
     'window_end': '1958-04-27T07:00:35Z', 'failreason': 'None',
     'image': 'https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launcher_images/sputnik_8a91_image_20210830171943.png',
     'infographic': 'None', 'orbital_launch_attempt_count': 9.0, 'orbital_launch_attempt_count_year': 6,
     'location_launch_attempt_count': 3, 'location_launch_attempt_count_year': 1, 'pad_launch_attempt_count': 3,
     'pad_launch_attempt_count_year': 1, 'agency_launch_attempt_count': 3, 'agency_launch_attempt_count_year': 1,
     'status_name': 'Launch Failure', 'launch_service_provider_name': 'Soviet Space Program',
     'launch_service_provider_type': 'Government', 'rocket_id': 3011, 'rocket_configuration_full_name': 'Sputnik 8A91',
     'mission_name': 'D-1 1',
     'mission_description': 'First complex scientific satellite with 12 experiments and a total mass of1327 kg. It failed to reach orbit due to a launch vehicle failure.',
     'mission_type': 'Earth Science', 'mission_orbit_name': 'Low Earth Orbit', 'pad_wiki_url': '',
     'pad_longitude': 63.342, 'pad_latitude': 45.92, 'pad_location_name': 'Baikonur Cosmodrome, Republic of Kazakhstan',
     'pad_location_country_code': 'KAZ'}), 10: Launch(
    {'name': 'Sputnik 8A91 | D1- 2', 'net': '1958-05-15T07:12:00Z', 'window_start': '1958-05-15T07:12:00Z',
     'window_end': '1958-05-15T07:12:00Z', 'failreason': 'None',
     'image': 'https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launcher_images/sputnik_8a91_image_20210830171943.png',
     'infographic': 'None', 'orbital_launch_attempt_count': 11.0, 'orbital_launch_attempt_count_year': 8,
     'location_launch_attempt_count': 4, 'location_launch_attempt_count_year': 2, 'pad_launch_attempt_count': 4,
     'pad_launch_attempt_count_year': 2, 'agency_launch_attempt_count': 4, 'agency_launch_attempt_count_year': 2,
     'status_name': 'Launch Successful', 'launch_service_provider_name': 'Soviet Space Program',
     'launch_service_provider_type': 'Government', 'rocket_id': 3013, 'rocket_configuration_full_name': 'Sputnik 8A91',
     'mission_name': 'D1- 2', 'mission_description': 'First complex scientific satellite to reach orbit.',
     'mission_type': 'Earth Science', 'mission_orbit_name': 'Low Earth Orbit', 'pad_wiki_url': '',
     'pad_longitude': 63.342, 'pad_latitude': 45.92, 'pad_location_name': 'Baikonur Cosmodrome, Republic of Kazakhstan',
     'pad_location_country_code': 'KAZ'}), 71: Launch(
    {'name': "Vostok 8K72 | Korabl'-Sputnik-1", 'net': '1960-05-15T00:00:05Z', 'window_start': '1960-05-15T00:00:05Z',
     'window_end': '1960-05-15T00:00:05Z', 'failreason': '', 'image': 'None', 'infographic': 'None',
     'orbital_launch_attempt_count': 66.0, 'orbital_launch_attempt_count_year': 12, 'location_launch_attempt_count': 14,
     'location_launch_attempt_count_year': 3, 'pad_launch_attempt_count': 14, 'pad_launch_attempt_count_year': 3,
     'agency_launch_attempt_count': 14, 'agency_launch_attempt_count_year': 3, 'status_name': 'Launch Successful',
     'launch_service_provider_name': 'Soviet Space Program', 'launch_service_provider_type': 'Government',
     'rocket_id': 3068, 'rocket_configuration_full_name': 'Vostok 8K72', 'mission_name': "Korabl'-Sputnik-1",
     'mission_description': 'Korabl-Sputnik was the first test flight of the Vostok programme and the first Vostok spacecraft.',
     'mission_type': 'Test Flight', 'mission_orbit_name': 'Low Earth Orbit', 'pad_wiki_url': '',
     'pad_longitude': 63.342, 'pad_latitude': 45.92, 'pad_location_name': 'Baikonur Cosmodrome, Republic of Kazakhstan',
     'pad_location_country_code': 'KAZ'}), 75: Launch(
    {'name': 'Vostok 8K72 | Korabl-Sputnik (2)', 'net': '1960-07-28T09:31:00Z', 'window_start': '1960-07-28T09:31:00Z',
     'window_end': '1960-07-28T09:31:00Z', 'failreason': '', 'image': 'None', 'infographic': 'None',
     'orbital_launch_attempt_count': 70.0, 'orbital_launch_attempt_count_year': 16, 'location_launch_attempt_count': 15,
     'location_launch_attempt_count_year': 4, 'pad_launch_attempt_count': 15, 'pad_launch_attempt_count_year': 4,
     'agency_launch_attempt_count': 15, 'agency_launch_attempt_count_year': 4, 'status_name': 'Launch Failure',
     'launch_service_provider_name': 'Soviet Space Program', 'launch_service_provider_type': 'Government',
     'rocket_id': 3072, 'rocket_configuration_full_name': 'Vostok 8K72', 'mission_name': 'Korabl-Sputnik (2)',
     'mission_description': 'A test of the Vostok capsule carrying a pair of dogs. Unfortunately this failed after a failure of the booster.',
     'mission_type': 'Test Flight', 'mission_orbit_name': 'Low Earth Orbit', 'pad_wiki_url': '',
     'pad_longitude': 63.342, 'pad_latitude': 45.92, 'pad_location_name': 'Baikonur Cosmodrome, Republic of Kazakhstan',
     'pad_location_country_code': 'KAZ'}), 81: Launch(
    {'name': "Vostok 8K72 | Korabl'-Sputnik-2", 'net': '1960-08-19T08:44:06Z', 'window_start': '1960-08-19T08:44:06Z',
     'window_end': '1960-08-19T08:44:06Z', 'failreason': '', 'image': 'None', 'infographic': 'None',
     'orbital_launch_attempt_count': 75.0, 'orbital_launch_attempt_count_year': 21, 'location_launch_attempt_count': 16,
     'location_launch_attempt_count_year': 5, 'pad_launch_attempt_count': 16, 'pad_launch_attempt_count_year': 5,
     'agency_launch_attempt_count': 16, 'agency_launch_attempt_count_year': 5, 'status_name': 'Launch Successful',
     'launch_service_provider_name': 'Soviet Space Program', 'launch_service_provider_type': 'Government',
     'rocket_id': 3077, 'rocket_configuration_full_name': 'Vostok 8K72', 'mission_name': "Korabl'-Sputnik-2",
     'mission_description': 'A test of the Vostok capsule which carried dogs Belka and Stelka (amonst other animals) the flight was successful and all animals were recovered successfully.',
     'mission_type': 'Test Flight', 'mission_orbit_name': 'Low Earth Orbit', 'pad_wiki_url': '',
     'pad_longitude': 63.342, 'pad_latitude': 45.92, 'pad_location_name': 'Baikonur Cosmodrome, Republic of Kazakhstan',
     'pad_location_country_code': 'KAZ'}), 97: Launch(
    {'name': "Vostok 8K72 | Korabl'-Sputnik-3", 'net': '1960-12-01T07:30:04Z', 'window_start': '1960-12-01T07:30:04Z',
     'window_end': '1960-12-01T07:30:04Z', 'failreason': '', 'image': 'None', 'infographic': 'None',
     'orbital_launch_attempt_count': 88.0, 'orbital_launch_attempt_count_year': 34, 'location_launch_attempt_count': 19,
     'location_launch_attempt_count_year': 8, 'pad_launch_attempt_count': 19, 'pad_launch_attempt_count_year': 8,
     'agency_launch_attempt_count': 19, 'agency_launch_attempt_count_year': 8, 'status_name': 'Launch Successful',
     'launch_service_provider_name': 'Soviet Space Program', 'launch_service_provider_type': 'Government',
     'rocket_id': 3091, 'rocket_configuration_full_name': 'Vostok 8K72', 'mission_name': "Korabl'-Sputnik-3",
     'mission_description': "Another test of the Vostok capsule which had a successful flight into orbit but during re-entry the engine failed to cut off and burned to completion resulting in an incorrect entry trajectory. The vehicle was destroyed in order to ensure the vehicle didn't fall into enemy hands.",
     'mission_type': 'Test Flight', 'mission_orbit_name': 'Low Earth Orbit', 'pad_wiki_url': '',
     'pad_longitude': 63.342, 'pad_latitude': 45.92, 'pad_location_name': 'Baikonur Cosmodrome, Republic of Kazakhstan',
     'pad_location_country_code': 'KAZ'}), 103: Launch(
    {'name': 'Vostok | Korabl-Sputnik (4)', 'net': '1960-12-22T07:45:19Z', 'window_start': '1960-12-22T07:45:19Z',
     'window_end': '1960-12-22T07:45:19Z', 'failreason': '',
     'image': 'https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launcher_images/vostok_image_20191104130128.jpg',
     'infographic': 'None', 'orbital_launch_attempt_count': 93.0, 'orbital_launch_attempt_count_year': 39,
     'location_launch_attempt_count': 20, 'location_launch_attempt_count_year': 9, 'pad_launch_attempt_count': 20,
     'pad_launch_attempt_count_year': 9, 'agency_launch_attempt_count': 20, 'agency_launch_attempt_count_year': 9,
     'status_name': 'Launch Failure', 'launch_service_provider_name': 'Soviet Space Program',
     'launch_service_provider_type': 'Government', 'rocket_id': 3096, 'rocket_configuration_full_name': 'Vostok-K',
     'mission_name': 'Korabl-Sputnik (4)',
     'mission_description': 'Maiden flight of Vostok-K, second stage engine failure, spacecraft separated and recovered. Two dogs aboard, both survived.',
     'mission_type': 'Test Flight', 'mission_orbit_name': 'Low Earth Orbit', 'pad_wiki_url': '',
     'pad_longitude': 63.342, 'pad_latitude': 45.92, 'pad_location_name': 'Baikonur Cosmodrome, Republic of Kazakhstan',
     'pad_location_country_code': 'KAZ'}), 114: Launch(
    {'name': 'Vostok-K | Sputnik 9', 'net': '1961-03-09T06:29:00Z', 'window_start': '1961-03-09T06:29:00Z',
     'window_end': '1961-03-09T06:29:00Z', 'failreason': '',
     'image': 'https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launcher_images/vostok_image_20191104130128.jpg',
     'infographic': 'None', 'orbital_launch_attempt_count': 102.0, 'orbital_launch_attempt_count_year': 102,
     'location_launch_attempt_count': 23, 'location_launch_attempt_count_year': 3, 'pad_launch_attempt_count': 23,
     'pad_launch_attempt_count_year': 3, 'agency_launch_attempt_count': 23, 'agency_launch_attempt_count_year': 3,
     'status_name': 'Launch Successful', 'launch_service_provider_name': 'Soviet Space Program',
     'launch_service_provider_type': 'Government', 'rocket_id': 2370, 'rocket_configuration_full_name': 'Vostok-K',
     'mission_name': 'None', 'mission_description': 'None', 'mission_type': 'None', 'mission_orbit_name': 'None',
     'pad_wiki_url': '', 'pad_longitude': 63.342, 'pad_latitude': 45.92,
     'pad_location_name': 'Baikonur Cosmodrome, Republic of Kazakhstan', 'pad_location_country_code': 'KAZ'}),
    117: Launch({'name': 'Vostok-K | Sputnik 10', 'net': '1961-03-25T05:54:00Z',
                 'window_start': '1961-03-25T05:54:00Z', 'window_end': '1961-03-25T05:54:00Z',
                 'failreason': '',
                 'image': 'https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launcher_images/vostok_image_20191104130128.jpg',
                 'infographic': 'None', 'orbital_launch_attempt_count': 103.0,
                 'orbital_launch_attempt_count_year': 103, 'location_launch_attempt_count': 24,
                 'location_launch_attempt_count_year': 4, 'pad_launch_attempt_count': 24,
                 'pad_launch_attempt_count_year': 4, 'agency_launch_attempt_count': 24,
                 'agency_launch_attempt_count_year': 4, 'status_name': 'Launch Successful',
                 'launch_service_provider_name': 'Soviet Space Program',
                 'launch_service_provider_type': 'Government', 'rocket_id': 2371,
                 'rocket_configuration_full_name': 'Vostok-K', 'mission_name': 'None',
                 'mission_description': 'None', 'mission_type': 'None', 'mission_orbit_name': 'None',
                 'pad_wiki_url': '', 'pad_longitude': 63.342, 'pad_latitude': 45.92,
                 'pad_location_name': 'Baikonur Cosmodrome, Republic of Kazakhstan',
                 'pad_location_country_code': 'KAZ'}), 181: Launch(
        {'name': 'Kosmos-2I 63S1 | Sputnik 13', 'net': '1962-04-24T04:00:00Z', 'window_start': '1962-04-24T04:00:00Z',
         'window_end': '1962-04-24T04:00:00Z', 'failreason': 'None',
         'image': 'https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launcher_images/kosmos-2i252063s1_image_20191201205435.jpg',
         'infographic': 'None', 'orbital_launch_attempt_count': 157.0, 'orbital_launch_attempt_count_year': 16,
         'location_launch_attempt_count': 5, 'location_launch_attempt_count_year': 3, 'pad_launch_attempt_count': 5,
         'pad_launch_attempt_count_year': 3, 'agency_launch_attempt_count': 30, 'agency_launch_attempt_count_year': 3,
         'status_name': 'Launch Successful', 'launch_service_provider_name': 'Soviet Space Program',
         'launch_service_provider_type': 'Government', 'rocket_id': 3116, 'rocket_configuration_full_name': 'Kosmos-2I',
         'mission_name': 'Sputnik 13',
         'mission_description': 'Cosmos 3 was the first 2MS satellite deployed by the OKB-1. It operated until August 20, 1962 and re-entered the atmosphere on October 17, 1963 .',
         'mission_type': 'Astrophysics', 'mission_orbit_name': 'Elliptical Orbit', 'pad_wiki_url': 'None',
         'pad_longitude': 46.295814, 'pad_latitude': 48.569551, 'pad_location_name': 'Kapustin Yar, Russian Federation',
         'pad_location_country_code': 'RUS'}), 193: Launch(
        {'name': 'Kosmos-2I 63S1 | Sputnik 15', 'net': '1962-05-28T03:00:00Z', 'window_start': '1962-05-28T03:00:00Z',
         'window_end': '1962-05-28T03:00:00Z', 'failreason': 'None',
         'image': 'https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launcher_images/kosmos-2i252063s1_image_20191201205435.jpg',
         'infographic': 'None', 'orbital_launch_attempt_count': 167.0, 'orbital_launch_attempt_count_year': 26,
         'location_launch_attempt_count': 6, 'location_launch_attempt_count_year': 4, 'pad_launch_attempt_count': 6,
         'pad_launch_attempt_count_year': 4, 'agency_launch_attempt_count': 32, 'agency_launch_attempt_count_year': 5,
         'status_name': 'Launch Successful', 'launch_service_provider_name': 'Soviet Space Program',
         'launch_service_provider_type': 'Government', 'rocket_id': 3126, 'rocket_configuration_full_name': 'Kosmos-2I',
         'mission_name': 'Sputnik 15',
         'mission_description': 'This was the second 2MS satellite. It re-entered the atmosphere on May 2, 1963.',
         'mission_type': 'Astrophysics', 'mission_orbit_name': 'Elliptical Orbit', 'pad_wiki_url': 'None',
         'pad_longitude': 46.295814, 'pad_latitude': 48.569551, 'pad_location_name': 'Kapustin Yar, Russian Federation',
         'pad_location_country_code': 'RUS'}), 214: Launch(
        {'name': 'Kosmos-2I 63S1 | Sputnik 18', 'net': '1962-08-18T15:00:00Z', 'window_start': '1962-08-18T15:00:00Z',
         'window_end': '1962-08-18T15:00:00Z', 'failreason': 'None',
         'image': 'https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launcher_images/kosmos-2i252063s1_image_20191201205435.jpg',
         'infographic': 'None', 'orbital_launch_attempt_count': 187.0, 'orbital_launch_attempt_count_year': 46,
         'location_launch_attempt_count': 8, 'location_launch_attempt_count_year': 6, 'pad_launch_attempt_count': 8,
         'pad_launch_attempt_count_year': 6, 'agency_launch_attempt_count': 38, 'agency_launch_attempt_count_year': 11,
         'status_name': 'Launch Successful', 'launch_service_provider_name': 'Soviet Space Program',
         'launch_service_provider_type': 'Government', 'rocket_id': 3144, 'rocket_configuration_full_name': 'Kosmos-2I',
         'mission_name': 'Sputnik 18',
         'mission_description': 'Cosmos 8 is a DS-K8 demonstration satellite. It re-entered the atmosphere on August 17, 1963.',
         'mission_type': 'Earth Science', 'mission_orbit_name': 'Low Earth Orbit', 'pad_wiki_url': 'None',
         'pad_longitude': 46.295814, 'pad_latitude': 48.569551, 'pad_location_name': 'Kapustin Yar, Russian Federation',
         'pad_location_country_code': 'RUS'}), 314: Launch(
        {'name': 'Sputnik 11A59 | Polyot', 'net': '1963-11-01T08:56:38Z', 'window_start': '1963-11-01T08:56:38Z',
         'window_end': '1963-11-01T08:56:38Z', 'failreason': 'None', 'image': 'None', 'infographic': 'None',
         'orbital_launch_attempt_count': 278.0, 'orbital_launch_attempt_count_year': 55,
         'location_launch_attempt_count': 52, 'location_launch_attempt_count_year': 11, 'pad_launch_attempt_count': 1,
         'pad_launch_attempt_count_year': 1, 'agency_launch_attempt_count': 67, 'agency_launch_attempt_count_year': 18,
         'status_name': 'Launch Successful', 'launch_service_provider_name': 'Soviet Space Program',
         'launch_service_provider_type': 'Government', 'rocket_id': 3233,
         'rocket_configuration_full_name': 'Sputnik 11A59', 'mission_name': 'Polyot',
         'mission_description': 'Polyot 1 (I1) was a mission to test the propulsion of the I2P coorbital ASAT satellite.',
         'mission_type': 'Test Flight', 'mission_orbit_name': 'Low Earth Orbit',
         'pad_wiki_url': 'https://en.wikipedia.org/wiki/Baikonur_Cosmodrome_Site_31', 'pad_longitude': 63.564003,
         'pad_latitude': 45.996034, 'pad_location_name': 'Baikonur Cosmodrome, Republic of Kazakhstan',
         'pad_location_country_code': 'KAZ'}), 352: Launch(
        {'name': 'Sputnik 11A59 | Polyot-2', 'net': '1964-04-12T09:30:00Z', 'window_start': '1964-04-12T09:30:00Z',
         'window_end': '1964-04-12T09:30:00Z', 'failreason': 'None', 'image': 'None', 'infographic': 'None',
         'orbital_launch_attempt_count': 315.0, 'orbital_launch_attempt_count_year': 23,
         'location_launch_attempt_count': 63, 'location_launch_attempt_count_year': 7, 'pad_launch_attempt_count': 3,
         'pad_launch_attempt_count_year': 2, 'agency_launch_attempt_count': 81, 'agency_launch_attempt_count_year': 9,
         'status_name': 'Launch Successful', 'launch_service_provider_name': 'Soviet Space Program',
         'launch_service_provider_type': 'Government', 'rocket_id': 3271,
         'rocket_configuration_full_name': 'Sputnik 11A59', 'mission_name': 'Polyot-2',
         'mission_description': 'Polyot 2 (I1) was a mission to test the propulsion of the I2P coorbital ASAT satellite. It did not conduct any interception maneuveres.',
         'mission_type': 'Test Flight', 'mission_orbit_name': 'Low Earth Orbit',
         'pad_wiki_url': 'https://en.wikipedia.org/wiki/Baikonur_Cosmodrome_Site_31', 'pad_longitude': 63.564003,
         'pad_latitude': 45.996034, 'pad_location_name': 'Baikonur Cosmodrome, Republic of Kazakhstan',
         'pad_location_country_code': 'KAZ'}), 2578: Launch(
        {'name': 'Kosmos-3M | Radio Sputnik 3 to 8', 'net': '1981-12-17T11:00:00Z',
         'window_start': '1981-12-17T11:00:00Z', 'window_end': '1981-12-17T11:00:00Z', 'failreason': 'None',
         'image': 'None', 'infographic': 'None', 'orbital_launch_attempt_count': 2501.0,
         'orbital_launch_attempt_count_year': 122, 'location_launch_attempt_count': 847,
         'location_launch_attempt_count_year': 60, 'pad_launch_attempt_count': 119, 'pad_launch_attempt_count_year': 8,
         'agency_launch_attempt_count': 1546, 'agency_launch_attempt_count_year': 98,
         'status_name': 'Launch Successful', 'launch_service_provider_name': 'Soviet Space Program',
         'launch_service_provider_type': 'Government', 'rocket_id': 5350,
         'rocket_configuration_full_name': 'Kosmos-3M (11K65M)', 'mission_name': 'Radio Sputnik 3 to 8',
         'mission_description': '6 Soviet amateur radio satellites', 'mission_type': 'Communications',
         'mission_orbit_name': 'Low Earth Orbit', 'pad_wiki_url': 'https://en.wikipedia.org/wiki/Plesetsk_Cosmodrome',
         'pad_longitude': 40.869806, 'pad_latitude': 62.883,
         'pad_location_name': 'Plesetsk Cosmodrome, Russian Federation', 'pad_location_country_code': 'RUS'})}


def test_search_astro_by():
    x = finder.search_astro_by("flights_count", "30")
    assert str(x) == str({641: Astronaut(
        {'name': 'Mark Stucky', 'date_of_birth': '1958-11-09', 'date_of_death': None, 'nationality': 'American',
         'bio': "Mark P. 'Forger' Stucky  was an American test pilot and commercial astronaut for Virgin Galactic. He left the company in July 2021.",
         'twitter': None, 'instagram': None, 'wiki': 'https://en.wikipedia.org/wiki/Mark_P._Stucky',
         'profile_image': 'https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/astronaut_images/mark_stucky_image_20210522145002.jpg',
         'profile_image_thumbnail': 'https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/astronaut_images/mark_stucky_thumbnail_20220911033904.jpeg',
         'flights_count': 30, 'landings_count': 30, 'last_flight': '2020-06-25T12:00:00Z',
         'first_flight': '2010-10-28T12:00:00Z', 'status_name': 'Retired', 'type_name': 'Private',
         'agency_name': 'Virgin Galactic', 'agency_type': 'Private', 'agency_country_code': 'USA',
         'agency_abbrev': 'VG',
         'agency_logo_url': 'https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/logo/virgin2520galactic_logo_20210522131723.png'})})


def test_find_astro_by():
    x = finder.find_astro_by("name", "Shaun the Sheep").show_basic_info
    assert x == ('\n'
                 'BASIC ASTRONAUT INFO:\n'
                 'Name: Shaun the Sheep\n'
                 'Age: The birth date was not found.\n'
                 'Birth Date: None\n'
                 'Death Date: None\n'
                 'Nationality: Earthling\n'
                 'Description: Shaun the Sheep is the main character of the eponymous British '
                 'stop-motion TV show. This plushie serves as zero-G indicator on the '
                 'Artemis-1 mission.\n'
                 'Profile image link: '
                 'https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/astronaut_images/shaun_the_sheep_image_20220818114142.jpg\n'
                 'Flights count: 1\n'
                 'Landings count: 0\n'
                 'Last flight: 2022-11-16T06:47:44Z\n'
                 'Agency acronym: ESA')


def test_populate_astro():
    a = finder.populate_astro("miro rava", "2001-05-22", "None", "italy", "test di prova post", "100", "100",
                              "prova-landing01", "TST")
    assert type(a) == type(Astronaut())


def test_add_astro():
    a = finder.populate_astro("miro rava", "2001-05-22", "None", "italy", "test di prova post", "100", "100",
                              "prova-landing01", "TST")

    finder.add_astro(a)
    x = finder.find_astro_by("name", "miro rava")
    finder.delete_astro_by("name", "miro rava")
    assert x.show_basic_info == ('\n'
                                 'BASIC ASTRONAUT INFO:\n'
                                 'Name: miro rava\n'
                                 'Age: 21\n'
                                 'Birth Date: 2001-05-22\n'
                                 'Death Date: None\n'
                                 'Nationality: italy\n'
                                 'Description: test di prova post\n'
                                 'Profile image link: None\n'
                                 'Flights count: 100\n'
                                 'Landings count: 100\n'
                                 'Last flight: prova-landing01\n'
                                 'Agency acronym: TST')


def test_delete_astro_by():
    a = finder.populate_astro("miro rava", "2001-05-22", "None", "italy", "test di prova post", "100", "100",
                              "prova-landing01", "TST")
    finder.add_astro(a)
    finder.delete_astro_by("name", "miro rava")
    x = finder.find_astro_by("name", "miro rava")

    assert x == {'error': 'Entry not found:  name == miro rava'}


def test_update_astro_by():
    a = finder.populate_astro("miro rava", "2001-05-22", "None", "italy", "test di prova post", "100", "100",
                              "prova-landing01", "TST")

    b = finder.populate_astro("Oleg Lastocichin", "boh", "None", "moldova", "test di prova update", "300", "300",
                              "prova-landing02", "KKK")
    finder.add_astro(a)
    finder.update_astro_by("name", "miro rava", b)
    x = finder.find_astro_by("name", "Oleg Lastocichin")
    finder.delete_astro_by("name", "Oleg Lastocichin")
    assert x.show_basic_info == ('\n'
                                 'BASIC ASTRONAUT INFO:\n'
                                 'Name: Oleg Lastocichin\n'
                                 'Age: The birth date was not found.\n'
                                 'Birth Date: boh\n'
                                 'Death Date: None\n'
                                 'Nationality: moldova\n'
                                 'Description: test di prova update\n'
                                 'Profile image link: None\n'
                                 'Flights count: 300\n'
                                 'Landings count: 300\n'
                                 'Last flight: prova-landing02\n'
                                 'Agency acronym: KKK')


def test_search_launcher_by():
    x = finder.search_launcher_by("flights", "9")
    assert str(x) == str({96: Launcher({'flight_proven': 'True', 'serial_number': 'NS-3', 'status': 'Destroyed',
                                        'details': 'New Shepard vehicle #3 was the third flight vehicle of the New '
                                                   'Shepard suborbital rocket. It suffered an anomaly during its '
                                                   'ninth flight.',
                                        'image_url': 'https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com'
                                                     '/media/launcher_core_images/63_image_20190225165029.jpeg',
                                        'flights': 9, 'last_launch_date': '2022-09-12T14:26:00Z',
                                        'first_launch_date': '2017-12-12T16:59:00Z',
                                        'launcher_config_full_name': 'New Shepard'})})


def test_find_launcher_by():
    x = finder.find_launcher_by("serial_number", "B1060").show_basic_info
    assert x == ('\n'
                 'BASIC LAUNCHER INFO:\n'
                 'Full Name: Falcon 9 Block 5\n'
                 'Status: active\n'
                 'Description: Landed on ASOG as of Oct 8, 2022.\n'
                 'Launcher Image: '
                 'https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launcher_core_images/72_image_20200706205625.jpg\n')


def test_populate_launcher():
    a = finder.populate_launcher("Razzo super spaziale", "a1b2c3", "imaginary", "Razzo di prova per api versione 01",
                                 "250")
    assert type(a) == type(Launcher())


def test_add_launcher_by():
    a = finder.populate_launcher("Razzo super spaziale", "a1b2c3", "imaginary", "Razzo di prova per api versione 01",
                                 "250")
    finder.add_launcher(a)
    x = finder.find_launcher_by("serial_number", "a1b2c3")
    finder.delete_launcher_by("serial_number", "a1b2c3")
    assert x.show_basic_info == ('\n'
                                 'BASIC LAUNCHER INFO:\n'
                                 'Full Name: Razzo super spaziale\n'
                                 'Status: imaginary\n'
                                 'Description: Razzo di prova per api versione 01\n'
                                 'Launcher Image: None\n')


def test_delete_launcher_by():
    a = finder.populate_launcher("Razzo super spaziale", "a1b2c3", "imaginary", "Razzo di prova per api versione 01",
                                 "250")
    finder.add_launcher(a)
    finder.delete_launcher_by("serial_number", "a1b2c3")
    x = finder.find_launcher_by("serial_number", "a1b2c3")

    assert x == {'error': 'Entry not found:  serial_number == a1b2c3'}


def test_update_launcher_by():
    a = finder.populate_launcher("Razzo super spaziale", "a1b2c3", "imaginary", "Razzo di prova per api versione 01",
                                 "250")
    b = finder.populate_launcher("Mucca spaziale", "aabbcc", "imaginary", "Razzo di prova per api versione 02",
                                 "800")

    finder.add_launcher(a)
    finder.update_launcher_by("serial_number", "a1b2c3", b)
    x = finder.find_launcher_by("serial_number", "aabbcc")
    finder.delete_launcher_by("serial_number", "aabbcc")
    assert x.show_basic_info == ('\n'
                                 'BASIC LAUNCHER INFO:\n'
                                 'Full Name: Mucca spaziale\n'
                                 'Status: imaginary\n'
                                 'Description: Razzo di prova per api versione 02\n'
                                 'Launcher Image: None\n')


def test_search_launch_by():
    x = finder.search_launch_by("name", "sputnik")
    assert str(x) == str(launch_out)


def test_find_launch_by():
    x = finder.find_launch_by("name", "Sputnik 8K74PS | Sputnik 1")
    assert x.show_basic_info == ('\n'
                                 'BASIC LAUNCH INFO:\n'
                                 'Name: Sputnik 8K74PS | Sputnik 1\n'
                                 'Net launch: 1957-10-04T19:28:34Z\n'
                                 'Image url: '
                                 'https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launcher_images/sputnik_8k74ps_image_20210830185541.jpg\n'
                                 'Launch status: Launch Successful\n'
                                 'Service provider name: Soviet Space Program\n'
                                 'Rocket name: Sputnik 8K74PS\n'
                                 'Mission description: First artificial satellite consisting of a 58 cm '
                                 'pressurized aluminium shell containing two 1 W transmitters for a total mass '
                                 'of 83.6 kg.\n'
                                 'Pad longitude: 63.342\n'
                                 'Pad latitude: 45.92\n'
                                 'Pad location name: Baikonur Cosmodrome, Republic of Kazakhstan\n')


def test_populate_launch():
    a = finder.populate_launch("Sopra la panca", "2023-09-10", "imaginary", "Balle spaziali",
                               "Star destroyer", "test for the api, number 01", "Uranus")
    assert type(a) == type(Launch())


def test_add_launch_by():
    a = finder.populate_launch("Sopra la panca", "2023-09-10", "imaginary", "Balle spaziali",
                               "Star destroyer", "test for the api, number 01", "Uranus")
    finder.add_launch(a)
    x = finder.find_launch_by("rocket_configuration_full_name", "Star destroyer")
    finder.delete_launch_by("rocket_configuration_full_name", "Star destroyer")
    assert x.show_basic_info == ('\n'
                                 'BASIC LAUNCH INFO:\n'
                                 'Name: Sopra la panca\n'
                                 'Net launch: 2023-09-10\n'
                                 'Image url: None\n'
                                 'Launch status: imaginary\n'
                                 'Service provider name: Balle spaziali\n'
                                 'Rocket name: Star destroyer\n'
                                 'Mission description: test for the api, number 01\n'
                                 'Pad longitude: None\n'
                                 'Pad latitude: None\n'
                                 'Pad location name: Uranus\n')


def test_delete_launch_by():
    a = finder.populate_launch("Sopra la panca", "2023-09-10", "imaginary", "Balle spaziali",
                               "Star destroyer", "test for the api, number 01", "Uranus")
    finder.add_launch(a)
    finder.delete_launch_by("rocket_configuration_full_name", "Star destroyer")
    x = finder.find_launch_by("rocket_configuration_full_name", "Star destroyer")
    assert x == {'error': 'Entry not found:  rocket_configuration_full_name == Star destroyer'}


def test_update_launch_by():
    a = finder.populate_launch("Sopra la panca", "2023-09-10", "imaginary", "Balle spaziali",
                               "Star destroyer", "test for the api, number 01", "Uranus")
    b = finder.populate_launch("Antonucci_space_stuff", "0001-01-01", "imaginary", "Python guys",
                               "Cosmetics", "test for the api, number 02", "Help me")
    finder.add_launch(a)
    finder.update_launch_by("launch_service_provider_name", "Balle spaziali", b)
    x = finder.find_launch_by("rocket_configuration_full_name", "Cosmetics")
    finder.delete_launch_by("rocket_configuration_full_name", "Cosmetics")
    assert x.show_basic_info == ('\n'
                                 'BASIC LAUNCH INFO:\n'
                                 'Name: Antonucci_space_stuff\n'
                                 'Net launch: 0001-01-01\n'
                                 'Image url: None\n'
                                 'Launch status: imaginary\n'
                                 'Service provider name: Python guys\n'
                                 'Rocket name: Cosmetics\n'
                                 'Mission description: test for the api, number 02\n'
                                 'Pad longitude: None\n'
                                 'Pad latitude: None\n'
                                 'Pad location name: Help me\n')