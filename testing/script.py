
from library.space_api import SpaceApi
from library.class_folder.astronaut import  Astronaut

finder = SpaceApi()
'''if __name__ == '__main__':
    # x = finder.search_astro_by("flights_count", "30")
    #print(x[641].jsonify)

    x = finder.search_launcher_by("flights", "9")
    print(x[96].jsonify)

    print('\n')
    print('\n')
    x = finder.search_launch_by("name", "sputnik")

    for i in x:
        print(i, ":Launch(",x[i].jsonify, end='),')'''

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

